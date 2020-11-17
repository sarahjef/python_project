from PIL import Image
import numpy as np

import cv2



class Profile:
    id=()

    img=[]
    data=[]
    def __init__(self,user,password,picture,flag,email,phone_no,bio,comment,follower,following):
        self.user=user
        self.password=password
        self.picture=picture
        self.flag=flag
        self.email=email
        self.phone_no=phone_no
        self.bio=bio
        self.comment=comment
        self.follower=follower
        self.following=following

    def save_user_and_pass(self):
        global id
        f=open('data','wt')
        while True:
            self.user=input("enter your personal user(more than 5 chars):\n")
            self.password=input("enter your security password(more than 6 chars):\n")
            if len(self.user>=5 and self.password>=6):
                id=(self.user,self.password)
                data.append(id)
            try:
                f.write(data)
            except:
                raise ValueError("invalid input")
                continue
            else:
                break
        f.close()
        return  data

    def upload_pic(self, img=None):

        self.picture = input("type your address of your profile image\n")
        # with open(file_name, "rb") as e:
        #     image = Image.open(e)
        #     image.show()
        try:

            img.append((self.save_user_and_pass(), self.picture))
            cv2.imread(self.picture,1)
            cv2.imshow(self.picture,cv2.imread(self.picture,1))
            cv2.waitKey(0)
            # cv2.destroyAllWindows()
            if  cv2.waitKey(0)==27:
                cv2.destroyAllWindows()
            elif cv2.waitKey(0)==ord('s'):
                cv2.namedWindow(self.picture, cv2.WINDOW_NORMAL)
                # cv2.imshow(self.picture, cv2.imread(self.picture,1))
                cv2.imwrite('pic_saved.png',cv2.imread(self.picture,1))
            return cv2.imshow(self.picture, cv2.imread(self.picture,1))
        # print(image.size)
        # print(image.format)
        # print(image.mode)

        except:
            raise ValueError("invalid input")


