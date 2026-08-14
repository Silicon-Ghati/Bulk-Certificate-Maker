# Bulk Certificate Maker

Turn an Excel or CSV recipient list and a certificate image into personalized PDFs. Check the layout with a PNG preview, export a verification spreadsheet, and optionally email each certificate.

## Install

Requires Python 3.9 or newer.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate with `.venv\Scripts\activate` instead. The two bundled fonts are used by default; custom fonts can be passed as options.

## Prepare your files

1. Save your certificate background as `cert.jpg` (PNG and other Pillow-supported image formats also work).
2. Create `file.xlsx`, using the active worksheet, or a UTF-8 CSV with a header row:

   | Name | Email |
   | --- | --- |
   | Ada McDonald | ada@example.com |
   | Ravi Kumar | ravi@example.com |

`Name` is required. `Email` is optional when generating locally and required with `--send`. Header matching ignores case and surrounding spaces. Blank rows are skipped; missing names and malformed nonempty email addresses produce an error with the row number. Names and email addresses retain their capitalization. For Excel formulas, save the workbook in Excel or another spreadsheet app first so calculated values are available.

## Preview and generate

```sh
# Check the first recipient's layout without generating a batch or sending email.
python certs.py --preview preview.png

# Generate PDFs and out/verify.xlsx. No email is sent by default.
python certs.py

# Use CSV, a different template, and certificate numbers beginning at 031.
python certs.py --input recipients.csv --template background.png \
  --output workshop-certificates --prefix WORKSHOP- --start 31
```

Output directories are created automatically and must be new or empty. Existing batches and previews are never overwritten. Choose a different path for each run. Certificate IDs increase sequentially with at least three digits, and filenames include the ID so duplicate names remain separate.

The default name position is the image center. Long names shrink to fit 80% of its width. The ID and date are placed near the bottom. Customize the layout in **image pixels**:

```sh
python certs.py --preview adjusted-preview.png \
  --name-position 1500 1050 --name-width 2200 --font-size 250 \
  --id-position 100 2000 --date-position 2200 2000 \
  --detail-size 50 --color '#0089d1' --date '11-09-2026'
```

`--name-position` sets the name's center; ID and date positions set the top-left of their text. Text that extends outside the image produces an error. Adjust these example coordinates for your template. `--name-font` and `--detail-font` select other TrueType/OpenType fonts; choose fonts that cover your recipients' languages. Preview shows only the first recipient, so also inspect generated PDFs with unusually long names.

PDFs use 300 DPI by default; `--dpi` changes their physical print size without changing the image dimensions. For example, a 3000 × 2100 image prints at 10 × 7 inches at 300 DPI.

## Optional email delivery

Use credentials supplied by your email provider for SMTP authentication. Keep them in environment variables, never in the source code. Set `SENDER_EMAIL` to the sender address and `SENDER_EMAIL_PASSWORD` to its SMTP password or app password in your shell.

Then explicitly enable delivery:

```sh
python certs.py --send --output emailed-batch \
  --subject 'Your workshop certificate' \
  --message 'Dear {name}, your certificate {certificate_id} is attached.'
```

Email uses implicit TLS, with `smtp.gmail.com:465` as the default. Override it with `--smtp-host` and `--smtp-port` for another provider that supports implicit TLS. STARTTLS-only servers are not supported. `--logo logo.png` includes an inline image. The message supports `{name}` and `{certificate_id}`; use `{{` and `}}` for literal braces.

All PDFs and `verify.xlsx` are saved **before** connecting to the email server. Recipient delivery failures are reported, recorded in `delivery.csv`, and do not stop later recipients. The log is flushed after each attempt. An accepted message means the SMTP server accepted it, not that it reached the inbox. A connection failure during sending can leave delivery uncertain; check your provider before retrying. There is no automatic resend. A rerun into the same output directory is refused to help prevent duplicate mail.

Input, generation, or delivery failures return a nonzero exit status. A generation failure may leave partial PDFs in the output directory; inspect them and choose a new output directory after fixing the problem.

## Checks and options

```sh
python certs.py --help
python test_certs.py
```

The checks generate temporary PDFs and spreadsheets and use a mocked SMTP connection. They send no email.

This version writes `verify.xlsx` instead of the older `verify.xls` and replaces pandas, xlwt, and yagmail with openpyxl and Python's email/SMTP libraries. `defusedxml` protects Excel XML parsing.

Originally inspired by [mursalfk/Certificate-Generator](https://github.com/mursalfk/Certificate-Generator). Maintained by [Ayush R](https://www.linkedin.com/in/ayushr1/).
