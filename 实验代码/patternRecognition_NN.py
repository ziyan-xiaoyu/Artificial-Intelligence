import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt
import numpy as np

# 加载MNIST数据集，通过设置 one_hot=True 来使用独热编码标签
# 独热编码：对于每个图片的标签 y，10 位中仅有一位的值为 1，其余的为 0。
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


# mnist = tf.keras.datasets.mnist
# 权重正态分布初始化函数
def weight_variable(shape):
    # 生成截断正态分布随机数,shape表示生成张量的维度，mean是均值(默认=0.0)，stddev是标准差。
    # 取值范围为 [ mean - 2 * stddev, mean + 2 * stddev ]，这里为[-0.2, 0.2]
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


# 偏置量初始化函数
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)  # value=0.1, shape是张量的维度
    return tf.Variable(initial)


# 绘制‘准确率’随迭代数增加的折线图
def plot_broken_line(X, Y1, Y2):
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 在图中可以显示中文
    plt.figure(figsize=(20, 10), dpi=100)
    plt.plot(X, Y1, c='red', linestyle='-.', label="训练集上的准确率")
    plt.plot(X, Y2, c='blue', label="测试集上的准确率")
    plt.scatter(X, Y1, c='red')
    plt.scatter(X, Y2, c='blue')
    plt.legend(loc='best')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("迭代步数", fontdict={'size': 16})
    plt.ylabel("准确率", fontdict={'size': 16})
    plt.title("模型在训练集、测试集上的准确率随迭代步数的变化趋势图", fontdict={'size': 20})
    plt.show()


# 绘制‘损失函数值’随迭代数增加的折线图
def plot_broken_line2(X, Y):
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 在图中可以显示中文
    plt.figure(figsize=(20, 10), dpi=100)
    plt.plot(X, Y, c='green', label="损失函数值")
    plt.scatter(X, Y, c='green')
    plt.legend(loc='best')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("迭代步数", fontdict={'size': 16})
    plt.ylabel("损失函数值", fontdict={'size': 16})
    plt.title("每次迭代的损失函数值变化趋势图", fontdict={'size': 20})
    plt.show()


if __name__ == "__main__":
    print(int(mnist.train.num_examples))  # 55000
    print(int(mnist.test.num_examples))  # 10000

    # 为训练数据集的输入 x 和标签 y 创建占位符
    x = tf.placeholder(tf.float32, [None, 784])  # None用以指代batch的大小，意即输入图片的数量不定，一张图28*28=784
    y = tf.placeholder(tf.float32, [None, 10])
    # 意思是每个元素被保留的概率，keep_prob=1即所有元素全部保留。大量数据训练时，为了防止过拟合，添加Dropout层，设置一个0~1之间的小数
    keep_prob = tf.placeholder(tf.float32)

    # 创建神经网络第1层，输入层，激活函数为relu
    W_layer1 = weight_variable([784, 512])
    b_layer1 = bias_variable([512])
    h1 = tf.add(tf.matmul(x, W_layer1), b_layer1)  # W * x + b
    h1 = tf.nn.relu(h1)
    # 创建神经网络第2层，隐藏层，激活函数为relu
    W_layer2 = weight_variable([512, 1024])
    b_layer2 = bias_variable([1024])
    h2 = tf.add(tf.matmul(h1, W_layer2), b_layer2)  # W * h1 + b，h1为第1层的输出
    h2 = tf.nn.relu(h2)
    # 创建神经网络第3层，隐藏层，激活函数为relu
    W_layer3 = weight_variable([1024, 512])
    b_layer3 = bias_variable([512])
    h3 = tf.add(tf.matmul(h2, W_layer3), b_layer3)  # W * h2 + b，h2为第2层的输出
    h3 = tf.nn.relu(h3)
    # 新增神经网络第4层，隐藏层，激活函数为relu
    W_layer4 = weight_variable([512, 256])
    b_layer4 = bias_variable([256])
    h4 = tf.add(tf.matmul(h3, W_layer4), b_layer4)  # W * h3 + b，h3为第3层的输出
    h4 = tf.nn.relu(h4)
    # 新增神经网络第5层，隐藏层，激活函数为relu
    W_layer5 = weight_variable([256, 128])
    b_layer5 = bias_variable([128])
    h5 = tf.add(tf.matmul(h4, W_layer5), b_layer5)  # W * h4 + b，h4为第4层的输出
    h5 = tf.nn.relu(h5)
    # 新增神经网络第6层，隐藏层，激活函数为relu
    W_layer6 = weight_variable([128, 64])
    b_layer6 = bias_variable([64])
    h6 = tf.add(tf.matmul(h5, W_layer6), b_layer6)  # W * h5 + b，h5为第5层的输出
    h6 = tf.nn.relu(h6)
    # 创建神经网络第7层，输出层，激活函数为softmax
    W_layer7 = weight_variable([64, 10])
    b_layer7 = bias_variable([10])
    predict = tf.add(tf.matmul(h6, W_layer7), b_layer7)  # W * h6 + b，h6为第6层的输出
    y_conv = tf.nn.softmax(tf.matmul(h6, W_layer7) + b_layer7)
    # 计算交叉熵代价函数
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predict, labels=y))
    # 使用Adam下降算法优化交叉熵代价函数
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    # 预测是否准确的结果存放在一个布尔型的列表中
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y, 1))  # argmax返回的矩阵行中的最大值的索引号
    # 求预测准确率
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, 'float'))  # cast将布尔型的数据转换成float型的数据；reduce_mean求平均值

    # 初始化
    init_op = tf.global_variables_initializer()

    all_train_accuracy = []  # 用于存储绘图所需的数据
    all_test_accuracy = []
    all_step = []
    all_loss = []
    with tf.Session() as sess:
        sess.run(init_op)
        for i in range(550):  # 训练样本为55000，分成550批，每批为100个样本
            batch = mnist.train.next_batch(100)
            if i % 50 == 0:  # 每过50批，显示其在训练集上的准确率和在测试集上的准确率
                train_accuracy = accuracy.eval(feed_dict={x: batch[0], y: batch[1], keep_prob: 1.0})
                test_accuracy = accuracy.eval(feed_dict={x: mnist.test.images, y: mnist.test.labels})
                loss = sess.run(cross_entropy, feed_dict={x: batch[0], y: batch[1], keep_prob: 0.5})  # 计算每一步的损失函数值;
                all_train_accuracy.append(train_accuracy)  # 用于存储绘图的数据
                all_test_accuracy.append(test_accuracy)
                all_step.append(i)
                all_loss.append(float(loss))
                print('step %d, training accuracy %g, test accuracy %g, loss %g' % (
                    i, train_accuracy, test_accuracy, loss))
            # 每一步迭代，都会加载100个训练样本，然后执行一次train_step，并通过feed_dict，用训练数据替代x和y张量占位符。
            sess.run(train_step, feed_dict={x: batch[0], y: batch[1], keep_prob: 0.5})
        # 显示最终在测试集上的准确率
        print(
            'test accuracy %g' % accuracy.eval(feed_dict={x: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0}))
    print("学号：20002462")
    plot_broken_line(all_step, all_train_accuracy, all_test_accuracy)  # ‘准确率’折线图
    plot_broken_line2(all_step, all_loss)  # ‘损失函数值’折线图
