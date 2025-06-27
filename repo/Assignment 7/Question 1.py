import re

email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
mobile_pattern = r"^[6-9]\d{9}$"
alpha_pattern = r"^[A-Za-z]+$"
digit_pattern = r"^\d+$"


def is_valid_mobile(mobile):
    return bool(re.match(mobile_pattern, mobile))


def is_alpha(text):
    return bool(re.match(alpha_pattern, text))


def is_digit(text):
    return bool(re.match(digit_pattern, text))


def is_valid_email(email):
    try:
        local, domain = email.split("@")
        if not local or not domain:
            return False
        if "." not in domain:
            return False
        if domain.startswith(".") or domain.endswith("."):
            return False
        if ".." in email:
            return False
        return True
    except ValueError:
        return False


email = input("Enter email: ")
(
    print("Valid email format")
    if (is_valid_email(email))
    else print("Invalid email format")
)

mobile = input("Enter mobile number: ")
(
    print("Valid mobile number")
    if (is_valid_mobile(mobile))
    else print("Invalid mobile number")
)

alpha = input("Enter alphabetic string: ")
(
    print("Valid alphabetic string")
    if (is_alpha(alpha))
    else print("Invalid alphabetic string")
)

digit = input("Enter digit string: ")
print("Valid digit string") if (is_digit(digit)) else print("Invalid digit string")
