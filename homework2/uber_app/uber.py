
import json


def start_sign_up():
    user_function = input("Are you a driver or a passenger?: ")
    if user_function == "driver":
        new_driver = Driver()
        new_driver.sign_up()
    elif user_function == "passenger":
        new_passenger = Passenger()
        new_passenger.sign_up()
    else:
        print("Wrong input. PLease choose either driver or passenger option")


class User:

    def __init__(self):
        self.username = input("Please choose an username: ")
        self.logged_in = False

    def login(self):
        with open("uber_users.json") as app_users:
            users_data = json.load(app_users)
            if self.username in users_data:
                print("Username exists")
                while not self.logged_in:
                    password = input("Please type your password: ")
                    if users_data[self.username] == password:
                        self.logged_in = True
                        print("You are logged in")
                    else:
                        print("Wrong password")

    def sign_up(self):
        print("Creating your account!")
        with open("uber_users.json", "w"):
            password = input("Please type your new password: ")
            json.dumps(f"'{self.username}': '{password}'")
        print("Now you should log in!")


class Driver(User):

    def __init__(self):
        super().__init__()


class Passenger(User):

    def __init__(self):
        super().__init__()


start_sign_up()
