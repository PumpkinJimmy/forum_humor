# from .embeding_vec import *
import re

import torch

from .net import Net
from gensim.models.doc2vec import Doc2Vec

class EmotionClassifier:
    def __init__(self,modelpath, netpath):
        '''
        :param modelpath: 句向量文件 doc2vec.model 的路径
        :param netpath: 网络模型文件 net.pth 的路径
        '''
        
        # 导入训练好的句向量模型
        self.model = Doc2Vec.load(modelpath)
        # 导入训练好的网络
        self.net = Net(64)
        self.net.load_state_dict(torch.load(netpath))


    def infer_emotion(self, sentence):
        '''
        预测情感的函数
        :param sentence: 句子字符串
        
        :return: 预测结果的字典
        '''
        # 将输入句子转化成句向量
        vec = self.model.infer_vector(re.split(r'\W+', sentence))
        # 预测情感
        outputs = self.net(torch.Tensor(vec)).tolist()
        # 创建情感字典
        emotion_dic = {'sadness':outputs[0], 'joy':outputs[1], 'love':outputs[2], 'anger':outputs[3], 'fear':outputs[4], 'surprise':outputs[5]}
        return emotion_dic


# if __name__ == "__main__":
#     modelpath = "6class_classification\\checkpoint\\doc2vec.model"
#     netpath = '6class_classification\\checkpoint\\net.pth'
#     sentence = input("请输入欲预测情感的句子:")
#     emotion_dic = infer_emotion(sentence, modelpath, netpath)
#     print(emotion_dic)