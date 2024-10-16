# Project 1. Phone Number and Email Address Extractor 
import  re

phoneRegex = re.compile(r'(\d{3}|\(\d{3}\)?(\s|\.|-)?(\d{3})(\s|\.|-)?(\d{4}))')
number = phoneRegex.search('(333) 444-2345')

# This regex is designed to match different phone number formats:
# 1. It matches an area code of 3 digits either with or without parentheses:
#    - \d{3} matches the area code without parentheses (e.g., 123)
#    - \(\d{3}\)? matches the area code with optional parentheses (e.g., (123))
# 2. After the area code, it matches an optional separator (space, dot, or dash):
#    - (\s|\.|-)?, where \s matches a space, \. matches a dot, and - matches a dash.
#    The separator is optional.
# 3. It then matches the next 3 digits of the phone number.
# 4. Again, it matches an optional separator (space, dot, or dash).
# 5. Finally, it matches the last 4 digits of the phone number.
# This allows for flexible formats such as: 
# - 123-456-7890
# - (123) 456-7890
# - 123 456 7890
# - (123)456.7890
# - 1234567890

# Create email regex
emailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4})')
email = emailRegex.search('test.email+filter@sub.domain.co')

# This regex matches a standard email format:
# - Local part: Allows letters (a-z, A-Z), digits (0-9), and special characters (._%+-)
# - Domain part: Allows letters, digits, dots, and hyphens
# - Top-level domain: Requires a period followed by 2 to 4 letters (e.g., .com, .org)

print(number.group(), email.group())