# Path Aggregation Network for Instance Segmentation

### 改进

![PA-net](PA-NET.assets/20180729173615359)

1. **红色虚线箭头**表示在FPN算法中，因为要走自底向上的过程，浅层的特征传递到顶层要经过几十甚至一百多个网络层
2. 绿色虚线箭头表示作者添加一个bottom-up path augmentation，本身这个结构不到10层，这样浅层特征经过底下原来FPN的lateral connection连接到$P_2$再从$P_2$沿着bottom-up path augmentation传递到顶层，经过的层数就不到10层，能较好地保留浅层特征信息。