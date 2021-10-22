import tensorflow as tf

a = tf.zeros([2,2])
b = tf.ones(3)
c = tf.fill([3,3,3],9)
d = tf.constant(([1,5],[1,2],[2,3]),dtype=tf.int32)
print(a)
print(b)
print(c)
print(d)