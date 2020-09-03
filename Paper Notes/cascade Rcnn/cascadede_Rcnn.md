# 	Cascade Rcnn

### 创新点

1. RPN 给出的proposals大部分质量不高，所以检测阶段阈值设置过大容易导致模型失效。
2. 设计了一种cascade 回归，实现多重采样机制分阶段提高porposal的阈值