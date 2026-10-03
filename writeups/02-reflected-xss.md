# Reflected XSS into HTML context with nothing encoded

**Type:** Cross-Site Scripting (reflected) — OWASP A03: Injection
**Target:** PortSwigger Web Security Academy lab (training environment)
**Date:** 2026-10-03
**Status:** Exploited ✅

## Summary
The blog search function reflects user input directly into the page HTML with no
encoding, allowing arbitrary JavaScript to run in the browser of anyone who opens
the crafted URL.

## Steps to reproduce
1. Open the blog and use the search box (parameter `search`).
2. Submit the payload: `<script>alert(1)</script>`
3. The page reflects it unencoded; the browser executes it → alert fires.

## Payload
<script>alert(1)</script>

## Why it works
The server embeds the raw `search` value into the HTML response. With no output
encoding, `<script>` is parsed as real markup and runs in the site's own origin.

## Impact
Arbitrary JS execution in a victim's browser: steal session cookies, act as the
user, deface pages, or redirect to phishing sites. Reflected XSS needs the victim
to click a crafted link.

## Remediation
- Context-aware output encoding (HTML-encode input before rendering)
- Content-Security-Policy (CSP) header
- Validate / whitelist input
