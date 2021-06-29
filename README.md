**:star2: this repo if it helped you**
# Certificate-Generator
This script can create bulk amount of certificates in a fraction of :hourglass_flowing_sand: ..
Mail them to respective email ids and save the data of the certificates for verification purposes

## Prep. To Generate Certificates :blue_book::pencil2:
- Design your certificate with name cert.jpg and put inside root folder
- Determine the coordinates for the name,id,date to be placed on the certificate
- Put your font on root folder and set its name as fontname.ttf, fontid.ttf
- keep the excel .xlsx file in root with name file.xlsx
- Make Sure the .xlsx file has following column in exact same shape:
  - Name
  - Email
- Enter you mail,pass from which you will send in send mails in SENDER_EMAIL, SENDER_EMAIL_PASSWORD respectively
- Enter what you want to write for title, contents of mail in "title", "mailtext" respectively
- Enter your uid for certificate in id
- Make a folder named out in the same directory.
- Star this repo

# You are ready to run :heavy_check_mark:
+ Install python and the dependancies required to run this script
  + **_python3 certs.py_**

# Your certificates would be there in out directory, emailed to respective mails & an excel sheet would be created with uid, name and email

# Troubleshooting
- make sure to install the dependencies required by the script.
  use "pip install **"
  whatever dependency is needed for you
- If you cant send the mails turn on thirdy party access in email account settings.

# Get in Touch with me :link:
* [AyushR1's LinkedIn](https://www.linkedin.com/in/ayushr1/)

Script inspired from https://github.com/mursalfk/Certificate-Generator Get in Touch with him 
 [LinkedIn](https://www.linkedin.com/in/mursalfurqan/)
 [Dev.to](https://dev.to/mursalfk)