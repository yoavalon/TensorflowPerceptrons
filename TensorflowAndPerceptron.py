import tensorflow as tf

#training dataset

T, F = 1., -1.
train_x = [
 [T, T],
 [T, F],
 [F, T],
 [F, F],
]
train_y = [
 [T],
 [F],
 [F],
 [F],
]
#Model Variable

w1 = tf.Variable(tf.random_normal([2, 2]))
b1 = tf.Variable(tf.zeros([2]))

w2 = tf.Variable(tf.random_normal([2, 1]))
b2 = tf.Variable(tf.zeros([1]))

out1 = tf.tanh(tf.add(tf.matmul(train_x, w1), b1))
out2 = tf.tanh(tf.add(tf.matmul(out1, w2), b2))

error = tf.subtract(train_y, out2)
cost = tf.reduce_mean(tf.square(error))

optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(cost)

#session 

with tf.Session() as sess : 
    tf.global_variables_initializer().run()

    err, target = 1, 0.01
    epoch, max_epochs = 0, 5000
    while err > target and epoch < max_epochs:
         epoch += 1
         err, _ = sess.run([cost, optimizer])
         print(f'epoch: {epoch} mse: {err}')
        
    print(sess.run(w1))
    print(sess.run(b1))
    print(sess.run(w2))
    print(sess.run(b2))
