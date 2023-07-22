### 本代码基于torch利用迁移学习实现猫狗识别
首先在github寻找现有模型 （https://github.com/chenshunpeng/Cat-dog-recognition-based-on-CNN.git）。

然后将ipynb转换为py文件[Catdog_CNN_checkpoint](Catdog_CNN_checkpoint.py)，从而导入神经网络结构LeNet，接着获取model.pth参数，实现原模型导入。

之后是寻找数据集。pytorch自带数据集为32\*32大小，但本代码把限制大小大于224\*224,故无法使用。此模型数据集来源于网络https://tianchi.aliyun.com/dataset/129027?t=1690024199954 存储于[originaldata](originaldata)。经除去过大与过小的文件[Restrict_data_size](Restrict_data_size.py)，并划分训练集与测试集后[form_train&val](form_train&val.py)，存储在[data](data)中。

最后在[use_model](use_model.ipynb)中导入模型和数据，选择交叉熵损失函数和SGD优化方法（lr=0.11），epoch=20可以实现准确率大于97%