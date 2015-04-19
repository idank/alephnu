Title: solving the selection problem given the im/n smallest element
Date: 2011-12-10 22:35:00
Tags: algorithms
Math: yes

Given a black-box capable of finding the $\left \lfloor \frac{in}{m} \right \rfloor$
smallest element in an array of length $n$, where $1 \leq i \lt m$ are constant,
find the $k$-th smallest element in a given array using the black-box in linear time.

Suppose our black-box is capable of finding the median of an array of length $n$, how would we solve the same problem?

1. Find the median of $A[p..r]$ using the black-box.
2. Partition $A$ using the median as our pivot. Suppose the median's index after partitioning is $q$.
3. If $q-p+1 = k$ then $A[q]$ is the element we're looking for and we're done.
4. If $k \lt q-p+1$, recursively call our procedure on $A[p..q-1]$, otherwise call it on $A[q+1..r]$ with $k=k-(q-p+1)$.

Steps 1 and 2 take $\Theta(n)$ time. In step 4 we cut the array in half, so we can express the running time of our algorithm using this recurrence relation: $$T(n)=T\left (\frac{n}{2} \right )+\Theta(n)$$ Solving this gives us $T(n)=\Theta(n)$.

Back to our original problem: if we use the exact same algorithm, except in step 1 find the $\left \lfloor \frac{in}{m} \right \rfloor$ smallest element in $A[p..q]$ where $q-p+1=n$, it will still work.

The question that remains, is it still linear? It turns out the answer is yes. Let's prove it:$$ T(n)=T(\max (\left \lfloor \frac{in}{m} \right \rfloor-1, n-\left \lfloor \frac{in}{m} \right \rfloor-1))+\Theta(n)$$

Let $an \in \Theta(n)$. Suppose there exists some $c$ such that $T(n) \leq cn$, then: $$ \begin{align}
    T(n) & =T(\max (\left \lfloor \frac{in}{m} \right \rfloor-1, n-\left \lfloor \frac{in}{m} \right \rfloor-1))+an \\\\\\
         & \leq c (\max (\left \lfloor \frac{in}{m} \right \rfloor-1, n-\left \lfloor \frac{in}{m} \right \rfloor-1))+an \\\\\\
         &\leq c (\max ( \frac{in}{m} , n- \frac{in}{m} ))+an \\\\\\
         &=cn(\max ( \frac{i}{m} , 1-\frac{i}{m} ))+an
  \end{align}$$

Since $\frac{i}{m} \lt 1$, let us denote $q=\max ( \frac{i}{m} , 1-\frac{i}{m} ) \lt 1$: $$T(n) \leq cqn+an = cn - (1-q)cn+an = cn+(an-(1-q)cn)$$ We are looking for $c$ such that $an-(1-q)cn \leq 0$, any $c \geq \frac{a}{1-q}$ will do.
