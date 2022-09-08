from bs4 import BeautifulSoup
from requests import get

# # 회사 이름
# tbody의 "td", class_="company position company_and_position"
# 저 안에 "sapn", class_="companyLink" 안의 "h3" .string 가져오면 될듯
# (가능하면 span 생략)

# # position
# tbody까지는 똑같이 가져오고 안의 "a", class_="preventLink" 안의 "h2" .string 으로 가져오기
# 위와 마찬가지로 span 생략 가능시 생략

# # region
# "td", class_="company position company_and_position" 안의 "div", class_="location"[0] .string
# location[1]은 연봉인거 같음( 월급일지도)


def extract_jobs(term):
    url = f"https://remoteok.com/remote-{term}-jobs"
    request = get(url, headers={"User-Agent": "Nine1ll"})

    if request.status_code == 200:
        results = []
        soup = BeautifulSoup(request.text, "html.parser")
        # write your ✨magical✨ code here
        jobs = soup.find_all("table", id="jobsboard")

        for job_section in jobs:
            companies_source = job_section.find_all("td", class_="company position company_and_position")
            # print(companies_source)

            for company_source in companies_source:
                company = company_source.h3.string
                position = company_source.h2.string
                regions = company_source.find_all("div")

                if len(regions) != 0:
                    region = regions[0].string
                    if '$' in region:
                        try:
                            region = regions[1].string
                        except IndexError:
                            region = "None"
                    job_data = {
                        "company": company.strip(),
                        "region": region.strip(),
                        "position": position.strip()
                    }
                    results.append(job_data)

        return results

    else:
        print("Can't get jobs.")


user_language = input("Enter the programming language for the job you are looking for: ")

for result in extract_jobs(user_language):
    print("--------------------------------------------------")
    print(f"Company: {result['company']}\nRegion: {result['region']}\nPosition: {result['position']}")
    print("--------------------------------------------------")
#
# from bs4 import BeautifulSoup
# import requests
#
#
# def extract_jobs(term):
#     url = f"https://remoteok.com/remote-{term}-jobs"
#     request = requests.get(url, headers={"User-Agent": "Kimchi"})
#     results = []
#     if request.status_code == 200:
#         soup = BeautifulSoup(request.text, "html.parser")
#         jobs = soup.find_all("tr", class_="job")
#         for job in jobs:
#             company = job.find("h3", itemprop="name")
#             position = job.find("h2", itemprop="title")
#             location = job.find("div", class_="location")
#             if company:
#                 company = company.string.strip()
#             if position:
#                 position = position.string.strip()
#             if location:
#                 location = location.string.strip()
#
#             if company and position and location:
#                 job = {
#                     'company': company,
#                     'position': position,
#                     'location': location
#                 }
#                 results.append(job)
#     else:
#         print("Can't get jobs.")
#     return results
#
#
# jobs = extract_jobs("golang")
# print(jobs)
