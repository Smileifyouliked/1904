# SETUP.md — Tools for the Weatherbot

Do these steps in order. One step at a time. Each step says WHERE to run it.

- **Terminal** = your normal command window (Terminal on Mac/Linux, WSL on Windows).
- **Inside Claude Code** = after you type `claude` and press Enter, you type there.

Commands were checked against each project's docs on 2026-09-28. If one fails, tell
Claude Code the exact error. It will look up the current command with Firecrawl
instead of guessing.

---

## Before Step 0 (Windows only). Set up WSL 2 + Ubuntu

Run everything in this guide inside **Ubuntu (WSL 2)**, opened in the **Windows
Terminal** app. Don't use PowerShell or CMD.

1. Open **PowerShell as Administrator**. Right-click the Start button, then pick
   "Terminal (Admin)". Run:
   ```powershell
   wsl --install
   ```
   Restart your PC when it asks.
2. After the restart, Ubuntu opens by itself. Pick a username and password. The
   password won't show while you type. That's normal.
3. From now on, open **Windows Terminal**, click the **v** arrow next to the tab, and
   pick **Ubuntu**.
4. In Ubuntu, install the basic tools:
   ```bash
   sudo apt update && sudo apt install -y git python3 python3-venv python3-pip tmux curl
   ```
5. Install Claude Code inside Ubuntu, not in Windows:
   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```
   Close the terminal, open it again, and run `claude --version`.
6. Keep your repo in the Ubuntu home folder, not on your C: drive:
   ```bash
   cd ~ && git clone https://github.com/YOUR-NAME/YOUR-REPO.git && cd YOUR-REPO
   ```
   To see these files in Windows File Explorer, type `\\wsl$` in the address bar.

---

## Step 0. Check you have the basics

Run these in the **Ubuntu terminal**, one line at a time:

```bash
git --version
python3 --version
claude --version
```

**What you should see:** three version numbers. Python must be 3.10 or newer.

**Node.js is optional.** Nothing in this setup needs it right now. If you want it
anyway, for other MCP servers later, install it like this:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash
```

Close the terminal and open it again. Then run:

```bash
nvm install --lts
node --version
```

---

## Step 1. Put the setup files in your repo

Unzip `weatherbot-setup.zip`. Copy everything inside the `weatherbot-setup` folder into
your repo's main folder. That includes the hidden `.claude` folder. Then run this in the
**Terminal**, inside your repo:

```bash
echo ".venv-tools/" >> .gitignore
git add CLAUDE.md SETUP.md .claude .gitignore
git commit -m "Add Claude Code setup: CLAUDE.md, skills, setup guide"
```

**What it does:** saves the rules and skills in your repo, so every Claude Code session
uses them.

---

## Step 2. Connect Firecrawl to Claude Code (internet research)

Your Firecrawl connector on claude.ai does NOT carry over to Claude Code. You add it
separately.

**Option A (easiest, recommended): log in with your Firecrawl account.**

Run this in the **Terminal**:

```bash
claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/v2/mcp-oauth
```

Then start Claude Code (`claude`) and type `/mcp` **inside Claude Code**. Pick
firecrawl and follow the login.

**Option B: use an API key.** Get the key from your Firecrawl dashboard. It starts with
`fc-`. Then run this in the **Terminal**:

```bash
claude mcp add --transport http firecrawl https://mcp.firecrawl.dev/v2/mcp --header "Authorization: Bearer fc-YOUR-KEY"
```

⚠️ **Never** add `--scope project` to the Option B command. That flag writes your key
into a file that gets pushed to GitHub. A leaked key is like posting your GCash PIN.

**Check it worked:** inside Claude Code, type `/mcp`. Firecrawl should show as
connected.

---

## Step 3. Install Superpowers

Type this **inside Claude Code**:

```
/plugin install superpowers@claude-plugins-official
```

**What it does:** adds a plan, then test, then build workflow, so Claude Code plans
before coding.

---

## Step 4. Install Superpowers Lab (experimental)

Type these **inside Claude Code**, one at a time:

```
/plugin marketplace add obra/superpowers-marketplace
```

```
/plugin install superpowers-lab@superpowers-marketplace
```

Its tmux skill needs tmux installed. In the **Terminal**, run one of these:

```bash
sudo apt install -y tmux     # Ubuntu / WSL
brew install tmux            # Mac
```

After installing, quit Claude Code (`/exit`) and start it again (`claude`). Then type
`/plugin` to see both plugins listed.

---

## Step 5. Let Claude Code install Skill Seekers and build the doc skills

Start Claude Code in your repo and paste this:

```
Read CLAUDE.md. Do the Setup phase only. Install Skill Seekers in .venv-tools
(not the bot's environment), build the doc skills listed in <tools_and_plugins>,
spot-check each with Firecrawl, then report in the required format and stop.
Explain everything to me like a beginner.
```

**For reference:** these are the commands Claude Code will roughly run. You don't need
to type them yourself.

```bash
python3 -m venv .venv-tools
.venv-tools/bin/pip install skill-seekers
.venv-tools/bin/skill-seekers create <docs-url>
.venv-tools/bin/skill-seekers package output/<name> --target claude
```

---

## Step 6. Start the real work

When the Setup report looks good, tell Claude Code:

```
Start Phase 0 only.
```

It stops after each phase. Read the "In Plain Words" part of its report. Say "go" when
you're ready for the next phase.
