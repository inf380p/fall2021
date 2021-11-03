 ---
layout: post
author: <YitongFeng726>
title: "YitongFeng's first post!"
--- 
  
# Open file in read mode
with open("mbox-short.txt3", "r") as filename:
# Create an email_count dictionary
   email_count = {}
# Create variable for lines of the file
    messages = filename.readlines()
# Traverse each email (each line)
    for message in messages:
# Assign the key and value to elemets of the email
        key = message.split()[0]
        value = message.split()[1]
# Check if key is not in dictionary then add key value pair into dictionary
        if key not in message_count.keys():
            message_count[key] = value
# Create initial variable to count emails
max_emails = 0
# Traverse keys in dictionary
for key in message_count.keys():
    # Check if key is larger than the max emails then reassign max-e-mails to key
    if int(message_count[key]) >= max_emails:
        max_emails = int(message_count[key])
print(max_emails)
