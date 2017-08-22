'''
MNIST
Modified National Institute of Standards and Technology
국립표준기술연구소 데이터의 (modefied)서브셋을 MNIST라 한다.

TensoFlow에서 제공하는 MNIST 관련문서(한글)
https://tensorflowkorea.gitbooks.io/tensorflow-kr/content/g3doc/tutorials/mnist/beginners/
'''

import tensorflow as tf
import matplotlib.pyplot as plt
import random
from tensorflow.examples.tutorials.mnist import input_data

# one_hot - The locations represented by indices in indices take value on_value, while all other locations take value off_value.
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
nb_classes = 10

# Model Input and Output
# MNIST data image of shape 28 * 28 = 784
X = tf.placeholder(tf.float32, shape=(None, 784))
Y = tf.placeholder(tf.float32, shape=(None, nb_classes))

# Model parameters
W = tf.Variable(tf.random_normal([784, nb_classes]), name="weight")
b = tf.Variable(tf.random_normal([nb_classes]), name="bias")

# Hypothesis (using softmax)
hypothesis = tf.nn.softmax(tf.matmul(X, W) + b)

# cost/loss(Cross Entropy)
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(0.1).minimize(cost)

# Test Model
is_correct = tf.equal(tf.arg_max(hypothesis, 1), tf.arg_max(Y, 1))

# Calculate accuracy
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))

# parameters
training_epochs = 15
batch_size = 100

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    total_batch = int(mnist.train.num_examples / batch_size)
    
    for epoch in range(training_epochs):
        avg_cost = 0
        for i in range(total_batch):
            # Training Data
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            c, _ = sess.run([cost, optimizer], feed_dict={X: batch_xs, Y: batch_ys})
            avg_cost += c / total_batch
        print("Epoch:", "%04d" % (epoch + 1), "cost = ", "{:.9f}".format(avg_cost))

    # Test the model using test sets
    print("Accuracy: ", accuracy.eval(session=sess, feed_dict={X: mnist.test.images, Y: mnist.test.labels}))

    # Get one and predict
    r = random.randint(0, mnist.test.num_examples - 1)
    print("Label:", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
    print("Prediction:", sess.run(tf.argmax(hypothesis, 1), feed_dict={X: mnist.test.images[r:r + 1]}))
    plt.imshow(mnist.test.images[r:r + 1].reshape(28, 28), cmap="Greys", interpolation="nearest")
    plt.show()