# BottleNeck

### 什么是BottleNeck？

bottleneck简单翻译就是瓶颈层，一般在深度较高的网络（如resnet101）中使用

![bottlenck](bottleneck.assets/20190412171201596.png)

两个1X1 fliter 分别用于降低和升高特征维度，主要目的是为了减少参数的数量，从而减少计算量，且在降维之后可以更加有效

2. resnet 中bottle neck的 对比

   ![img](bottleneck.assets/20180521111543135)