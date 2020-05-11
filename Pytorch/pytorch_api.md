# pytorch API 学习笔记

1. tensor类

   - tensor.view(a,b)

     将tensor 重新构造为 a * b 维向量

     若b = -1 则转化为一维向量

2. torch.nn.Module
    - fc()
      	- net.fc.out_features = 10 设置fc层的输出
      	- 若知道上一层格式在可使用self.fc = 形式定义
      	- 在 forward 函数中 self.fc() 仅用设置一个参数

