import numpy as np
import streamlit as st
from mtcnn import MTCNN
from PIL import Image, ImageDraw

st.title("Pythonで顔認識して服を変更する")

# 画像ファイルをアップロードするためのウィジェット
imgfile = st.file_uploader("Upload Image", type=["png", "jpg"], accept_multiple_files=False)

# 画像ファイルがアップロードされていなければ何もしない
if imgfile is not None:    
    img = Image.open(imgfile)

    # マスクのイラストの画像
    mask = Image.open("img/h4.jpg")

    # 元の画像を表示
    st.write("元の画像")
    st.image(img, use_column_width=True)

    # 画像に写っている顔を検出する
    detector = MTCNN()  
    # 検出された顔ごとに，顔のBounding Box，顔である確率，目や鼻などのKeypointsが得られる． 
    results = detector.detect_faces(np.asarray(img))

    for result in results:
        # 顔である確率
        confidence = result["confidence"]

        # 顔である確率が90%以下ならスルー
        if confidence < 0.9:
            continue

        # 顔のBounding Box
        x, y, w, h = result["box"]

        # マスクの画像を顔のサイズに合わせる．
        mask_resized = mask.resize((3*w, 3*h)) 

        # マスクの画像を，検出された顔に貼り付ける． a      
        img.paste(mask_resized, (x-120, 2*y+h//2-80), mask_resized.convert("RGBA"))

    pil_img = Image.fromarray(np.uint8(img))

    st.write("マスクを付けた画像")
    st.image(pil_img, use_column_width=True)
