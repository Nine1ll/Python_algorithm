from bs4 import BeautifulSoup
from requests import get


def extract_remote_jobs(term):
    base_url = "https://remoteok.com"
    url = f"{base_url}/remote-{term}-jobs"
    request = get(url, headers={"User-Agent": "Nine1ll"})

    results = []
    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("tr", class_="job")
        for job in jobs:
            company = job.find("h3", itemprop="name")
            position = job.find("h2", itemprop="title")
            location = job.find("div", class_="location")
            anchors = job.find_all("a", itemprop="url")
            anchor = anchors[0]
            link = anchor['href']

            if company:
                company = company.string.strip()
            if position:
                position = position.string.strip()
            if location:
                location = location.string.strip()

            if company and position and location:
                job = {
                    'company': company,
                    'position': position,
                    'location': location,
                    'link': f"{base_url}{link}"
                }
                results.append(job)
    else:
        print("Can't get jobs.")
    return results
