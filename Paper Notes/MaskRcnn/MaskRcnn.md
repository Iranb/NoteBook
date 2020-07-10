# MaskRcnn 论文解读

### 对比FastRcnn

1. Mask RCNN是Faster RCNN的扩展，对于Faster RCNN的每个Proposal Box都要使用FCN（Fully Convolutional Networks）进行语义分割，分割任务与定位、分类任务是同时进行的

### 基本过程

与Faster RCNN采用了相同的two-state步骤：首先是找出RPN，然后对RPN找到的每个RoI进行分类、定位、并找到binary mask。这与当时其他先找到mask然后在进行分类的网络是不同的。

1. 没有采用全连接层并且使用了RoIAlign，可以实现输出与输入的像素一一对应