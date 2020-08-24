import datetime
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#API Auth
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
client = gspread.authorize(credentials)
print("Authorized.")
sheet = client.open("Borneman").sheet1

#When to run
lastup = sheet.cell(3,11, value_render_option = "UNFORMATTED_VALUE").value
print("Last updated:", lastup)
t_info = datetime.datetime.today()
day = t_info.weekday()
print("Current day:", day)

#GenParams
nstudents = len(sheet.col_values(1))
print(nstudents - 1, " students found.")
i = 1

def update_caps(stacks, caps, prob):
    if stacks == 3:
        prob = 1
        sheet.update_cell(i + 1, 9, str(prob))
        caps = 1
    if stacks > 3:
        caps = stacks - 2
    if stacks > 6:
        caps = 5
    if stacks == 0 and prob == 1:
        prob = 0
        caps = 0
    sheet.update_cell(i + 1, 8, str(caps))
    sheet.update_cell(i + 1, 9, str(prob))

#Weekday run
if day != lastup and day != 5 and day != 6:
    #Update time
    print("Updating time.")
    sheet.update_cell(3,11, str(day))
    sheet.update_cell(2,11, str(t_info))
    print("Time updated.")

    #Iterate
    print("Main loop.")
    while i < nstudents:
        studentinfo = sheet.row_values(i + 1)
        t = studentinfo[day + 1]
        stacks = int(sheet.cell(i+1, 7).value)
        caps = int(sheet.cell(i+1, 8).value)
        prob = int(sheet.cell(i+1, 9).value)
        #InSanitize
        if t == "T":
            t = "t"
        #Stack update
        print("Updating student ", i, " of ", nstudents - 1)
        if t == "t" and prob == 0:
            stacks += 1
        if t == "t" and prob == 1:
            stacks += 2
        if stacks < 4 and stacks > 0 and prob == 1:
            stacks -= 1
        if stacks > 3:
            stacks -= 1
        sheet.update_cell(i + 1, 7, str(stacks))
        #Cap and Prob
        update_caps(stacks, caps, prob)
        i += 1
    print("Done!")

#Weekend run
elif day != lastup and day == 6:
    #Update time
    print("Updating time.")
    sheet.update_cell(3,11, str(day))
    sheet.update_cell(2,11, str(t_info))
    print("Time updated.")

    #Iterate
    print("Main loop.")
    while i < nstudents:
        stacks = int(sheet.cell(i+1, 7).value)
        caps = int(sheet.cell(i+1, 8).value)
        prob = int(sheet.cell(i+1, 9).value)
        amn = int(sheet.cell(i+1, 12).value)
        weeks = int(sheet.cell(i+1, 10).value)
        #Stack reset, streak, and quiz exception
        print("Updating student ", i, " of ", nstudents - 1)
        if stacks == 0 and prob == 0:
            weeks += 1
        if stacks == -1 and prob == 0:
            weeks += 1
        if stacks < 3 and stacks > 0 and prob == 0:
            stacks = 0
        if amn == 1 and prob == 1 and stacks > 1:
            stacks -= 2
            amn = 0
        elif amn == 1 and prob == 1 and stacks == 1:
            stacks -= 1
        elif amn == 1 and prob == 0:
            stacks = -1
            amn = 0
        sheet.update_cell(i + 1, 7, str(stacks))
        sheet.update_cell(i + 1, 10, str(weeks))
        sheet.update_cell(i + 1, 12, str(amn))
        update_caps(stacks, caps, prob)
        i += 1
    print("Done!")
else:
    #Update time
    print("Updating time.")
    sheet.update_cell(3,11, str(day))
    sheet.update_cell(2,11, str(t_info))
    print("Time updated.")
i = 1
