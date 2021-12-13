from embeding_vec import *
from net import *


def infer_emotion(sentence):
    '''
    输入句子字符串
    返回预测结果的字典
    '''
    # 导入训练好的句向量模型
    model = Doc2Vec.load("6class_classification\\checkpoint\\doc2vec.model")
    # 导入训练好的网络
    net = torch.load('6class_classification\\checkpoint\\net.pth')
    # 将输入句子转化成句向量
    vec = model.infer_vector(re.split(r'\W+', sentence))
    # 预测情感
    outputs = net(torch.Tensor(vec)).tolist()
    # 创建情感字典
    emotion_dic = {'sadness':outputs[0], 'joy':outputs[1], 'love':outputs[2], 'anger':outputs[3], 'fear':outputs[4], 'surprise':outputs[5]}
    return emotion_dic


if __name__ == "__main__":
    sentence = input("请输入欲预测情感的句子:")
    emotion_dic = infer_emotion(sentence)
    print(emotion_dic)