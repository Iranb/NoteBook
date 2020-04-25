# Torch C++ API 笔记

### Basic 

0. include

   ```c++
   #include <torch/torch.h>
   #include <torch/script.h>
   // 这两个include  出错必定是torch c++ 环境配置的问题
   ```

   

1. Tensor

   ```c++
   // 创建 
   torch::Tensor tensor_name = torch::tensor(int value, torch::requires_grad());
   // torch::requires_grad() 添加后会自动计算梯度
   
   torch::Tensor x = torch::tensor(1.0, torch::requires_grad());
   torch::Tensor w = torch::tensor(2.0, torch::requires_grad());
   torch::Tensor b = torch::tensor(3.0, torch::requires_grad());
   
   torch::Tensor y = w * x + b;
   
   // 如果想查询某个参数的梯度，必须先进行方向传播
   y.backward();  // 反向传播，会在各个参数生成对应的梯度
   
   x.grad();  // w 
   w.grad();   // x
   ```

2. basic function

   ```c++
   // 创建随机数组
   x = torch::rnad({3, 2}); // 返回一个3*2 的tensor
   w = torch::randn({2, 3}) // 返回一个满足标准正太分布的tensor
   
   // 全连接层的创建
   torch::nn::liner()
   ```

   