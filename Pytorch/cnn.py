# https://github.com/mrdbourke/pytorch-deep-learning/blob/main/03_pytorch_computer_vision.ipynb
# pip install torch
import matplotlib.pyplot as plt
import torch
from torchvision import datasets
from torchvision.transforms import ToTensor

train_data = datasets.FashionMNIST(root='data',train=True,download=True,transform=ToTensor(),target_transform=None)
test_data = datasets.FashionMNIST(root='data',train=False,download=True,transform=ToTensor(),target_transform=None)
train_data
class_names = train_data.classes

## To see images using plotly multiple images 4 row , 4 column with label
torch.manual_seed(42)
plt.figure(figsize=(9,9))
row,col = 4,4

for i in range(1,row*col+1):
  image_idx = torch.randint(0,len(train_data),size=(1,)).item()
  image,label = train_data[image_idx]
  plt.subplot(row,col,i)
  plt.imshow(image.squeeze(),cmap='gray')
  plt.title(class_names[label])
  plt.axis(False)

from torch import nn

test_data,train_data

from torch.utils.data import DataLoader

train_dataloader = DataLoader(train_data, batch_size=32, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=32, shuffle=True)



train_features, train_labels = next(iter(train_dataloader))
print(f"Feature batch shape: {train_features.size()}")
print(f"Labels batch shape: {train_labels.size()}")

len(train_labels)

image_size = train_features.size()[-1]
input_channel = 1
feature_map_num = 10
output_shape = len(train_labels)

class FashionMNISTModel_v1(nn.Module):
  def __init__(self,input_channel,feature_map_num:int,output_shape=10,image_size=28):
    super().__init__()
    self.conv_layer_1 = nn.Sequential(
                        nn.Conv2d(in_channels = input_channel,
                                      out_channels = feature_map_num,
                                      kernel_size = 3,
                                      stride=1,
                                      padding=1),
                        nn.ReLU(),
                        nn.Conv2d(in_channels = feature_map_num,
                                  out_channels = feature_map_num,
                                  kernel_size = 3,
                                  stride=1,
                                  padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=2)
    )  
    self.conv_layer_2 = nn.Sequential(
                        nn.Conv2d(in_channels=feature_map_num,
                                  out_channels=feature_map_num,
                                  kernel_size=3,
                                  stride=1,
                                  padding=1),
                        nn.ReLU(),
                        nn.Conv2d(in_channels=feature_map_num,
                                  out_channels=feature_map_num,
                                  kernel_size=3,
                                  stride=1,
                                  padding=1),
                        nn.ReLU(),
                        nn.MaxPool2d(kernel_size=2)
    )
    # Compute flatten size dynamically using a dummy input
    with torch.no_grad():
        dummy_input = torch.zeros(1, input_channel, image_size, image_size)
        x = self.conv_layer_1(dummy_input)
        x = self.conv_layer_2(x)
        flatten_size = x.shape[1] * x.shape[2] * x.shape[3]
                        
    # Classifier
    self.classifier_layer = nn.Sequential(
        nn.Flatten(),
        nn.Linear(in_features=flatten_size, out_features=output_shape)
    )

  def forward(self,x):
    x = self.conv_layer_1(x)
    x = self.conv_layer_2(x)
    x = self.classifier_layer(x)
    return x

image_size = train_features.size()[-1]
output_shape = len(train_labels)
input_channel = 1
feature_map_num = 10
output_shape = len(train_labels)

model = FashionMNISTModel_v1(input_channel,feature_map_num,output_shape=output_shape,image_size=image_size)

model.state_dict()
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(params=model.parameters(),lr=0.01)

device = 'cuda' if torch.cuda.is_available() else 'cpu'


# Calculate accuracy (a classification metric)
def accuracy_fn(y_true, y_pred):
    """Calculates accuracy between truth labels and predictions.

    Args:
        y_true (torch.Tensor): Truth labels for predictions.
        y_pred (torch.Tensor): Predictions to be compared to predictions.

    Returns:
        [torch.float]: Accuracy value between y_true and y_pred, e.g. 78.45
    """
    correct = torch.eq(y_true, y_pred).sum().item()
    acc = (correct / len(y_pred)) * 100
    return acc


import time
def print_train_time(start: float, end: float, device: str) -> float:
    """
    Prints and returns the training time between start and end timestamps.

    Args:
        start (float): Training start time (from time.time()).
        end (float): Training end time (from time.time()).
        device (str): Device used for training ("cpu" or "cuda").

    Returns:
        float: Total training time in seconds.
    """
    total_time = end - start
    print(f"\n[INFO] Training completed on {device}.")
    print(f"[INFO] Total training time: {total_time:.3f} seconds ({total_time/60:.2f} minutes)")
    return total_time

def train_step(model: torch.nn.Module,
               data_loader: torch.utils.data.DataLoader,
               loss_fn: torch.nn.Module,
               optimizer: torch.optim.Optimizer,
               accuracy_fn,
               device: torch.device = device):

    train_loss, train_acc = 0, 0
    model.to(device)
    for batch, (X, y) in enumerate(data_loader):
        # Send data to GPU
        X, y = X.to(device), y.to(device)

        # 1. Forward pass
        y_pred = model(X)

        # 2. Calculate loss
        loss = loss_fn(y_pred, y)
        train_loss += loss
  
        train_acc += accuracy_fn(y_true=y,
                                 y_pred=y_pred.argmax(dim=1)) # Go from logits -> pred labels

        # 3. Optimizer zero grad
        optimizer.zero_grad()

        # 4. Loss backward
        loss.backward()

        # 5. Optimizer step
        optimizer.step()

    # Calculate loss and accuracy per epoch and print out what's happening
    train_loss /= len(data_loader)
    train_acc /= len(data_loader)
    print(f"Train loss: {train_loss:.5f} | Train accuracy: {train_acc:.2f}%")


def test_step(data_loader: torch.utils.data.DataLoader,
              model: torch.nn.Module,
              loss_fn: torch.nn.Module,
              accuracy_fn,
              device: torch.device = device):
    test_loss, test_acc = 0, 0
    model.to(device)
    model.eval() # put model in eval mode
    # Turn on inference context manager
    with torch.inference_mode(): 
        for X, y in data_loader:
            # Send data to GPU
            X, y = X.to(device), y.to(device)
            
            # 1. Forward pass
            test_pred = model(X)
            
            # 2. Calculate loss and accuracy
            test_loss += loss_fn(test_pred, y)
            test_acc += accuracy_fn(y_true=y,
                y_pred=test_pred.argmax(dim=1) # Go from logits -> pred labels
            )
        
        # Adjust metrics and print out
        test_loss /= len(data_loader)
        test_acc /= len(data_loader)
        print(f"Test loss: {test_loss:.5f} | Test accuracy: {test_acc:.2f}%\n")



# make prediction 
torch.manual_seed(42)
def eval_model(model: torch.nn.Module, 
               data_loader: torch.utils.data.DataLoader, 
               loss_fn: torch.nn.Module, 
               accuracy_fn):
    """Returns a dictionary containing the results of model predicting on data_loader.

    Args:
        model (torch.nn.Module): A PyTorch model capable of making predictions on data_loader.
        data_loader (torch.utils.data.DataLoader): The target dataset to predict on.
        loss_fn (torch.nn.Module): The loss function of model.
        accuracy_fn: An accuracy function to compare the models predictions to the truth labels.

    Returns:
        (dict): Results of model making predictions on data_loader.
    """
    loss, acc = 0, 0
    model.eval()
    with torch.inference_mode():
        for X, y in data_loader:
            X, y = X.to(device), y.to(device)
            # Make predictions with the model
            y_pred = model(X)
            
            # Accumulate the loss and accuracy values per batch
            loss += loss_fn(y_pred, y)
            acc += accuracy_fn(y_true=y, 
                                y_pred=y_pred.argmax(dim=1)) # For accuracy, need the prediction labels (logits -> pred_prob -> pred_labels)
        
        # Scale loss and acc to find the average loss/acc per batch
        loss /= len(data_loader)
        acc /= len(data_loader)
        
    return {"model_name": model.__class__.__name__, # only works when model was created with a class
            "model_loss": loss.item(),
            "model_acc": acc}



len(train_dataloader)

from timeit import default_timer  as timer
training_timer_start_model = timer()
for epoch in range(10):
  print(f"Epoch: {epoch}\n---------")
  model_train = train_step(model=model,
                          data_loader=train_dataloader,
                          loss_fn=loss_fn,
                          optimizer=optimizer,
                          accuracy_fn=accuracy_fn)
  
  model_test_results = test_step(data_loader=test_dataloader,
                               model=model,
                               loss_fn=loss_fn,
                               accuracy_fn=accuracy_fn)
  
training_timer_end_model = timer()

total_training_time  = print_train_time(training_timer_start_model,training_timer_end_model,device) 

total_training_time

# Calculate model 0 results on test dataset
model_results = eval_model(model=model, data_loader=list(test_dataloader),
    loss_fn=loss_fn, accuracy_fn=accuracy_fn
)
model_results

def make_predictions(model: torch.nn.Module, data: list, device: torch.device = device):
    pred_probs = []
    model.eval()
    with torch.inference_mode():
        for sample in data:
            # Prepare sample
            sample = torch.unsqueeze(sample, dim=0).to(device) # Add an extra dimension and send sample to device

            # Forward pass (model outputs raw logit)
            pred_logit = model(sample)

            # Get prediction probability (logit -> prediction probability)
            pred_prob = torch.softmax(pred_logit.squeeze(), dim=0) # note: perform softmax on the "logits" dimension, not "batch" dimension (in this case we have a batch size of 1, so can perform on dim=0)

            # Get pred_prob off GPU for further calculations
            pred_probs.append(pred_prob.cpu())
            
    # Stack the pred_probs to turn list into a tensor
    return torch.stack(pred_probs)

import random
# random.seed(42)
test_samples = []
test_labels = []
for sample, label in random.sample(list(test_data), k=9):
    test_samples.append(sample)
    test_labels.append(label)

# Make predictions on test samples with model 2
pred_probs= make_predictions(model=model, 
                             data=test_samples)
# Turn the prediction probabilities into prediction labels by taking the argmax()
pred_classes = pred_probs.argmax(dim=1)
pred_classes

# Plot predictions
plt.figure(figsize=(9, 9))
nrows = 3
ncols = 3
for i, sample in enumerate(test_samples):
  # Create a subplot
  plt.subplot(nrows, ncols, i+1)

  # Plot the target image
  plt.imshow(sample.squeeze(), cmap="gray")

  # Find the prediction label (in text form, e.g. "Sandal")
  pred_label = class_names[pred_classes[i]]

  # Get the truth label (in text form, e.g. "T-shirt")
  truth_label = class_names[test_labels[i]] 

  # Create the title text of the plot
  title_text = f"Pred: {pred_label} | Truth: {truth_label}"
  
  # Check for equality and change title colour accordingly
  if pred_label == truth_label:
      plt.title(title_text, fontsize=10, c="g") # green text if correct
  else:
      plt.title(title_text, fontsize=10, c="r") # red text if wrong
  plt.axis(False);


# Import tqdm for progress bar
from tqdm.auto import tqdm

# 1. Make predictions with trained model
y_preds = []
model.eval()
with torch.inference_mode():
  for X, y in tqdm(test_dataloader, desc="Making predictions"):
    # Send data and targets to target device
    X, y = X.to(device), y.to(device)
    # Do the forward pass
    y_logit = model(X)
    # Turn predictions from logits -> prediction probabilities -> predictions labels
    y_pred = torch.softmax(y_logit, dim=1).argmax(dim=1) # note: perform softmax on the "logits" dimension, not "batch" dimension (in this case we have a batch size of 32, so can perform on dim=1)
    # Put predictions on CPU for evaluation
    y_preds.append(y_pred.cpu())
# Concatenate list of predictions into a tensor
y_pred_tensor = torch.cat(y_preds)

y_pred_tensor

# See if torchmetrics exists, if not, install it
try:
    import torchmetrics, mlxtend
    print(f"mlxtend version: {mlxtend.__version__}")
    assert int(mlxtend.__version__.split(".")[1]) >= 19, "mlxtend verison should be 0.19.0 or higher"
except:
    !pip install -q torchmetrics -U mlxtend # <- Note: If you're using Google Colab, this may require restarting the runtime
    import torchmetrics, mlxtend
    print(f"mlxtend version: {mlxtend.__version__}")

from torchmetrics import ConfusionMatrix
from mlxtend.plotting import plot_confusion_matrix

# 2. Setup confusion matrix instance and compare predictions to targets
confmat = ConfusionMatrix(num_classes=len(class_names), task='multiclass')
confmat_tensor = confmat(preds=y_pred_tensor,
                         target=test_data.targets)

# 3. Plot the confusion matrix
fig, ax = plot_confusion_matrix(
    conf_mat=confmat_tensor.numpy(), # matplotlib likes working with NumPy 
    class_names=class_names, # turn the row and column labels into class names
    figsize=(10, 7)
);


# save model
from pathlib import Path 
model_path = Path('models')
model_path.mkdir(parents=True,exist_ok=True)

model_name = 'torch_vision_cnn.pth'

save_model_path = model_path/model_name

torch.save(obj = model.state_dict(),f=path)

# use this model.state_dict() # parameters in new model

loaded_model = FashionMNISTModel_v1(input_channel=1,feature_map_num=10,output_shape=len(class_names),image_size=28)

# load state_dict of previous model
loaded_model.load_state_dict(save_model_path)

loaded_model.to(device)

# result of loeaded model should be similar to model result because we have use params of it

loaded_model_res = eval_model(model=loaded_model, data_loader=list(test_dataloader))

# check if both model results are close to each other 
torch.isclose(torch.tensor(model['model_loss']),
              torch.tensor(loaded_model['model_loss']),
              atol= 1e-08 # you can adjust value of  this means afrer decimal point 8 values should match 
              )