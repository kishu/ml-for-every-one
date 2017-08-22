import tensorflow as tf

# Training and Test datasets

# Training Data
x_train = [
    [1, 2, 1],
    [1, 3, 2],
    [1, 3, 4],
    [1, 5, 5],
    [1, 7, 5],
    [1, 2, 5],
    [1, 6, 6],
    [1, 7, 7]
]

y_train = [
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 0, 0]
]

# Test Data
x_test = [
    [2, 1, 1],
    [3, 1, 2],
    [3, 3, 4]
]

y_test = [
    [0, 0, 1],
    [0, 0, 1],
    [0, 0, 1]
]

# Model Input and Output
X = tf.placeholder(tf.float32, shape=(None, 3))
Y = tf.placeholder(tf.float32, shape(None, 3))

# Model parameters
W = tf.Variable(tf.random_normal[3, 3], name="weight")
b = tf.Variable(tf.random_normal[3], name="bias")

