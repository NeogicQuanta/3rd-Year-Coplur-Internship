import hashlib as hash, sqlite3 as sql
import getpass
import re


def bro_getpass(prompt):
    while True:
        # Password: 8+ chars, at least one letter, one number, one special char
        password_pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*\W).{8,}$"
        password = getpass.getpass(prompt)
        if (
            password != "null"
            and password != "None"
            and password != ""
            and re.match(password_pattern, password)
        ):
            return password
        print(
            """
            \t\t\t\tPassword cannot be empty.
            \t\t\t\tIs at least 8 characters long
            \t\t\t\tHas at least one letter
            \t\t\t\tHas at least one digit
            \t\t\t\tHas at least one special character
            \t\t\t\tPlease try again.
        """
        )


def bro_input(prompt):
    username_pattern = r"^[a-zA-Z0-9_]{3,20}$"
    while True:
        user_input = input(prompt)
        if (
            user_input != "null"
            and user_input != "None"
            and user_input != ""
            and re.match(username_pattern, user_input)
        ):
            return user_input
        print("\t\t\t\tInput cannot be empty. Please try again.")


def bro_choice(prompt):
    while True:
        choice = input(prompt)
        if choice.isnumeric():
            return choice
        return str(0)


print("Welcome to the Registration System")

conn = sql.connect("users.db")
cur = conn.cursor()
cur.execute(
    """
CREATE TABLE IF NOT EXISTS user (
    username TEXT PRIMARY KEY,
    password text NOT NULL,
    is_logged_in int DEFAULT 0,
    sec_ques text
)
"""
)
conn.commit()

while True:
    print("-" * 25)
    print("1. Register")
    print("2. Log In")
    print("3. Log Out")
    print("4. Change Password")
    print("5. Exit")
    choice = bro_choice("Enter your choice: ")
    print("-" * 25)
    match choice:
        case "1":
            print("\t\tYou selected Register")
            username = bro_input("\t\tEnter username: ")

            cur.execute("SELECT username FROM user WHERE username = ?", (username,))
            if cur.fetchone() is not None:
                print("\t\tUsername already exists!")
                continue

            password = bro_getpass("\t\tEnter password: ")
            hashed_password = hash.sha256(password.encode()).hexdigest()
            ques = bro_input("\t\tEnter a Security Ques: ")
            ans = input("\t\tEnter the Answer: ")
            sec_ques = f"{ques}|{ans}"
            cur.execute(
                "INSERT INTO user (username, password, is_logged_in, sec_ques) VALUES (?, ?, ?, ?)",
                (username, hashed_password, 0, sec_ques),
            )
            conn.commit()
        case "2":
            print("\t\tYou selected Log In")
            username = bro_input("\t\tEnter username: ")

            cur.execute("SELECT is_logged_in FROM user WHERE username = ?", (username,))
            if cur.fetchone() is not None:
                print("\t\tUsername already exists!")
                continue
            if cur.fetchone()[0] is not 0:
                print("\t\tUser is already logged in!")
                continue
            password = getpass.getpass("\t\tEnter password: ")
            hashed_password = hash.sha256(password.encode()).hexdigest()

            cur.execute(
                "SELECT password, is_logged_in FROM user WHERE username = ?",
                (username,),
            )
            credentials = cur.fetchone()

            if credentials is None:
                print("\t\tUser not found!")
                continue

            if credentials[1] == 1:
                print("\t\tUser is already logged in!")
                continue

            if credentials[0] == hashed_password:
                cur.execute(
                    "UPDATE user SET is_logged_in = 1 WHERE username = ?", (username,)
                )
                conn.commit()
                print("\t\tLogin successful!")
            else:
                print("\t\tLogin failed!")
                while True:
                    print("\t\t\t1. Try Again")
                    print("\t\t\t2. Forgot Password")
                    print("\t\t\t3. Exit")
                    choice = bro_choice("\t\t\tEnter your choice: ")
                    match choice:
                        case "1":
                            print("\t\tYou selected Try Again")
                        case "2":
                            print("\t\tYou selected Forgot Password")
                            cur.execute(
                                "SELECT sec_ques FROM user WHERE username = ?",
                                (username,),
                            )
                            ver_ques = cur.fetchone()
                            ques_ans = ver_ques[0]
                            print("\t\t\tEnter the Answer of Your Security Question")
                            ans = bro_getpass(f"{ques_ans}: ")
                            if ans == ques_ans[1]:
                                print("Security Answer Correct!")
                                password = bro_getpass("\t\t\tEnter New password: ")
                                hashed_password = hash.sha256(
                                    password.encode()
                                ).hexdigest()

                                cur.execute(
                                    "UPDATE user SET password = ? WHERE username = ?",
                                    (hashed_password, username),
                                )
                                conn.commit()
                            else:
                                print("Answer Not Matched!")
                        case "3":
                            break
                        case _:
                            print("Wrong Input")

        case "3":
            print("\t\tYou selected Log Out")
            username = bro_input("\t\tEnter username: ")

            cur.execute("SELECT is_logged_in FROM user WHERE username = ?", (username,))
            credentials = cur.fetchone()

            if credentials is None:
                print("\t\tUser not found!")
                continue

            else:
                if credentials[0] == 0:
                    print("\t\tUser is Already logged Out")
                    continue
                cur.execute(
                    "UPDATE user SET is_logged_in = 0 WHERE username = ?", (username,)
                )
                conn.commit()
                print("\t\tLog Out successful!")

        case "4":
            print("\t\tYou selected Change Password")
            username = bro_input("\t\tEnter username: ")

            cur.execute("SELECT is_logged_in FROM user WHERE username = ?", (username,))
            credentials = cur.fetchone()

            if credentials is None:
                print("\t\tUser not found!")
                continue

            else:
                if credentials[0] == 0:
                    print("\t\tUser is not logged in")
                    continue

                password = bro_getpass("\t\tEnter password: ")
                hashed_password = hash.sha256(password.encode()).hexdigest()

                cur.execute(
                    "UPDATE user SET password = ? WHERE username = ?",
                    (hashed_password, username),
                )
                conn.commit()

        case "5":
            print("\t\tYou selected Exit")
            conn.close()
            print("\t\t\t\tThank You!")
            print("-" * 25)
            break
        case _:
            print("\t\tInvalid choice Entered\n\t\t Please try again.")
