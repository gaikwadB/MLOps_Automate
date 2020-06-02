#import packages
from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from keras.optimizers import Adam

#load dataset
dataset = mnist.load_data(path="/root/mlops/mnist.npz")

