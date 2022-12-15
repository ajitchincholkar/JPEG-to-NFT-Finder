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

nft_collections = ['Azuki', 'Moonbirds', 'Doodles', 'BAYC', 'WoW', 'CloneX', 'MAYC', 'Cool Cats', 'Pudgy Penguins', 'CryptoPunks']

selected_collection = st.selectbox('Select Collection', nft_collections)

uploaded_img = st.file_uploader('Upload Image')

if selected_collection == 'Azuki':
    filenames_azuki = os.listdir('Azuki')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)

            col1, col2 = st.columns(2)
            with col1:
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
            if max_score < 0.8:
                st.subheader('Please upload a better quality image!')
            else:
                for i in range(len(filenames_azuki)):
                    if name_scores[i][1] == max_score:
                        final_nft = name_scores[i][0][:-4]
                        nft_num = name_scores[i][0].split('#')[1].split('.')[0]

                        opensea_link = f'https://opensea.io/assets/ethereum/0xed5af388653567af2f388e6224dc7c4b3241c544/{nft_num}'
                        rarity_link = f'https://rarity.tools/azuki/view/{nft_num}'

            with col1:
                st.subheader(final_nft)
            with col2:
                st.subheader("Check on [Opensea](%s)" % opensea_link)
                st.subheader("Check [Rarity Score](%s)" % rarity_link)


if selected_collection == 'Doodles':
    filenames_doodles = os.listdir('Doodles')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)

            col1, col2 = st.columns(2)
            with col1:
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
            if max_score < 0.8:
                st.subheader('Please upload a better quality image!')
            else:
                for i in range(len(filenames_doodles)):
                    if name_scores[i][1] == max_score:
                        final_nft = name_scores[i][0][:-4]
                        nft_num = name_scores[i][0].split('#')[1].split('.')[0]

                        opensea_link = f'https://opensea.io/assets/ethereum/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/{nft_num}'
                        rarity_link = f'https://rarity.tools/doodles-official/view/{nft_num}'

            with col1:
                st.subheader(final_nft)
            with col2:
                st.subheader("Check on [Opensea](%s)" % opensea_link)
                st.subheader("Check [Rarity Score](%s)" % rarity_link)


if selected_collection == 'Moonbirds':
    filenames_mb = os.listdir('Moonbirds')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)

            col1, col2 = st.columns(2)
            with col1:
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
            if max_score < 0.8:
                st.subheader('Please upload a better quality image!')
            else:
                for i in range(len(filenames_mb)):
                    if name_scores[i][1] == max_score:
                        final_nft = name_scores[i][0][:-4]
                        nft_num = name_scores[i][0].split('#')[1].split('.')[0]

                        opensea_link = f'https://opensea.io/assets/ethereum/0x23581767a106ae21c074b2276d25e5c3e136a68b/{nft_num}'
                        rarity_link = f'https://rarity.tools/proof-moonbirds/view/{nft_num}'

            with col1:
                st.subheader(final_nft)
            with col2:
                st.subheader("Check on [Opensea](%s)" % opensea_link)
                st.subheader("Check [Rarity Score](%s)" % rarity_link)


if selected_collection == 'BAYC':
    filenames_bayc = os.listdir('BAYC')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)

            col1, col2 = st.columns(2)
            with col1:
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
            if max_score < 0.8:
                st.subheader('Please upload a better quality image!')
            else:
                for i in range(len(filenames_bayc)):
                    if name_scores[i][1] == max_score:
                        final_nft = name_scores[i][0][:-4]
                        nft_num = name_scores[i][0].split('#')[1].split('.')[0]

                        opensea_link = f'https://opensea.io/assets/ethereum/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/{nft_num}'
                        rarity_link = f'https://rarity.tools/boredapeyachtclub/view/{nft_num}'

            with col1:
                st.subheader(final_nft)
            with col2:
                st.subheader("Check on [Opensea](%s)" % opensea_link)
                st.subheader("Check [Rarity Score](%s)" % rarity_link)


if selected_collection == 'WoW':
    filenames_wow = os.listdir('WoW')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)

            col1, col2 = st.columns(2)
            with col1:
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
            if max_score < 0.8:
                st.subheader('Please upload a better quality image!')
            else:
                for i in range(len(filenames_wow)):
                    if name_scores[i][1] == max_score:
                        final_nft = name_scores[i][0][:-4]
                        nft_num = name_scores[i][0].split('#')[1].split('.')[0]

                        opensea_link = f'https://opensea.io/assets/ethereum/0xe785e82358879f061bc3dcac6f0444462d4b5330/{nft_num}'
                        rarity_link = f'https://rarity.tools/world-of-women-nft/view/{nft_num}'

            with col1:
                st.subheader(final_nft)
            with col2:
                st.subheader("Check on [Opensea](%s)" % opensea_link)
                st.subheader("Check [Rarity Score](%s)" % rarity_link)


if selected_collection == 'CloneX':
    filenames_clonex = os.listdir('CloneX')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)

            col1, col2 = st.columns(2)
            with col1:
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
            if max_score < 0.8:
                st.subheader('Please upload a better quality image!')
            else:
                for i in range(len(filenames_clonex)):
                    if name_scores[i][1] == max_score:
                        final_nft = name_scores[i][0][:-4]
                        nft_num = name_scores[i][0].split(' ')[1].split('.')[0]

                        opensea_link = f'https://opensea.io/assets/ethereum/0x49cf6f5d44e70224e2e23fdcdd2c053f30ada28b/{nft_num}'
                        rarity_link = f'https://rarity.tools/clonex/view/{nft_num}'

            with col1:
                st.subheader(final_nft)
            with col2:
                st.subheader("Check on [Opensea](%s)" % opensea_link)
                st.subheader("Check [Rarity Score](%s)" % rarity_link)


if selected_collection == 'MAYC':
    filenames_mayc = os.listdir('MAYC')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)

            col1, col2 = st.columns(2)
            with col1:
                st.image(display_img, width=200)

            img1 = cv2.imread(os.path.join('Uploads', uploaded_img.name), 0)
            resized_img = resize(img1, (128, 128), anti_aliasing=True, preserve_range=True)

            name_scores = []
            scores = []

            for name in filenames_mayc:
                img = cv2.imread(os.path.join('MAYC', name), 0)
                ssim = structural_sim(img, resized_img)

                name_score = (name, ssim)
                scores.append(ssim)

                name_scores.append(name_score)

            max_score = max(scores)
            if max_score < 0.8:
                st.subheader('Please upload a better quality image!')
            else:
                for i in range(len(filenames_mayc)):
                    if name_scores[i][1] == max_score:
                        final_nft = name_scores[i][0][:-4]
                        nft_num = name_scores[i][0].split('#')[1].split('.')[0]

                        opensea_link = f'https://opensea.io/assets/ethereum/0x60e4d786628fea6478f785a6d7e704777c86a7c6/{nft_num}'
                        rarity_link = f'https://rarity.tools/mutant-ape-yacht-club/view/{nft_num}'

            with col1:
                st.subheader(final_nft)
            with col2:
                st.subheader("Check on [Opensea](%s)" % opensea_link)
                st.subheader("Check [Rarity Score](%s)" % rarity_link)


if selected_collection == 'Cool Cats':
    filenames_cc = os.listdir('Cool Cats')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)

            col1, col2 = st.columns(2)
            with col1:
                st.image(display_img, width=200)

            img1 = cv2.imread(os.path.join('Uploads', uploaded_img.name), 0)
            resized_img = resize(img1, (128, 128), anti_aliasing=True, preserve_range=True)

            name_scores = []
            scores = []

            for name in filenames_cc:
                img = cv2.imread(os.path.join('Cool Cats', name), 0)
                ssim = structural_sim(img, resized_img)

                name_score = (name, ssim)
                scores.append(ssim)

                name_scores.append(name_score)

            max_score = max(scores)
            if max_score < 0.8:
                st.subheader('Please upload a better quality image!')
            else:
                for i in range(len(filenames_cc)):
                    if name_scores[i][1] == max_score:
                        final_nft = name_scores[i][0][:-4]
                        nft_num = name_scores[i][0].split('#')[1].split('.')[0]

                        opensea_link = f'https://opensea.io/assets/ethereum/0x1a92f7381b9f03921564a437210bb9396471050c/{nft_num}'
                        rarity_link = f'https://rarity.tools/cool-cats-nft/view/{nft_num}'

            with col1:
                st.subheader(final_nft)
            with col2:
                st.subheader("Check on [Opensea](%s)" % opensea_link)
                st.subheader("Check [Rarity Score](%s)" % rarity_link)


if selected_collection == 'Pudgy Penguins':
    filenames_pudpen = os.listdir('Pudgy Penguins')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)

            col1, col2 = st.columns(2)
            with col1:
                st.image(display_img, width=200)

            img1 = cv2.imread(os.path.join('Uploads', uploaded_img.name), 0)
            resized_img = resize(img1, (128, 128), anti_aliasing=True, preserve_range=True)

            name_scores = []
            scores = []

            for name in filenames_pudpen:
                img = cv2.imread(os.path.join('Pudgy Penguins', name), 0)
                ssim = structural_sim(img, resized_img)

                name_score = (name, ssim)
                scores.append(ssim)

                name_scores.append(name_score)

            max_score = max(scores)
            if max_score < 0.8:
                st.subheader('Please upload a better quality image!')
            else:
                for i in range(len(filenames_pudpen)):
                    if name_scores[i][1] == max_score:
                        final_nft = name_scores[i][0][:-4]
                        nft_num = name_scores[i][0].split('#')[1].split('.')[0]

                        opensea_link = f'https://opensea.io/assets/ethereum/0xbd3531da5cf5857e7cfaa92426877b022e612cf8/{nft_num}'
                        rarity_link = f'https://rarity.tools/pudgypenguins/view/{nft_num}'

            with col1:
                st.subheader(final_nft)
            with col2:
                st.subheader("Check on [Opensea](%s)" % opensea_link)
                st.subheader("Check [Rarity Score](%s)" % rarity_link)


if selected_collection == 'CryptoPunks':
    filenames_punk = os.listdir('Punks')

    if uploaded_img is not None:

        if save_uploaded_image(uploaded_img):
            display_img = Image.open(uploaded_img)

            col1, col2 = st.columns(2)
            with col1:
                st.image(display_img, width=200)

            img1 = cv2.imread(os.path.join('Uploads', uploaded_img.name), 0)
            resized_img = resize(img1, (128, 128), anti_aliasing=True, preserve_range=True)

            name_scores = []
            scores = []

            for name in filenames_punk:
                img = cv2.imread(os.path.join('Punks', name), 0)
                ssim = structural_sim(img, resized_img)

                name_score = (name, ssim)
                scores.append(ssim)

                name_scores.append(name_score)

            max_score = max(scores)
            if max_score < 0.8:
                st.subheader('Please upload a better quality image!')
            else:
                for i in range(len(filenames_punk)):
                    if name_scores[i][1] == max_score:
                        final_nft = name_scores[i][0][:-4]
                        nft_num = name_scores[i][0].split('#')[1].split('.')[0]

                        opensea_link = f'https://opensea.io/assets/ethereum/0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb/{nft_num}'
                        rarity_link = f'https://rarity.tools/cryptopunks/view/{nft_num}'

            with col1:
                st.subheader(final_nft)
            with col2:
                st.subheader("Check on [Opensea](%s)" % opensea_link)
                st.subheader("Check [Rarity Score](%s)" % rarity_link)
