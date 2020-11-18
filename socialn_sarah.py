from PIL import Image
import numpy as np
import logging
import datetime
import cv2



class Profile:
    id=()
    followers=0
    followings=0
    new_followed=[]
    new_follower=[]
    img=[]
    data=[]

    def __init__(self,user,password,picture,flag,email,phone_no,status,comment,follower,following):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('a profile is created!')

        self.user=user
        self.password=password
        self.picture=picture
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

        # self.user=input("enter your personal user(more than 5 chars):\n")
        # self.password=input("enter your security password(more than 6 chars):\n")
        if len(self.user)>=5 and len(self.password)>=6:
            id=(hash(self.user),hash(self.password))
            data.append(id)
            f.write(str(data))


        f.close()
        return  data

    def upload_pic(self,picture):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user uploads the profile picture!')

        # self.picture = input("type your address of your profile image\n")
        # with open(file_name, "rb") as e:
        #     image = Image.open(e)
        #     image.show()


        data.append( self.picture)
        with open(self.picture, "rb") as f:
            picture = Image.open(f)
            picture.show()
            # print(image.size)
            # print(image.format)
            print(picture.mode)
        # print(image.size)
        # print(image.format)
        # print(image.mode)
        f.close()



    def enter_email(self,email):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to enter the email!')

        f = open('data', 'wt')


            # self.email=input("enter your valid email:\n")

        if '@' in self.email or self.email=="":
            data.append(self.email)

            f.write(str(data))


        f.close()
        return  data

    def phone_no(self,phone_no):


        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user  enters the phone_no!')



        f = open('data', 'wt')


            # self.phone_no =int(input("type your address of your phone_no:\n"))

        if  int(self.phone_no):
            data.append(self.phone_no)

            f.write(str(data))


        f.close()
        return data

def main():
    u = input("enter your personal user(more than 5 chars):\n")
    p= input("enter your security password(more than 6 chars):\n")
    pic = input("type your address of your profile image:\n")
    e = input("enter your valid email:\n")

    ph = input("type your phone_no:\n")

    b=Profile(u,p,pic,0,e,ph,0,0,0,0)
    b.save_user_and_pass(u,p)
    print(b.upload_pic(pic))
    print(b.enter_email(e))
    print(b.phone_no(ph))


main()