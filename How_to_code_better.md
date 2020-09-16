# How_to_code_better 

#### 前言

这份笔记起源于在看github开源代码时候的一些感悟，不同编码风格的代码看起来给人的感觉也不同，但是最近看到了几个赏心悦目的代码，于是觉得有必要规范一下自己写代码的过程，增加代码可读性的同时也让自己写的代码看起来赏心悦目就是这个笔记的目的

#### yacs

yacs可以理解成一个配置文件的管理工具，常用语配置神经网络中的超参数等信息，同时能够在每次实验的过程中保存超参数，方便结果的复现过程，基础用法如下：

```
# my_project/config.py
from yacs.config import CfgNode as CN


_C = CN()

_C.SYSTEM = CN()
# Number of GPUS to use in the experiment
_C.SYSTEM.NUM_GPUS = 8
# Number of workers for doing things
_C.SYSTEM.NUM_WORKERS = 4

_C.TRAIN = CN()
# A very important hyperparameter
_C.TRAIN.HYPERPARAMETER_1 = 0.1
# The all important scales for the stuff
_C.TRAIN.SCALES = (2, 4, 8, 16)

# Exporting as cfg is a nice convention
cfg = _C
```

\_C中申明过后的变量才能被赋值和修改，如果_C中没有某个变量，而yaml中有，那就会报错，因为该变量未能事先申明