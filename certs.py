#Imports Required Packages from PIL
from PIL import Image, ImageDraw, ImageFont

from yagmail import SMTP, inline

#Import Pandas for better access of Data and .xlsx File
import pandas as pd

#Import the file that contains all the details
data = pd.read_excel("file.xlsx")

#Import 'Name' List from the imported .xlsx file
name_list = data['Name'].to_list()
Email_list = data['Email'].to_list()
LOGO='logo.png'


#Determining the length of the list
max_no = len(name_list)

SENDER_EMAIL = ''  # SET THIS
SENDER_EMAIL_PASSWORD = ''  # SET THIS
idpass = SMTP(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)

#The Loops for creating certificates in bulk
# for i in name_list:
for i, j in zip(name_list, Email_list):

    im = Image.open("cert.jpg")
    d = ImageDraw.Draw(im)
    location = (275, 1050)
    locationid= (100, 100)
+   id='Add your certification ID here'
    text_color = (0, 137, 209)
    font = ImageFont.truetype("AlexBrush-Regular.ttf", 250, encoding="unic")
    d.text(location, i.title(), fill=text_color,font=font)
    font = ImageFont.truetype("tnr.ttf", 50, encoding="unic")
    d.text(locationid, id, fill=text_color,font=font

    
    im.save("out/certificate_"+i+".pdf")
    print("Certificate Created for:  %s" % (i.title()))
    mailtext = 'Dear %s,\n\n. Enter your text for the automatically generated emai\n\n' % (i)
    title = 'Enter your title'
    email = j.title()
    contents = [mailtext, inline(LOGO)]
    print("Emailing this %s to %s" % (i.title(), j.title()))
    idpass.send(email, title,
        contents, attachments="out/certificate_"+i+".pdf")
    
print("""\n*************************
All Certificates Created and mailed to respective emails.
*************************
""")
#Read readme.md for further instructions