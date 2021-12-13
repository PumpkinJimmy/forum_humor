import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

inputVecFile = "6class_classification\\checkpoint\\docVec_Matrix.npy"

class Net(nn.Module):
    '''
    定义神经网络类
    以下定义了两种结构
    '''
    def __init__(self, input_size):
        super(Net, self).__init__()
        self.layer1 = nn.Linear(input_size, 512)
        self.active1 = nn.PReLU()
        self.layer2 = nn.Linear(512, 256)
        self.active2 = nn.PReLU()
        self.layer3 = nn.Linear(256, 128)
        self.active3 = nn.PReLU()
        self.layer4 = nn.Linear(128, 64)
        self.active4 = nn.PReLU()
        self.layer5 = nn.Linear(64, 32)
        self.active5 = nn.PReLU()
        self.layer6 = nn.Linear(32, 16)
        self.active6 = nn.PReLU()
        self.layer7 = nn.Linear(16, 6)

    def forward(self, x):
        fc1 = self.active1(self.layer1(x))
        fc2 = self.active2(self.layer2(fc1))
        fc3 = self.active3(self.layer3(fc2))
        fc4 = self.active4(self.layer4(fc3))
        fc5 = self.active5(self.layer5(fc4))
        fc6 = self.active6(self.layer6(fc5))
        fc7 = self.layer7(fc6)
        return fc7


def predict(net, inputVec):
    '''
    输入训练好的网络，欲预测的输入向量
    返回预测结果
    '''
    # 得到预测概率
    outputs = np.array(net(inputVec).tolist())
    # 输出预测标签
    outputs = outputs.argmax(axis=1)
    outputs = torch.Tensor(outputs)
    return outputs


def train_net(input_size):
    '''
    输入输入向量的大小
    将训练好的网络写到文件中
    '''
    # 导入训练集数据
    train_inputVec = torch.Tensor(np.load(inputVecFile))
    train_size = len(train_inputVec)
    train_labels = torch.Tensor(np.load("6class_classification\\checkpoint\\labels.npy").reshape(train_size)).long()
    # 导入验证集数据
    # valid_inputVec = torch.Tensor(np.load(inputVecFile)[30000:40000])
    # valid_labels = torch.Tensor(np.load("labels.npy")[30000:40000].reshape(10000)).int()
    valid_inputVec = train_inputVec
    valid_labels = train_labels
    valid_size = train_size
    # 设置训练批次
    total = len(train_labels)
    batch_count = 1
    batches_size = int(total / batch_count)
    # 定义网络
    net = Net(input_size)
    # 定义损失函数
    criterion = nn.CrossEntropyLoss()
    # 定义优化器
    optimizer = optim.Adam(net.parameters(), lr=0.001)
    # 开始训练
    batchCount_list = []
    loss_list = []
    accuarcy_list = []
    plt.ion()
    maxepoch = 2500
    for epoch in range(maxepoch): 
         for i in range(batch_count):
             ## 在训练集上更新参数
             #获取该批次的数据
             inputs = train_inputVec[i*batches_size : (i+1)*batches_size]
             labels = train_labels[i*batches_size : (i+1)*batches_size]
             #清空参数梯度
             optimizer.zero_grad()
             #利用损失更新参数
             outputs = net(inputs)
             loss = criterion(outputs, labels)
             loss.backward()
             optimizer.step()
             ## 在验证集上得到此时的预测准确率
             valid_outputs = predict(net, valid_inputVec)
             accuracy = torch.eq(valid_outputs, valid_labels).sum().item() / valid_size
             ## 实时作图
             batchCount_list.append(epoch * batch_count + i)
             loss_list.append(loss.item())
             accuarcy_list.append(accuracy)
             plt.clf()
             #训练集上损失的图像
             plt.subplot(1, 2, 1)
             plt.plot(batchCount_list, loss_list)
             plt.title('Loss in train set')
             plt.xlabel('batchCount')
             plt.ylabel('Loss')
             #验证集上正确率的图像
             plt.subplot(1, 2, 2)
             plt.plot(batchCount_list, accuarcy_list)
             plt.title('Accuracy in validation set')
             plt.xlabel('batchCount')
             plt.ylabel('Accuracy')
             #停顿以便看清
             plt.tight_layout()
             plt.pause(0.001)
    # 保存作图结构
    plt.savefig('{}_train.png'.format(inputVecFile))
    plt.ioff()
    # 保存整个神经网络的模型结构以及参数
    torch.save(net, '6class_classification\\checkpoint\\net.pth')
    print('Finished Training')


if __name__ == "__main__":
    train_net(64)