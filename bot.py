from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import smtplib
import requests

sender = 'pythonbott25@gmail.com'
receivers = ['pythonbott25@gmail.com']
body_of_email = 'Graafikakaardi hind langes teie soovitud hinnale! Siin on link: https://www.klick.ee/graafikakaart-gigabyte-geforce-rtx-3090-vision-oc-24gb'
msg = MIMEText(body_of_email, 'plain')
# html_body_of_email = '<h1>The html body of the email</h1>'
# msg = MIMEText(html_body_of_email, 'html')
msg['Subject'] = 'Graafikakaardi hind langes'
msg['From'] = sender
msg['To'] = ','.join(receivers)

URL = "https://www.klick.ee/graafikakaart-gigabyte-geforce-rtx-3090-vision-oc-24gb"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

price = soup.find("div", class_="formatted-price relative")

if "3149" in price.contents[0]:

    s = smtplib.SMTP_SSL(host='smtp.gmail.com', port=465)
    s.login(user='pythonbott25@gmail.com', password='pythonbot')
    s.sendmail(sender, receivers, msg.as_string())
    s.quit()
