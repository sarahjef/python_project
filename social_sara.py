


import numpy as np
import logging
import datetime

from hashlib import sha256


class Profile:
    id=()

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

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user defines his/her user and password and save them!')
        global data
        data=[]
        f=open('data','wt')


        if len(self.user)>=5 and len(self.password)>=6:
            a=sha256(self.user.encode()).hexdigest()
            b=sha256(self.password.encode()).hexdigest()
            id=((a,self.user),(b,self.password))
            data.append(id)
            f.write(str(data))


        f.close()
        return  data





    def enter_email(self,email):
        global  emails
        emails = []
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to enter the email!')

        f = open('data', 'wt')




        if '@' in self.email or self.email=="":
            emails.append((self.email,sha256(self.user.encode()).hexdigest()))

            f.write(str(email))


        f.close()
        return  emails

    def phone_no(self,phone_no):

        phone_nos=[]


        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user  enters the phone_no!')



        f = open('data', 'wt')




        if  int(self.phone_no):
            phone_nos.append(self.phone_no)

            f.write(str(phone_nos))


        f.close()
        return phone_nos

def main():
    u = input("enter your personal user(more than 5 chars):\n")
    p= input("enter your security password(more than 6 chars):\n")

    e = input("enter your valid email:\n")

    ph = input("type your phone_no:\n")

    b=Profile(u,p,0,e,ph,0,0,0,0)
    print(b.save_user_and_pass(u,p))

    print(b.enter_email(e))



main()