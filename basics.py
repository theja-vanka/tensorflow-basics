import os
import tensorflow as tf

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

x = tf.constant(4, shape=(1, 1), dtype=tf.float32)
print(x)

y = tf.constant([1, 2, 3])
print(y)

x = tf.constant([[1, 2, 3], [4, 5, 6]])
print(x)

x = tf.ones((3, 3))
print(x)

x = tf.zeros((3, 3))
print(x)

x = tf.eye(3)
print(x)

x = tf.random.normal((3, 3), mean=0, stddev=1)
print(x)

x = tf.random.uniform((3, 3), minval=0, maxval=1)
print(x)

x = tf.range(10)
print(x)
