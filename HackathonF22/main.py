import helper
from pyzbar import pyzbar
from PIL import Image
from numpy import asarray
import colorama
from colorama import Fore
import cv2


#image = "WhatsApp Image 2022-11-06 at 12.49.21 PM.jpeg"


#ret, frame = cap.read()


def decoder2(image1):
    # img = Image.open(img)
    # numpydata = asarray(image1)
    decoded_objects = pyzbar.decode(image1)

    for obj in decoded_objects:
        # draw the barcode
        #print("detected barcode:", obj)

        # print barcode type & data
        return obj.data


cap = cv2.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    cv2.imshow('img1', frame)  # display the captured image
    if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'
        cv2.imwrite('images/c1.png', frame)
        cv2.destroyAllWindows()
        img = frame
        temp = str(decoder2(frame))
        break

cap.release()
# print(temp)
temp = temp[:-1]
temp = temp[2:]
temp = temp[:5]

# print(temp)
print(Fore.BLUE, helper.get_name(temp), helper.get_price(temp))
print("Appropriate amount is deducted from your meal plan!")
