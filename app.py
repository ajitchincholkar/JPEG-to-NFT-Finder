import streamlit as st
import cv2
from PIL import Image
from skimage.metrics import structural_similarity
from skimage.transform import resize
import os


def save_uploaded_image(uploaded_img):
    try:
        with open(os.path.join('Uploads', uploaded_img.name), 'wb') as f:
            f.write(uploaded_img.getbuffer())
        return True
    except:
        return False

def structural_sim(img1, img2):
    sim, diff = structural_similarity(img1, img2, full=True)
    return sim


st.title('JPEG to NFT # Finder')

nft_collections = ['Azuki', 'Moonbirds', 'Doodles', 'BAYC', 'WoW', 'CloneX']

selected_collection = st.selectbox('Select Collection', nft_collections)

uploaded_img = st.file_uploader('Upload Image')

if selected_collection == 'Azuki':
    filenames_azuki = os.listdir('Azuki')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)
            st.image(display_img, width=200)

            img1 = cv2.imread(os.path.join('Uploads', uploaded_img.name), 0)
            resized_img = resize(img1, (128,128), anti_aliasing=True, preserve_range=True)

            name_scores = []
            scores = []

            for name in filenames_azuki:
                img = cv2.imread(os.path.join('Azuki', name), 0)
                ssim = structural_sim(img, resized_img)

                name_score = (name, ssim)
                scores.append(ssim)

                name_scores.append(name_score)

            max_score = max(scores)

            for i in range(len(filenames_azuki)):
                if name_scores[i][1] == max_score:
                    final_nft = name_scores[i][0][:-4]
                    st.subheader(final_nft)

if selected_collection == 'Doodles':
    filenames_doodles = os.listdir('Doodles')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)
            st.image(display_img, width=200)

            img1 = cv2.imread(os.path.join('Uploads', uploaded_img.name), 0)
            resized_img = resize(img1, (128, 128), anti_aliasing=True, preserve_range=True)

            name_scores = []
            scores = []

            for name in filenames_doodles:
                img = cv2.imread(os.path.join('Doodles', name), 0)
                ssim = structural_sim(img, resized_img)

                name_score = (name, ssim)
                scores.append(ssim)

                name_scores.append(name_score)

            max_score = max(scores)

            for i in range(len(filenames_doodles)):
                if name_scores[i][1] == max_score:
                    final_nft = name_scores[i][0][:-4]
                    st.subheader(final_nft)

if selected_collection == 'Moonbirds':
    filenames_mb = os.listdir('Moonbirds')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)
            st.image(display_img, width=200)

            img1 = cv2.imread(os.path.join('Uploads', uploaded_img.name), 0)
            resized_img = resize(img1, (128, 128), anti_aliasing=True, preserve_range=True)

            name_scores = []
            scores = []

            for name in filenames_mb:
                img = cv2.imread(os.path.join('Moonbirds', name), 0)
                ssim = structural_sim(img, resized_img)

                name_score = (name, ssim)
                scores.append(ssim)

                name_scores.append(name_score)

            max_score = max(scores)

            for i in range(len(filenames_mb)):
                if name_scores[i][1] == max_score:
                    final_nft = name_scores[i][0][:-4]
                    st.subheader(final_nft)


if selected_collection == 'BAYC':
    filenames_bayc = os.listdir('BAYC')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)
            st.image(display_img, width=200)

            img1 = cv2.imread(os.path.join('Uploads', uploaded_img.name), 0)
            resized_img = resize(img1, (128, 128), anti_aliasing=True, preserve_range=True)

            name_scores = []
            scores = []

            for name in filenames_bayc:
                img = cv2.imread(os.path.join('BAYC', name), 0)
                ssim = structural_sim(img, resized_img)

                name_score = (name, ssim)
                scores.append(ssim)

                name_scores.append(name_score)

            max_score = max(scores)

            for i in range(len(filenames_bayc)):
                if name_scores[i][1] == max_score:
                    final_nft = name_scores[i][0][:-4]
                    st.subheader(final_nft)


if selected_collection == 'WoW':
    filenames_wow = os.listdir('WoW')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)
            st.image(display_img, width=200)

            img1 = cv2.imread(os.path.join('Uploads', uploaded_img.name), 0)
            resized_img = resize(img1, (128, 128), anti_aliasing=True, preserve_range=True)

            name_scores = []
            scores = []

            for name in filenames_wow:
                img = cv2.imread(os.path.join('WoW', name), 0)
                ssim = structural_sim(img, resized_img)

                name_score = (name, ssim)
                scores.append(ssim)

                name_scores.append(name_score)

            max_score = max(scores)

            for i in range(len(filenames_wow)):
                if name_scores[i][1] == max_score:
                    final_nft = name_scores[i][0][:-4]
                    st.subheader(final_nft)


if selected_collection == 'CloneX':
    filenames_clonex = os.listdir('CloneX')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)
            st.image(display_img, width=200)

            img1 = cv2.imread(os.path.join('Uploads', uploaded_img.name), 0)
            resized_img = resize(img1, (128, 128), anti_aliasing=True, preserve_range=True)

            name_scores = []
            scores = []

            for name in filenames_clonex:
                img = cv2.imread(os.path.join('CloneX', name), 0)
                ssim = structural_sim(img, resized_img)

                name_score = (name, ssim)
                scores.append(ssim)

                name_scores.append(name_score)

            max_score = max(scores)

            for i in range(len(filenames_clonex)):
                if name_scores[i][1] == max_score:
                    final_nft = name_scores[i][0][:-4]
                    st.subheader(final_nft)