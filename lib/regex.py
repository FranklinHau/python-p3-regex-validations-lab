import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^[A-Z'][a-zA-Z'-]*(?: [A-Z'][a-zA-Z'-]*)*$"
name_regex = re.compile(name)
# This regular expression is used to match names. Here's the breakdown:

# ^: Asserts the beginning of the string.
# [A-Z']: Matches a single uppercase letter or an apostrophe.
# [a-zA-Z'-]*: Matches zero or more occurrences of lowercase letters, uppercase letters, hyphens, and apostrophes.
# (?: [A-Z'][a-zA-Z'-]*)*: This is a non-capturing group. It matches zero or more occurrences of a space followed by an uppercase letter or an apostrophe and more letters, hyphens, or apostrophes.
# $: Asserts the end of the string.
# In simpler terms, this regular expression will match names that:

# Start with an uppercase letter or an apostrophe (e.g., "John" or "'Angelo").
# Can have any number of letters, hyphens, and apostrophes after the first character (e.g., "John Cena" or "'Angelo D'Angelo").
# import re
# name = "John Cena"
# if name_regex.fullmatch(name):
#     print("Valid name:", name)
# else:
#     print("Invalid name:", name)

phone_number = r"^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$"
phone_regex = re.compile(phone_number)

# This regular expression is used to match phone numbers in different formats. Here's the breakdown:

# ^: Asserts the beginning of the string.
# \(?\d{3}\)?: Matches an optional opening parenthesis, followed by three digits, and an optional closing parenthesis (e.g., "(555)" or "555").
# [-.\s]?: Matches an optional hyphen, dot, or space.
# \d{3}: Matches three digits.
# [-.\s]?: Matches an optional hyphen, dot, or space.
# \d{4}: Matches four digits.
# $: Asserts the end of the string.
# In simpler terms, this regular expression will match phone numbers that can be in various formats, such as "(555) 555-5555", "555.555.5555", "555 555 5555", or "5555555555".
# import re

# phone_number = "555-555-5555"
# if phone_regex.fullmatch(phone_number):
#     print("Valid phone number:", phone_number)
# else:
#     print("Invalid phone number:", phone_number)
email_address = r"^[a-zA-Z._%+-][a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
email_regex = re.compile(email_address)

# This regular expression is used to match email addresses. Here's the breakdown:

# ^: Asserts the beginning of the string.
# [a-zA-Z._%+-]: Matches a single character from the set of lowercase letters, uppercase letters, and the special characters ". _ % + -". This ensures that the email address starts with a letter or one of these special characters.
# [a-zA-Z0-9._%+-]*: Matches zero or more occurrences of letters, digits, and the special characters ". _ % + -".
# @: Matches the "@" symbol.
# [a-zA-Z0-9.-]+: Matches one or more occurrences of letters, digits, dots, and hyphens. This represents the domain name.
# \.: Matches the dot symbol (escaped with a backslash).
# [a-zA-Z]{2,}: Matches two or more occurrences of letters. This represents the top-level domain (e.g., ".com" or ".org").
# $: Asserts the end of the string.
# In simpler terms, this regular expression will match email addresses that:

# Start with a letter or one of the special characters ". _ % + -".
# Can have any combination of letters, digits, dots, and hyphens before the "@" symbol.
# Have a domain name consisting of letters, digits, dots, and hyphens, followed by a top-level domain with at least two letters (e.g., "example@example.com" or "user.name123@example.co.uk").
# import re

# email = "john.doe@example.com"
# if email_regex.fullmatch(email):
#     print("Valid email address:", email)
# else:
#     print("Invalid email address:", email)

