# Security Schemes

Authentication and authorization schemes defined in the API specification.

**Total schemes:** 2

---

## userAgent

**Type:** `apiKey`

We require that all consumers of the API include a User-Agent header in requests. This is due to a high number of scripts exhibiting abusive behavior (intentional or unintentional). We recommend setting the value to something that identifies your application and includes a contact email. This will help us contact you if we notice unusual behavior and also aid in troubleshooting issues.
The API remains open and free to use and there are no limits imposed based on the User-Agent string.
This mechanism will be replaced with a more typical API key system at a later date.


- **Parameter name:** `User-Agent`
- **Location:** `header`


## apiKeyAuth

**Type:** `apiKey`

We are testing including a more traditional API Key system on certain endpoints.  This is due to a large change in the weather.gov site.
The API remains open and free to use and there are no limits imposed based on the X-Api-Key string.


- **Parameter name:** `API-Key`
- **Location:** `header`

