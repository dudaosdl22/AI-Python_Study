# AI-Python_Study
<h2>파이토치 기초</h2>

* torch: 텐서를 생성하는 라이브러리
* torch.autograd: 자동미분 기능을 제공하는 라이브러리
* torch.nn: 신경망을 생성하는 라이브러리
* torch.multiprocessing: 병렬처리 기능을 제공하는 라이브러리
* torch.utils: 데이터 조작 등 유틸리티 기능 제공
* torch.legacy(./nn/.optim): Torch로부터 포팅해온 코드
* torch.onnx: ONNX(Open Neural Network Exchange)
            서로 다른 프레임워크 간의 모델을 공유할 때 사용
<h2>텐서(Tensors)</h2>

* 넘파이(NumPy)의 ndarry(n차원 array)와 유사
* GPU를 사용한 연산 가속도 가능한 기능

<pre>
<code>
import torch
torch.__version__
</code>
</pre>

<h2>초기화 되지 않은 행렬</h2>

<pre>
<code>
x = torch.empty(4, 2)
print(x)
</code>
</pre>

<h2>무작위로 초기화된 행렬</h2>

<pre>
<code>
x = torch.rand(4, 2)
print(x)
</code>
</pre>

<h2>dtype이 long, 0으로 채워진 텐서</h2>

<pre>
<code>
x = torch.zeros(4, 2, dtype=torch.long)
print(x)
</code>
</pre>

<h2>텐서를 직접 만들기</h2>

<pre>
<code>
x = torch.tensor([3, 2])
print(x)
</code>
</pre>

<pre>
<code>
x = x.new_ones(2, 4, dtype=torch.double)
print(x)
-> tensor([[1., 1., 1., 1.],
          [1., 1., 1., 1.]], dtype=torch.float64)
  : double은 float64로 매칭됨을 알 수 있다.
</code>
</pre>

<pre>
<code>
x = torch.randn_like(x, dtype=torch.float)
print(x)
//기존의 x라는 shape(형)을 그대로 가져와서 random으로 값 채우고 그 값을 dtype의 torch를 float으로 바꿔줘
</code>
</pre>

<h2>텐서의 크기</h2>

<pre>
<code>
print(x.size())
</code>
</pre>

<h2>텐서의 연산(operations)</h2>
<h3>덧셈1</h3>

<pre>
<code>
x = torch.rand(2, 4)
y = torch.rand(2, 4)
print(x)
print(y)
print(x + y)
</code>
</pre>

<h3>덧셈 2</h3>

<pre>
<code>
x = torch.rand(2, 4)
y = torch.rand(2, 4)
print(x)
print(y)
print(torch.add(x, y))
</code>
</pre>

<h3>덧셈3 결과 텐서를 인자로 제공</h3>

<pre>
<code>
result = torch.empty(2, 4)  //result에 torch.empty(2, 4) 만들고
torch.add(x, y, out=result)  //torch.add 연산 하는데 x, y를 주고 이 x, y 결과값을 out=result로 뺄 수 있다
print(result)
</code>
</pre>

<h3>덧셈4</h3>

* in-place 방식
- in-place방식으로 텐서의 값을 변경하는 연산 뒤에는 _''가 붙음
- x.copy_(y), x.t_()

<pre>
<code>
print(x)
print(y)
y.add_(x) // y+=x
print(y)
</code>
</pre>

<h2>그 외의 연산</h2>

* torch.sub: 뺄셈
<pre>
<code>
x = torch.Tensor([[1, 3], [5, 7]])
y = torch.Tensor([[2, 4], [6, 8]])
print(x - y)
print(torch.sub(x, y))
print(x.sub(y))
// 세 방법 모두 결과 동일
</pre>
</code>

* torch.mul: 곱셈
<pre>
<code>
x = torch.Tensor([[1, 3], [5, 7]])
y = torch.Tensor([[2, 4], [6, 8]])
print(x * y)
print(torch.mul(x, y))
print(x.mul(y))
</pre>
</code>

* torch.div: 나눗셈
<pre>
<code>
x = torch.Tensor([[1, 3], [5, 7]])
y = torch.Tensor([[2, 4], [6, 8]])
print(x / y)
print(torch.div(x, y))
print(x.div(y))
</pre>
</code>

* torch.mm: 내적(dot product)
<pre>
<code>
x = torch.Tensor([[1, 3], [5, 7]])
y = torch.Tensor([[2, 4], [6, 8]])
print(torch.mm(x, y))
</pre>
</code>

<h2>인덱싱</h2>

* 넘파이처럼 인덱싱 사용 가능
<pre>
<code>
print(x[:, 1])
</pre>
</code>

<h2>view</h2>

* 텐서의 크기(size)나 모양(shape)을 변경
<pre>
<code>
x = torch.randn(4, 5) 
y = x.view(20) 
z = x.view(5, -1)

print(x.size()) //4, 5행렬
print(y.size()) //1차원 행렬
print(z.size) //5, random 행렬 -> 5, 4 형태
</pre>
</code>

<h2>item</h2>

* 텐서에 값이 단 하나라도 존재하면 숫자값을 얻을 수 있음
<pre>
<code>
x = torch.randn(1)
print(x)
print(x.item()) // x 안에 있는 실제값을 출력
print(x.dtype)
</pre>
</code>

* 스칼라값 하나만 존재해야 함
<pre>
<code>
x = torch.randn(2) // element tensor 2개라서 오류
print(x)
print(x.item()) 
print(x.dtype)
</pre>
</code>

<h2>squeeze</h2>

* 차원을 축소(제거)
<pre>
<code>
tensor = torch.randn(1, 3, 3)
print(tensor)
print(tensor.shape)

-> tensor([...])
   torch.Size([1, 3, 3])
</pre>
</code>

<pre>
<code>
t = tensor.squeeze()

print(t)
print(t.shape)

-> tensor([...])
   torch.Size([3, 3]) // 1, 3, 3에서 3, 3으로 차원 축소
</pre>
</code>

<h2>unsqueeze</h2>

* 차원을 증가(생성)
<pre>
<code>
tensor = torch.randn(1, 3, 3)
print(tensor)
print(tensor.shape)

-> tensor([...])
   torch.Size([1, 3, 3])
</pre>
</code>

<pre>
<code>
t = tensor.unsqueeze(dim=0) //unsqueeze할 때 dim 지정 가능

print(t)
print(t.shape)

-> tensor([...])
   torch.Size([1, 1, 3, 3]) // 1, 3, 3에서 1, 1, 3, 3으로 차원 증가
</pre>
</code>

<h2>stack</h2>

* 텐서 간 결합
<pre>
<code>
x = torch.FloatTensor([1, 4])
x = torch.FloatTensor([2, 5])
x = torch.FloatTensor([3, 6])

print(torch.stack([x, y, z]))

-> tensor([[1., 4.]
          [2., 5.]
          [3., 6.]])
</pre>
</code>

<h2>cat</h2>

* 텐서를 결합하는 메소드(concatenate)
* 넘파이의 stack과 유사하지만, 쌓을 dim이 존재해야 함
    - 예를 들어, 해당 차원을 늘려준 후 결합

<pre>
<code>
a = torch.randn(1, 1, 3, 3)
b = torch.randn(1, 1, 3, 3)
c = torch.cat((a, b), dim=0) //dim을 0으로 지정해줬기 때문에 그 단위로 concatenate 된 것

print(c)
print(c.size())
</pre>
</code>

<h2>chunk</h2>

* 텐서를 여러 개로 나눌 때 사용
* 몇 개의 텐서로 나눌 것이냐

<pre>
<code>
tenso = torch.rand(3, 6)
t1, t2, t3 = torch.chunk(tensor, 3, dim=1) // chunk의 개수(텐서를 나누는 개수) 3개로 지정

print(tensor)
print(t1)
print(t2)
print(t3)
</pre>
</code>

<h2>split</h2>

* chunk와 동일한 기능이지만 조금 다름
* 하나의 텐서 당 크기가 얼마이냐
<pre>
<code>
tenso = torch.rand(3, 6)
t1, t2= torch.split(tensor, 3, dim=1) // 하나의 텐서가 의미하는 크기가 3

print(tensor)
print(t1)
print(t2)
</pre>
</code>

<h2>torch<->numpy<h2>

* Torch Tensor(텐서)를 Numpy array(배열)로 변환 가능
    - numpy()
    - from_numpy()
* (참고)
    - Tensor가 CPU상에 있다면 Numpy 배열은 메모리 공간을 공유하므로 하나가 변하면, 다른 하나도 변함

<pre>
<code>

</pre>
</code>

ddddddddddddddd