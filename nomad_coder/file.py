def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w",encoding='UTF-8')
    file.write("position,Company,Location,URL\n")

    for job in jobs:
        file.write(
            f"{job['position']},{job['company']},{job['location']}\n"
        )

    file.close()
