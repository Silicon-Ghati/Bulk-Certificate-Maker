#Imports Required Packages from PIL
from PIL import Image, ImageDraw, ImageFont

from yagmail import SMTP, inline

#Import Pandas for better access of Data and .xlsx File
import pandas as pd

#Import the file that contains all the details
data = pd.read_excel("file.xlsx")

#export id to excel sheet
import xlwt
from xlwt import Workbook

#Import 'Name' List from the imported .xlsx file
name_list = data['Name'].to_list()
Email_list = data['Email'].to_list()
LOGO='logo.png'


#Determining the length of the list
max_no = len(name_list)

SENDER_EMAIL = ''  # SET THIS
SENDER_EMAIL_PASSWORD = ''  # SET THIS
idpass = SMTP(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)

#create excel sheet
book = xlwt.Workbook(encoding="utf-8")

sheet = book.add_sheet("Sheet")

sheet.write(0, 0, "Name")
sheet.write(0, 1, "Email")
sheet.write(0, 2, "Certificate ID")

#The Loops for creating certificates in bulk

for i, (mname, memail) in enumerate(zip(name_list, Email_list)):

    im = Image.open("cert.jpg")
    d = ImageDraw.Draw(im)
    location = (275, 1050)
    locationid= (100, 100)
    id = 'Add your certification ID here %d' % (i+1)
    text_color = (0, 137, 209)
    font = ImageFont.truetype("AlexBrush-Regular.ttf", 250, encoding="unic")
    d.text(location, mname.title(), fill=text_color, font=font)
    font = ImageFont.truetype("tnr.ttf", 50, encoding="unic")
    d.text(locationid, id, fill=text_color,font=font)
    im.save("out/certificate_"+mname+".pdf")
    print("Certificate Created for:  %s" % (mname.title()))
    print("Exporting data to excel sheet")
    sheet.write((i+1), 0, (mname.title()))
    sheet.write((i+1), 1, (memail.title()))
    sheet.write((i+1), 2, (id))
    book.save("out/verify.xls")
    
    mailtext = 'Dear %s,\n\n. Enter your text for the automatically generated emai\n\n' % (mname)
    title = 'Enter your title'
    email = memail.title()
    contents = [mailtext, inline(LOGO)]
    print("Emailing this %s to %s" % (mname.title(), memail.title()))
    idpass.send(email, title,
        contents, attachments="out/certificate_"+mname+".pdf")
    
print("""\n*************************
All Certificates Created and mailed to respective emails.
*************************
""")
#Read readme.md for further instructions