# Cuda C++ 编程指北

### 前言

​	笔记中的资源来自于 [超算习堂](easyhpc.net) CUDA 编程实战教程及 BJTU 并行域分布式计算课程

如有错误，请在issue 中留言指正，感激不尽。

### CUDA 编程笔记

##### basic

1. CUDA 编程需要考虑 CPU ，GPU ， 内存， 显存之间的数据交换，使用host 代表CPU和内存，使用device 代表 GPU 和显存

2. CPU 负责定义 kernel 函数，GPU 负责对 kernel 函数进行执行，执行参数由程序指定

3. 可以将kernel 函数看作是CPU 对GPU 中的方法定义

4. kernel 函数的定义,使用 `__global__`​ 修饰方法

   ```C++
   __global__ type function(patamaters){
   	content
   }
   ```

5. kernel 函数的GPU 运行参数指定

   ```c++
   function<<<block, thread>>>(parameters);
   ```

6. 函数修饰符

   ```c++
   //  __host__ 代表在CPU 上运行，只能被CPU 调用且函数若没有标注则默认为host函数
   //  __global__ kernel 函数的声明标识符 
   //  __device__ 代表在GPU上运行，且只能被GPU 调用
   ```

7. 显存的分配

   ```C++
   __host__ cudaError_t cudaMelloc(void **devPtr, size_t size)
   /* 
   cudaMelloc 用于分配显存
   该函数被声明为了__host__，即表示被host所调用，即在cpu中执行的代码所调用。 这里存疑，GPU 中不能执行申请显存的代码吗？
   第一个参数，void ** 类型，devPtr：用于接受该函数所分配的内存地址。
   第二个参数，size_t类型，size：指定分配内存的大小，单位为字节。
   */
   ```

8. 显存和内存间的数据拷贝

   ```C++
   __host__ cudaError_t cudaMemcpy (void *dst, const void *src, size_t count, enum cudaMemcpyKind kind)
   /*	
   dst：为目的内存地址
   src：源内存地址
   count：将要进行拷贝的字节大小
   kind：拷贝的类型，决定拷贝的方向， enum  cudaMemcpyKind类型，
   这个函数可以执行从显存， 内存之间的不同方向的拷贝，使用 cudaMemcpyKind类型：
   cudaMemcpyHostToHost,
   cudaMemcpyHostToDevice,
   cudaMemcpyDeviceToHost, cudaMemcpyDeviceToDevice, 
   cudaMemcpyDefault。
   */
   ```

    **注意**： 设备指针要强制转化为 Void 类型的指针，但是这里有个疑问，如何设置这个指针所指向的数据类型？

9. 显存，内存等空间的释放

   ```C++
   __host__ cudaError_t cudaFree (void* devPtr)
   ```

10. 连续空间的申请

    ```c++
    cudaError_t  cudaMallocPitch(void **devPtr, size_t *pitch, size_t width, size_t height);
    
    /*
        该函数用来分配指定大小的线性内存，宽度至少为width，高度为height。
        该函数在分配内存时会适当的填充一些字节来保证对其要求，从而在按行访问时，或者在二维数组和设备存储器的其他区域间复制是，保证了最佳的性能s
        实际的分配的内存大小为：sizeof(T)*pitch * height，则访问2D数组中任意一个元素[Row,Column]的计算公式如下：
            T* pElement = (T*)((char*)BaseAddress + Row * pitch) + Column。
        第一个参数，void**类型，devPtr：用来接受被分配内存的其实地址
        第二个参数，size_t*类型，pitch：用来接受实际行间距，即被填充后的实际宽度（单位字节），大于等于第三个参数width
        第三个参数，size_t类型，width：请求分配内存的宽度（单位字节），如2D数组的列数
        第四个参数，size_t类型，height：请求分配内存的高度（单位字节），如2D数组的行数
    
    */
    ```

11. CUDA 无法直接操作内存

    ```c++
    __device__ void dev1(int &x) {
    	x = 2;
    }
    
    __device__ void dev2(int &x) {
    	x = 3;
    }
    
    __global__ void calcute(int &x) {
    	dev1(x);
    	dev2(x);
    }
    
    int i = 0;
    	calcute<<< 2, 5 >>>(i);
    	cout << "result is:   " << i << endl;
    /*
    	最后输出  result is 0
    	原因： cuda 程序无法直接读取内存中的数据
    */
    ```

12. CUDA 程序存在执行顺序

    ```c++
    __device__ void dev1(int &x) {
    	printf("1");
    }
    
    __device__ void dev2(int &x) {
    	printf("2");
    }
    
    __global__ void calcute(int &x) {
    	dev1(x);
    	dev2(x);
    }
    
    calcute<<< 5, 2 >>>(0);
    
    /* 
    	计算结果 111111111112222222222
    	而不是   1212121212121212121212
    	初步分析： 每个block 上的执行速度是相同的，所以 1 总是被先打印出来
    */
    ```

13. CUDA 内置函数

<img src="..\imgs\gpu_structure.png" alt="gpu_structure" style="zoom: 80%;" />

```C++
maxThreadsPerBlock:每个block上的thread最大值，默认为1024。
对于一个kernel函数，具有B个block，每个block有T个thread：
blockIdx.x：当前block在x方向上的ID，取值为0~B-1。
threadIdx.x：当前block上的当前thread在x方向上的ID，取值为0~T-1。
gridDim.x：当前grid的block在x方向上的数量。
blockDim.x：当前block的thread在x方向上的数量。
/*
	如何使用这些属性？
*/
    
cudaDeviceProp prop; // 首先定义 cuda device prop  变量
cudaGetDeviceProperties(&prop, i）
```

14. CUDA 内置函数（待更新）

### 后记

1. VS 常用快捷键

   ```bash
   注释：     先CTRL+K+C
   取消注释：  先CTRL+K+U
   ```

   