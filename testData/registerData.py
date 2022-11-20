import secrets

# first name and last name


firstName = "Mahim"
lastName = "Rezwan"

# date of birth : day, month, year
date = "21"
month = "April"
year = "1998"


# Email Field
def email_generator():
    return f"{secrets.token_hex(8)}@gmail.com"


email = email_generator()
# Company field
company = "Red.Digital Limited"

# password
password = "Robi@123"
