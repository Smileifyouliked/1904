"""Save verbatim copies of official doc pages into a generated doc skill.

Skill Seekers 3.9.1 drops code blocks inside tabs and flattens tables on some
sites (Polymarket, Open-Meteo), and got no content from the NWS docs page.
This script stores the official text next to the Skill Seekers output so the
skill always has a faithful copy to check against.

Run with the tools venv (needs requests, beautifulsoup4, markdownify):
    .venv-tools/bin/python docs/skill-configs/fetch_verbatim.py <sources.json> <skill_dir>

<sources.json> is a list of {"url": ..., "file": ..., "mode": "raw" | "html"}.
"raw" saves the response body as-is (for llms-full.txt style markdown).
"html" keeps the page's <main> (or <body>), converts it to markdown, and lists
the id and label of any model checkbox (Open-Meteo pages), which carry the
model API names.
"""

from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify

USER_AGENT = "weatherbot-doc-skills (github.com/Smileifyouliked/1904)"
TIMEOUT_S = 30
RETRIES = 3


def fetch(url: str) -> str:
    last_error: Exception | None = None
    for attempt in range(RETRIES):
        try:
            resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=TIMEOUT_S)
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as exc:
            last_error = exc
            print(f"fetch failed ({attempt + 1}/{RETRIES}) {url}: {exc}", file=sys.stderr)
            time.sleep(2**attempt)
    raise RuntimeError(f"could not fetch {url}") from last_error


def html_to_markdown(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    # Open-Meteo renders model choices as <button role="checkbox" id="<api_name>_<group>_models">
    # with a matching <label for=...>. Keep the raw id and label; do not guess the API name.
    model_inputs = []
    for btn in soup.find_all("button", attrs={"role": "checkbox"}):
        btn_id = btn.get("id", "")
        if btn_id.endswith("_models"):
            label = soup.find("label", attrs={"for": btn_id})
            model_inputs.append((btn_id, label.get_text(" ", strip=True) if label else ""))
    for tag in soup(["script", "style", "svg", "nav", "footer", "header", "form", "button"]):
        tag.decompose()
    main = soup.find("main") or soup.body or soup
    text = markdownify(str(main), heading_style="ATX")
    text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
    if model_inputs:
        lines = [
            "",
            "## Model checkboxes on this page (raw checkbox id -> label)",
            "",
            "The id is `<api_name>_<group>_models`. Confirm an API name with a live call before use.",
            "",
        ]
        lines += [f"- `{btn_id}` -> {label}" for btn_id, label in model_inputs]
        text += "\n".join(lines) + "\n"
    return text


def main() -> None:
    sources_path, skill_dir = Path(sys.argv[1]), Path(sys.argv[2])
    out_dir = skill_dir / "references" / "verbatim"
    out_dir.mkdir(parents=True, exist_ok=True)
    fetched_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for src in json.loads(sources_path.read_text()):
        body = fetch(src["url"])
        if src["mode"] == "html":
            body = html_to_markdown(body)
        header = (
            f"<!--\nSource: {src['url']}\nFetched: {fetched_at} (UTC)\n"
            f"Mode: {src['mode']} (verbatim official text, not edited)\n-->\n\n"
        )
        (out_dir / src["file"]).write_text(header + body, encoding="utf-8")
        print(f"saved {src['file']} ({len(body)} chars) from {src['url']}")


if __name__ == "__main__":
    main()
