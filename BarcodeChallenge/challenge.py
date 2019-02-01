from PIL import Image
import os

#I transposed and split a barcode image into 9 pieces. I deleted the original image and left these broken up pieces.
#The purpose of that is so that I don't have easy access to the barcode anywhere in my computer. I have to complete a challenge to view it.
#I am using the barcode to help me wake up, as my alarm app requires me to scan a specific barcode for me to turn it off.
#This whole thing might seem kind of dumb lol, but I've been struggling immensely with waking up on time...

def open_barcode():
    try:
        img = Image.open(r"C:\Users\Charlie Xu\Documents\red.png") #background for which to paste the images

        path = "C:/Users/Charlie Xu/Downloads/split-2019-2-1 (1)/"
        dirs = os.listdir(path)

        images = []
        for item in dirs:
            temp = Image.open(path+item)
            images.append(temp.transpose(Image.FLIP_LEFT_RIGHT)) #transposing final product did not work. Cannot save to bypass this.


        x9, y9 = images[8].size
        x8, y8 = images[7].size
        # x7, y7 = images[6].size
        x6, y6 = images[5].size
        x5, y5 = images[4].size
        # x4, y4 = images[3].size
        x3, y3 = images[2].size
        x2, y2 = images[1].size
        # x1, y1 = images[0].size

        img.paste(images[8], (x9 + x8, 0))
        img.paste(images[7], (x9, 0))
        img.paste(images[6], (0, 0))
        img.paste(images[5], (x6 + x5, y9))
        img.paste(images[4], (x6, y9))
        img.paste(images[3], (0, y9))
        img.paste(images[2], (x3 + x2, y9 + y6))
        img.paste(images[1], (x3, y9 + y6))
        img.paste(images[0], (0, y9 + y6))

        img.show()

    except IOError:
        print("bruh")
        pass

def challenge():
    #work in progress
    return