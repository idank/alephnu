Title: lower bound on finding the k-smallest elements in sorted order
Date: 2012-01-01 14:58:00
Tags: algorithms
Math: True

> Any comparison based algorithm solves the problem of finding the _k_-smallest
> elements in sorted order in $\Omega(k\lg{n})$ time for an _n_-length array.

To find a lower bound on the running time of any algorithm solving the above problem using comparisons we use the [decision tree model](http://en.wikipedia.org/wiki/Decision_tree_model).

What are the possible solutions an algorithm solving this problem produces?
For an input array of length *n*, any subset of length *k* is a possible
solution. But because the algorithm needs to produce the result in sorted
order, we have to take into account every possible permutation of those *k*-length
solutions.

So in total there are $\binom{n}{k} k!=n(n-1)\cdot \ldots \cdot (n-k+1)$ possible solutions.

Suppose our decision tree has *l* leaves, and its height is *h*.
Every possible solution is a leaf in the tree, so $n(n-1)\cdot \ldots \cdot (n-k+1) \leq l$.
Also, a binary tree of height *h*, has at most $2^h$ leaves.

We have the following bounds for the number of leaves *l*: $$(n-k+1)^k < n(n-1)\cdot \ldots \cdot (n-k+1) \leq l \leq 2^h$$ and we're looking to bound *h* from below.

Taking $\lg$ from both sides gives us $\lg{(n-k+1)^k} = k\lg{(n-k+1)} < h$.

For $k \leq n/2$ the above inequality gives us $h > k\lg{n}$, so the height of the tree is $\Omega(k\lg{n})$.

If $k > n/2$, we can think of the problem as finding the *n-k* **largest** elements and sorting the rest of the elements (this works because the "rest" are in fact the smallest).

We already showed that we can solve the problem if $k \leq n/2$ for the smallest, but it doesn't really matter whether it's the smallest or largest. So finding the $n-k < n/2$ largest elements will take $\Omega((n-k)\lg{n})$, and sorting the *k > n/2* remaining elements will take $\Omega(k\lg{k})=\Omega(k\lg{n/2})=\Omega(k\lg{n})$.

Overall it takes $\Omega((n-k)\lg{n})+\Omega(k\lg{n})=\Omega(k\lg{n})$, since $n-k < n/2 < k$, and we're done.
