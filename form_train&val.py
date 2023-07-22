import os
import shutil
import random
#将得到的图像划分为训练集与验证集

# 定义文件夹路径和划分比例
data_dog_dir = r'satisfact_data\dogs'
data_cat_dir = r'satisfact_data\cats'
train_dog_dir = 'data\\train\\dog'
train_cat_dir = 'data\\train\\cat'
test_dog_dir = 'data\\test\\dog'
test_cat_dir = 'data\\test\\cat'

split_ratio = 0.8 

image_files = [os.path.join(data_cat_dir, f) for f in os.listdir(data_cat_dir) if f.endswith('.jpg')]

# 随机打乱
random.shuffle(image_files)

train_size = int(split_ratio * len(image_files))
test_size = len(image_files) - train_size

# 移动图像到训练集文件夹
for img_file in image_files[:train_size]:
    shutil.move(img_file, os.path.join(train_cat_dir, os.path.basename(img_file)))

# 移动图像到验证集文件夹
for img_file in image_files[train_size:]:
    shutil.move(img_file, os.path.join(test_cat_dir, os.path.basename(img_file)))

print("训练集样本数:", train_size)
print("验证集样本数:", test_size)
'''结果:
dog:
训练集样本数: 2497
验证集样本数: 625
cat:
训练集样本数: 2449
验证集样本数: 613'''