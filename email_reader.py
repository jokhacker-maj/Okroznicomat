import imaplib
import email
import credentials


user = credentials.email

password = credentials.geslo

imap_url = 'imap.gmail.com'

my_mail = imaplib.IMAP4_SSL(imap_url)


my_mail.login(user, password)


my_mail.select('Inbox')

#For other keys (criteria): https://gist.github.com/martinrusev/6121028#file-imap-search
key = 'FROM'
value = 'andrej.smrdu@gimvic.org'
_, data = my_mail.search(None, key, value)  #Search for emails with specific key and value

mail_id_list = data[0].split()  #IDs of all emails that we want to fetch 



def get_messages():
    msgs = [] # empty list to capture all messages
    #Iterate through messages and extract data into the msgs list
    for num in mail_id_list:
        typ, data = my_mail.fetch(num, '(RFC822)') #RFC822 returns whole message (BODY fetches just body)
        msgs.append(data)


    final_message = []


    for msg in msgs[::-1]:
        for response_part in msg:
            if type(response_part) is tuple:
                my_msg=email.message_from_bytes((response_part[1]))
                for part in my_msg.walk():  
                    if part.get_content_type() == 'text/plain':
                        a = (part.get_payload())
                        a = a.replace("\r\n" , "")
                        final_message.append(a)
    return(final_message)
