{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyPK+Uc49BPFxp8TIHlZLI14"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"id":"QuIEF5DuHiDr"},"outputs":[],"source":["import numpy as np\n","import imageio\n","import imgaug as ia\n","from imgaug import augmenters as iaa\n","ia.seed(4)\n","from google.colab.patches import cv2_imshow\n","import matplotlib.pylab as plt\n","%matplotlib inline\n","import cv2\n","import os"]},{"cell_type":"code","source":["def augment(image_path):\n","    \n","    full_path=image_path+f\"00{i}_HC.png\"\n","    image = cv2.imread(full_path)\n","    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)\n","        \n","    seq = iaa.Sequential([\n","          iaa.Affine(rotate=(-25, 25)),\n","          iaa.AdditiveGaussianNoise(scale=(10, 60)),\n","          iaa.Crop(percent=(0, 0.2))])\n","      \n","    images_aug = seq(images=image_gray )\n","      \n","    return images_aug"],"metadata":{"id":"IrBctwQvHz6w"},"execution_count":null,"outputs":[]}]}