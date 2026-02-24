# for vision data like images use torchvision, for audio data use torch audio, for text data use torchtext, to recommandation problem use torchrec


import torch
import numpy as np
import matplotlib.pyplot as plt

from torch import nn # nn contain all of pytorch building block for neural network

nn.Module is a calss has inbuild thing which help to create pytorch model easily ex. layers, optimizers layers etc

class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(1,requires_grad=True,dtype=torch.float32))
        self.bias = nn.paarameter(torch.randn(1,requires_grad=True,dtype=torch.float32))

    def forward(self,x:torch.Tensor)->torch.Tensor: # this defines forward computation of model.
        return self.weight * x +self.bias
    
# requires_grad = True at time of training and at time of prediction  = False
# because in training forward and backward propagation happen 
# in backward calculation gradiants are calculate based on error and then we update 
# weight and bies using this 
# in testing we are not doing this thats why False in testing.


# we can get the parameters of model using .params
model_0 = LinearRegression()
model_0.parameters()

# list name parameters, List of Tuple ex.[('weights',value),('bias',value)]
model_0.state_dict()

# torch.inference_mode() at time of prediction which turn off the requires_grade 
# we do not need track of gradient at time of prediction 
with torch.inference_mode():
    y_pred = model_0(X_test)

# also with torch.no_grad() work same as torch.inference_mode(), however torch.inference_mode() is preffered.

# Loss Function : also called as cost function , criterian.

# Optimizers : takes into account the loss and adjust the params to update the weights for reduce the loss.

# check the device on which model train
next(model_0.parameters()).device

# to set model to use cuda device
model_0.to(device)


# BCE : binary cross entropy -> this provides result in probability 
# BCEWithLogitLoss : get row outpout of model after to get probability use sigmoid on that we get probability  

# to check howmany values prediction equals to the true label (classification problem and use BCEWithLogitLoss)
torch.eq(y_true,y_pred).sum().item()

def accuracy(y_true,y_pred):
    correct = torch.eq(y_true,y_pred).sum().item()
    acuuracy = (correct/len(y_true)) * 100


# how to request the python file from github
import requests
request = requests.get('https://raw.githubusercontent.com/Nandan1041996/GHCL_Bot/refs/heads/main/exception.py')
with open('abcd.py','wb') as f:
    f.write(request.content)
# from abcd.py import any function then 

# BCEWithLogitLoss and CrossEntropyLoss provides logits , we have to apply sigmoid function to convert for binary classification and for multiclass we use softmax to convert into probability

####################
# CNN 
# torchvision.dataset :- get dataset and data loading function for computer vision
# torchvision.model : pretrain models that we can use 
# torchvision.transform : turns out image data to numbers or numeric data for ML models

input shape ex.(batch_size,color_channel,hight,width)
convolution layer :  extract and learn important feature
pooling layer: reduce dimensionality of learned features
padding : used to update the size of feature map if no padding then size of feature map reduce as it go ahead in process
if same padding then size of feature map will be same.

# create dummy data for image
images = torch.randn(size=(32,3,64,64)) #[batch_size,channel,hight,width]
test_image = images[0]

# to add extradimension , ex = image_shape = (3,24,24)
image_shape.unsqueeze(0).shape   # res = ([1,3,24,24]) or torch.unsqueeze(sample,dim=0).to(device)


 