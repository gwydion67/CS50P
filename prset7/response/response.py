from validator_collection import validators
try:
    email = validators.email(input("what is your email address? "))
    print('Valid')
except:
    print("Invalid")
