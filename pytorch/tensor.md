# Tensor operations


## Definiation of Tensor 

Tensor 中文为张量，即一个多维数组，是标量、向量和矩阵对高维扩展。

|数学| 计算机科学  |  抽象概念| 具像化例子|
|---|---|---|---|
|标量|数字|点|得分，概率|
|向量|数组|线|列表|
|矩阵|2维数组|面|excel表格|

---

## Initial tensor

### torch.tensor  

* format: torch.tensor是python函数 
    ```bash
    torch.tensor(data, dtype = None, device = None, required_grad = False, pin_memory = False)

    # data: can be a list, tuple Numpy ndarray, scalar and other types
    ```

* Example:
    ```python
    import torch

    torch.tensor([[0.1, 1.2], [2.2, 3.1], [4.9, 5.2]])

    torch.tensor([0,1])

    torch.tensor([[0.11111, 0.222222, 0.3333333]],dtype=torch.float64,device = torch.device('cuda:0')

    torch.tensor(3.14159)

    torch.tensor([])

    ```

---

## torch.Tensor

* format: class类， 相当于调用Tensor类的构造函数__init__
    ```bash
    a = torch.Tensor([1,2])
    ```

* 


---





## torch.repeat  

* repeat参数个数与tensor维数一致时，repeat参数是对应维度的复制个数

    ```python
    import torch
    a = torch.tensor([[1, 2, 3],
                        [1, 2,3]])

    b =a.repeat(2,2)
    print(b.shape)
    ```


* repeat参数个数与tensor维数不一致时， 首先在第0维扩展一个维度，维数为1，然后按照参数指定的次数进行复制

    ```python
    import torch
    a = torch.tensor([[1,2,3], [1,2,3]])
    b = a.repeat(2,1,1)
    print(b.shape)
    ```

* 注:  
    * repeat参数的个数应大于等于tensor维度数
    * 以tensor维度数开始 逆序进行复制操作（先对tensor内部进行复制，再对外面数据进行复制）






