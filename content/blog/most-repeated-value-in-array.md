Title: finding the most repeated value in an array
Date: 2012-02-04 11:37:00
Tags: algorithms

> An array of length _n_ has _k_ distinct elements, $k \lt n$. Find the most
> repeated value in the array.

(note that this isn't the same as finding the majority (if there is one) in an
array which can be done in $\Theta(n)$ by finding the median or using the more
simplistic Boyer-Moore Majority Vote Algorithm)

The straight forward solution gives us $\Theta(n\lg{n})$, by sorting the array
and doing a linear pass while maintaining the maximum pair of (value, number of
repeats).

We can slightly improve this to $\Theta(n\lg{k})$ by using $O(k)$ memory.

Build a Red-Black tree of all distinct values in the array. There are _k_ of
those, so insertion takes $O(\lg{k})$. In every node, store the number of times
its key has appeared in a field, call it _size_.

We build the tree by going over the input array and inserting each value. If
a value is already in the tree, we simply increment its _size_ by 1.

Like before, we keep a pair of (value, size) for the most repeated value that
is currently in the tree. Update this pair as necessary when inserting into the
tree (by examining the _size_ of the inserted node).

We have _n_ values to insert to a tree with _k_ nodes which gives us a total
running time of $\Theta(n\lg{k})$.
