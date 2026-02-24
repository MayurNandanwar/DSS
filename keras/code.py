# Data PreProcessing
import numpy as np
from random import randint
from sklearn.utils import shuffle
from sklearn.preprocessing import MinMaxScaler

train_label = []
train_samples =[]

# generate train  and test random 
for i in range(50):
    # 5% of younger individuals experience the side effects
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_label.append(1)

    # 5% of older individuals not experience the side effects
    random_older = randint(65,100)
    train_samples.append(random_older)
    train_label.append(0)

for i in range(1000):
    # 95% of younger individuals not experience the side effects
    randon_younger = randint(13,64)
    train_samples.append(random_younger)
    train_label.append(0)

    # 95% of older individuals not experience the side effects
    random_older = randint(65,100)
    train_samples.append(random_older)
    train_label.append(1)

train_label = np.array(train_label)
train_samples = np.array(train_samples)

train_label,train_samples = shuffle(train_label,train_samples)


scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_sample = scaler.fit_transform(train_samples.reshape(-1,1)) # reshape because does not accept the 1 D array each value [0.213],[0.998]


# sequential model using keras
import tensorflow as tf
from tenssorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import categorical_crossentropy


physical_devices = tf.config.experimental.list_physical_device('GPU')
print("num of GPU::",len(physical_devices))
tf.config.experimental.set_memory_growth(physical_devices[0],True)

# linear stack of layer 
model = Sequential([
    Dense(units=16,input_shape(1,),activation='relu'),
    Dense(units=32,activation='relu'),
    Dense(units=2,activation='softmax')
                    ])

# see the sumamry
model.summary()

# optimizer, learning rate and metrics
model.compile(optimizer=Adam(learning_rate=0.0001,loss='sparse_categorical_crossentropy',metrics=['accuracy']))

model.fit(x=scaled_train_sample,y=train_label,batch_size=10,epoch=30,shuffle=True,verbose=2)

# add validation split

model.fit(x=scaled_train_sample,y=train_label,validation_split=0.1,batch_size=10,epoch=30,shuffle=True,verbose=2)
# we can also add validation_data = validation_set


# create test set
test_label = []
test_samples =[]
# generate train  and test random 
for i in range(50):
    # 5% of younger individuals experience the side effects
    random_younger = randint(13,64)
    test_samples.append(random_younger)
    test_label.append(1)

    # 5% of older individuals not experience the side effects
    random_older = randint(65,100)
    test_samples.append(random_older)
    test_label.append(0)

test_label = np.array(test_label)
test_samples = np.array(test_samples)

test_label,test_samples = shuffle(test_label,test_samples)

scaled_test_samples = scaler.fit_transform(test_samples.reshape(-1,1))

predictions = model.predict(x = scaled_test_samples,batch_size=10,verbose=0)

rounded_prediction = np.argmax(predictions,axis=-1)


# confusion metrics
from sklear.metrics import confusion_metrix

confusion_metrix(y_true=test_label,y_pred = rounded_prediction)

# model.save()
import os.path
if os.path.isfile('model/medical_trial_model.h5') is False:
    model.save('models/medical_trial_model.h5')


from tensorflow.keras.models import load_model
new_model = load_model('models/medical_trial_model.h5')

#summary
new_model.summary()

# get params
new_model.get_weights()

#optimizers:
new_model.optimizer

# model to json or yaml
json_string = model.to_json()

from tensorflo3.keras.models import model_from_json,model_from_yaml
model_architecture = model_from_json(json_string)

# save weights
import os.path
if os.path.isfile('models/my_model_weights.h5') is False:
    model.save_weights('models/my_model_weights.h5')

model2 = Sequential([
        Dense(units=16,input_shape=(1,),activation='relu'),
        Dense(units=32,activation='relu'),
        Dense(unit=2,activation='softmax')
        ])

model2.load_weights('models/my_model_weights.h5')

####
model2.get_weights()




#### Convolution Neural Network 
import numpy as np
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation,Dense,Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Model
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.processing.image import ImageDataGenerator
from sklearn.metrics import confusion_metrics
import itertools
import os
import shutil
import random
import glob
import matplotlib.pyplot as plt
import warnings
warning.simplefilter(action='ignore',category='FutureWarning')
%matplotlib inline


physical_devices = tf.config.experimental.list_physical_device('GPU')
print("num of GPU::",len(physical_devices))
tf.config.experimental.set_memory_growth(physical_devices[0],True)

# dog_vs_cat has both category 

os.chdir('data/dog_vs_cat')
if os.path.isdir('train/dog') is False:
    os.makedirs('train/dog')
    os.makedirs('train/cat')
    os.makedirs('valid/dog')
    os.makedirs('valid/cat')
    os.makedirs('test/dog')
    os.makedirs('test/cat')

    for c in random.sample(glob.glob('cat*'),500):
        shutil.move(c,'train/cat')

    for c in random.sample(glob.glob('dog*'),500):
        shutil.move(c,'train/dog')

    for c in  random.sample(glob.glob('cat*'),100):
        shutil.move(c,'valid/cat')

    for c in random.sample(glob.glob('dog*'),100):
        shutil.move(c,'valid/dog')

    for c in  random.sample(glob.glob('cat*'),50):
        shutil.move(c,'test/cat')

    for c in random.sample(glob.glob('dog*'),50):
        shutil.move(c,'test/dog')
os.chdir('../../')

train_path = 'data/dog_vs_cat/train'
valid_path = 'data/dog_vs_cat/valid'
test_path = 'data/dog_vs_cat/test'


train_batches = ImageDataGenerator(processing_function=tf.keras.applications.vgg16.preprocess_input)\
                .flpow_from_directory(directory=train_path,target_size=(224,224),classes=['cat','dog'],batch_size=10)

valid_batches = ImageDataGenerator(processing_function=tf.keras.applications.vgg16.preprocess_input)\
                .flpow_from_directory(directory=valid_path,target_size=(224,224),classes=['cat','dog'],batch_size=10)

test_batches = ImageDataGenerator(processing_function=tf.keras.applications.vgg16.preprocess_input)\
                .flpow_from_directory(directory=test_path,target_size=(224,224),classes=['cat','dog'],batch_size=10,shuffle=False)


assert train_batches ==1000
assert valid_batches==200
assert test_batches==100

imgs,label = next(train_batches)

def plotImages(image_arr):
    fig,axis=plt.subplots(1,10,figsize=(20,20))
    axes = axes.flatten()
    for img,ax in zip(image_arr,axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

plotImages(imgs)


#######################################
# Build and train CNN:
model = Sequential([
        Conv2D(filters=32,kernel_size=(3,3),actuvation='relu',padding='same',input_shape=(224,224,3)),
        MaxPool2D(pool_size=(2,2),stride=2),
        Conv2D(filters=64,kernel_size=(3,3),activation='relu',padding='same'),
        MaxPool2D(pool_size=(2,2),stride=2),
        Flatten(),
        Dense(units=2,activation='softmax'),
                ])

model.summary()

model.compile(optimizer=Adam(learning_rate=0.0001,loss='categorical_crossentropy',metrics=['accuracy']))

model.fit(x=train_batches,validation_data=valid_batches,epochs=10,verbose=2) # here we have not specified y , because data is stored as genertor so generator itself actualy conatins corresponding labels so not need to specify


#predict
test_imgs,test_lables = next(test_batches)
plotImages(test_imgs)

test_batches.classes
#prediction
predictions = model.predict(x=test_batches,verbose=0)
np.round(predictions)

# confusion metrics
cm = confusion_metrix(y_true=test_batches.classes,y_pred = np.argmax(predictions,axis=-1))

###########################################################
# fine tune model vgg16
vgg16_model = tf.keras.applications.vgg16.VGG16()

vgg16_model.summary()

def count_params(model):
    non_trainable_weights = np.sum([np.prod(v.shape.as_list()) for v in model.non_trainable_weights])
    trainable_weights  = np.sum([np.prod(v.shape.as_list()) for v in model.trainable_weights])
    return {'non_trainable_params':non_trainable_weights,'trainable_params':trainable_weights}

params = count_params(vgg16_model)
assert params['non_trainable_params']==0
assert params['trainable_params'] == 138357544

# remove last layer
model = Sequential()
for layer in vgg16_model.layers[:-1]:
    model.add(layer)

params = count_params(vgg16_model)
assert params['non_trainable_params']==0
assert params['trainable_params'] == 134260544

# freeze the trainable params
for layer in model.layers:
    layer.trainable = False

model.add(Dense(units=2,activation='softmax'))
model.summary()

params = count_params(vgg16_model)
assert params['non_trainable_params']==134260544
assert params['trainable_params'] == 8194


# train the fine-tuned vgg16 model
model.compile(optimizer=Adam(learning_rate=0.0001),loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(x=train_batches,validation_data=valid_batches,epochs=5,verbose=2)

assert model.history.history.get('accuracy')[-1]>0.95

# prediction usiing fine-tuned vgg16
predictions=model.predict(x=test_batches,verbose=0)

cm = confusion_metrix(y_true=test_batches.classes,y_pred = np.argmax(predictions,axis=-1))

# MobileNet : LightWeight CNN model
mobile = tf.keras.applications.mobilenet.MobileNet()

from tensorflow.keras.processing import image
from tensorflow.keras.applications import imagenet_utils

def prepare_image(file):
    img_path = 'data/mobilenet-samples/'
    img = image.load_img(img_path+file,target_size=(224,224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array,axis=0)
    return tf.keras.applications.mobilenet.process_input(img_array_expanded_dims)

from Ipython.display import Image
Image(filename='data/mobilenet-samples/1.PNG',width=300,hight=200)

preprocessed_image=prepare_image('1.PNG')
predictions = mobile.predict(preprocessed_image)
results = imagenet_utils.decode_predictions(predictions)



################# dataset contain class wise folder ex.dataset/class1, class2,class3 folders

# move 30 samples from train for each class to valid and 5 sample to test
os.chdir('data/sign-language-digits-dataset')
if os.path.isdir('train/0') is False:
    os.makedirs('train')
    os.makedirs('valid')
    os.makedirs('test')

    # 10 class i have so 
    for i in  range(0,10):
        shutil.move(f'{i}','train')
        os.mkdir(f'valid/{i}')
        os.mkdir(f'test/{i}')

        valid_samples = random.sample(os.listdir(f'train/{i}'),30)
        for j in valid_samples:
            shutil.move(f'train/{i}/{j}',f'valid/{i}')

        test_samples = random.sample(os.listdir(f'train/{i}',5))
        for k in test_samples:
            shutil.move(f'train/{i}/{k}',f'test/{i}')
os.chdir('../../')



train_batches = ImageDataGenerator(processing_function=tf.keras.applications.mobilenet.preprocess_input)\
                .flpow_from_directory(directory=train_path,target_size=(224,224),batch_size=10)

valid_batches = ImageDataGenerator(processing_function=tf.keras.applications.vgg16.preprocess_input)\
                .flpow_from_directory(directory=valid_path,target_size=(224,224),batch_size=10)

test_batches = ImageDataGenerator(processing_function=tf.keras.applications.vgg16.preprocess_input)\
                .flpow_from_directory(directory=test_path,target_size=(224,224),batch_size=10,shuffle=False)

assert train_batches.n == 1712
assert valid_batches.n ==300
assert test_batches.n == 50
assert train_batches.num_classes ==valid_batches.num_classes == test_batches.num_classes ==10


mobile = tf.keras.applications.mobilenet.MobileNet()

mobile.summary()

params = count_params(mobile)

params = count_params(mobile)
assert params['non_trainable_params'] == 21888
assert params['trainable_params'] == 4231976

x = mobile.layers[-6].output
output = Dense(units=10,actuvation='softmax')(x)

model = Model(inputs=mobile.input,output=output)

for layer in model.layers[:-23]:
    layer.trainable=False

model.summary()

params = count_params(model)
assert params['non_trainable_params'] == 1365184
assert params['trainable_params'] == 1873930



# train the fine-tuned vgg16 model
model.compile(optimizer=Adam(learning_rate=0.0001),loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(x=train_batches,validation_data=valid_batches,epochs=5,verbose=2)

# prediction usiing fine-tuned vgg16
predictions=model.predict(x=test_batches,verbose=0)

cm = confusion_metrix(y_true=test_batches.classes,y_pred = np.argmax(predictions,axis=-1))


## data Augmentation 
from tensoflow.keras.preprocessing.image import ImageDatagenerator
def plotImages(images_arr):
    fig,axes = plt.subplots(1,10,figsize=(20,20))
    axes =axes.flatten()
    for image,ax in zip(images_arr,axes):
        ax.imshow(image)
        ax.axis('off')
    plt.tight_layout()
    plt.show()

gen = ImageDataGenerator(rotation_range=10,
                         width_shift_range=0.1,
                         hight_shift_range=0.1,
                         shear_range=0.15,
                         zoom_range=0.1,
                         channel_shift_range=10,
                         horizontal_flip=True)

choosen_image = random.choice(os.listdir('data/dog-vs-cat/train/dog'))

image_path = 'data/dog-vs-cat/train/dog/'+choosen_image

assert os.path.isfile(image_path)

image = np.expand_dims(plt.imread(image_path),0)
plt.imshow(image[0])

aug_iter = gen.flow(image)

# get 10 sample if augmented images
aug_images = [next(aug_iter)[0].astype(np.uint8) for i in range(10)]

plotImages(aug_images)