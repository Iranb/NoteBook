# Object detection

### 流程 

- One Stage 算法
  - 特征提取
  - 分类 + 回归定位
- Two Stage 算法
  - 添加了 生成 RP ( region proposal ) 的步骤
  - RP 包含一系列候选框（先验框）
    - 滑动窗口法生成 （先验框）
  - 对候选框进行回归定位，对物体进行分类

### Loss Function

- IOU
  - $IOU = $
- GIOU

###  Anchor 

 - 人为设计的一组框，作为分类（classification）和框回归（bounding box regression）的基准框
 - Anchor的设置需要手动去设计，对不同数据集也需要不同的设计
 - Anchor设计的理想状态：
    - 稀疏，尽可能少的 候选框个数
    - 形状根据位置可变的，能够适应不同位置不同大小的物体
    - **alignment**（中心对齐） 和 **consistency**（特征一致）
 - Anchor 分布公式
    - $ P(x,y,w,h|I) = p(x,y|I)p(w,h|x,y,I)$
    - 中心坐标和宽高表示法
 - Anchor的 位置预测和形状预测滑动窗口法
    - 位置预测
       - 预测区域中作为object中心点的部分，并以此生成 Anchor
    - 形状预测
       - 形状预测分支的目标是给定 anchor 中心点，预测最佳的长和宽
    - 常用方法
       - 滑动窗口法

