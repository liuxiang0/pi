# The different algorithms for calculating $\pi$ (circumference ratio)

$π = \frac{C}{D}$ where C is circumference of a circle, and D is its diameter.  

$π = \frac{A}{R^2}$ where A is the area of a circle and R is its radius.  

$SA = 4πR^2$ where SA is the Surface Area of a sphere, and R is its radius.  

$V=\frac{4}{3} πR^3$ where V is the volume of a sphere and R is its radius.  

**Question**: How to calculate $π$?

## Some algorithms for calculating $π$

* **Gregory-Leibnize** series Sum for $\frac{π}{4}$

$$\frac{\pi}{4} = \sum_{n=0}^{\infty}\frac{(-1)^n}{2n+1} = \frac{1}{1}- \frac{1}{3}+ \frac{1}{5}- \frac{1}{7}+ \cdots.$$

* **John Wallis'** Series Product for $\frac{π}{2}$

$${\displaystyle {\begin{aligned} \frac{π}{2} &= \prod_{k=1} ^{\infty} \frac{2k}{2k-1} \centerdot \frac{2k}{2k+1}  \\&=\frac{2}{1} \centerdot \frac{2}{3} \centerdot \frac{4}{3} \centerdot \frac{4}{5} \centerdot \frac{6}{5} \centerdot \frac{6}{7} \cdots \end{aligned}}}$$

* **Euler Identify** for $\frac{π^2}{6}$

$${\displaystyle {\begin{aligned} \frac{π^2}{6}&= \sum_{k=1} ^{\infty} \frac{1}{k^2} &=1+\frac{1}{4}+\frac{1}{9}+\cdots + \frac{1}{n^2}+\cdots \end{aligned}}}$$

* **Nilakantha** Series Sum for $π$

$${\displaystyle {\begin{aligned} {\pi} &= 3+ \frac{1}{1 \centerdot 3 \centerdot 2}- \frac{1}{2 \centerdot 5 \centerdot 3}+ \frac{1}{3 \centerdot 7 \centerdot 4}- \frac{1}{4 \centerdot 9 \centerdot 5}+ \cdots \\&= 3+ \sum_{n=2}^{\infty} \frac{(-1)^n}{(n-1)n(2n-1)}  \end{aligned}}}$$

* **Stirling's approximation** for $n!$

$${\displaystyle {\begin{aligned} {n!} &= \sqrt{2 \pi n}(\frac{n}{e})^n [1+O(\frac{1}{n})]  \end{aligned}}}$$

    Therefore 

$${\displaystyle {\begin{aligned} {\pi} \approx \frac{[e^n n!]^2}{2n^{2n+1}}  \end{aligned}}}$$

## Different algorithms and different results

- Below are the tests performed with each of the algorithms for calculating pi to **8 decimal places** (3.14159265).
The deviation is less than 1e-8.

- Computer configuration

    Compiler: Python 3.6.8 64-bit('base':conda3)  
    Processor: 2.5GHz Intel Core i5  
    Memory 4GB 1600MHz DDR3  
    MacOS MoJave Version 10.14.4  
    Computer: MacBook Pro(13-inch, Mid 2012)

 Algorithms|Iterations (n)|Time (seconds)|PI ($π$)
--------|-------|------|-----
Gregory- Leibniz|99995330|49.21365842499927|3.141592663589793
**Nilakantha**|293|0.00016225599938479718|3.141592643651065
**Viete**|**15**|1.3628000033349963e-05 |3.141592648776985
Wallis	|59805706|29.035706771999685|3.141592643589793

## Different Algorithms of Python Language

1. [Gregory-Leibniz][Leibniz] series sum for $\frac{π}{4}$

    elapsed time= 5.193804737999926 iteration number= 10000002 deviations%%= 0.0009999998829002266 $π$= 3.1415927535897814

    elapsed time= 49.21365842499927 iteration number= 99995330 deviations%%= 9.99999993922529e-05 $π$= 3.141592663589793

2. [Nilakantha][Nilakantha] series sum for $π$

    elapsed time= 7.982299939612858e-05 iteration number= 136 epson= 1e-07 deviations%%= 0.0009937884470900826 $π$= 3.141592752968638

    elapsed time= 0.00016225599938479718 iteration number= 293 epson= 1e-08 deviations%%= 9.938728062763857e-05 $π$= 3.141592643651065

3. [Viete][Viete] Formula for $\frac{2}{π}$

    elapsed time= 1.9795000298472587e-05 iteration number= 13 epson= 1e-07 deviations%%= 0.0007700492110629398 $π$= 3.141592576584872

    elapsed time= 1.3628000033349963e-05 iteration number= 15 epson= 1e-08 deviations%%= 4.8128079299658566e-05 $π$= 3.141592648776985

4. [Wallis'][Wallis] product for $π$

    elapsed time= 3.83474428000045 iteration number= 7854418 epson= 1e-07 deviations%%= 0.0009999999361909317 $π$= 3.1415925535897995
    
    elapsed time= 29.035706771999685 iteration number= 59805706 epson= 1e-08 deviations%%= 9.99999993922529e-05 $π$= 3.141592643589793

Observation: Test results are not conclusive because they were not performed with proper techniques. Furthermore, several factors can influence, such as the compiler, algorithm, computer, etc.

[Leibniz]:Gregory_Leibnize_pi.py
[Nilakantha]:Nilakantha_pi.py
[Viete]:Viete_pi.py
[Wallis]:Wallis_pi.py
