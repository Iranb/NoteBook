# DetectoRS: Detecting Objects with Recursive Feature Pyramid and Switchable Atrous Convolution  

使用递归FPN 和 空洞卷积的目标检测

### 摘要

1. 比较先进的目标检测算法一般使用 looking and thinking twice 的设计原则，在宏观和微观层面对模型进行了设计
2. 设计了RFP（Recursive Feature Pyramid ）骨架网络，用于目标检测
3. 微观层面设计了可切换的空洞卷积，使用不同的空洞率及切换方程控制特征的卷积过程

### 介绍

1. 基于HTC 算法进行了改进