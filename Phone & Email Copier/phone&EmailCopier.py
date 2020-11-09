
#! python 3
import re, pyperclip

# Create a regex for phone numbers

phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))? # area code (optional)
(\s|-) # first separator
(\d\d\d) # first 3 digits: 
- # separator:  
(\d\d\d\d) # last 4 digits      
(((ext(\.)?\s)|x) # Extension (word-part)
(\d{2,5}))? # Extension (optional)
)
''', re.VERBOSE)


# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+    # name part
@    # @ symbol
[a-zA-Z0-9_.+]+    # domain name part
''', re.VERBOSE)



# TODO: Get the text off the clipboard
text = pyperclip.paste()


# TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

extractedEmail = emailRegex.findall(text)
allEmailAddresses = []
for emailAddress in extractedEmail:
    allEmailAddresses.append(emailAddress)



# TODO: Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n'.join(allEmailAddresses)
pyperclip.copy(results)