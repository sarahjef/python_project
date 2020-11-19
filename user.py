# Python_project
import logging
import datetime
from post import Post
import hashlib
import os
from hash1 import HASH



# her we define class User to do all the things asked in project
class User:
    # to track the number of users
    track = 0

    def __init__(self):
        User.track += 1
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('creating new user!')
        self.user_name = ''
        self.pass_word = ''
        self.email = ''
        self.phone = ''
        self.bio = ''
        self.login_status = False
        self.following_list = []
        self.followers_list = []
        self.profile = []

    def get_Info(self):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info("getting information from user!")
        self.user_name = input("Enter your desired username: ")
        while len(self.pass_word) < 8:
            self.pass_word = input("Enter your desired password(It should be at least 8 letters): ")
        self.bio = input("You can add bio to your profile: ")
        self.phone = input("You can add phone number to your profile: ")
        self.email = input("You can add email to your profile: ")
        # here we save personal detail in txt files
        with open("username.txt", "a+") as file_object1:
            # Move read cursor to the start of file.
            file_object1.seek(0)
            # If file is not empty then append '\n'
            data = file_object1.read(100)
            if len(data) > 0:
                file_object1.write("\n")
            # Append text at the end of file
            file_object1.write(self.user_name)
        with open("password.txt", "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            password = self.pass_word
            file_object.write(HASH(password))

    def follow(self, append=None):
        self.following = []
        if self.get_Info():
            self.following = append.self.self.following
            self.following = + 1
            print("A user added in your following list")
        else:
            print("Your following list is same")

    def unfollow(self, remove=None):
        self.following = []
        if self.get_Info():
            self.following = remove.self.self.following
            self.following = - 1
            print("A user deleted in your following list")
        else:
            print("Your following list is same")

    # here we want to check whether user name pass word are correct or not
    def login(self, username, password):
        with open("username.txt") as file_object:
            for i,line1 in enumerate(file_object):
                if str(line1) == username + "\n":
                    print("1")
                    with open("password.txt") as file_object2:
                        for j, line2 in enumerate(file_object2):
                            if j == i:
                                print("hi")
                                if str(line2) == HASH(password) + "\n":
                                    print("hiii")
                                    self.login_status = True




    def watch_other_profile(self):
        pass





# Run part
d = User()
d.get_Info()
d.login("fatemehh1376",'208074abc')
if d.login_status == True:
    print("you are logged in!")