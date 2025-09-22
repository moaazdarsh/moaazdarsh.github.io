At first we may think of sequences intuitively without the formal definition, it's clear that $0,\ 2,\ 4,\ 6,\ 8,...$ and $1,\ 2,\ 4,\ 8,\ 16,...$ are sequences. One may say he knows the next number in those sequences, or even say that both of them increase indefinitely to infinity, but is there any logical arguments for these claims?!

A sequence can be characterized in more general and exact ways, either by an explicit formula for each term such as the harmonic sequence.
$$
x_n = \frac{1}n \rightarrow 1,\ \frac{1}2,\ \frac{1}3,\ \frac{1}4,...
$$
Or by a recursion formula such as the following famous sequence, which can also be characterized with an explicit formula that can be left for the reader to derive.
$$x_1 = 1, \ x_{n+1} = \frac{x_n}{2} \rightarrow 1,\ \frac{1}2,\ \frac{1}4,\ \frac{1}8,...$$
The next example can answer one of the questions presented in the first paragraph, can we logically deduce the next term in a sequence?
$$x_n = 2(n-1) \; mod\:10 \rightarrow 0,\ 2,\ 4,\ 6,\ 8,\ 0,\ 2,...$$
If we look only at the first five terms, we would assume that the next term is $10$, but as we can see the sequence deviates from this pattern afterwards. So it's not possible to predict the next term using the previous ones without making additional assumptions.

Now let's introduce a more formal definition of sequences:

> A function $f(n): \mathbb{N} \rightarrow \mathbb{R}$ is called a *sequence* and is denoted by ${\{x_n\}}_{n=1}^\infty$ or ${\{x_n\}}_{1}^\infty$.

---
## Limits
You may notice an interesting property in some sequences such as $\left\{ \frac{n-1}n \right\}_1^\infty$ which is that they seem to approach a specific value as $n$ gets bigger.
$$\left\{ \frac{n-1}n \right\}_1^\infty \rightarrow 0,\ \frac{1}2,\ \frac{2}3,\ \frac{3}4,\ \frac{4}5,...$$
For this specific sequence we can explain that clearly.
$$\left\{ \frac{n-1}n \right\}_1^\infty = \left\{ 1-\frac{1}n \right\}_1^\infty$$
As $n$ increases the value $\frac{1}n$ gets smaller, that enables us to make $x_n$ as close as we would like to $1$, the sequences which have this property are *convergent* and the number they approach is their *limit*, we define both as follows.

>A sequence *converges* to its *limit* $L$ if $\forall \epsilon > 0 \; \; \exists N \in \mathbb{Z}$ such that $|x_n - L| < \epsilon \; \; \forall n \geq N$ and we denote that as
>$$\lim_{n \rightarrow \infty}{x_n} = L$$

This definition may seem much more complex than the intuition we had, or even detached from it, but it's in fact the same thing. We can make $x_n$ as close to $L$ as we would like, which means that we can make $|x_n -L|$ smaller than any number $\epsilon$ given that $n$ is large enough, so we choose to make it larger than some number $N$.

---
Using this definition we can prove that $\lim_{n \rightarrow \infty} \frac{n^2}{2n^2 + 1} = \frac{1}2$ by supposing some number $\epsilon > 0$ and investigating the inequality
$$\left| \frac{1}2 - \frac{n^2}{2n^2 + 1} \right| < \epsilon \implies - \epsilon < \frac{1}2 - \frac{n^2}{2n^2 + 1} < \epsilon$$
$$ \frac{1}2 - \epsilon < \frac{n^2}{2n^2 + 1} < \frac{1}2 + \epsilon $$
Multiplying by $2n^2 +1$
$$ - \epsilon \, 2n^2 + \cancel{n^2} + \frac{1}2 - \epsilon < \cancel{n^2} < \epsilon \, 2n^2 + \cancel{n^2} + \frac{1}2 + \epsilon $$
Splitting into two inequalities we find
$$n^2 > \frac{1 + 2 \epsilon}{4 \epsilon}$$
$$n^2 > \frac{1 - 2 \epsilon}{4 \epsilon}$$
If we set $N$ to be any number greater than $\frac{1 + 2 \epsilon}{4 \epsilon}$ then $\left| \frac{1}2 - \frac{n^2}{2n^2 + 1} \right| < \epsilon \; \; \forall n>N$. $\qquad \blacksquare$ 

---
## Partial Sums Sequences
Given any sequence ${\{x_n\}}^{\infty}_1$ we can construct another one ${\{ s_n\}}_1^\infty$ such that
$$s_n = x_1 + x_2 +...+ x_{n-1} + x_n = \sum_{i=1}^n x_i$$
We can try this with the sequence ${\{2^n\}}_0^\infty$ and the constructed sequence would look like this
$$1,\; 1.5,\; 1.75,\; 1.875,\; 1.9375,...$$
These sequences are called partial sums sequences or *[[Series]]*.

---
## Cauchy Convergence Criterion
The previous definition of convergence assumes that we know the limit, we now want a definition of convergence that doesn't depend on knowing that information, before let's first look at an example of a convergent sequence.
$${\left\{ \frac{2n + 3}{3n + 4} \right\}}_0^\infty \rightarrow \frac{3}4,\ \frac{5}7,\ \frac{7}{10},\ \frac{9}{13},\ \frac{11}{16},... $$
If we look at the difference between any two terms we'll find that the differences get smaller as we go into the sequence, referring back to the previous definition that makes sense. If we can ensure that all the terms where $n\geq N$ are as close to $L$ as we like, then we can make the differences between them as small as we like, because they can't be larger than $\epsilon$.

This may become clearer when we look at the formal definition and its proof.
>A sequence is convergent $\iff \forall \epsilon > 0 \; \; \exists N \in \mathbb{Z}$ such that $|s_n - s_m| \; \; \forall n,m \geq N$.
