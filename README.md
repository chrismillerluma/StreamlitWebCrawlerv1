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
git clone https://github.com/[YOUR_USERNAME]/OpenSchedulingLinkFinder.git
cd OpenSchedulingLinkFinder
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Disclaimer
Legal Disclaimer (U.S., EU, UK, NL, AUS)
This software is provided for informational, research, and educational purposes only. It is designed to identify publicly available web resources with no authentication, credentialing, or access to secure or protected systems needed. The tool does not collect, access, or process personal data, health information, or any other sensitive or regulated data as defined under applicable laws in the United States (e.g., HIPAA), the European Union (e.g., GDPR), the United Kingdom (UK GDPR and DPA 2018), the Netherlands (UAVG), or Australia (Privacy Act 1988).

The developer of this tool: Has no affiliation, endorsement, or partnership with any third-party organization, company, health system, or intellectual property holder referenced directly or indirectly via use of the tool. Does not claim ownership of any trademarks, logos, service marks, or content retrieved through publicly available pages; all such rights remain with their respective owners.

By using this software, you agree that: You are solely responsible for ensuring your use complies with all applicable local, regional, and international laws, including but not limited to those governing data access, web scraping, intellectual property, and data protection. You assume full responsibility for any output, insight, or dataset obtained using this tool and its application in any professional or non-professional context. 

The developer shall not be held liable for any direct, indirect, incidental, special, punitive, or consequential damages arising from your use or misuse of the software, even if advised of the possibility of such damages.
No warranties, express or implied, are made regarding the accuracy, legality, reliability, or completeness of the tool or its outputs.
Use of this software constitutes your full understanding and acceptance of this disclaimer.
