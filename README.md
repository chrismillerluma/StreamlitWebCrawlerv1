# 🔗 OpenSchedulingLinkFinder

OpenSchedulingLinkFinder is a web-based Streamlit application designed to identify publicly accessible MYC Open Scheduling hyperlinks published by hospitals and health systems worldwide. The goal is to build a comprehensive dataset that reveals how different organizations implement open scheduling, what types of services are being offered, lead-times, analysis of adoption patterns, usability gaps, and digital front-door strategies. These insights can help inform the development of tools and best practices that improve patient access, reduce administrative burden, and support a more efficient, consumer-friendly healthcare experience—where the experience is frictionless, transparent, and accessible to all.

## Features
- Input a list of domains or upload a CSV
- Crawl each domain for known open scheduling paths
- Export results to CSV
- 100% web-based — no installation needed

## Run Online

### Option 1: [Streamlit Cloud](https://streamlit.io/cloud)
1. Push this repo to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app, select this repo, and deploy

### Option 2: Hugging Face Spaces
1. Create a new Space with the Streamlit SDK
2. Upload this project and deploy

## Local Development

```bash
git clone https://github.com/YOUR_USERNAME/OpenSchedulingLinkFinder.git
cd OpenSchedulingLinkFinder
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Disclaimer
This tool scans publicly accessible scheduling pages and does not authenticate or scrape protected content.
