 read_emails.py                                                                                                                                       
   2 import email
   3 from bs4 import BeautifulSoup
   4 
   5 host = 'imap.gmail.com'
   6 username = 'abrahamssterling@gmail.com'
   7 password = '421305GaSa'
   8 
   9 def get_inbox():
  10     mail = imaplib.IMAP4_SSL(host)
  11     mail.login(username, password)
  12     mail.select("inbox")
  13     _, search_data = mail.search(None, 'UNSEEN')
  14     my_message = []
  15     for num in search_data[0].split():
  16         email_data = {}
  17         _, data = mail.fetch(num, '(RFC822)')
  18         _, b = data[0]
  19         email_message = email.message_from_bytes(b)
  20         for header in ['subject', 'to', 'from', 'date']:
  21             print('{}: {}'.format(header, email_message[header]))
  22             email_data[header] = email_message[header]
  23         for part in email_message.walk():
  24             if part.get_content_type() == 'text/plain':
  25                 body = part.get_payload(decode=True)
  26                 email_data[body] = body.decode()
  27             elif part.get_content_type() == 'text/html':
  28                 html_body = part.get_payload(decode=True)
  29                 text = BeautifulSoup(html_body).get_text('\n')
  30                 email_data['html_body'] = text
  31         my_message.append(email_data)
  32         return my_message
  33 
  34 if __name__ == '__main__':
  35     my_inbox = get_inbox()
  36     print(my_inbox)
  37 
