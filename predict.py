#-------------------------------------#
#       对单张图片进行预测
#-------------------------------------#
from yolo import YOLO
from PIL import Image

yolo = YOLO()
path1="/home/yylab/Research/2080_224_lb/hnd_test/original/"
path="/home/yylab/Research/2080_224_lb/hnd_test/1/"
he=0
s=0
for img in range(81):
#img = input('Input image filename:')
    image = Image.open(path1+str(img+1)+".png")
    if (img+1)<=9 or (img+1)>=63 or (img+1)%9==0 or (img+1)%9==1:
        image.save(path+str(img+1)+".png")
        continue
    else:
        image = Image.open(path1+str(img+1)+".png")
        r_image,s= yolo.detect_image(image)
        #s=yolo.num()
        print(s)
        he=he+s
        r_image.save(path+str(img+1)+".png")
print(he)
