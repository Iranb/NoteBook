# Fully Convolutional Networks for Semantic Segmentation

### 创新点

1. 包含了对 CNN 的改进

2. 不含全连接层(fc)的全卷积(fully conv)网络。可适应任意尺寸输入。
3. 增大数据尺寸的反卷积(deconv)层。能够输出精细的结果。

4. 结合不同深度层结果的跳级(skip)结构。将来自深层、粗糙的语义信息与来自浅层、细致的外观信息结合起来，同时确保鲁棒性和精确性

 FCN和CNN的区别：CNN卷积层之后连接的是全连接层；FCN卷积层之后仍连接卷积层，输出的是与输入大小相同的特征图。