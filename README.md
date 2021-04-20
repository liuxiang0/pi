# 圆周率$π$的计算方法

From [翔文公益数学](https://www.geogebra.org/u/kumath)  &copy; kumath@outlook.com

**圆周率**    
- 从代数上来讲，就是一个无理数（即无限不循环小数），也是一个超越数，与三角函数有密切关系，与无限级数和有关系。
- 从几何上来说，就是一个比值，特殊图形圆的周长与其直径的比值，也就是单位圆的半周长，还可以是单位圆的面积或圆面积与其半径的平方之比；也有人提出：如果用圆的周长与其半径的比值作为圆周率的话，也是可以的。
- $\pi$ 是一个常数，目前谷歌宣布已经计算到了 **31.4万亿 $=3.14\times10^{13}$** 位了，为了纪念 圆周率日-PAI Day（每年的3月14日）。

下面主要阐述 **现代分析方法** 对计算圆周率的贡献。

## 泰勒级数理论（Taylor's theorem and Taylor series）

### 多项式逼近任意函数

多项式 (polynomial) 逼近 (approximate) 未知函数 $f$ 在给定点附近的值，实际上就是找到多项式的系数 (coefficients):  $a_0, a_1, \cdots, a_n$ 

$P_n(x)=a_0+a_1(x-a)+a_2(x-a)^2+\cdots+a_n(x-a)^n+R((x-a)^{n+1})$

靠近给定点 $x=a$ 逼近函数 $f(x)$, 此处假定 (assuming) 函数 $f(x)$ 在 $x = a$ 有 $nth$ 微分(differentiable). 从而有 $f(x)\approx P_n(x)$, 下面试着找出系数 $a_n, n=0,1,2,\cdots,n$.  

~~~python
>>> f=Function('f')
>>> series(f(x))
f(0) + x*Subs(Derivative(f(_x), _x), _x, 0) + x**2*Subs(Derivative(f(_x), (_x, 2)), _x, 0)/2 + x**3*Subs(Derivative(f(_x), (_x, 3)), _x, 0)/6 + x**4*Subs(Derivative(f(_x), (_x, 4)), _x, 0)/24 + x**5*Subs(Derivative(f(_x), (_x, 5)), _x, 0)/120 + O(x**6)
~~~

[泰勒级数(Taylor series)][TS] 实函数或复函数(a real or complex-valued function) $f(x)$ 在 $x=a$ 有无限阶微分，则可以表示为幂级数 (power series):

$f(x) \approx \displaystyle f(a)+{\frac {f'(a)}{1!}}(x-a)+{\frac {f''(a)}{2!}}(x-a)^{2}+{\frac {f'''(a)}{3!}}(x-a)^{3}+\cdots$

此处 $n!$ 表示$n$的阶乘 (denotes the factorial), $f^{(n)}(a)$ 表示 $f$ 在$x=a$ 处的 $nth$ 微分 (derivative). 可以写成更加紧凑的求和式子：

泰勒级数 $f(x)={\displaystyle \sum _{n=0}^{\infty }{\frac {f^{(n)}(a)}{n!}}(x-a)^{n}.}$

$f$ 的0阶导数就是它自己 $f$，且$(x − a)^0 = 0!=1$. 当 $a = 0$, 此时的泰勒级数又叫做 麦克劳林级数 [Maclaurin series][1].

### 举例 (For instance)

**指数函数(exponential function)**    
    
- 指数函数是重要的基本初等函数之一。一般地，$y=a^x$ 函数 $(a$ 为常数且 $a>0，a≠1)$ 叫做 **指数函数**。
- 指数函数的定义域是 $x \in \mathbb{R}$; 
- 值域 $\text{(Domain)}\;(0,+\infty)$;  
- 单调递增： $a>1$ 时, 单调递减： $0 < a < 1$ 时。 
 
注意，在指数函数的定义表达式中，在 $a^x$ 前的系数必须是数1,

指数函数应用到值 $a=e$ 上的这个函数写为 $\exp(x)$。还可以等价的写为 $e^x$，这里的 $e$ 是数学常数，就是自然对数的底数，近似等于 $2.718281828$，还称为**欧拉数**.

作为实数变量 $x$ 的函数， $e^x$ 的图像总是正的(在 $x$ 轴之上)并递增(从左向右看)。它永不触及 $x$ 轴，尽管它可以无限程度地靠近 $x$ 轴(所以，$x$ 轴是这个图像的**水平渐近线**。它的反函数是 **自然对数 $\ln(x)$**，其定义域是所有正数 $x>0$ 。

指数函数 $e^x$ 在 $x_0 = 0$ 处的泰勒级数展开式为： 

$\displaystyle \begin{aligned}\sum _{n=0}^{\infty }{\frac {x^{n}}{n!}}& = {\frac {x^{0}}{0!}}+{\frac {x^{1}}{1!}}+{\frac {x^{2}}{2!}}+{\frac {x^{3}}{3!}}+{\frac {x^{4}}{4!}}+{\frac {x^{5}}{5!}}+\cdots \\& = 1+x+{\frac {x^{2}}{2}}+{\frac {x^{3}}{6}}+{\frac {x^{4}}{24}}+{\frac {x^{5}}{120}}+\cdots \end{aligned}$

- $e^x$ 对 $x$ 求导，始终不变，即 $\dfrac{\mathbf{d}^{k} }{\mathbf{d}x^k} e^x = e^x$，
- 且 $e^0=1$. 
- 剩下的分子 (numerator) 为 $(x − 0)^n$, 分母 (denominator) 为 $n!$.

[1]: https://en.wikipedia.org/wiki/Colin_Maclaurin#Contributions_to_mathematics

## 欧拉公式 (Euler formula): $e^{ix}=\cos(x)+\text{i}\; \sin(x)$

欧拉公式有时候记为 $cis(x)=e^{ix}=\cos(x)+i \sin(x)$

~~~python
>>> series(sin(x),n=10)
x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 + O(x**10)
>>> series(cos(x),n=10)
1 - x**2/2 + x**4/24 - x**6/720 + x**8/40320 + O(x**10)
>>> series(exp(x),n=10)
1 + x + x**2/2 + x**3/6 + x**4/24 + x**5/120 + x**6/720 + x**7/5040 + x**8/40320 + x**9/362880 + O(x**10)
~~~

指数函数 $e^z$ 在 $z_0=0$ 的泰勒级数展开式为

$\displaystyle \begin{aligned}{e^z}&=\sum _{n=0}^{\infty }{\frac {z^{n}}{n!}}\\&={\frac {z^{0}}{0!}}+{\frac {z^{1}}{1!}}+{\frac {z^{2}}{2!}}+{\frac {z^{3}}{3!}}+{\frac {z^{4}}{4!}}+{\frac {z^{5}}{5!}}+\cdots \\&=1+z+{\frac {z^{2}}{2}}+{\frac {z^{3}}{6}}+{\frac {z^{4}}{24}}+{\frac {z^{5}}{120}}+\cdots \end{aligned}$

令 $z=ix$(纯虚数), 此处 $i$ 虚数单位(imaginary unit), 满足 $i^{4k}=1, i^{4k+1}=i, i^{4k+2}=-1, i^{4k+3}=-i, k\in \mathbb{N^+}$.

左边为 $\large\red {e^{ix}=\cos(x)+i\;\sin(x)}$    
右边为 ${\displaystyle {\begin{aligned} 1+ix-\frac{x^2}{2!}-i \frac{x^3}{3!}+\frac{x^4}{4!}+i \frac{x^5}{5!}-\frac{x^6}{6!}-i \frac{x^7}{7!}+\cdots \end{aligned}}}$

所以

$\displaystyle \red{\cos(x)} = 1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots  （偶函数）\\[1em]
\red{\sin(x)} = x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots  （奇函数）$

上面也是函数 **$\cos(x)$** 和 **$\sin(x)$** 的泰勒级数展开式. (请参照 **[Colin Maclaurin series][Maclaurin]**, $\forall x$)

写成紧凑的求和式为：   
$\displaystyle \begin{aligned}\cos(x)&=\sum _{n=0}^{\infty }{\frac {(-1)^nx^{2n}}{(2n)!}}\\&={1}-{\frac {x^{2}}{2!}}+{\frac {x^{4}}{4!}}-{\frac {x^{6}}{6!}}+\cdots  .\end{aligned}$

$\displaystyle \begin{aligned}\sin(x)&=\sum _{n=0}^{\infty }{\frac {(-1)^nx^{2n+1}}{(2n+1)!}}\\&={x}-{\frac {x^{3}}{3!}}+{\frac {x^{5}}{5!}}-{\frac {x^{7}}{7!}}+\cdots  .\end{aligned}$

可见，**$\cos(x)$ 是偶函数，$\sin(x)$ 是奇函数**。   

显然，我们也可以通过泰勒展开得到上述式子。多阶导数有下列规律：

$\sin^{(2k)}(x)= \frac{d^{(2k)}\sin(x)}{dx}=(-1)^k \sin(x)\\[1em]
\sin^{(2k+1)}(x)=(-1)^k \cos(x)$

$\sin(x)$ 在 $x=0$ 处的偶次导数为 0, $\sin(x)$ 在 $x=0$ 奇次导数为 $(-1)^k$ 

### 欧拉恒等式 (Euler identity)

只要在欧拉公式 $cis(x) = \boxed{\red {e^{ix} = \cos(x)+i \sin(x)}}$ 中令 $x=\pi$, 即可得到 **上帝恒等式——欧拉恒等式**
$\boxed{\red {e^{i\pi} = -1, e^{i\pi} + 1=0}}$

神奇的是：这个欧拉恒等式包含了 $e,i,\pi,0,1,=$ 这几个基本单元数和等号，故称为上帝公式。

## 多项式逼近理论应用 (Polynomial approximation theorem)

下面应用多项式逼近理论，得到几个常用的三角函数（$\sin(x),\cos(x),\tan(x)$）的乘积展开式。主要还是代数学中的求根方法。

**问题**: 求方程 $\sin(x)=0$ 的解。

1. 首先, $\sin(x)=0$ 有解 $\{kπ，k=0,\pm 1,\pm 2, \cdots .\}$

2. 假设 $\sin(x)$ 是多项式函数，由多项式有根的代数基本理论 (the fundamental theorem of algebra) 即 多项式逼近理论 (polynomial approximation theorem)

    $\displaystyle \sin(x) = c*\prod_{k=1}^{\infty} (kπ-x)(kπ+x)x \\[1em]\frac{\sin(x)}{x} = c*\prod_{k=1}^{\infty} (kπ-x)(kπ+x)$

    令 $x \to 0$， 求极限得到 
    $\displaystyle c=\prod_{k=1}^{\infty} \frac {1}{k^2π^2}$

    我们得到：

    $\displaystyle \begin{aligned} \sin(x) &= x {\prod_{k=1} ^{\infty} ({1- \frac{x}{kπ})} (1+ \frac{x}{kπ})} \\&= x \prod_{k=1} ^{\infty} \left[1- \frac{x^2}{(kπ)^2}\right ] \end{aligned}$

令 $x = \frac{π}{2}$, 有 

$\displaystyle \begin{aligned} \frac{π}{2} &= \prod_{k=1} ^{\infty} \frac{2k}{2k-1} \centerdot \frac{2k}{2k+1}   \\&= \prod_{k=1} ^{\infty} \frac{1}{1- \frac{1}{4k^2}} \\&=\frac{2}{1} \centerdot \frac{2}{3} \centerdot \frac{4}{3} \centerdot \frac{4}{5} \centerdot \frac{6}{5} \centerdot \frac{6}{7} \cdots \\&=\frac{4}{3} \centerdot \frac{16}{15} \centerdot \frac{36}{35} \centerdot \frac{64}{63} \cdots \end{aligned}$

参见 [John Wallis' product for $π$][Wallis]

同理可得

$\displaystyle \begin{aligned}\cos(x)&=\prod_{k=1} ^{\infty} {(1 - \frac{2x}{(2k-1)π})} {(1 + \frac{2x}{(2k-1)π})}\\&=x \prod_{k=1} ^{\infty} {(1-\frac{4x^2}{(2k-1)^2 π^2})} \end{aligned}$

$\displaystyle \begin{aligned} \tan(x)&=\frac{x}{\frac{\pi}{4}} \centerdot \prod_{k=1} ^{\infty} \frac{1 - \frac{x}{kπ}}{1-\frac{1}{4k}} \centerdot \frac{1 + \frac{x}{kπ}}{1+\frac{1}{4k}}\end{aligned}$

## 所有正整数平方的倒数和

通过泰勒级数展开理论和多项式逼近理论这两种不同方法所得到的结果进行比较。

~~~python
>>> series(sin(x),n=10)  # 正弦函数幂级数展开式
x - x**3/6 + x**5/120 - x**7/5040 + x**9/362880 + O(x**10)
~~~

1. 泰勒展开理论得到   
    $\displaystyle \begin{aligned} \sin(x)&=x-\frac{x^3}{3!}+\frac{x^5}{5!}+\cdots \end{aligned}$
2. 多项式逼近理论得到  
    $\displaystyle \begin{aligned} \sin(x)&= x \prod_{k=1} ^{\infty} (1- \frac{x^2}{(kπ)^2})  \end{aligned}$   
3. 比较 $x^3$ 的系数可得    
    $\displaystyle {\begin{aligned} \frac{1}{3!}&= \sum_{k=1} ^{\infty} \frac{1}{(kπ)^2}  \end{aligned}}$   
    
    所以    
    $\displaystyle \begin{aligned} \frac{π^2}{6}&=\sum_{k=1} ^{\infty} \frac{1}{k^2}\\&=1+\frac{1}{4}+\frac{1}{9}+\cdots + \frac{1}{n^2}+\cdots \end{aligned}$   
    **收敛速度还可以接受。**

    ~~~python
    from sympy import summation
    k = Symbol('k',integer=True)
    summation(1/k**2,(k,1,oo))  #符号运算可以得到无穷级数和就是π**2/6
    ~~~

    计算 $\pi=\sqrt{6 \displaystyle \sum_{k=1}^{\infty}\dfrac{1}{k^2}}$ 

## 格雷戈里-莱布尼茨级数(Gregory-Leibniz series)

格雷戈里-莱布尼茨级数于 1671年2月15日提出。利用**反正切函数**的泰勒级数展开得到 $\dfrac{\pi}{4}$ 的级数算法。

~~~python
>>> from sympy import *
>>> x,y,z=symbols('x y z')
>>> series(atan(x),n=10)  # 反正切函数幂级数展开
x - x**3/3 + x**5/5 - x**7/7 + x**9/9 + O(x**10)
~~~

反正切函数的级数 (series for the **inverse tangent** function), 也称为 **Gregory's series**:    
$\displaystyle \begin{aligned}    \arctan(x)&=x-\dfrac{x^3}{3}+\dfrac{x^5}{5}-\dfrac{x^7}{7}+\cdots\\&=\sum_{k=0}^\infty(-1)^k\dfrac{x^{2k+1}}{2k+1}
\end{aligned}$    

具体推导过程如下：  
$\because \dfrac{\mathbf{d}(\arctan x)}{\mathbf{d}x}=\dfrac{1}{1+x^2}$   
$\because 1-x^n=(1-x)(1+x+x^2+\cdots+x^{n-1})\\\therefore \dfrac{1}{1-x}=\displaystyle\sum_{n=0}^{\infty} x^n,\;|x|<1$   
$\dfrac{1}{1+x^2}=\dfrac{1}{1-(-x^2)}=\displaystyle\sum_{n=0}^{\infty}(-x^2)^n=\sum_{n=0}^{\infty}(-1)^nx^{2n}$   

$\begin{aligned}
    \therefore \arctan(x) &=\int\dfrac{1}{1+x^2}\mathrm{d}x\\
    &=\displaystyle\int\sum_{n=0}^{\infty}(-1)^nx^{2n}\mathrm{d}x\\
    &=\sum_{n=0}^{\infty}(-1)^n\dfrac{x^{2n+1}}{2n+1}, \;|x|<1
\end{aligned}$

**莱布尼茨公式** （**Leibniz formula**）  

$\dfrac{π}{4}$ 可以通过 $x = 1$ $\red{(TODO)}$ 代入上述反正切函数的级数中得到。这里有一个疑问，既然 要求 $|x|<1$, 又怎么能取  $x=1$ 呢？这里存在一个 $0\times\infty \overset{?} = 0$ 的问题。

$\displaystyle \frac{\pi}{4} = \sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1} = \frac{1}{1}- \frac{1}{3}+ \frac{1}{5}- \frac{1}{7}+ \cdots$   

正如你看到，这个级数的**收敛极慢！不可取**。

## Nilakantha Series

$\displaystyle \begin{aligned} {\pi} &= 3+ \frac{4}{2 \centerdot 3 \centerdot 4}- \frac{4}{4 \centerdot 5 \centerdot 6}+ \frac{4}{6 \centerdot 7 \centerdot 8}- \frac{4}{8 \centerdot 9 \centerdot 10}+ \cdots \\&= 3+ \frac{1}{1 \centerdot 3 \centerdot 2}- \frac{1}{2 \centerdot 5 \centerdot 3}+ \frac{1}{3 \centerdot 7 \centerdot 4}- \frac{1}{4 \centerdot 9 \centerdot 5}+ \cdots \\&= 3+ \sum_{n=2}^{\infty} \frac{(-1)^n}{(n-1)n(2n-1)}  \end{aligned}$

This is  for pi.   
**这是计算圆周率的更快一点的收敛方法。（the faster convergent method）**

**Nilakantha 级数的有理数迭代结果**   
>耗时(s), 迭代次数, 圆周率 π
1.9259201999999997, 4500, 3.1415926535870515825837405507560137150803433030977
3.6562770999999996, 6500, 3.1415926535888833262423877236599992905011247088849
6.4071963, 8500, 3.1415926535893862988637989428921227071088158696038
9.226604299999998, 10000, 3.1415926535895433134507693207779502215449257421397
59.0730983, 20000, 3.1415926535897619931497723041779282156055633567492
166.8244976, 30000, 3.1415926535897839801292611829194198667214211744860
364.8126532, 40000, 3.1415926535897893325056005368286971249174170406760


## 收敛更快的 Viete's Formula

Viète's formula is the following infinite product of nested radicals representing the mathematical constant $π$:   
$\displaystyle {\frac {2}{\pi }}={\frac {\sqrt {2}}{2}}\cdot {\frac {\sqrt {2+{\sqrt {2}}}}{2}}\cdot {\frac {\sqrt {2+{\sqrt {2+{\sqrt {2}}}}}}{2}}\cdots$   

实验证明，迭代200次就已经超出了Python的最大迭代深度（RecursionError: maximum recursion depth exceeded）

>耗时(s),         迭代次数,       近似 π
46.814693,       150,    3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482  4707897442(90位正确)

It is named after François Viète (1540–1603), who published it in 1593. 

Viète's formula may be rewritten and understood as a limit expression.   
$\displaystyle \lim _{n\rightarrow \infty }\prod _{i=1}^{n}{\frac {a_{i}}{2}}={\frac {2}{\pi }}$   
where $a_n = \sqrt{2 + a_{n − 1}}$, with initial condition $a_1 = \sqrt{2}$.

Viète's formula may be obtained as a special case of a formula given more than a century later by Leonhard Euler, who discovered that:    

${\displaystyle {\frac {\sin x}{x}}=\cos {\frac {x}{2}}\cdot \cos {\frac {x}{4}}\cdot \cos {\frac {x}{8}}\cdots }$

Substituting   
${\displaystyle x={\frac {\pi }{2}}}$ in this formula yields:    

${\displaystyle {\frac {2}{\pi }}=\cos {\frac {\pi }{4}}\cdot \cos {\frac {\pi }{8}}\cdot \cos {\frac {\pi }{16}}\cdots}$

Then, expressing each term of the product on the right as a function of earlier terms using the half-angle formula:   

${\displaystyle \cos {\frac {x}{2}}={\sqrt {\frac {1+\cos x}{2}}}}$   

gives Viète's formula.

It is also possible to derive from Viète's formula a related formula for $π$ that still involves nested square roots of two, but uses only one multiplication: [ref Viete formula][Viete]

$\displaystyle \pi =\lim _{k\to \infty }2^{k}\underbrace {\sqrt {2-{\sqrt {2+{\sqrt {2+{\sqrt {2+{\sqrt {2+\cdots +{\sqrt {2}}}}}}}}}}}} _{k\ \mathrm {square \;roots}}$

该算法效率最高，计算时间最短，精度也高。170次迭代报错，超出了迭代深度（RecursionError: maximum recursion depth exceeded，缺省是5000）。

>耗时(s),         迭代次数,       近似 π
0.3498688000000001, 165,    3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067

## 反三角函数 $\arcsin(x)$

1676年，牛顿给出的方法。令下列 $x=\dfrac{1}{2}$  
$\dfrac{d}{dx}(\sin^{-1}x)=\dfrac{1}{\sqrt{1-x^2}}\implies$

$\begin{aligned}
\displaystyle \sin^{-1}x &=\int(1-x^2)^{-1/2}\mathrm{d}x+c(constant)\\
&=\int(1+\dfrac{x^2}{2}+\dfrac{3x^4}{8}+\dfrac{5x^6}{16}+\cdots+c),\;|x|<1\\
&=x+\dfrac{1}{2}\dfrac{x^3}{3}+\dfrac{1\cdot3}{2\cdot4}\dfrac{x^5}{5}+\dfrac{1\cdot3\cdot5}{2\cdot4\cdot6}\dfrac{x^7}{7}+\cdots+c    
\end{aligned}$

$\because \sin^{-1}x=0\; \text{at}\; x=0\implies c=0$

$\therefore \sin^{-1}(x)=x+\dfrac{1}{2}\dfrac{x^3}{3}+\dfrac{1\cdot3}{2\cdot4}\dfrac{x^5}{5}+\dfrac{1\cdot3\cdot5}{2\cdot4\cdot6}\dfrac{x^7}{7}+\cdots,\;|x|<1\\
=\displaystyle \sum_{n=0}^{\infty}\dfrac{(2n)!}{2^{2n}(n!)^2(2n+1)}x^{2n+1}$

同理可以得到    
$\therefore \cos^{-1}(x)=\dfrac{\pi}{2}-\left(x+\dfrac{1}{2}\dfrac{x^3}{3}+\dfrac{1\cdot3}{2\cdot4}\dfrac{x^5}{5}+\dfrac{1\cdot3\cdot5}{2\cdot4\cdot6}\dfrac{x^7}{7}+\cdots\right),\;|x|<1\\
=\displaystyle \dfrac{\pi}{2}-\sum_{n=0}^{\infty}\dfrac{(2n)!}{2^{2n}(n!)^2(2n+1)}x^{2n+1}$

### Stirling's Approximation for n!

$\begin{aligned} \ln n! &=\ln1+\ln2+...+\ln n\\ &= \sum_{k=1}^{n} \ln k\\
&= \int_1^n \ln x \mathbf{d}x \\
&= (x \ln x-x)|_1^n\\
&= n \ln n-n+1\\
&\approx n \ln n-n 
\end{aligned}$

所以 对于很大的 $n$，Stirling斯特林逼近公式为  $\boxed{\ln n! \approx n\ln n-n}$   
或 $\boxed{n!\approx n^n e^{-n} \sqrt{2\pi n}}$

更精确的有:   
$\sqrt{2\pi n}\left( \dfrac{n}{e}\right)^n \le n! \le \sqrt{2\pi n}\left(\dfrac{n}{e}\right)^n e^{\frac{1}{12n}}$

## Taylor级数和Maclaurin Series的实现

在GeoGebra中可以轻松实现多项式之和逼近各种函数。

1. 先定义次数Order的滑条 $n=slider(1,20,1)$
2. 再定义要逼近的函数，如 $f(x)=\arctan(x),g(x)=\sin(x),h(x)=\cos(x),\cdots$
3. 调用函数 $g=TaylorPolinomial(f,x(A),n),\;A=(0,0)$
4. 调用函数 $FormulaText(g, true, true)$ 可以显示级数

[TaylorSeries的多项式逼近演示GGB](ggb/TaylorSeries的多项式逼近演示.ggb)

## 计算 $\pi$ 收敛速度极快算法

代数和几何结合的方法。

采用刘徽割圆术，用正 $n$ 边形逼近圆的方法，实现计算圆周率 $\pi$ 的目的。

记 正 $n$ 边形的边长为 $L_n$, 由正 $n$ 边形产生的正 $2n$ 边形的边长为 $L_{2n}$, 则如图可有    
![刘徽割圆术](image/刘徽割圆术.png)   
$L_n=AA',L_{2n}=AB\\
L_{2n}^2=(\dfrac{L_n}{2})^2+(1-OC)^2\\
=\dfrac{1}{4}L_n^2+\left(1-\sqrt{1-\dfrac{1}{4}L_n^2}\right)^2\\
=2-2\sqrt{1-\dfrac{1}{4}L_n^2}\\
L_{2n}=\sqrt{2-\sqrt{4-L_n^2}}$

单位圆的半径 $r=1$, 则有正 $6$ 边形的边长 $L_6=1$, 利用迭代关系式可以快速求出 **周长**    
$\displaystyle C_{O}=2\pi=\lim_{n\to \infin} (n\times L_{n})\\
\pi=\dfrac{1}{2}\times \lim_{n\to \infin} (n \times L_{n})$

即圆周率就是**半周长**，上述算法收敛性很快！

### 在GeoGebra中实现

1. 先建立迭代次数滑动条 $n=slider(1,10,1)$
2. 再建立迭代函数 $f(x)=sqrt(2 - sqrt(4 - x\; x))$
3. 然后用GGB的迭代命令 $value = Iteration(f, 1, n)\to$ $L_{2n}=\sqrt{2-\sqrt{4-L_n\times L_n}},L_6=1$，初始值取正6边形时的值1.
4. 正 $2n$ 边形的**半周长**为 $\pi=value\times6\times2^{n-1}$

这一算法的收敛也极快，正多边形的边数以指数级增长。边数 $=6\times2^{n-1}$

### Python程序得到的结果

**Python 源码** 参见[迭代计算圆周率π的Python源码](iteration_pi.py) 

采用符号运算得到前10个结论：
>12*sqrt(2 - sqrt(3))
24*sqrt(2 - sqrt(sqrt(3) + 2))
48*sqrt(2 - sqrt(sqrt(sqrt(3) + 2) + 2))
96*sqrt(2 - sqrt(sqrt(sqrt(sqrt(3) + 2) + 2) + 2))
192*sqrt(2 - sqrt(sqrt(sqrt(sqrt(sqrt(3) + 2) + 2) + 2) + 2))
384*sqrt(2 - sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(3) + 2) + 2) + 2) + 2) + 2))
768*sqrt(2 - sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(3) + 2) + 2) + 2) + 2) + 2) + 2))
1536*sqrt(2 - sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(3) + 2) + 2) + 2) + 2) + 2) + 2) + 2))
3072*sqrt(2 - sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(3) + 2) + 2) + 2) + 2) + 2) + 2) + 2) + 2))
6144*sqrt(2 - sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(sqrt(3) + 2) + 2) + 2) + 2) + 2) + 2) + 2) + 2) + 2))

第151次 到 第159次的迭代结果：

>3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825324499856
3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825337712765
3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825341015992
3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825341841799
3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342048251
3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342099864
3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342112767
3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342115993
3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342116799

第 160 次迭代结果，准确到小数点后 第96位：
>3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117001


### 圆周率 $\pi$ 生成器

- 方法一、在网络上搜索到一个圆周率生成器，只要输入一个数：生成位数，就可以算出该圆周率。没有验证正确否。供大家参考。

    [圆周率$\pi$生成器](https://www.jisuan.mobi/pbBHmBz1b6z61yUU.html)

- 方法二、在Python环境下，只要调用 `sympy.pi.evalf(n+1)` 就可以得到任意 $n$ 位小数的 圆周率 $\pi$. 

~~~python
from sympy import pi

pi.evalf(1001)  # 得到1000位小数位的π
~~~


### 圆周率小数点后100位

　　14 15 92 65 35 89 79 32 38 46 26 43 38 32 79 50 28 84 19 71 69 39 93 75 10 58 20 97 49 44　59 23 07 81 64 06 28 62 08 99 86 28 03 48 25 34 21 17 06 79 。



### 圆周率小数点后1000位

在Python环境下，输入了 `sympy.pi.evalf(1001)` 位数，计算结果如下：

>3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679 821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989



[Viete]:https://en.wikipedia.org/wiki/Viète%27s_formula#cite_note-servi-12
[TS]:https://en.wikipedia.org/wiki/Taylor_series
[Maclaurin]:https://en.wikipedia.org/wiki/Colin_Maclaurin
[Wallis]:https://en.wikipedia.org/wiki/Wallis_product