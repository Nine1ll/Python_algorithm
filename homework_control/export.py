import re


def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding='UTF-8')
    file.write("position,Company,Location,URL\n")

    for job in jobs:

        location_ = job['location']
        location = re.sub('[^A-Za-z0-9]','', location_)

        file.write(
            f"{job['position']},{job['company']},{location},{job['link']}\n"
        )

    file.close()
