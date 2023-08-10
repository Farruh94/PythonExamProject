"""Checks the contents of folders and selects 'html' files and checks the contents of the matched
files."""


import os

from bs4 import BeautifulSoup

PATH = "C:\\Users\\Kamaz\\PycharmProjects\\PythonExamProject\\app"


def directory_lookup():
    """Check the contents of a directory for html files."""
    html_list = []
    for address, dirs, files in os.walk(PATH):
        for name in files:
            if name.endswith(".html"):
                html_list.append(os.path.join(address, name))
    return html_list


def check_html_content(directory_lookup):
    """
    Checking the contents of selected html files
    :param directory_lookup: function returns list of html files
    :return: Returns files and strings with missing labels
    """
    tags_to_check = ["p", "button", "h2", "h"]
    mark = "i18n"
    for i in directory_lookup:  # Going through the list of html files.
        with open(i, "r") as file:
            lines = file.readlines()  # Read the lines.
            for number_of_line, line in enumerate(lines, start=1):  # Output the rows with their
                # number.
                for tag in tags_to_check:
                    if tag in line:
                        soup = BeautifulSoup(line, "lxml")
                        for elem in soup.find_all(tag):  # Going by tags.
                            if not elem.has_attr(mark):  # If we don't find an attribute with a
                                # mark, then we show where and which tag, and on which line.
                                print(f"Tag {tag} not contain {mark} in file {os.path.abspath(i)} "
                                      f"at  line {number_of_line}: {elem}")
