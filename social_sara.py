


# import numpy as np
import logging
import datetime
import  csv
from hashlib import sha256


class Profile:
    id=()
    data=[]
    img=[]


    def __init__(self,user,password,flag,email,phone_no,status,comment,follower,following):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('a profile is created!')

        self.user=user
        self.password=password

        self.flag=flag
        self.email=email
        self.phone_no=phone_no
        self.status=status
        self.comment=comment
        self.follower=follower
        self.following=following


    def save_user_and_pass(self,user,password):

        global  data
        data = []
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user defines his/her user and password and save them!')






        if len(self.user)>=5 and len(self.password)>=6:
            a=sha256(self.user.encode()).hexdigest()
            b=sha256(self.password.encode()).hexdigest()
            data.append(self.user)
            data.append(b)

            with open('data.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(data )






        return  self.user,b





    def enter_email(self,email):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to enter the email!')






        if '@' in self.email or self.email=="":


            data.append(self.email)
            with open('data.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(data )



        return  self.email

    def phone_nu(self,phone_no):




        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user  enters the phone_no!')

        if  int(self.phone_no):
            data.append(phone_no)
            with open('data.csv', 'w', newline='') as csvfile:

                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(data)



        return phone_no

    def infos_users(self,user):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user added to the file and saved!')
        with open('users.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow("@"+str(self.user))
        return "@"+self.user

class Login:

    def __init__(self,enteruser,enterpass):
        self.enteruser=enteruser
        self.enterpass=enterpass
        self.login_status=""

    def login1(self,enteruser,enterpass):
        reader=""
        login_status=""
        # aa= sha256(self.enteruser.encode()).hexdigest()
        bb = sha256(self.enterpass.encode()).hexdigest()

        with open('data.csv', newline='') as csvfile:


            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

            for row in spamreader:

                cc=print(', '.join(row))

        print(self.enteruser)
        if row[0] == self.enteruser :
            if row[1] == bb :



                self.login_status = True
                print("you will able to login")
                print("hi")
            else:
                self.login_status=False
                print(("you can't log in!!"))

        return self.login_status



class Searching_people:
    def __init__(self,user_following):
        self.user_following=user_following

    def searching(self,user_following):
        with open('users.csv', newline='') as csvfile:


            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

            for row in spamreader:
            #
            #     print(row)
                if list(self.user_following) == row:
                    with open('data.csv', newline='') as csvfile:

                        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

                        for line in spamreader:

                            ee=self.user_following.split('@')
                            if line[0]==ee[1]:
                                print("the  information of profile that you searched:\n"+line[0]+"*******\n"+line[2]+"********\n"+line[3])
                                pass


    def watch_other_profile(self):
        pass











def main():
    u = input("enter your personal user(more than 5 chars):\n")
    p= input("enter your security password(more than 6 chars):\n")

    e = input("enter your valid email:\n")

    ph = input("type your phone_no:\n")

    b=Profile(u,p,0,e,ph,0,0,0,0)
    print(b.save_user_and_pass(u,p))
    print(b.enter_email(e))
    b.phone_nu(ph)
    print(b.infos_users(u))
    print ("your profile compeleted:\n","user=",u,"\n email=",e,"\n phone_number=",ph)

    eu= input("enter your user for getting login:\n")
    ep= input("enter your password for getting login:\n")

    c=Login(eu,ep)
    print(c.login1(eu,ep))
    if c.login_status==True:
        g=input("do you want to find your friends? if you want type her id:")
        h=Searching_people(g)
        print(h.searching(g))

main()


