import streamlit as st
import requests
import beautifulsoup4
import pandas as pd
import concurrent.futures

PATHS = [
    "/mychart/openscheduling",
    "/MyChart/openscheduling",
    "/OpenScheduling/SignupAndSchedule/EmbeddedSchedule",
    "/mychart/OpenScheduling/SignupAndSchedule/EmbeddedSchedule",
    "/find-a-doctor/?query=&onlineScheduling=1",
    "/find-a-doctor/?query=",
    "/mychartmcmprd/OpenScheduling/Standalone?",
    "/mychartmcmprd/OpenScheduling/",
    "prd/OpenScheduling/",
    "/OpenScheduling/"
]

st.set_page_config(page_title="Epic Open Scheduling Finder", layout="wide")
st.title("🌐 Epic MyChart Open Scheduling Finder")
st.markdown("Enter one domain per line or upload a CSV file.")

domains_input = st.text_area("Enter domains (e.g. `mychart.rush.edu`):", height=150)
uploaded_file = st.file_uploader("Or upload a CSV with domains", type=["csv"])

domains = []
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    domains = df.iloc[:, 0].dropna().tolist()
elif domains_input:
    domains = [d.strip() for d in domains_input.splitlines() if d.strip()]

def crawl_domain(domain):
    for path in PATHS:
        url = f"https://{domain}{path}"
        try:
            r = requests.get(url, timeout=6)
            if r.ok and "schedule" in r.text.lower():
                soup = BeautifulSoup(r.text, "html.parser")
                title = soup.title.string.strip() if soup.title else "No title"
                return {"Domain": domain, "URL": url, "Title": title}
        except:
            continue
    return {"Domain": domain, "URL": "", "Title": "❌ Not Found"}

if st.button("🔍 Run Scanner"):
    if not domains:
        st.warning("Please enter or upload domains.")
    else:
        st.info(f"Scanning {len(domains)} domains...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(crawl_domain, domains))

        df_results = pd.DataFrame(results)
        st.success("✅ Scan complete!")
        st.dataframe(df_results)

        csv = df_results.to_csv(index=False).encode("utf-8")
        st.download_button("📥 Download CSV", csv, "open_scheduling_links.csv", "text/csv")
