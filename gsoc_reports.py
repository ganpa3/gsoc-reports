import requests
import os
import html5lib
from bs4 import BeautifulSoup
import json
from pprint import pprint


base = "https://summerofcode.withgoogle.com"
data = {}


def get_report_url(url):
    student_page = requests.get(url)
    student_soup = BeautifulSoup(student_page.content, "html5lib")
    return student_soup.select_one("div.org__meta div a").attrs["href"]


def get_report(soup):
    students = soup.select("h5 a")
    number_of_students = len(students)

    reports = {}
    for student in students:
        student_name = student.text
        reports[student_name] = get_report_url(base + student.attrs["href"])

    return number_of_students, reports


for year in reversed(range(2016, 2021)):
    url = "https://summerofcode.withgoogle.com/archive/" + str(year) + "/organizations/"
    orgs_page = requests.get(url)
    orgs_soup = BeautifulSoup(orgs_page.content, "html5lib")
    orgs = orgs_soup.findAll("a", class_="organization-card__link")

    for org in orgs:
        org_url = base + (org.attrs["href"])
        org_page = requests.get(org_url)
        org_soup = BeautifulSoup(org_page.content, "html5lib")
        org_name = org_soup.find("h3", class_="banner__title").text

        # Clear screen before printing next organization.
        os.system("cls" if os.name == "nt" else "clear")
        print("Currenyly scrapping:\n\n\tOrganization: {}\n\tYear: {}".format(org_name, year))

        if org_name not in data:
            data[org_name] = {}

        data[org_name][str(year)] = {}
        number_of_students, reports = get_report(org_soup)

        data[org_name][str(year)]["org_url"] = org_url
        data[org_name][str(year)]["number_of_students"] = number_of_students
        data[org_name][str(year)]["reports"] = reports


with open("data{}.json".format(year), "w") as fout:
    json.dump(data, fout, indent=4)
