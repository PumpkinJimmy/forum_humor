​		`checkpoint` 文件夹中保存有全部训练好的模型，`dataset` 文件夹中为数据集。

​		对外接口为 `classification.py` 文件中的如下函数：

```python
def infer_emotion(sentence, modelpath, netpath):
    '''
    预测情感的函数
    :param sentence: 句子字符串
    :param modelpath: 句向量文件 doc2vec.model 的路径
    :param netpath: 网络模型文件 net.pth 的路径
    :return: 预测结果的字典
    '''
```

