# WebScraper · Product-page parsing experiment

An early **Beautiful Soup parsing script** for extracting product details from a specific Flipkart earphone-results page.

**Historical personal project · 2019 · Python / Beautiful Soup / urllib**

## What it demonstrates

`scraper.py` fetches a hard-coded results URL, locates product containers, and attempts to write model, color, rating, price, and discount fields to a text file.

## Limits

This is site-specific parsing code, not a scraper for arbitrary websites. Its selectors reflect the original page structure and have not been checked against today's site. The price/discount cleanup also contains a bug: it uses the return value of an in-place list operation, which can produce `None` instead of a cleaned number.

A useful future refresh would work from a small saved HTML fixture, fix field parsing, and test absent or malformed fields before adding any live requests. The current version is preserved as an early experiment and is not advertised as a working live scraper.
