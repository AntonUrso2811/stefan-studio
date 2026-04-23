# Holding site — ursoandco.co.uk

First deliverable. One page. Hero lockup + tagline + three-paragraph positioning + single CTA (Cal.com) + compliance footer.

- `index.html` — structure
- `site.css` — layout on top of `../02-tokens/colors_and_type.css` (palette + type tokens)
- Assets pulled from `../04-logos/` (wordmark-lockup.svg, favicon.ico)

**One ox-blood mark:** the CTA inverts from Ink → Ox-blood on hover / focus. Nothing else is ox-blood on this page.

**Banned on this page:** JS, gradients, shadows, icons, emoji, hashtags, stock imagery, forms. Restraint is the aesthetic.

For production deploy:
- inline Google Fonts `<link rel="preconnect">` + the families in the `<head>` (currently pulled via CSS `@import` for prototype fidelity — swap to `<link>` tags for LCP in production)
- swap relative paths (`../04-logos/`, `../02-tokens/colors_and_type.css`) for absolute site paths
- replace `[COMPANY_NO]` placeholder once Companies House registration is back
- point Cal.com URL once account is live
