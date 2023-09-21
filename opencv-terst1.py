#ライブラリの読み込み
import cv2
import matplotlib.pyplot as plt

#neko.jpgを読み込んで、imgオブジェクトに入れる
img = cv2.imread("neko.jpg")

#imgオブジェクトをmatlotlibを用いて表示する
# plt.imshow(img)
# plt.show()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()