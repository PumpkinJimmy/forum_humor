import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class Net(nn.Module):
    '''
    定义神经网络类
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
