TF2.0 学习笔记

１．有注册该layers，那么在后面应用梯度时会找不到model.trainable_variables

```python
# 错误的写法
class Map_model(tf.keras.Model):
    def __init__(self, is_train=False):
        super(Map_model, self).__init__()
    def call(self, x):
        x = tf.keras.layers.Dense(10, activation='relu')
        return x
 # 正确的写法
class Map_model(tf.keras.Model):
    def __init__(self, is_train=False):
        super(Map_model, self).__init__()
        self.layer1 = tf.keras.layers.Dense(10, activation='relu')
    def call(self, x):
        x = layer1(x)
        return x
```

