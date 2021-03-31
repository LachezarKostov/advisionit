import os
import csv


def list_of_files_in_folder(dir):
    file_names = os.listdir(dir)
    result = []
    for file_name in file_names:
        result.append(os.path.abspath(os.path.join(dir, file_name)))

    return result


def csv_to_list(list_of_files):
    list_of_urls = []
    for file in list_of_files:
        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            list_of = []
            for row in csv_reader:
                list_of.append(row[0])
        list_of_urls.append(list_of)
    return list_of_urls
