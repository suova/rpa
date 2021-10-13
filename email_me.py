import smtplib
from email.message import EmailMessage


def send_an_email(receiver_address, email, password, subject, path_to_file):

    message = EmailMessage()
    message['From'] = email
    message['To'] = receiver_address
    message['Subject'] = subject

    with open(path_to_file, 'rb') as f:
        file_data = f.read()
        file_name = path_to_file
    message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(email, password)
    text = message.as_string()
    session.sendmail(email, receiver_address, text)
    session.quit()
