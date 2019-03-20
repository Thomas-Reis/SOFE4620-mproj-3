import tensorflow as tf
import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

test_directory = 'Numbers/'
train_directory = 'Numbers/'
validation_directory = 'Numbers/'

i = 0
default_label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
train_images = []
train_labels = []

for f in os.listdir(train_directory):
    # Opens the test Image
    img = Image.open(train_directory + f)
    # Converts image to Black and White
    img = img.convert('L')
    # Sets a numpy array of size [width x height] with the greyscale value of each pixel (>200 = White), (<50 = Black))
    arr = np.array(img)
    train_images.append(np.copy(arr))
    default_label[i] = 1
    train_labels.append(np.copy(default_label))
    default_label[i] = 0
    i += 1
    # print('WIDTH: ' + str(arr.shape[1]))
    # print('HEIGHT: ' + str(arr.shape[0]))
    # print(arr)


validation_images = []
validation_labels = []
for f in os.listdir(validation_directory):
    # Opens the test Image
    img = Image.open(validation_directory + f)
    # Converts image to Black and White
    img = img.convert('L')
    # Sets a numpy array of size [width x height] with the greyscale value of each pixel (>200 = White), (<50 = Black))
    arr = np.array(img)
    validation_images.append(np.copy(arr))
    default_label[i] = 1
    validation_labels.append(np.copy(default_label))
    default_label[i] = 0
    i += 1
    # print('WIDTH: ' + str(arr.shape[1]))
    # print('HEIGHT: ' + str(arr.shape[0]))
    # print(arr)


test_images = []
test_labels = []
for f in os.listdir(test_directory):
    # Opens the test Image
    img = Image.open(test_directory + f)
    # Converts image to Black and White
    img = img.convert('L')
    # Sets a numpy array of size [width x height] with the greyscale value of each pixel (>200 = White), (<50 = Black))
    arr = np.array(img)
    test_images.append(np.copy(arr))
    default_label[i] = 1
    test_labels.append(np.copy(default_label))
    default_label[i] = 0
    i += 1
    # print('WIDTH: ' + str(arr.shape[1]))
    # print('HEIGHT: ' + str(arr.shape[0]))
    # print(arr)


# Number of training examples we have
n_train = len(train_images)
# Number of validation examples we have
n_validation = len(validation_images)
# Number of testing examples we have
n_test = len(test_images)

# set the number of neurons per layer
# 45 input for each pixel
n_input = 45
# 5 because the example has 5 on hidden layer 1
n_hidden1 = 5
# 10 for output as classification
n_output = 10

# Neural Network Variables
learning_rate = 1e-4
n_iterations = 1000
batch_size = 10
dropout = 0.5

X = tf.placeholder("float", [None, n_input])
Y = tf.placeholder("float", [None, n_output])
keep_prob = tf.placeholder(tf.float32)


weights = {
    'w1': tf.Variable(tf.truncated_normal([n_input, n_hidden1], stddev=0.1)),
    'out': tf.Variable(tf.truncated_normal([n_hidden1, n_output], stddev=0.1)),
}

biases = {
    'b1': tf.Variable(tf.constant(0.1, shape=[n_hidden1])),
    'out': tf.Variable(tf.constant(0.1, shape=[n_output]))
}

layer_1 = tf.add(tf.matmul(X, weights['w1']), biases['b1'])
layer_drop = tf.nn.dropout(layer_1, keep_prob)
output_layer = tf.matmul(layer_1, weights['out']) + biases['out']

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=output_layer))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

correct_pred = tf.equal(tf.argmax(output_layer, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
