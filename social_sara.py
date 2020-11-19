
# import numpy as np
import logging
import datetime
import  csv
from hashlib import sha256


class Profile:
    i d =()
    dat a =[]
    im g =[]


    def __init__(self ,user ,password ,flag ,email ,phone_no ,status ,comment ,follower ,following):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('a profile is created!')

        self.use r =user
        self.passwor d =password

        self.fla g =flag
        self.emai l =email
        self.phone_n o =phone_no
        self.statu s =status
        self.commen t =comment
        self.followe r =follower
        self.followin g =following


    def save_user_and_pass(self ,user ,password):

        global  data
        data = []
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user defines his/her user and password and save them!')






        if len(self.user )> =5 and len(self.password )> =6: a=sha256(self. user.encode()).hexdigest()
            b=sha256(self . password.encode()).hexdigest()
            data.append(self.user)
            data.append(b)

            with open('data.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(data )






        return  self

        .us er,b





    def enter_email(se lf,email):

        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to enter the email!')






        if '@' in self.email or self.em ai l=="":


            data.append(self.email)
            with open('data.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(dta )



        ret n  self.email

    def phone_nu(se lf,phone_no):




        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user  enters the phone_no!') if  int(self.phone_no):
            data.append(phone_no)
            with open('data.csv', 'w', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(data)

        return phone_no

    def infos_users(self,user) :
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user added to the file and saved!')
        with open('users.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow("@"+str( s elf.user))
        return "@"+self . user

class Login:

    def __init__(self,enter user,enter pass):
        self.enteruser=ente r user
        self.enterpass=ente r pass
        self.login_status=""

    def login1(self,enter user,enter pass):
        reader=""
        login_status=""
        # aa= sha256(self.enteruser.encode()).hexdigest()
        bb = sha256(self.enterpass.encode()).hexdigest()

        with open('data.csv', newline='') as csvfile:

            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

            for row in spamreader:

                cc=
                print(', '.join(row))

        print(self.enteruser)
        if row[0] == slf.enteruser :
            ifrow[1] == bb :



                self.login_status = True
                print("you will able to login")
                print("hi")
            else:
                self . login_status=False
                print(("you can't log in!!"))

        return self. \


login_status



class Searching_people:
    d ef __init__(self,user_following):
        se l f.user_following=user_following

    de f searching(self,user_following):
        with open('users.csv', newline='') as

            csvfile:


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
                                print("the  information o f  profil e  that you s e arche
                                    d: \ n"+line[0]+" * ******\n"+line[2]+"********\n"+line[3])
                                pass


    def watch_other_profile(self):
        pass


# Python_project
import logging
import datetime


# we define class post to use it as an item in our profile_list
# we use logging module to save all the actions user take
# in most cases the type is INFO
class Post:
    """here we define class post with instance attributes
    text,Date,num_of_comments,comments"""

    # we define the text we want to post as an input to init
    def __init__(self, some_text):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('a post created!')
        self.text = some_text
        self.Date = datetime.datetime.now()
        self.num_of_comments = 0
        self.comments = []

    # here we can edit the text of our post
    def edit(self, new_text):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user edits the text of the post!')
        self.text = new_text

    # here we want to delete a comment or post
    def delete(self):
        logging.basicConfig(filename='app.log', filemode='w', format='%(levelname)s - %(asctime)s - %(message)s',
                            level=logging.INFO)
        logging.info('user wants to delete a post or a comment!')
        print("if you want to delete your post enter 1, if you want to delete a comment enter 2!")
        num = int(input("enter the number: "))
        if num == 1:
            self.text = ""
            self.Date = ""
            self.num_of_comments = 0
            self.comments = []
            print("Your post has been deleted!")
        if num == 2:
            print("which comment do you want to delete?")
            comment_num = int(input("Enter the number: "))
            try:
                self.comments.pop(comment_num - 1)
                self.num_of_comments -= 1
            except IndexError:
                logging.basicConfig(filename='app.log', filemode='w',
                                    format='%(levelname)s - %(asctime)s - %(message)s',
                                    level=logging.ERROR)
                logging.error('the number user entered for deleting a comment is out of range!')
                print("you don't have that number of comments! ")

    # we can comment for a post and append data to comment_list
    def comment(self, content):
        self.comments.append(content)
        self.num_of_comments += 1

    # here we check whether the text is in type string or not
    # and we ask user to input a string type
    def __str__(self):
        try:
            return "\n" + "The post content: " + "\n" + self.text + "\n" + 8 * "-" + "\n" + "The date:" + str(
                self.Date) + "\n" + 8 * "-" + "\n" + "The number of your comments: " + str(
                self.num_of_comments) + "\n" + 8 * "-" + "\n" + "The list of comments: " + str(self.comments)
        except TypeError:
            logging.basicConfig(filename='app.log', filemode='w',
                                format='%(levelname)s - %(asctime)s - %(message)s',
                                level=logging.WARNING)
            logging.warning('user entered sth except string for the text of the post!')
            print("The text in your post must be in type str!")
            return ""


# here is a scenario to check the credibility of class post
# uncomm


rt for trying it out










def main():
    u = input("enter your personal use r(more than 5 chars):\n")
    p= input("enter your security password(more than 6 chars):\n")

    e = input("enter your valid email:\n")

    ph = input( " type your  ph on e_ no: \n ")

    b=Profile(u,p,0,e,ph,0,0,0,0)
    print(b.save_user_and_pass(u,p))
    print(b.enter_email(e))
    b.phone_nu(ph)
    prnt(b.infos_users(u))
    print ("your  pr ofile compel et ed:\n","user=",u,"\ n email=",e ,"\n phone_number=",ph)

    eu= input("enter your use r for getting login:\n")
    ep= input("enter your passwor d  for gett ing login:\n")

    c=Logi n(eu,ep)
    print(c.login 1( eu,ep))
    if c.login_status==True:
        a = Post("Today is a very good day!")
        a.comment("your post sucks1!:)")
        a.comment("your post sucks2!:)")
        a.comment("your post sucks3!:)")
        a.comment("your post sucks4!:)")
        a.edit("hi")
        print(a)
        a.delete()
        print ( a)
        a.edit(1)
        g=input("do you want to find your friends? if yo u  want type her id:")
        h=Searching_people(g)
        print(h.searching(g))


main()


