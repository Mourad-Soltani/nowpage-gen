# NowPage Generator

A minimal, zero-dependency CLI tool that generates a clean, responsive single-file "Now Page".

Perfect for indie hackers and solo founders who want a simple `/now` page without setting up a full site.

## Signature

**Mourad.Soltani**

## Features

- Single HTML file output
- Responsive, dark/light mode aware
- No dependencies beyond Python 3.11+
- Instant generation

## Usage

```bash
python nowpage_gen.py \
  --name "Alex Rivera" \
  --currently "Shipping a micro-SaaS for freelancers and writing daily" \
  --projects "Waitlist tool, Personal site, Open source CLI" \
  --location "Lisbon, Portugal" \
  --output now.html
```

Then open `now.html` or drop it into any static host (GitHub Pages, Netlify, etc.).

## Health Tests

```bash
pip install pytest
pytest
```

## License

MIT — see LICENSE

Built by Mourad.Soltani
