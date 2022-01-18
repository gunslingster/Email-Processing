import win32com.client 
import codecs
import datetime

name = input('Enter your first name: ')
inbox = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI").GetDefaultFolder(6)
corpus = codecs.open(f'{name}_email_corpus.txt', 'w', 'utf-8')
messages = inbox.Items
for message in messages:
    subject = message.Subject
    body = message.body
    corpus.write(subject + '\n')
    corpus.write(body + '\n')
