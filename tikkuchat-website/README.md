# TIKKUCHAT website
Static site (no build step). Output directory: `public`. Forms: `functions/api/contact.js`.
## Deploy on Cloudflare Pages
1. Push this folder to GitHub. Cloudflare > Workers & Pages > Create > Pages > connect repo.
2. Build command: (none). Output directory: `public`.
3. Settings > Variables and Secrets: RESEND_API_KEY, TURNSTILE_SECRET, TO_EMAIL, FROM_EMAIL (e.g. "TIKKUCHAT <noreply@tikkuchat.com>").
4. Replace TURNSTILE_SITE_KEY in public/contact/index.html (or in build.py) with your Turnstile site key.
5. Custom domains: add tikkuchat.com and www.
## Staging
`STAGING=1 python3 build.py` adds noindex and blocks crawlers. Rebuild without it for launch.
## Regenerate pages
Edit build.py (copy, services, industries) and run `python3 build.py`.
