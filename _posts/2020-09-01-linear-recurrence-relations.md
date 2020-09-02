---
title: Notes for solving linear recurrence relations with constant coefficients
categories:
 - notes
tags: math, recurrence, algorithm
author: tenpages

---

Some notes on solving linear recurrence relations (just in case I need analyze algorithms again).

<!--more-->

## Homogeneous linear recurrence with constant coefficients

Order-$k$ homogeneous linear recurrence with constant coefficients is in form of


$$
a_n=c_1a_{n-1}+c_2a_{n-2}+...+c_da_{n-k},
$$


where $k$ coefficients $c_i(\forall i)$ are constants, and $c_k\neq0$. The equation


$$
r-c_1r^{k-1}-...-c_k=0
$$


is called the characteristic equation, whose $t$ distinct roots $r_1, ..., r_t$ with multiplicities $m_1, ..., m_t$, respectively, solve the recurrence relation by


$$
\begin{align*}
a_n=&(\alpha_{1,0}+\alpha_{1,1}n+...+\alpha_{1,m_1-1}n^{m_1-1})r_1^n \\
& +(\alpha_{2,0}+\alpha_{2,1}n+...\alpha_{2,m_2-1}n^{m_2-1})r_2^n \\
& +...+(\alpha_{t,0}+\alpha_{t,1}n+...\alpha_{t,m_t-1}n^{m_t-1})r_t^n,
\end{align*}
$$


where $\alpha_{i,j}$ are constants for $1\leq i\leq t$ and $0\leq j\leq m_i-1(\forall i)$.

In a simpler special case:


$$
a_n=c_1a_{n-1}+c_2a_{n-2}
$$


has a solution in form of 


$$
a_n=(\alpha_1+\alpha_2n)r_0^n
$$


when the equation $r^2-c_1r-c_2=0$ has only one root $r_0$.

## Linear non-homogenous recurrence relations with constant coefficients

Order-$d$ homogeneous linear recurrence with constant coefficients is in form of


$$
a_n=c_1a_{n-1}+c_2a_{n-2}+...+c_da_{n-d}+F(n),
$$


where $d$ coefficients $c_i(\forall i)$ are constants, $c_d\neq0$, and 


$$
F(n)=(b_tn^t+b_{t-1}n^{t-1}+...+b_1n+b_0)s^n.
$$


Using the <u>method of undetermined coefficients</u>, to solve the recurrence relation, first solve characteristic equation of the homogenous recurrence relation associated to it:


$$
a_n=c_1a_{n-1}+c_2a_{n-2}+...+c_da_{n-d}.
$$


Suppose $s$ is one of its root for the characteristic equation, there is a particular solution of the form


$$
(p_tn^t+...+p_1n+p_0)s^n;
$$


otherwise, suppose $s$ has a multiplicity of $m$, the particular solution is of the form


$$
n^m(p_tn^t+...+p_1n+p_0)s^n,
$$


where in both cases, $p_t(\forall t)$ are undetermined coefficients. Combining the particular solution with the general solution to the associated homogenous relation, the coefficients can be determined by solving linear equations. 



For the case where there are multiple components in form of $F(n)$ mentioned above, *i.e.* 


$$
a_n=c_1a_{n-1}+c_2a_{n-2}+...+c_da_{n-d}+F_1(n)+...+F_u(n),
$$


where 


$$
F_i(n)=(b_{i,t_i}n^{t_i}+b_{i,t_i-1}n^{t_i-1}+...+b_{i,1}n+b_{i,0})s_i^n
$$


for every $1\leq i\leq u$, there is a particular solution for each component $F_i(n)$, following the form described above. The solution is of the form summing up all particular solutions and the general solution.



### References

[1] D.P. , A. 2007. Finding non-homogenous part of solution $\{a_n^{(p)}\}$ . *Probability and combinatorics*. Excel Books India. 393–394.