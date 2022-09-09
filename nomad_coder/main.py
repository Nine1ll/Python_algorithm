from extractors.wwr import extract_wwr_jobs
from extractors.remote import extract_remote_jobs
from file import save_to_file


keyword = input("What do you want to search for?: ")

remote = extract_remote_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
# extractor에 링크 추가 필요!
jobs = remote + wwr

save_to_file(keyword, jobs)
