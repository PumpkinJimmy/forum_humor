import re
import numpy as np
from pandas import read_csv
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


def readFile():
    '''
    读取目标文件中的语句信息
    保存目标文件中语句信息形成的单词二维列表和标签列表到文件中
    sadness (0), joy (1), love (2), anger (3), fear (4)，surprise(5)
    '''
    sentences_array = []
    words_Matrix = []
    # 读取数据
    df = read_csv('6class_classification\\dataset\\training.csv')
    # 对text进行预处理
    message = df['text'].tolist()
    for sentence in message:
        sentences_array.append(sentence)
        tmp = re.split(r'\W+', sentence)
        words_Matrix.append(tmp)
    sentences_array = np.array(sentences_array)
    words_Matrix = np.array(words_Matrix)
    # 对标签进行预处理
    labels = df['label'].tolist()
    labels = np.array(labels)
    # 保存处理结果
    np.save("6class_classification\\checkpoint\\sentences_array.npy", sentences_array)
    print("save sentences_array!")
    np.save("6class_classification\\checkpoint\\words_Matrix.npy", words_Matrix)
    print("save words_Matrix!")
    np.save("6class_classification\\checkpoint\\labels.npy", labels)
    print("save labels!")


def train_DocVecModel(vector_size):
    '''
    输入欲训练词向量的维数
    输出训练好的词向量模型到文件中
    '''
    # 读取数据
    words_Matrix = np.load('6class_classification\\checkpoint\\words_Matrix.npy', allow_pickle=True)
    # 用gensim训练句向量模型
    documents = [TaggedDocument(doc, [i]) for i, doc in enumerate(words_Matrix)]
    model = Doc2Vec(documents, vector_size=vector_size, window=10, min_count=15, workers=4, negative=15)
    # 保存处理结果
    model.save("6class_classification\\checkpoint\\doc2vec.model")
    print("save doc2vec model!")


def docVec(vector_size):
    '''
    输入欲训练词向量的维数
    输出数据集对应的词向量矩阵到文件中
    '''
    docVec_Matrix = []
    # 加载数据
    words_Matrix = np.load('6class_classification\\checkpoint\\words_Matrix.npy', allow_pickle=True)
    model = Doc2Vec.load("6class_classification\\checkpoint\\doc2vec.model")
    # 计算
    for sentence in words_Matrix:
        vec = model.infer_vector(sentence)
        docVec_Matrix.append(vec)
    docVec_Matrix = np.array(docVec_Matrix)
    # 保存处理结果
    np.save('6class_classification\\checkpoint\\docVec_Matrix.npy', docVec_Matrix)
    print("save docVec_Matrix!")


if __name__ == "__main__":
    '''
    整个的数据预处理函数
    '''
    # 读取文件
    # readFile()
    # 训练词向量模型
    train_DocVecModel(64)
    # 得到文档的词向量表示矩阵
    docVec(64)

    # 检验预处理结果
    labels = np.load("6class_classification\\checkpoint\\labels.npy")
    docVec_Matrix = np.load("6class_classification\\checkpoint\\docVec_Matrix.npy")
    print("labels:===========================================================================")
    print(labels)
    print("docVec_Matrix:======================================================================")
    print(docVec_Matrix)
