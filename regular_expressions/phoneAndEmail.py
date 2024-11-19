import pyperclip
import re

# Define the regex for phone numbers
phoneRegex = re.compile(r'''
    (\(?\d{3}\)?)?          # Area code (optional, with or without parentheses)
    (\s|\.|-)?              # Separator (optional)
    (\d{3})                 # First three digits
    (\s|\.|-)               # Separator
    (\d{4})                 # Last four digits
    (?:\s*x(\d+))?          # Extension (optional)
''', re.VERBOSE)

# Define the regex for email addresses
emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')

# Find matches in the clipboard text
text = str(pyperclip.paste())

matches = []

# Extract phone numbers
for groups in phoneRegex.findall(text):
    phoneNum = ''.join(filter(None, [groups[0], groups[2], groups[3], groups[4]]))  # Joining only non-empty groups
    if groups[5]:  # Check if extension exists
        phoneNum += ' x' + groups[5]  # groups[5] is the extension
    matches.append(phoneNum)

# Extract email addresses
for groups in emailRegex.findall(text):
    matches.append(groups)

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')