import torch 
from torch import nn
import zipfile
from pathlib import Path 
import requests

# want to extract zip file images in path data/pizza_steak_sushi

data_path = Path('data/')
image_path = data_path/ "pizza_steak_sushi"

if image_path.is_dir():
    print('path exist: {image_path}')
else:
    print('does not exist create one')
    image_path.mkdir(parents=True,exist_ok=True)

with open(data_path/"pizza_steak_sushi.zip","wb") as f:
    request_data = requests.get('github_url')
    f.write(request_data.content)


with zipfile.ZipFile(data_path/"pizza_steak_sushi.zip",mode='r') as zip_ref:
    print('unzip pizza, steak and sushi....')
    zip_ref.extractall(image_path)

# now data folder has folder pizza_steak_sushi and also it has folder of pizza, steak, sushi and each category has train and test folder.
import os
def walk_through_path(dir_path):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        print(f"there are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")

train_dir = image_path/"train"
test_dir  = image_path/'test'

# get all the image path list:
import random 
from PIL import Image 

random.seed(42)
image_path_list  = image_path.glob("*/*/*.jpg") # hete image path = data/pizza_steak_sushi has pizza/train/images.jpg,same for test : pizza/test/images.jpg, same for all category of images
# above */*/*.jpg means pizza/train/images.jpg...,pizza/test/images.jpg...,......

# pick random image path 
random_image_path = random.choice(image_path_list)

# get image class of random_image_path
get_image_class = random_image_path.parent.stem

img = Image.open(random_image_path)

# meta data 
print(img.hight,img.width)


# image to numpy array and then plot using matplotlib
import numpy as np
import matplotlib.pyplot as plt

img_array = np.asarray(img)
plt.figure(figsize=(9,6))
plt.imshow(img_array)
plt.title(f"Image Class: {get_image_class} | Image Shape: {img_array.shape} -> [hight,width,color channel]")
plt.axis(False)


from torchvison import transforms
# data transform from image to tensor 
data_transform = transforms.Compose([
    # resize image to 64 X 64
    transforms.resize(size=(64,64)),

    # flip the image randomly on the horizontal # data augmentation
    transforms.RandomHorizontalFlip(p=0.5),

    #image inform of PIL to tensor
    transforms.Totensor()   
    ])



def plot_transformed_images(image_paths:list,transform,n=3,seed=None):

    if seed:
        random.seed(seed)

    random_image_paths = random.sample(image_path,k=n)

    for image_path in random_image_paths:
        with Image.open(image_path) as f:
            fig,ax = plt.subplot(nrows=1,ncols=2)
            ax[0].imshow(f)
            ax[0].set_title(f"Original\nSize: {f.size}")
            ax[0].axis[False]

            transformed_image = transform(f)

            # change channel to first for torch 
            transformed_image.permute(1,2,0) # from(h,w,c) to (c,h,w)
            ax[1].imshow(transformed_image)
            ax[1].set_title(f"Transformed\nShape: {transformed_image.shape}")
            ax[1].axis(False)
            fig.suptitle(f"class:{image_path.parent.stem}",fontsize=16)

plot_transformed_images(image_paths = image_path_list,transform=data_transform,n=3,seed=42)


# use ImageFolder to create dataset(s)
from torchvision import datasets

train_data = datasets.ImageFolder(root=train_dir,
                                  transform = data_transform,
                                  target_transform=None)

test_data = datasets.ImageFolder(root=test_dir,
                                 transform=data_transform,
                                 target_transform=None)

class_names = train_data.classes
class_dict = train_data.class_to_idx
train_data.sample[0]
target = train_data.target # we can see many more things

# turn test and train dataset into dataloader
from torch.utils.data import DataLoader
train_dataloader = DataLoader(dataset=train_data,
                              batch_size=1,
                              num_workers=os.cpu_count(),shuffle=True)

test_datalaoder = DataLoader(dataset=test_data,
                              batch_size=1,
                              num_workers=os.cpu_count(),shuffle=False)



# custorm build dataloader
from typing import Tuple, Dict,List

ex. folder path = 'data/piza_steak_sushi/train/pizza/images..','data/piza_steak_sushi/train/sushi/images...','data/piza_steak_sushi/train/steak/images..'
target_dir = 'data/piza_steak_sushi/train'

class_names_found = sorted([entry.name for entry in list(os.scandir(target_dir))])

def find_classes(directory:str)-> Tuple[List[str],Dict[str,int]]:
    classes = sorted(entry.name for entry in os.scandir(directory) if entry.is_dict())

    if not classes:
        raise FileNotFoundError(f"could not found {directory}")

    class_to_idx = {class_name:i for i,class_name in enumerate(classes)}

    return classes, class_to_idx
