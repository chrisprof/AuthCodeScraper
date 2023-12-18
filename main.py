from simplegmail import Gmail

gmail = Gmail()
messages = gmail.get_unread_inbox()
#On run it will open a login link to login with your personal email, HAS TO BE DONE ON HOME WINDOWS LAPTOP
#Go to google developer api and create an application, copy the client secret into client_secret.json
for message in messages:
  try:
    msg = message.plain
  except:
    msg = message.html
  msg=str(msg)

  if not msg.count('code'): 
    continue
  sender = message.sender
  subject = message.subject
  print(f"'{subject}' From {sender}\n{msg}")
    
