import os, re, csv

# get current dir of script
dir = os.getcwd()

# get current_files in dir that are .msg
current_files = os.listdir(dir)

email_messages = [email for email in current_files if email.endswith('.msg')]

print email_messages
# look for text starting with 'X-Original' followed by whitespace followed by words/digits/specials char, followed by an at sign...
regex_to_email = re.compile(r'X-Original-To:\s*([\w\d\.-]+@[\w\d\.-]+)')
# look for text starting with 'From:' followed by whitespace followed by words/digits/specials char, followed by an at sign...
# regex_from_email = re.compile(r'From:\s*(\"?\w*\s*)*<([\w\d\.-]+@[\w\d\.-]+)>')
regex_from_email = re.compile(r'From:\s*(\"\w*\s\w*\"\s)<([\w\d\.-]+@[\w\d\.-]+)')
# match the remainder of the pattern following (?m)^ until the end of a line $ and capture the group of text
regex_subject = re.compile(r'(?m)^Subject: (.+)$')  # this also works in some instance Subject:\s?(.+)

to_email_list = []
from_email_list = []
subject_list = []

# loop through current file list & perform actions
for email in email_messages:
    open_file = open(email)
    email_data = open_file.read()
    open_file.close()

    print regex_from_email,email_data
    to_email_addresses = re.search(regex_to_email, email_data)


    if to_email_addresses:
        to_email_list.append(to_email_addresses.group(1))

    from_email_addresses = re.search(regex_from_email, email_data)
    if from_email_addresses:
        # print(from_email_addresses.group(2)
        from_email_list.append(from_email_addresses.group(2))

    subjects = re.search(regex_subject, email_data)
    if subjects:
        subject_list.append(subjects.group(1))

# write results to a csv file.  The "w" mode means that the existing file is wiped and a new one is created. an 'a' mode means info is appended to the old file
with open('results.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    # the zip method aggregates elements from each of the lists into one iterable
    zipped = zip(to_email_list, from_email_list, subject_list)
    print(zipped)
    for row in zipped:
        writer.writerow(row)