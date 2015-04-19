Title: kth smallest element in union of sorted arrays
Date: 2011-12-8 12:25:00
Tags: algorithms
Math: yes

<blockquote>
Given two sorted arrays A and B of length n, find the kth smallest element in the union of the two arrays (imagine the two arrays are merged into one sorted array of length 2n). Do so in $ \Theta (\lg n) $.
</blockquote>

If we pick two elements, $A[i]$ and $B[j]$, and look at the bigger of the two, let it be $A[i]$, we know that it is **at least** the $i+j$ smallest element in $A \cup B$. Why? Because it is bigger than everything in $A[1..i-1]$ and $B[1..j]$, and the amount of elements in those two is equal to $i+j$.

What about the smaller of the two, $B[j]$? We can say that it's **at most** the $i+j-1$ smallest element in $A \cup B$. Why? Because $A[i+1..n], B[j..n]$ are all bigger than it.

Now if $k &lt; i+j$, we can say for sure that our $k$th smallest element is not $A[i]$ or any of A's elements after it. Similarly, if $k \geq i+j$, that rules out $B[1..j]$.

We start at $A[\lfloor \frac{n}{2} \rfloor], B[\lfloor \frac{n}{2} \rfloor]$, and depending on who's bigger, we use the above observations to rule out either the bottom or top half of one of the arrays. If we rule the top of an array, we go back to our original problem only one of the arrays has shrunk in half. If we rule out the bottom, we now have to find the $(k-$ number of elements thrown$)$ smallest element in the halved array and the untouched one.

We are done when one of the arrays is empty, then we simply return the $k$th element in the other one.

It should be fairly obvious why this takes $\Theta (\lg n)$. At each step of the algorithm we do a constant amount of work, and our recursion call loses half an array (similar to binary search).
