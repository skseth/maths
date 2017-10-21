# Set Theory and Numbers

Halmos, Naive Set Theory

## Basics

The most primitive concept in set theory is one of belonging / containing / member of

Axiom of Extension : Two sets are equal if and only if they have the same extension

We can then define "subset of" $\subset$ / "includes" $\supset$

All other axioms allow us to make new types of sets:

Axiom of Specification : To every set A, and every condition S(A), there corresponds a set B whose elements are exactly those elements s of A for which S(x) is true

Russell's Paradox : B = $\{ x \in A : x \notin x \}$. Question : Does B belong to A? No, as it creates a contradiction. Hence there is no set of all sets.

Axiom : There exists a set => there exists an empty set $\emptyset$ (by Axiom of specification)

The empty set is a subset of every set - proved vacuously => given any set A, find an element of the empty set not in A.

Axiom of Pairing : Given any two sets there exists a set containing them => there exists a set containing only the two sets {a,b} - the unordered pair. The set {a,a} = {a} is called a singleton of a.

Axiom of Unions : For every collection of sets, there exists a set containing all the elements that belong to at least one of the sets => there is a unique set which contains only these specific elements.

Intersection : Given a non-empty collection of sets, we can define a set which only elements which exist in every set of the collection $\bigcap C = \{x : x \in X \text{ for every} X \in C\}$

Disjoint Sets : Sets with empty intersection

Pairwise Disjoint collection : any pair in a collection has an empty intersection

Set Difference or Relative Complement : A \ B = { x in A : x not in B}

Complement : Given A as a subset of E, A' = { x in E : x not in A}. 

De Morgan's Laws

Principle of duality : theorems about sets come in pairs - replace intersections by unions, unions by intersections and reverse any inclusions.

Symmetric Difference - $A \Delta B = A \setminus B \bigcup B \setminus A = A \cup B - A \cap B$

Redefining Intersection : If we consider the intersection of a collection of subsets of a particular set E, we can now define intersection for all collections, including the empty set : $\bigcap C = \{x \in E: x \in X \text{ for every} X \in C\}$. Now, $\bigcap \emptyset = E$.

Axiom of Powers : For each set, there exists a set containing every subset of that set amongst its elements => there is a unique set containing only these subsets. This is called the Power Set of the given set.

$P(E) = 2^E = \{ X : X \subset E \}$

$2^n = \binom{n}{0} + \binom{n}{1} + \binom{n}{2} ... \binom{n}{n}$

The intersection of powersets of some sets is equal to the powerset of the intersection - and the same holds for unions.

E = U P(E), but P (U E) => E is a subset of P (U E), often a proper subset. In general, E is not a subset of its power set, though it belongs to the power set.

An ordered pair of a and b (a,b) = {{a}, {a,b}}. a is the first coordinate, b is the second coordinate.

We can see that (a,b) = (x,y) => a = x, b = y.

Cartesian product : A x B = { (a,b): for some a in A, for some b in B}

Cartesian product with empty set is empty. 

Projection : Conversely, if R is a set such that every member is an ordered pair, then there exist sets A and B such that A x B = R. A,B are called the projections of R into the first and second coordinate. 

Relation : A relation is a set of ordered pairs. We can write $(x,y) \in R$ as x R y. The projection of R to the first coordinate is called the domain of R, and the projection to the second coordinate is called the range or co-domain of R.

dom R = {x : for some y, x R y}
ran R = {y : for some x, x R y}

The empty set is a relation, trivially, with empty domain and range.

A relation R in X (i.e. where dom R, ran R are subsets of X), can have some properties :

reflexive : x R x, for all x in X
anti-reflexive : x R y => x <> y
symmetric : x R y => y R x
transitive : x R y and y R z => y R x
anti-symmetric : x R y and y R x => x = y

An equivalence relation is one which is reflexive, transitive and symmetric.

A partial order relation is one which is reflexive, transitive and anti-symmetric.

Note that for any relation R, we can define a strict or a weak version of it by changing the reflexivity. The strict relation corresponding to R will be anti-reflexive, the weak one will be reflexive.

An equivalence relation R in X induces a unique partition in X - a partition is a disjoint collection of subsets of X whose union is X. This is sometimes called X/R or X modulo R.

For an element x of X, the subset of elements y of X such that x R y is called the equivalence class of x w.r.t. R. 

Every partition C of X induces an equivalence relation in X which is call X/C, such that x X/C y iff x,y belong to the same set in C.

Partial orders are in some sense the opposite, being anti-symmetric. Typically referred to as <=. A partially ordered set is a set along with a partial order in it. For every partial order, we can define a strict partial order which is anti-reflexive - this can be referred to as "<".

A total order is a partial order, where for every x and y, either x <= y, or y <= x. A total ordered set is often called a chain.

Set inclusion is a partial order on the power set of a set.

Partial orders will be discussed in depth again later on.

## Functions

f: X -> Y

is a relation from X to Y, such that for any x in X, there is a unique y in X such that (x,y) is in f. We can therefore say y = f(x). Functions are thus single valued.

Also often called map, transformation, correspondence, operator.

The set of all functions from X to Y is a subset of the powerset of X x Y. The set is called $Y^X$.

A function is thus identified by its domain, codomain and the rule for mapping the elements. 

The ordered pairs forming the function is called the graph of the function.

A function f from X to Y may have as its range only a subset of Y. If ran f = Y, we say f maps X onto Y.

Given a subset A of x, the set of all elements of Y which are mapped to elements of A are called the image of A in Y : f(A). Sometimes this is confusing if A is both an element of X and a subset.

If X is a subset of Y, the unique function f:X -> Y, such that f(x) = x is called the embedding or inclusion map of X in Y.

The inclusion map of X into X is called the identity map on X.

We can create extensions or restrictions of functions. If f is a function from Y to Z, and X is a subset of Y, then we can define a function g from Y to Z such that g(x) = f(x) for each x in X. g is called the restriction of f to X, and f is called an extension of g to Y. We write : g = f|X. Also, ran f|X = f(X). 

Note that if we take two sets X and Y, and all functions whose domain is X, and co-domain is Y, then the restriction defines a partial order between these functions - it is reflexive, transitive and anti-symmetric. This relation is called precedence - if g is a restriction of f, we say g precedes f.

We are often interested in extending functions which preserve certain properties.

The inclusion map of a subset X of a set Y is a restriction of the identity map of Y to the set X.

Inverse image of a function : given f: X -> Y, given any subset B of Y, $f^{-1}(B) = A$ if for any y in A, if f(x) = y then x is in A. Inverse image always exists.

Into : ran f is subset of codomain
Onto : ran f = codomain
One-to-One : f(x) = y and f(z) = y => x = z
One-to-One correspondence : Onto + one-to-one

Inverse of a function exists iff one-to-one and onto. In such a case f is also called an isomorphism (in set-theoretic terms). If there is an isomorphism from A to B, then we call the two sets isomorphic. Isomorhism is transitive.

TODO : Composites and inverses - more details.

* Prof Vittal Rao : Lecture 1 : Functions  
  https://www.youtube.com/watch?v=-WPQP8MhgZg&t=279s

## Natural Numbers - Counting to the first Infinity

We now come to the first big leap in set theory - the contruction of the natural numbers N.

To identify a number, we have to create sets who represent that number. We start with the most basic :

$$0 = \emptyset$$

Now, we define a successor set of a set x :

$$x^+ = x \cup \{x\}$$

Now, we can define 1,2,3 and so on. But we still need to define the set of natural numbers - to make the "so on" work we need an axiom :

**Axiom of Infinity : There exists a set contain 0 and all its successors**

We will define a successor set as one which contains 0 and if it contains x, then it contains $x^+$ also - the Axiom of infinity guarantees such a set exists. This set X may be too big - it may contain elements which are not strictly numbers.

Now, consider a family of successor sets F. The intersection of all sets in this family contains 0. Also, if such an intersection contain n, then n must be in all the sets, and hence $n^+$ must also be in all the sets. Thus the intersection will also contain $n^+$ - i.e. it will be a successor set too.

Consider the set Y

Y = {S in P(X): S contains 0 and all its successors }

S is not empty - definitely X is a member. 

Let N = $\bigcap S$

N is a successor set - in fact it is the minimal successor set that we wanted. We call this the set of natural numbers. A natural number is a member of the set N.

We can now define a **sequence** as a function from N to the any set X.

## Natural Numbers - Peano Axioms and Arithmetic

Before we go further, we want to built some key results which are useful for future steps.

The Peano Axioms are the set of following statements about N :

1) $0 \in N$, where $0 = \emptyset$  
2) If n is in N, then so is the successor $n^+ = n \cup \{n\}$  
3) **Principle of Mathematical Induction** : If S is a subset of N, S contains 0, and whenever S contains n, S also contain the successor to n, then S = N.

These properties follow immediately from our definition of natural numbers as the minimal successor set.

4) $n^+ \neq 0$ for all n in N. This follows from the definition of a successor.
5) If n and m are in N, and $n^+ = m^+$, then n = m. This proof need work

### Proof of Peano's Axiom (5)

**Transitive Set**  
We define a transitive set E as a set such that for every x in E, if $x \in y$ and $y \in E$, then $x \in E$

**No natural number is a subset of any of its elements**

We apply induction. Let S be the set of natural numbers not included in any of its elements. Clearly S is not empty because 0 is a member, vacuosly.

Let n be a member of S. Then n is not a subset of any of its elements. $n^+ = n \cup \{n\}$. Is $n^+$ a subset of any of its elements? The elements of $n^+$ are all the elements of n and n itself. If $n^+$ was a subset of any element of n, then by definition so would n, since n is a subset of $n^+$. This would contradict the fact that n is a member of S. So is $n^+$ a member of n? Since n is a member of S, it cannot contain itself as a member (since every set is a subset of itself). Hence $n^+$ is not a member of any of its elements. Thus S = N, by the principle of mathematical induction.

**Every element of a natural number is a subset of it (n is transitive)**
Let S be the set of all natural numbers whose members are its subsets. Clearly, 0 is in S (since it has no members).

Let n be in S. Then n contains all its members as subsets. Also, the $n^+$ contains n as its member + every element of n as a member. Thus n is a subset of $n^+$. Also every element of n is a subset of n, and hence also of $n^+$ since n is a subset of $n^+$. Thus $n^+$ is in S, and S = N.

**If $n^+ = m^+$, then n = m**

n+ = n U {n}, m+ = m U {m+}

Given n+ = m+ : Either n = m, or $n \in m$. Similarly, either m = n, or $m \in n$. 

Assume $m \neq n$. Then $m \in n$ and $n \in m$. Since n is transitive, this implies $n \in n$. But n is its own subset, and we have shown that no natural number is a subset of itself. 

**Building up Z,Q,R**

Starting from the Peano axioms one can build up the entire number system. This is done in a separate document.

### Definition by Induction

**Recursion Theorem** : If f is a function on X, there is a function u from N to X, such that, for some a in X, u(0) = a, and $u(n^+) = f(u(n))$ for all n in N.

A definition of this type is called definition by induction. Remember that X can be any set, even the set of reals, which we will learn is strictly larger than N. Thus, u will, in general, not cover all values of f.

Proof: Consider :

$C = \{S \in N x X: (0,a) \in S, (n,x) \in S => (n^{+},f(x)) \in S\}$. 

C is not empty as N x X is in C.

Let u = $\bigcap C$. u clearly belongs to C. We have to show u is a function : if (n,x) and (n,y) are in u, then x = y. Let S = set of natural numbers such that this condition is true.

0 is in S : else we can create a strict subset of u as a member of C.

Let n be in S, and u(n) = x. Clearly (n+,f(x)) is in u. Is there another element (n+,y) such that y not equal to f(x). Again, we can create a strict subset of u as a member of C - we have a nested induction so we will use m, instead of n.

Consider the set w = u - {(n+,y)}. (0,a) is in this set, because n+ cannot be 0 (by Peano's axioms proved earlier). Assume (m,t) is in this set. Then we have to show (m+, f(t)) is in w too. 

If m = n, t = x (remember we are nested), and we know (n+, f(x)) is a member of the set w. If m not equal to n, then we m+ <> n+, and hence, since (m+, f(t)) is in u, it must be in w. Thus w is a member of C and a strict subset of u, which is a contradiction.

Going back to the original induction, n+ is in S, and hence S = N.

### Exercises

**If n is a natural number, n != n+**
Else n would be a subset of one of its members

**If n != 0, n = m+ for some m**
Let S = set of all such numbers. 0 is a member vacuously. Let n be a member. Clearly, n+ is a member (duh!) of S. S = N.

**N is transitive**
This follows from the result that for any n in N, every element of n is a subset of n. We do have to show that every element of n is also in N. Let S = set of all natural numbers n such that every element of n is in N. 0 is in S vacuously. If n is in S, then n+ is in S by simple definition. S = N.

**If E is a nonempty subset of a natural number. Then there exists an element k in E such that k is in m whenever m is an element of E distinct from k**

*If n is a natural number containing another number m, then either n = m+, or n contains m+*

Let S be the set of all natural numbers that either contain the successor of all its elements, or if there is an element whose successor is not in n, then n is the successor of that element.

0 belongs to S. Assume n belongs to S. n+ = n U {n}. For all elements in n, the successor either belongs to n => it belongs to n+, or the n is the successor, in which case it belongs to n+. For n itself, n+ is of course the successor. Hence n+ is in S. Thus S = N.

*If E is a non-empty set of natural numbers, $\cap E$ is transitive*

Let a = $\cap E$. If x belongs to a, then x belongs to each member of E, and hence every member of x belongs to each member of E and therefore to a. x is a subset of a. 

*0 is a member of n, or n is zero*
By induction. 0 is true vacuously. Let the statement be true for some n. Then consider n+ = n U {n}. If n is 0, then clearly, n+ = {0}. If n is non-zero, then n contains 0, hence n+ contains 0. 

*If E is a non-empty set of natural numbers, $\cap E$ is a natural number*

Let a = $\cap E$. If a is empty, it is a natural number.

If a is not empty, if e is a member of a, it is a member of each element of E. If e+ is a member of each element of E then it must also be a member of a. 

Consider an e, such that e+ is not a member of each element of E. Then there must be at least one element of E which contains e, but not e+ => this element must be e+. Thus, e+ is a member of E. But e and every element of e is a member of a since a is transitive => a = e+. Thus a is in E, and is a number.

Why must there be an e such that e+ is not a member of a? Because otherwise a = N : 0 is a member of a, if n is a member of a, n+ is a member of a => a = N. But this means a contains the number it is a subset of, a contradiction, since no number is a member of itself.

**the final proof**
We now know a is a natural number. If a is 0, 0 must be in E since every non-zero natural number contains 0, and in that case a would have had at least one memeber.

If a is non-zero, then a is a member of E, and a subset of every other member of E != a. All these members of E either contain a+ or are a+ => a is a member of each of them.

## Arithmetic of Natural Numbers

**sum** 

$s_m(0) = m$, $s_m(n^+) = s_m(n)^+$

We define $s_m(n) = m + n$.

*associativity*

(k + m) + n = k + (m + n)  
For n = 0, this is k + m. Assume this is true for n.

(k + m) + n+  
= ((k+m) + n)+ (def)  
= (k + (m+n))+ (induction)  
= k + (m + n)+ (def)  
= k + (m + n+)

*commutativity*

*0 + n = n*  
0 in S (def). If n in s, then, 0 + n+ = (0 + n)+ = n+

*m+ + n = (m + n)+*

For 0, m+ + 0 = m+ = (m + 0)+  
Assume true for n. m+ + n+ = (m+ + n)+ = ((m + n)+)+ = (m + n+)+

*m + n = n + m*

m = 0: 0 + n = n = n + 0  
Assume true for m. m+ + n = (m + n)+ = (n + m)+ = n + m+

*$1 + n = n^+$*

Definition : s_1(n+) = s_1(n)+

We want to prove : s_1(n) = n+

n = 0: s_1(0) = 1 = 0+. Assume true for n.

s_1(n+) = s_1(n)+ = (n+)+.

**product**

$p_m(0) = 0$, $p_m(n^+) = p_m(n) + m$

We define p_m(n) = m.n

*distributive* 

k.(m + n) = k.m + k.n

For n = 0: k.(m + 0) = k.m = k.m + 0 = k.m + k.0

Assume true for n 

k.(m + n+) = k.(m + n)+ = k.(m+n) + k = (k.m + k.n) + k

= k.m + (k.n + k)  
= k.m + k.n+ 

*associativity*  
(k.m).n = k.(m.n)

For n = 0, (k.m).n = 0, k.(m.n) = k.(0) = 0

Assume true for n ie (k.m).n = k.(m.n)

(k.m).n+ = (k.m).n + k.m  (def)  
= k.(m.n) + k.m (ind)  
= k(m.n + m) (distributive)  
= k.(m.n+) (def)

*commutatitivity*  

*0.n = 0*

0 in S : 0.0 = 0

0.n+ = 0.n + 0 = 0 + 0 = 0

*m+.n = m.n + n*

n = 0. True. Assume for n

m+.n+ = m+.n + m+ = (m.n + n) + m+ = m.n + (n + m+)  

= m.n + (n + m)+ = m.n + (m + n)+ = m.n + (m + n+)

= (m.n + m) + n+ = m.n+ + n+

*m.n = n.m*

m = 0: 0.n = 0. n.0 = 0. Assume true for m.

m+.n = m.n + n = n.m + n = n.m+

*multiplicative unit*

1.n = n

For n = 0,  1.0 = 0. Assume true for n.

1.n+ = 1.n + 1 = n + 1 = n+

**power**

$e_m(0) = 1$, $e_m(n^+) = e_m(n).m$

We define e_m(n) = $m^n$

*$p^{m+n} = p^m.p^n$*

For n = 0, $p^{m+n} = p^{m + 0} = p^m = p^m.p^0$

Assume true for n

$p^{m+n+} = p^{m+ + n} = p^{m+}.p^n = p^m.p.p^n = p^m.p^n.p = p^m.p^{n+}$

## All natural numbers are comparable

We will first repeat a lemma we have proved earlier :

*If n is a natural number containing another number m, then either n = m+, or n contains m+*

Let S be the set of all natural numbers that either contain the successor of all its elements, or if there is an element whose successor is not in n, then n is the successor of that element.

Now for our main proof :

0 belongs to S. Assume n belongs to S. n+ = n U {n}. For all elements in n, the successor either belongs to n => it belongs to n+, or the n is the successor, in which case it belongs to n+. For n itself, n+ is of course the successor. Hence n+ is in S. Thus S = N.

We say that two natural numbers m and n are comparable if either m belongs n, or n belongs to m, or m = n. (recall that no number can belong to itself).

Let S(n) = all natural numbers comparable to N
Let S = all natural numbers where S(n) = N

Consider n = 0. 

0 = 0. If n is in S(n), the n contains 0 or is 0. If n is 0, n+ contains 0. If n contains 0, so does n+. Hence S(0) = N.

Assume S(n) = N.

For n+ : Is 0 comparable to n+ - yes, since 0 is in S.
Assume m is comparable to n+. We know m is comparable to n.

There are 3 cases : 

n+ belongs to m => n+ belongs to m+

m = n+ => m+ contains n+

m belongs to n+ => by the lemma proved earlier, we know that n+ = m+ or n+ contains m+.

In any of the 3 cases, m+ = n+ or m+ contains n+ or n+ contains m+.

Thus S(n+) = N, and n+ is in S. Thus S = N.

## Law of Trichotomy for natural numbers

Given two natural numbers m and n, only one of the 3 possibilities hold : m belongs to n, m = n, or n belongs to m.

Proof:

We have already seen that m and n are comparable. If n belongs to m, then m cannot also belong to n, otherwise by transitivity of natural numbers n would contain n.

## Ordering of Natural Numbers

We can naturally define an order on natural numbers : Given any two natural numbers m and n, m < n if m belongs to n (or equivalently, m is a proper subset of n).

### Exercises 

**Prove if m < n, m + k < n + k**

*If m < n, m+ < n+*
m < n => m belongs to n => n contains m+ or n = m+. Either case n+ contains m+.

*m < n => m + k < n + k*
For k = 0, this is true. Let it be true for k. Then,

m + k+ = (m+k)+ < (n + k)+ = n + k+

**If m < n, k != 0, m.k < n.k**

For k = 0, statement is vacuously true. For k = 1, m.1 < n.1 is true. We assume statement be true for any given k != 0.

m.k+ = m.k + k

n.k+ = n.k + k

Since m.k < n.k, we have m.k+ < n.k+

**If E is a non-empty subset of natural numbers, there exists a least element in E**

Let k = $\cap E$

If E contains 0, then k = 0, and is the least element since for every m in E, k <= m.

Consider E not containing 0. Then k != 0. Then k contains 0 i.e. k is not empty.

We note that k is transitive because every element of E is transitive.

k must have an element e such that e+ is not in k. Otherwise k = N (k contains 0, and if it contains e, then it contains e+) => k contains every natural number in E. This is obviously false, since if m is in E, then m will not contain m, and hence k cannot contain m. Thus, k contains an element e, such that e+ is not in k. 

Also, k cannot contain an element greater than e, because if it did, then this element would be e+ or contain e+ => k being transitive would contain e+, a contradiction. Thus k contains e and, since every set of E is transitive, k contains all members of e. K also cannot contain a non-member of e, other than e: If it did, this would be greater than e. Thus k = e U {e} = e+.

e+ must exist in E - if not then all elements in E contain e but not e+ => this is only possible if they are all e+! Thus k is in E and is the least element in E, since every other element at least equal.

## Equivalence of Sets

Two sets A and B are said to be equivalent ($A \sim B$), if there is a one-to-one correspondence between them.

A set is called finite if it is equivalent to a natural number. A set is called infinite if it is not.

**Every proper subset of a natural number n is equivalent to some element of n**

For 0, this is trivially true. Assume true for n.

For n+, let E be any subset. Either E contains n, or it does not. If it does not, set up a one to one correspondence between E and one of the members of n (this is true by hypothesis). If it contains n, take the set E-{n} and identify it with a member m of n. Note that m cannot be n, and in fact m < n. We map E to m+ by extending this function - m+ is a member of n+ and hence a proper subset of n.

**No natural number is equivalent to a proper subset of itself => no two different natural numbers are equivalent**

Trivially true for 0. Let it be true for n.

Assume f is a 1-1 correspondence from n+ to a proper subset E of itself. If n does not belong to E, then f|n is a 1-1 correspondence to a proper subset for n, contradicting the induction hypothesis. If n belongs to E, then n is equivalent to E - {n}, after some fiddling. This implies by induction hypothesis that E - {n} = n, or E = n+, contradicting the assumption that E is a proper subset.

For any two different natural numbers, one is a proper subset of the other => that no two different natural numbers are equivalent.

**N is infinite**

Let f be a 1-1 correspondence between N and some natural number m. Restrict f to m+ -> this is a 1-1 correspondence between m+ and m, which is not possible, since m is a proper subset of m, and no two different natural numbers are equivalent.

**Any set can be equivalent to at most one natural number**

Assume a set X has 1-1 correspondences f and g from numbers n and m, n != m. Then we can create a function h = $f(g^{-1})$ from n to m, which should be a 1-1 correspondence, a contradiction.

**No finite set is ever equivalent to a proper subset**

Let X be a set, and Y a proper subset of X. 

Let g be a 1-1 map from m, a natural number, to Y, and another, f, from n to X - Y, which is non-empty. We note that n > 0. We now construct a map h from m + n, to x, such that h(l) = g(l) when l < m, and h(m+l) = f(l) when l is greater than or equal to m. Then h is a bijection between X and (m + n), n > 0.

Also, since X is equivalent to Y, we can create a similar 1-1 map from X to m, which means X can have a 1-1 map to two different natural numbers.

## Number of elements in finite sets

The number of elements in a finite set E is the unique natural number equivalent to E - lets call it |E|.

*Consider a set X and its power set P(X). If E and F are in P(X), and $E \subset F$, then |E| <= |F|*

Since $E \sim |E| and $F \sim |F|$, it follows that |E| is equivalent to a subset of |F|.

*The union of two finite sets E and F is finite. Also, when E and F are disjoint, #(E U F) = #(E) + #(F)*

We first prove the "auxiliary fact" that in the number m + n, the complement to the sum m, is equivalent to n.

n = 0: m + n = m. Complement of m in m is empty set i.e. 0

Let this be true for n. 

Now, for n+, (m + n)+ = (m+n) U {m + n}. The complement of m in m+n is equivalent to n - let f be the bijection. We can extend the bijection f to n+ by setting f(m+n) = n+. Thus complement is n+.

Now, back to proof :
Let E and F be disjoint. In this case, let e and f be two bijections from E -> m, and f -> n respectively, where m and n are in N.

Since the complement of m in m + n is equivalent to n, we create a one one correspondence l, from n to the complement of m, and define f' = l(f(x)).

We create a new function h, from E U F to m + n, as follows : h(x) = e(x) when x in E, and h(x) = f'(x) when x is in F. 

To prove h is bijective : e(x) is bijective to from E to m, f'(x) is bijective from F to m'. E,F are disjoint as are m,m'. Hence e(x) U f'(x) is bijective from E U F, to m+n.

For any (non-disjoint) union, X U Y we take use the condition X U Y = X U (Y - X).

*Product: |E X F| = |E|.|F|*

Let e and f be the 1-1 correspondences. Then create a mapping from m*n to E X F, h, such that h(m*n - 1) = (e(m), f(n)), where 1 <= m <= |E| and 1 <= n <= |F|. 

*Number of functions: $|E^F| = |E|^{|F|}$*

Let's say E has m elements, and F has n. A functions from n F to E is a unique sequence of n numbers (e1, e2, ..., eN), such that e1 can take values of one of the m elements of E, hence the number m^n i.e. m values n times. We can write this in base m as a number ranging from 0 to m^n - 1.

Let e and f be the 1-1 correspondences. Then create h, such that h(m^n - 1) = {f : f is function in (m^n-1) in base m}, where q <= m <= |E| and 1 <= n <= |F|. 

*Powerset : $|2^E| = 2^{|E|}$*

We can think of the powerset of E as the set of all functions from E to the set {0,1}. The result follows.

### Exercises

*The union of a finite set of finite sets is finite*

For n = 0, this is trivially true. 
For n = 1, this is obviously true as well.

Let this be true for n >= 1 sets, numbered $X_1, X_2,..,X_n$

For n+, let $X = \bigcup_{i=1}^{n} X_i$. $X_n$ is finite by induction hypothesis. $\bigcup_{i=1}^{n+} X_i = X + X_n$. We have proved union of two finite sets is finite.

*If E is a non-empty finite set of natural numbers, it has a largest element*

First : Given any two natural numbers, one of them is the largest number (duh!), or the two are equal and both are the largest.

Also, given any two natural numbers, the union of the two is the same as the largest of the two numbers.

We set m = U E. We want to show m is the largest number in E, if E is non-empty.

If n = 0, statement is true, vacuously.
If n = 1, statement is true, obviously.

Let this be true for n. 

Consider E with n+ natural numbers $x_1,x_2,..,x_n, x_{n+}$. Let $X = \bigcup_{i=1}^{n} x_i$ The X is the largest of $x_1,x_2,..,x_n$. And m = U E = X U $x_{n+}$ is a union of two numbers and is equal to the larger of the two. Also m is either in X (by induction hypothesis) or is the number $x_{n+}$ - in either case it is in E.

## Ordering, Choice and Zorn's Lemma

### Definitions related to Partial Order

*(strict) initial segment $s(a)$*: If X is a partially ordered set, and a is an element, then the set { x in X : x < a} is called the initial segment of X determined by a.

*weak initial segment $\bar{s}(a)$* : like the initial segment, but using the weak relation <=

*(strict) predecessors, successors, between* If x < y, x is a (strict) predecessor of y, y is a (strict) successor of x. If x < z < y, we say z is (strictly) between x and y. We can also use the weak equivalents explicitly.

*immediate successor / predecessor* When x < y, and there is no element strictly between x and y, we say x is an immediate predecessor of y, and y is an immediate successor of x.

*greatest (largest, last, maximum), least(smallest, first, minimum) element* : In a poset X, the unique element a such that a >= x for all x in X is the greatest element - it may not exist. Similarly for the least element.

*maximal, maximal element* : Any element a of a poset X, such that it has no strict successor is called maximal. One with no strict predecessor is called minimal. These may not exist, or there may be many elements of each type. 

*lower bound, upper bound* A lower bound of a subset E of a poset X is an element a of X such that a <= x for all x in X. A set E may have none, one or many lower or upper bounds, and they if they exist, they may or may not be in E. 

*infimum (inf, glb, greatest lower bound), supremum (sup, lub, least upper bound)* an infimum is a lower bound a of a subset E of X such that a is greater than any other lower bound of E. a may not be in E. If $E_*$ is the set of all lower bounds of E, then the inf a is the greatest element of $E_*$. Similarly, if $E^*$ is the set of all upper bounds of E, then the supremum is the least element of $E^*$,

### The Axiom of Choice

**Given a finite sequence of sets, a necessary and sufficient condition for the cartesian product to be empty is that one of them be empty**

Proof : TBD

**Axiom of Choice** : The cartesian product of a non-empty family of empty sets is non-empty.

More formally : If $\{X_i\}$ is a non-empty family of sets indexed by a non-empty set I, then there exists a family $\{x_i\}$, i in I, such that $x_i$ in $X_i$ for each i in I.

Given any collection C of non-empty sets, we can use C itself as the index set, with the identity mapping playing the role of indexing. The axiom of choice says the cartesian product of the sets of C has at least one element. Such an element can be considered a function f with domain C, whose value at each point is the element of C with that index i.e. if $A \in C$, then $f(A) \in A$.

**Choice function**

Given a set X, let P(X) be the power set of X. We can define, using the axiom of choice, a function f, such that given any subset of X in P(X), we can choose one element of that subset i.e f is function that allows us to arbitrarily choose one element of any subset of X when we want. 

**If a set is infinite, it has a subset equivalent to N**  

Let f be a function from $2^X - {\emptyset}$ to X, such that $f(A) \in A$ (choice function).

Let C be collection of all finite subsets of X. Since X is infinite, if A is in C, then X-A is not empty.

Let g be a function on C, such that $g(A) = A \cup f(X-A)$. 

By recursion theorem, we can define a function U, such that $U(0) = g(\emptyset)$, $U(n+) = g(U(n)) = U(n) \cup {f(X - U(n))}$

Let v(n) = f(X - U(n)). We want to show v is a one-to-one correspondence between N and a subset of X.

i) v(n) is not a member of U(n), for any n (by definition of v(n))  
ii) v(n) is in U(n+) for all n (by definition of U)  
iii) If n <= m, then $U(n) \subseteq U(m)$ (by induction : True for empty set, then if true for n, it is true for n+)  
iv) If n < m, $v(n) \neq v(m)$ : v(n) in U(m), but v(m) not in U(m).

Given that for any two natural numbers, one is strictly less than the other, the last statement proves this is a one-to-one correspondence.

**A set if infinite if and only if it is equivalent to a proper subset of itself**

From the previous result : let v(n) be a one-one correspondence from N to a subset X, and infinite set.

Let h(x) = v(n+) if x = v(n), h(x) = x, if x is not in range of v.

Then h is a one-one function, but it is not onto, because v(0) is not in range of h. Thus X is equivalent to a proper subset of itself.

### Exercises on AC

**Every relation includes a function with the same domain**

Proof : Let R be a relation from X to Y. Let D = dom R. If D is empty, then there is just one function from D to Y. Let f be a choice function on P(Y)

Then, we can define a function g : dom R -> Y, such that g(a) = f({b in Y : aRb}).

**If C' is a collection of pairwise disjoint non-empty sets, then there exists a set A such that $A \bigcap C$ is a singleton for each C in C'.**

Take the cartesian product, using C' as the index set. By AC, we have a family $A = {x_i}$ such that $x_i$ is in i for each i in C'. Now, consider $A \cap C$, where C is in C'. Clearly $x_C$ is in A. So the intersection is not empty. But for any j != i, $x_j$ belongs to some other D in C', and hence does not belong to C, since C and D are disjoint. Then the intersection is a singleton.

### Zorn's Lemma

If X is a partially ordered set such that every chain in X has an upper bound, then X has a maximal element.

Proof :

**Let S = collection of all weak initial segments of X**

For every element x of X, we can map it to its weak initial segment $\bar{s}(x)$. 

x <= y => $\bar{s}(x) \subset \bar{s}(y)$

We now convert our problem of finding a maximal value in X, to finding a maximal set in S, i.e. an initial segment which is not included in any other initial segment.

The hypothesis on chains (every chain in X has an upper bound), now becomes the hypothesis that every chain in S has an upper bound (now ordered by inclusion).

**Let CC = collection of all chains in X**

Every member of X is a subset of some  $\bar{s}(x)$ in S. If C is a chain in CC ( a chain of chains), the U C is in CC, since it is also a chain.

The hypothesis now changes : instead of saying each chain C has some upper bound in S, we can say that the union of the sets of C, which is an upper bound of C, is a member of X (i.e. is also a chain). 

We now have a nonempty collection of subsets CC of a non-empty set X with two properties : Every subset of each set is in X (including the empty set, which is a chain!), and the union of any chain of sets in X is in X (note that we are not talking of all unions, only of union of chains ordered by inclusion, which form a bigger chain). We have to show CC contains a maximal set.

**Choice function f, and growth function g**

Let f be a choice function on X.

We want a way to grow chains in CC slowly, one at a time. To do that we define a function g as follows :

For each chain A in CC, we define A' as the set of all x in X, such that A U {x} is also a chain (and hence in CC). 

define g on X as follows :

g(A) = A U f(A' - A) if A' - A is not empty
g(A) = A, otherwise.

We have to find all A's for which g(A) = A - these chains are maxed out!.

It turns out crucial to the proof that we can grow A by one element at a time.

**Towers and the smallest tower T0**

A tower is a subset T of CC such that :

i) the empty set is in T
ii) If A is in T, g(A) is in T
iii) If C is a chain in T, then U A in C is in T

We have at least one tower - CC itself.

Consider the collection of all towers of CC, and consider their intersection T0. T0 is a tower. 

**T0 and Comparability**

We define a set C in T0 to be comparable if for every set A in T0, C is either included in A, or vice versa. To prove T0 is a chain, we have to show every element in T0 is comparable. Note that comparable sets definitely exist - the empty set is one.

Consider any given comparable set C in T0.

Suppose A is in T0 and A is a proper subset of C. Then, g(A) must be a subset of C (this is like in natural numbers where we say if m < n, m must be in n). Because since C is comparable, either C is a proper subset of g(A) or g(A) is a subset of C. But in the former case we have at least two elements between A and g(A) which is not possible (the importance of growing A slowly).

Now consider a collection U of all sets A in T0 such that A is a subset of C, or g(C) is a subset of A. Our intention is to show that this more restricted set is in fact a tower. 

Clearly U contains the empty set, since it is a subset of C.

For the second condition : if A is in U, g(A) is in U:

i) A is proper subset of C - Then g(A) is a subset of C, hence it is in U
ii) A = C. Then g(A) = g(C) is a subset of g(C) and in U
iii) g(C) is a subset of A, then g(C) is also a subset of g(A) and hence g(A) is in U

Finally, for the third condition (the union of a chain in U belongs to U), this follows from the definition of U. Thus U is a tower. But U is a subset of the smallest tower T0, which means U = T0.

**T0 is a chain**

We have basically shown that if C is comparable, so is g(C). Given any C, for U as above. Then U = T0 means that if A is in T0, A is a subset of C, in which case A is a subset of g(C), or g(C) is a subset of A. Thus starting from the empty set, we can build up, using our trusted function g, a chain of comparable elements.

Consider the comparable sets in T0. The empty set is comparable. If A is comparable, so is g(A). And the union of a chain of comparable sets is obviously comparable, since it is in T0, since it is just the largest of the comparable sets. Thus the comparable sets in T0 form a tower i.e. they exhaust T0 - every set in T0 is a comparable. Thus T0 is a chain.

Since T0 is a chain, the union, say A, of all sets in T0 is itself a set in T0. But this means g(A) is a subset of A. This is only possible if g(A) = A. 

**Wrapping Up**

This means there is no x in X such that we can make the chain A bigger. Since A must be a maximal chain in CC. Since every chain in CC is a subset of some $\bar{s}(x)$ in S, there must be an a in X such that $A \subset \bar{s}(a)$. The chain A must contain a (otherwise g(A) != A). This a is unique, because if A belonged to some other $\bar{s}(y)$, this would imply a <= y, which would again mean g(A) != A.

So a is the unique element such that $A \subset \bar{s}(a)$, and is the promised maximal element.

https://terrytao.wordpress.com/2009/01/28/245b-notes-7-well-ordered-sets-ordinals-and-zorns-lemma-optional/

https://arxiv.org/pdf/1207.6698.pdf

### Exercises on Zorn's Lemma

**ZL is equivalent to AC**

Let X be a set, P(X) be the power set. Let {f} be a set of functions such that dom f is a subset of P(X), and $f(A) \in A$

Order all f by extension. This is a partial order. Is there an upper bound? Let C be a chain in {f}. U C is an upper bound and is in {f} - why? The primary question is uniqueness. Assume e = (A,a) is in UC. Then this must be unique. If not, the (A,b) would be in UC, and there would be two functions in the chain neither of which would include the other, which is not possible. Hence, U C is a function and hence an upper bound of C. Thus every chain is bounded above. Hence there must be a maximal element, say, f. dom f = P(X) - {$\emptyset$}. If not, then let A be a non-empty element of P(X). Then there are |A| functions which extend f which contradicts the statement that f is maximal. Thus dom f = P(X) - {$\emptyset$}

AC was used to prove ZL earlier. So the two are equivalent.

**(HMP) Every partially ordered set has a maximal chain / In every partially ordered set, every chain is contained in a maximal chain**

ZL => HMP. Consider the set C of all chains of the (non-empty) poset X. C is ordered by inclusion, and every chain in C is a chain in X. A maximal element in C would be a maximal chain in X. Now consider a chain in C. Take the union. Given any 2 elements of the union a and b, either a < b, a = b, or a > b. Thus this union is in C and an upper bound of the chain in C. Hence every chain in C has an upper bound => C has a maximal element => X has a maximal chain. Note that this does not mean it has a maximal element. 

HMP => ZL. Every partially ordered set X has a maximal chain. By hypothesis of ZL, every chain is bounded above => the maximal chain is bounded above - let A be such a maximal chain, with a as an upper bound. Then i) a is in A ii) For every s in a, s <= a iii) There is no z in X such that a <= z otherwise A would not be maximal. Hence a is a maximal element.

Following on from this, given any poset P with a chain C, we have shown in the first part of the proof above that C must be contained in a maximal chain.

## Well-Ordering

A partially ordered set may not have a smallest element, or some subset may not have one. A well-ordered set is one where every subset has a smallest element.

In particular, every well-ordered set has a least element.

**Principle of transfinite induction**

Suppose S is a subset of a well-ordered set X, and suppose whenever an initial segment of x in X is a subset of S, then x is in S. Then S = X.

Note: For the least element e, initial segment of e = $\emptyset$, which is included in S, so e is in S.

Proof : Assume X - S is not empty, let x be the least element. Then initial segment is in S => x is in S - a contradiction.

**Comparison with Principle of Mathematical induction**

The principle of mathematical induction discussed for natural numbers goes from a predecessor of an element to itself. The principle of transfinite induction flows from the set of all predecessors to the element. In the set of natural numbers every number has an immediate predecessor ... this is not true of all well-ordered sets.

Assume S is a set, 0 is in S, if n is in S, then n+ is in S. Let m < n+. Then m <= n => m is in n. 

**continuation**

A well ordered set A is a continuation of B if B is an initial segment of some element of A, and has the same ordering.

In a well ordered set with two elements a and b, such that a > b, s(a) is a continuation of s(b), and X itself is a continuation of both s(a) and s(b). The set of initial segments of X are totally ordered by continuation. 

**Theorem**: The union of a chain C of well-ordered sets ordered by continuation has a unique well-ordering such that U is a continuation of each set distinct from U in the collection C.

Proof: If a and b belong to U, a < b, then there must be a set which contains both a and b. Indeed any set which contains b, must contain a, otherwise C would not be a chain. Also since C is a chain by continuation, the order has to be same in every set containing A and B. Similarly, if a < b, and b < c, same arguments cover a and c, hence the result is transitive. Finally, given a and b, either a < b, or b < a, or a = b as there has to be an set in C containing both, and each set in C is well ordered. 

Is U C a well-ordered set? Any non-empty subset of U has a non-empty intersection with some element of C, say W. Note that if a is any element of U in the intersection, all elements of U < a are also in the intersection because C is a chain by continuation. Thus the smallest element of U is the smallest element of the intersection. Now, this smallest element exists, because W is well ordered. Hence every subset of U C has a smallest element and U C is well-ordered.

**Exercise** Prove every totally ordered set X has a co-final well ordered subset.

Let Z be the set of all well-ordered subsets of X. Z is not empty - the empty set is a member. Order these subsets by continuation. Any chain in this set is bounded, because the union of the chain is itself well ordered subset of C. Hence, by Zorn's Lemma, there is a maximal well-ordered element of Z. Supposing there is an element x, such that for every a in the maximal set, a <= x, but x is not in Z. Then we can extend the chain, contradicting the conclusion that it is maximal. Hence this maximal well-ordered subset is cofinal.

**Well Ordering Theorem** Every set can be well ordered.

Proof : In an argument similar to above, consider a set Z of well ordered subsets of X - each element of Z is a subset of X with a well-order on it.

We order these subsets by continuation - this is a partial order. Then any chain in Z is bounded above. Hence, by Zorn's Lemma has a maximal element M, which is well ordered. Assume there is an element of x of X not in M. Then, we can define a new element N = M U {x}, with m <= x for all m in M. N is a well ordered set because M is well ordered, and it is a subset of X. Thus, we have a contradiction i.e. there is no element of X not in M => M = X.

**Exercise**

**A totally ordered set is well ordered iff strict predecessors of each element are well ordered.**

Let X be totally ordered. Assume strict preds of each element are well ordered. Take any non-empty subset A of X. If a is an element of A, then all predecessors of a in A will form a subset of the set of all predecessors of A, and hence will have a smallest element. This will also be the smallest element of a, unless a is itself the smallest element of A. In either case A has a smallest element. Hence, X is well ordered.

Assume X is a totally ordered set where there these exists an element x of X whose predecessors are not well ordered. Then there is a (non-empty) subset of these predecessors which has no smallest element => there is a non-empty subset of X with no smallest element => X is not well ordered.

**Well-Ordering => AC**

We already showed ZL => WO. Now we show that WO => AC and hence ZL. Let X = cross of product of non-empty sets Xi. Order X by well ordering, choose the smallest element.

**Every partial order can be extended to a total order**

X is a set, R is a partial order. We want to create T, a total order, such that $R \subset T$. Take the set of all partial orders on X, (X,S), such that $R \subset S$. This is a partial order. Since every chain has an upper bound, by Zorn's Lemma has a maximal element. This maximal element must be a total order. If not, let there be two elements x and y which are not related - we can create a larger set creating a contradiction. Hence this must be a total order.

https://math.stackexchange.com/questions/271003/every-partial-order-can-be-extended-to-a-linear-ordering

## Transfinite Recursion

Let W be a well ordered set, a an element of W, X is any set. Let f be a function from the s(a) of a to X. We call f a sequence of type a in X - an example is to take a function U from W to X, and restrict it to s(a).

A sequence function of type W in X is a function f from the set of all sequences of type a for all a in W, to X. In effect f allows us to lengthen the sequence by one more element.

**Transfinite Recursion Theorem** If W is a well ordered set, and if f is sequence function of type W in X, then there is a unique function U from W into X such that U(a) = f(U|s(a)) for each a in W. 

Unlike normal recursion, we are considering a function from all predecessors, and not the immediate predecessor, which may not exist. Definition by transfinite induction 

Proof :

(uniqueness of U) : Assume there is a function Q. Let S be the set of all elements a of W such that U(a) = Q(a). S is not empty : the empty set is a member. Assume W - S is not empty, let x be the smallest element. Then s(a) is in S. Thus Q|s(a) = U|s(a). Hence Q(a) = U(a) => a is in S. Contradiction.

(existence) Let an f-closed subset A of W x X be such that : Given an element a in W, if there is a sequence of type a (t) included in A, then (a,f(t)) is included in A. We consider all f-closed subsets of WxX (this is not empty since WxX is itself such a subset). Let U be an intersection of all such subsets. 

U is f-closed (else find an a where condition is not true). We have to show U is a function. 

Let S be the of all c of W where (c,x) in U for at most one x. Assume there is an a such that s(a) included in S => there is a sequence of type t, such that $t \subset U$ => (a,f(t)) is in U. Assume there is an a such that s(a) included in S, but there is an (a, y) in U, such that y != f(t). Then U - {a,y} is f-closed, which contradicts the assumption U is the smallest f-closed set.

In the above, the empty set is included because the initial segment of the empty set is the empty set and hence included in S.

**Similar Sets** Two posets A and B are similar $A \simeq B$ if there is an order preserving one-to-one correspondence between them (order isomorphism).

Thus, if f is a function from X to Y, such that f(a) <= f(b) (in Y) iff a <= b (in X), then A and B are said to be similar, and f is called a similarity. Note similarities in general are not unique - we shall show that similarity between well ordered sets are unique.

Simple conclusions

**similarity preserves <**

If a <= b, and a != b => a < b. We have to show f(a) < f(b). Obviously, f(a) <= f(b). If f(a) = f(b), then f is not one-one.

If f(a) < f(b) => a <= b. If a = b, then f would not be a function.

**inverse of similarity is a similarity**  
**composition of similarities is a similarity**  

**Comparability Theorem:If f is a similarity from a well ordered set W to a proper subset of itself, then for each a in W, a <= f(a)**

Proof : Let S be the set of all elements of W for which a <= f(a). If W-S is not empty, let x be the least element. Then x > f(x). Since f is order preserving, f(x) > f(f(x)).

But, since x > f(x) this implies f(x) is in S => f(x) <= f(f(x)), a contradiction.

**If 2 well ordered sets are similar, then the similarity is unique**

Let f and g be the similarities from well ordered sets X to Y. Let h = $g^{-1}f$ => this is a similarity from X to itself. Then a <= $g^{-1}f(a)$ for all a. Thus g(a) <= f(a) for all a, and vice versa, by symmetry. Hence f(a) = g(a).

**A well ordered set is never similar to one of its initial segments**

Let X be similar to s(a), by similarity f. Then a > f(a), which violates theorem that a <= f(a) for any similarity from a well ordered set to a proper subset.

**For any two well ordered sets, either they are similar, or one is similar to a subset of the other**

Assume X and Y are non-empty well ordered sets, such that neither is similar to a subset of the other. 

For any $a \in X$, and t is a function from s(a) into Y. Let f be a function such that f(t) is the least of the proper upper bounds of the range of t in Y, if one exists, else let f(t) = smallest element of Y. f is a sequence function of type X in Y. Let U be the corresponding function (so that U(a) = f(U|s(a))). 

Let S be the a, such that for U|s(a) is a one to one correspondence from s(a) to the initial segment of U(a). We know S is not empty since the smallest element of X is mapped to the smallest element in U. Let a be such that s(a) is in S. By definition U(a) = f(U|s(a)) = least upper bound of range of U|s(a). Since s(a) cannot be all of Y, Y = U|s(a) must be non-empty with a least element b. For any element b' in U|s(a), b' < b (otherwise ... $U^{-1}(b')$ will not have its initial segment in U|s(b)). But this implies s(b) = U|s(a). Since U(a) = b, then a is also in S.

## Ordinal Numbers - Counting Beyond Natural Numbers

How do we count beyond the natural numbers? $\omega = N$ itself is the first step. What about $\omega^+$ - the successor? And its successor and so on. Remember $\omega+ = \omega \bigcup \{w\}$

For each natural number we can define a function f as follows : f(0) = $\omega$. f($m^+$) = $(f(m))^+$ for m < n. This is a function from n -> a set F(n) which is made up of $\omega,\omega+1,\omega+2$ and so on. Note that we are using F(n) = range of f. 

We can now quite easily create a function Q on N itself, such Q(n) = F(n) for each n in N. Though this is a little obscure, in fact this is not possible using the existing axioms of set formation - we need a new axiom.

**Axiom of Substitution** Let S(a,b) is a statement we can make about each a in some set A, so that the set {b : S(a,b)} can be formed. Then we can define a function F with domain A, such that F(a) = {b: S(a,b)}.

This is called the axiom of substitution because we have create a new set of {b}'s, by substiuting these {b}'s for each a in A. The fact that we can do this procedure is in effect the axiom of substitution.

We can use the axiom of substitution to define **ordinal numbers**. An ordinal number is a well ordered set which has the additional property that each element of the set is equal to its initial segment i.e. e = s(e) for each e in the ordinal number. Thus every element of the ordinal number is also a subset of the ordinal number.

We have already shown all natural numbers are ordinal numbers. Now, by this new definition, N (a.k.a. $\omega$) is also an ordinal. In fact, if a is an ordinal, so is the set $a^+ = a \cup {a}$ (proof : every element is either a, or an element of a. Given a is an ordinal, the result follows). We can therefore confidently proceed beyond $\omega^+$ and further. How far?

We now bring in the axiom of substitution. Coming to our function earlier on N, we can define, using the axion of substitution, a function F with domain N, such that F(n) = {x : x is in range of f(n)}. The important thing here is the range of F. 

The set $\omega2 = \omega \cup range (F)$ is an ordinal
Proof : TBD
One way : We know this is true upto omega. Now prove for w+1 to ... by induction. Order is defined by a < b if $a \in b$. By definition, every element contains its initial segment. We have to show that every element is equal to its initial segment. Let S be the natural numbers n for which it is true that $\omega + n$ is equal to its initial segment. Then 0 is in S (by definition of $\omega$). If n is in S, then $\omega+n$ is equal to its initial segment. $\omega + n+ = (\omega + n) \cup \{\omega + n\}$. The main thing to verify is that every element is in $\omega2$. For this we see that every element of $\omega + n+$ is its predecessor or belongs to the initial segment of its predecessor. These are all elements of $\omega2$. By definition then, $\omega + n+$ is equal to its initial segment and n belongs to S. This implies that ran(F) meets the criteria for an ordinal. And of course, all elements of $\omega$ are already ordinals. So $\omega2$ is an ordinal.

**An order (partial or total) is determined by its initial segments**

Proof : To prove : If A is a poset, a <= b in A <=> s(a) $\subseteq$ s(b) in S, the set of initial segments (proper subset). 

This follows immediately from the reflexivity, transitivity and anti-symmetric properties of partial orders. 

**If a well ordered set is an ordinal number, there is only one possible ordering**

Since each set is equal to its initial segment, the set is itself a collection of initial segments and hence induces a specific order.

**Every element of an ordinal number is a subset of that ordinal number**

By definition.

**Every element of an ordinal number is an ordinal number, or every initial segment of an ordinal number is an ordinal number**

If e is an element, then it is a subset of the ordinal number and hence every element b of e is itself equal to its initial segment. But b is a subset of e, because if c in b => c < b => c < e => c is in e. Hence every element of e contains its initial segment in e. And of course, being a subset of a well ordered set, e is well ordered, so e is an ordinal.

The statement is even more immediate : the initial segment of an ordinal number has several elements, each of which are the same as their initial segments, and this segment is well ordered => it is an ordinal. 

**Two similar ordinal numbers are the same**

Let f be the similarity from a to b, both ordinal numbers. Write S = {e : f(e) = e}. 

For any element e in a, e is the "lub" of s(e), and since f is a similarity, f(e) is the "lub" of the image of s(e). If s(e) $\subset$ S, then f(e) and e have the same initial segments, and hence e = f(e) i.e e is also in S.

**Either two ordinals are similar, or one is similar to an initial segment of the other.**

This follows since ordinals are well ordered sets.

**If an ordinal number b is similar to an initial segment of ordinal number a, then b < a, b $\in$ a, b $\subset$ a, and a is a continuation of b**

**Every set of ordinal numbers is well ordered**

If E is a non-empty set of ordinals. Let a be an element of E. If a <= than all elements of E, then we have shown E is well ordered. Otherwise there must be an element b of E such that b < a => $b \in a$ => $a \cap E$ is not empty. Since a is an ordinal and is well ordered, the intersection must have a least element say a0. a0 is the least element of E since any element of E less than a belongs to the intersection, and hence the least of these is the least element of E.

**finite ordinals - natural numbers, transfinite ordinals - not finite, limit ordinals - no immediate predecessor**

**Every collection of ordinal numbers has an unique supremum**

Let C be such a collection. C is totally ordered by continuation.

Let a be the union of C. a is well ordered, since it is the union of a chain of well ordered sets ordered by continuation (we have proved this earlier).

For every element e of a, distinct from a, s(e) and e are both in a. e has to be in a because if not, then e would be = a. Thus a is an ordinal number.

Thus a is an upper bound. If b is another upper bound of C, then $a \subset b$ => a is least upper bound of C.

**Burali-Forti Paradox : There is no set of all ordinals**

If there was - take the supremum. This is an ordinal, greater than or equal to every ordinal. But given an ordinal a, i can always find a greater one, hence there is no set of all ordinals.

**Counting Theorem: Every well-ordered set is similar to some ordinal number**

Uniqueness is obvious since two similar ordinal numbers are the same.

*In a well ordered set, if for an element a, every element of s(a) is similar to an ordinal, then s(a) itself is similar to an ordinal* : 

Let X be a well ordered set. Let a be an element of X, such that for each x in s(a), x is similar to an ordinal. Let S(x,b) be the statement : b is an ordinal number, and $s(x) \simeq b$, where x is in a.

The { b: S(x,b) is true} exists and is non-empty (it will be a singleton). Then, by axiom of substitution, there is a function F with domain s(a), such that f(a') = {b ; S(a',b)} is true. ran(F) is a (well-ordered) collection of ordinals.

Let x be in s(a), such that $s(x) \simeq b$. Then all initial segments of s(x) are similar to initial segments of b. But the initial segments of b are in fact elements of b => these are also elements of ran(F). Thus b is a subset of ran(F). This implies that ran(F) is an ordinal. F then is a similarity and s(a) is similar to an ordinal.

*In a well ordered set, every initial segment is similar to an ordinal*

Let S be the set of all elements of X whose initial segments are similar to an ordinal. If X - S is not empty, let a be the smallest element. Then $s(a) \subset S$, and each element in s(a) is similar to an ordinal, and hence, by the result above, s(a) itself is similar to an ordinal. Thus a is in S. Thus X = S i.e. every initial segment of X is itself similar to an ordinal. 

*In a well ordered set, if every initial segment is similar to an ordinal, then the set itself is similar to an ordinal*

Let X be a well ordered set. As proved, each of X's initial segments are similar to an ordinal. Let T(x,b) be the statement : b is an ordinal number, and $s(x) \simeq b$, where x is in X. Then, by axiom of substitution, we can form a function H with domain X, such that H(a) = {b : T(x,b)}. Since all initial segments of X are similar to ran(H), it follows that every element of b is in ran(H), and hence ran(H) is itself an ordinal. But then X is similar to an ordinal.

## Ordinal Numbers

For a well ordered set X, let ord X be the unique ordinal similar to X. 

Let A and B be disjoint well ordered sets, with ord A = a, and ord B = b. Then C = A U B is called the ordinal sum of A and B. Let ord C = c. 

Note: To derive the ordering on C, we can assume that any element of B is greater than any element of A. We can extend this to infinite unions also. Also, even if A,B are not disjoint, we can create equivalent disjoint sets, by creating (x,0) for each x in A, and (x,1) for each x in B and then taking the union.

We then define a + b = c.

Properties:
a + 0 = a, 0 + a = a  
a + 1 = $a^+$
a + (b + c) = (a + b) + c

Commutativity fails in general:

$1 + \omega = \omega, \omega + 1 = \omega^+$. In general, tacking something to the beginning of an infinite well ordered set does not change the structure of the ordering. 

The ordinal product of two sets A and B can similarly be defined as the set C = A x B, with ordering in reverse lexicographic order i.e. given (a1,b1) and (a2, b2) in A x B, if b1 != b2, use the order in B, else use the order in A.

ab = c

a0 = 0a = 0  
a1 = 1a = a
a(bc) = (ab)c
a(b + c) = ab + ac (left distributive law)

But again, commutativity fails, and right distributive law fails in general.

$2\omega = \omega \neq \omega2$

$(1 + 1)\omega = 2\omega = \omega$, but $1.\omega + 1.\omega = \omega + \omega = \omega2$

Similarly, exponentiation can de dealt with.

$0^a = 0, a >= 1$

$1^b = 1$

$a^{b+c} = a^b.a^c$

$a^{bc} = (a^b)^c$

But,

$(ab)^c$ is not, in general equal to $a^cb^c$. E.g. $(2.2)^\omega = 4^\omega = \omega$, but $2^\omega.2^\omega = \omega.\omega = \omega^2$

# Cardinality - The Size of Sets

The purpose of counting is to compare the size of one set with another. It turns out that while ordinal numbers are useful step, they are not quite the right measure of the size. This is because while any set can be well ordered, we can well-order the same set in different ways. For example, we could order the natural numbers so that every odd number is greater than every even number - this will be the ordinal $\omega2$.

To get a correct measure of size, we turn to the theory of cardinal numbers. The problem is to compare the sizes of sets without worrying about any specific order. The key concept in order was similarity. The key concept in comparing size is equivalence. Recall that two sets A and B are said to be equivalent ($A \sim B$), if there is a one-to-one correspondence between them.

If X is equivalent to a subset of Y, we say Y dominates X. Consider the relation of "dominates" in the power set of some set E. Question : Is this a partial order? Reflexivity is obvious. Transitivity is obvious as well. What about anti-symmetry? This is obviously not true i.e if x dominates y, and y dominates x, we cannot say x = y. But we can say something else :

**Shroeder-Bernstein Theorem** If X is equivalent to a subset of Y, and Y is equivalent to a subset of X, then X and Y are equivalent.

The converse is obvious.

Let f be a 1-1 mapping from X to Y, and g from Y to X. Assume X and Y are disjoint (if not true we can do some jugglery to make it true)

We say x in X is a parent of f(x) in Y, and vice versa y in Y is a parent of g(y) in X. Then, we get a sequence of descendents f(x), g(f(x)) and so on, as well as g(y), f(g(y)) and so on. Each term is an ancestor of all subsequent terms.

If we keep tracing the ancestors, we have three cases : we have an element in X with no parent in Y - this is a member of X - g(Y). Or we hit an element in Y - f(X). Else, we have a regression. Let $X_X$ be elements of X which originate in X (i.e. X-g(Y) together with all descendents in X). Let $X_Y$ be elements of X originating in Y (all descendents of Y - f(X)), $X_{\infty}$ be all with no parentless ancestor. Similary we have $Y_Y, Y_X, Y_{\infty}$.

$f|X_X$ is a one-to-one map from $X_X$ to $Y_X$. $g^{-1}|Y_Y$ is a one-to-one map from $X_Y$ to $Y_Y$. And $f|X_{\infty}$ is a one-to-one map from $X_{\infty}$ to $Y_{\infty}$. Together, they form a one-to-one correspondence from X to Y.

*Exercise - Alternate Proof* 

Let f and g be the one-to-one functions between X and Y.

G = { x $\in g(Y) : g^{-1}(x) \in Y - f(X)$}

Let 

h(x) = $g^-1(x)$ when $x \in G$  
h(x) = $f(x) when $x \in X - G$

domain of h is X, because (X-G) U G = X, and $g^{-1}(x)$ is always defined in G.

h is one-one (injective): Suppose a,b in X are such that h(a) = h(b). Then a,b cannot both be in G or X - G, since both g and f are one-one. So, assume a is in G, and b is in X - G, without loss of generality. Then, h(a) is in Y - f(x), while h(b) is in f(X), implying that h(a) != h(b) - a contradiction. Hence h is one-one.

h is surjective : ran(h) = Y - f(X) U f(X) = Y.

**Comparability Theorem** Given any two sets X and Y, either X dominates Y, or Y dominates X, or they are equivalent.

Proof: Well order both sets : There is a similarity from one to an initial segment of the other, or vice versa, or both. If both, the two sets are equivalent. Else one dominates the other (strictly).

## Countable Sets

$|X| < |Y|$ if X is equivalent to a subset of Y, and not vice versa.

**Finite and Infinite Sets**

X is finite, if $|X| = n$, where n is some natural number.

If |X| < |Y| and Y is finite, X is finite.

$\omega$ is finite. Also, if X is infinite, $\omega \leq |X|$.

A set X is finite if and only if |X| < $|\omega|$
Proof: $|X| = n < \omega$, where n is some natural number. Since n is strictly less than omega, |X| < $\omega$, because equality would imply n < |X|, which is not possible.

Conversely, if |X| < $\omega$, X is finite.
Proof: Else $\omega <= |X|$, which would imply $\omega < \omega$, which is absurd

*Countable* X => |X| <= $\omega$  
*Countably infinite* |X| = $\omega$  

**Facts about Countable Sets**

*Every subset of $\omega$ is countable*  
Proof: Clearly, the identity mapping from the subset shows that for any subset X of $\omega$, |X| <= $\omega$

*Every subset of a countable set is countable*  
Proof: Let X be countable. Then, for any subset A of X, |A| <= X, and |X| <= $\omega$. So |A| <= $\omega$

*If f is function from $\omega$ onto a set X, X is countable*  
Proof: If x is in X, $f^{-1}({x})$ is not empty. Using AC, we can choose from each of these sets, a value, and this will be a function g(x) from X to $\omega$. Since f is onto, g is one-one. Thus |X| <= $\omega$.

*X is countable iff there is a function from some countable set onto X*
Proof: If has been proven in previous section. Note also that if X is countable, then X <= $\omega$ => there is a one-one function f from X to $\omega$. We can then construct a function g from $\omega$ to x, such that for ran f, g(x) = $f^{-1}(x)$ and for the rest, we pick any arbitrary value in X. This implies that g is a function onto X. We are assuming X is non-empty.

*If Y is any particular countably infinite set, then any non-empty set X is countable iff there is a function from Y onto X*
Proof: |X| <= $\omega$ = |Y|

*If X and Y are two countable sets, their union is countable. In fact, a union of a finite number of countable sets is countable*

First: for 2 sets. We can create 2 countable sets from $\omega$, the even numbers E and the odd numbers O. We have a one-one mapping from X to E, and Y to O, which is in effect a one-one mapping from X U Y to $\omega$, after some jugglery => |X U Y| <= $\omega$.

By induction, we can now show a union of a finite number of countable sets is countable.

*There exist a pairwise disjoint family {$A_n$} of infinite subsets of $\omega$ whose union is $\omega$, where n is a natural number*

Let A0 = {0} U {odd numbers}
A1 = {odd numbers} * 2 = {2,6,10,14,...}
A2 = {4,12,20,28,...}
A3 = {8,24,40,56,...}
A4 = {16,48,80,112,..}

In other words,

Am = {x $\in$ N | x = $(2^m)$(2n + 1)}, where m >= 2, n = 0,1,2..
Each number is $A^m$ is not divisible by $2^{m+1}$ or above.

Alternatively : diagonalize

0 1 3 6 10 ..  
2 4 7 11 ..  
5 8 12 ..  
9 13 ..  
14 ..  

Clearly, these sets are pairwise disjoint but their union is omega.

*Union of a countably infinite family of countable sets is countable*

Let {$X_n$}, $n \in \omega$ be a family of countable sets. Find {$f_n$}, a family of functions from each of $A_n$ onto the respective $X_n$, where {$A_n$} are a partion of $\omega$.

Now, we can define a function f from $\omega$ onto $\bigcup_n X_n$ by saying f(k) = $f_n(k)$, when $k \in A_n$.

This implies the union is countable.

*A cartesian product of two countable sets is countable. A cartesian product of any finite number of countable sets is countable. But a cartesian product of a countably infinite number of countable sets may not be countable*

X $\times$ Y = $\bigcup_{y \in Y} (X \times \{y\})$ is a union of a countable number of countable sets, hence countable.

Using induction, we can easily show this is true for any finite number of sets.

But a simple set such as $\times_{i \in \omega} \{0,1\}$ is not countable - this is equivalent to the power set of $\omega$, as can be seen next.

**Every set is strictly dominated by its power set, or, in other words, |X| < |P(X)| for all X**
Proof: From X to P(X) we have a natural one-one mapping of each element to the corresponding singleton. Thus |X| <= P(X).

Assume f is a one-one mapping from X onto P(X) - we want to show this is not possible. Let A = { x $\in$ X: x $\notin$ f(x)}. In other words A is the set of all elements of X which are not in the set they are mapped to - this could be the empty set. A is in P(X). Since f maps X onto P(X), there must be some a for which f(a) = A. Is a in A? If not, then a is in A, else if a is in A, then a is not in A!

P(X) is equivalent to $2^X$ where $2^X$ is the set of all functions from X into 2 => X < $2^X$ for all X.

Since $\omega < 2^\omega$, this implies the set of all sets of natural numbers is uncountable. 

*Note that for ordinal exponentiation $2^\omega$ is countable - so the meaning is different.*

Also, $\times_{i \in \omega} \{0,1\}$ is equivalent to $2^\omega$, which shows it is uncountable.

## Cardinal Arithmetic

We want to associate a cardinal number, card X, with each set X, with an ordering which matches the expected ordering of size of the sets.

**Sum**

If A,B are disjoint sets, with card A = a, and card B = b, then a + b = card (A $\cup$ B). This is commutative, associative as follows from the facts about unions.

Exercise: Prove a <= b, c <= d => a + c <= b + d
Proof. Take corresponding sets A,B,C,D. f be a 1-1 function from A to B, and g from C to D. We can from h from A U C to B U D. 

Even for infinitely many summands :

$\Sigma_i a_i = card(U_i A_i)$

**Product**

ab = card(A $\times$ B)

Commutative, associative, multiplication distributes over addition.

Exercise: a <= b, c <= d => AC <= bd
Proof:f is a 1-1 from A to B, g from C to D. Let h(x,y) = (f(x), g(y)). h(x,y) is a 1-1 from A x C, to B x D.

For infinitely many elements :

$\prod_i a_i = card(\times_i A_i)$

**Exponents**

$a^b = card(\prod_{i \in I} a_i)$, where card(I) = b, and $a_i = a$

$a^{b+c} = a^ba^c$  
$(ab)^c = a^cb^c$  
$a^{bc} = (a^b)^c$

**Infinite sets**

*If a and b are cardinal numbers, a finite, b infinite, then :
a + b = b*
Proof: Take A and B, A finite, B infinite, A and B disjoint. Form a mapping g from $\omega$ into B, and f from k to A, where k is a finite number. Then we can form h, a 1-1 correspondence from $\omega$ to A U ran(g) , such that h(n) = f(n) if n < k, h(n+k) = g(n). 

We can use this to form a 1-1 correspondence from A U ran(g) to ran(g). Coupled with the identity map on B - ran(G), we get a 1-1 correspondence from A U B to B.

*If a is infinite, then a + a = a*
Proof: Let A be a set of cardinality A. Let F be a collection of all functions f, such that domain is of form X x 2, for some subset X of A, and such that f is a 1-1 correspondence between X x 2 and X. If X is countably infinite, the X x 2 is equivalent to X => collection F is not empty.

Consider a chain in F ordered by extension. The union of the chain is also a member of F i.e. each chain is bounded. By Zorn's lemma we have a maximal element f, with ran f = M, say.

Assertion : A - M is finite. If not, it would have a countably infinite set, say Y. We could combine f with a 1-1 correspondence between Y x 2 and Y and get a strict extension of f, contradicting supposed maximality.

Thus card M + card M = card M, and since card A = card M + card(A-M) = card M, we get card(A) + card(A) = card(A).

*If a and b are cardinal numbers with at least one infinite, and c is the larger of a and b, then a + b = c*
Proof: Let card A = a, card B = b. Since a <= c, b <= c, it follows that a + b <= c + c. Also c <= card (A U B) = a + b. Thus a + b = c.

*If a is an infinite cardinal number, a.a = a*
Proof: Similar to the addition proof above, we can show that (card M)(card M) = (card M).

Assume card M < card A. Since card A is equal to the larger one of card M and card (A - M), this implies card A = card (A - M). This implies A-M has a subset Y equivalent to M, and of course Y and M are disjoint. Now (M U Y) x (M U Y) = union of MxM,MxY,YxM and YxY. Each is equivalent to M x M and hence to M, and hence to Y, it follows that we can create a 1-1 correspondence between the union of MxY,YxM and YxY and Y. Thus we can extend f, which is a mapping of MxM to M, to a mapping from (MUY) x (MUY) to M U Y. 

Exercise: 
*Prove if a,b are cardinal numbers, one of which is infinite, a + b = ab*
Proof: Assume a,b are non-zero. Let c be larger of a and b. Then a + b = c, if one is infinite. Now a <= c and b <= c. Thus ab <= c.c = c (as proved above). But c <= ab, because at least one of a,b is equal to c. Thus ab = c.

*If a and b are cardinal numbers, a infinite, b finite, $a^b = a$*
Proof: Assume b is not 0.
We know $a^1 = a$. If this is true for n, then for n+1, we can see that $a^{n+1} = a^n.a = a.a = a$

## Cardinal Numbers

*The set of all ordinal numbers equal to a set, form a set*

Let X be any set. Let x be any ordinal equivalent to X.

Consider P(X). P(X) is equivalent to some ordinal number, say p. Then X is strictly dominated by p i.e. card X < card p => x < p => $x \in p$. Thus the set of all ordinals equal to X is a subset of the ordinal number p.

**Cardinal Number** The cardinal number is an ordinal number a such that if b is an ordinal number equal to a (i.e. card a = card b), then a <= b - these are called initial numbers.

Then card X = least ordinal number equivalent to X.

*Each infinite cardinal number is a limit number*

If not, the p be the immediate predecessor of a cardinal number m. p < m. Note that since m is infinite, it is always equivalent to some subset. We can then create a function from p onto this subset. Thus p <= m, and card p = card m, which is a contradiction.

*card X = card Y, iff X is equivalent to Y*

Both X and Y are equivalent to card X => they are equivalent

If X and Y are equivalent, it follows card X <= card Y, and also card Y <= card X, thus implying card X = card Y.

*Every finite set is only equivalent to one ordinal*

*For a set A with card(A) = a, card P(A) = $2^a$*

*cardinal numbers are ordered in the same way ordinals are ordered*

*a < $2^a$, for all cardinal numbers a*  
Proof: If A is a set with cardinal number a, A is dominated by P(A), hence a < $2^a$

Exercise: 
i) If card A = a, what is cardinal number of all 1-1 mappings of A onto itself? 
Ans: all 1-1 mappings : a(a-1)...1 = a!.

ii) Cardinal number of the set of all countably infinite subsets of A
Clearly, this is between A and P(A). 
Proof: If a is finite, this is zero obviously.
If A is countably infinite, then |A| = $\omega$. A will have no uncountably infinite subsets, but we know |P(A)| = $2^\omega$. Now we know that for any finite subset X of A, A-X is countably infinite. If separate the finite and infinite subsets of A, then card(finite subsets of A) <= card(infinite subsets of A). But the sum of the two is the cardinality of P(A). We have proved earlier that for infinite cardinals a + b = c, where c is the larger of the two. Thus card(infinite subsets of A) = card(P(A)) = $2^\omega$.
What about larger sets? If A is uncountably infinite then how may countably infinite subsets does it have?

*Any 2 cardinal numbers are comparable*
Because they are ordinal numbers

*Any set of cardinal numbers is well ordered*
Because they are ordinal numbers

*Any set of cardinal numbers has a supremeum*
Because they are ordinal numbers

*Given any set of cardinal numbers, there is one strictly greater. Hence there is no largest cardinal number, or there is no set of all cardinal numbers (Cantor's Paradox)*
Because given a, we can form $2^a$.

Exercise: Prove is a and b are ordinal numbers, then card(a + b) = card a + card b. card(ab) = (card a)(card b).
Proof: We have defined the ordinal sum : a + b, as the ordinal which is similar (has a 1-1 correspondence with) A U B, where ord(A) = a, ord(B) = b, and A and B are disjoint. Thus the ordinal a + b has the same cardinality as A U B. 

Thus, card(a + b) = card(A U B) = card(A) + card(B) = card(a) + card(b), since A and B are individually similar to ordinals a and b respectively.

Similar, card(ab) = card(A x B) = card(A).card(B) = card(a).card(b)

### Alephs

$\aleph_0 = \omega$ : smallest transfinite ordinal number. This number has all of its initial segments as finite.

The smallest uncountable ordinal number then has all of its initial segments countable - this is often called $\Omega$. In its cardinal role, we call it aleph-1 :

$\aleph_1 = \Omega$: smallest uncountable ordinal number

What is the relation between the two? We know $\aleph_1$ is the smallest ordinal number strictly greater to $\aleph_0$, or the immediate successor of $\aleph_0$ in the ordering of cardinal numbers.
We also know $2^{\aleph_0}$ is greater than $\aleph_0$. So $\aleph_1 <= 2^{\aleph_0}$. 

**Continuum Hypothesis** $\aleph_1 = 2^{\aleph_0}$

We know from the works of Godel and Cohen that this can neither be proved not disproved within the existing axioms of set theory.

The generalized hypothesis says that this is true for each sucessive infinite cardinal number.

# Other topics to cover

## Development of N,Z,Q,R,C

## Boolean Algebra of Sets

## Limits of Sequences of Sets

## Rings and Fields of Sets, including sigma-rings and fields

## Borel Sets

## Measures

# Enderton - Elements of Set Theory

Chapter 4. Natural Numbers

Chapter 5. Construction of the Real Numbers

















# Joy of Sets by Keith Devlin

## notation
$\in$ element of / member of
$\notin$ element of / member of

$\neg$ not  
$\land$ and  
$a \lor b = \neg (\neg a \land \neg b)$ or  
$\forall$ forall  
$\exists x a = \neg (\forall x (\neg a))$ there exists  
$a \implies b = \neg a \lor b$  implies  
$a \iff b = (a \implies b) \land (b \implies a)$  iff  

rules of logic  
$p \implies q$. p is true, so q is true.  
$p \implies q$. q is false, so p is false
$(p \implies q) \land (q \implies r)$, so $(p \implies r)$
$(p \land q) \implies (\neg q \implies p)$  
$p  \implies (p \lor q)$  
$p \land q \implies q$



A set is determined when we know what its elements are
$x = y \iff \forall a [(a \in x) \iff (b \in y)]$

## Operations on sets :

$(z = x \cup y) \iff \forall a[(a \in x \lor a \in y) \iff (a \in z)]$ or  
$(a \in x \cup y) \iff (a \in x \lor a \in y)$

$(a \in x \cap y) \iff (a \in x \land a \in y)$

$(a \in x - y) \iff (a \in x \land a \notin y)$

(i) 
$(x \cup x) = $

## Sets of Sets

ordered pair : (a,b) = { {a}, {a,b}}  
inverse of ordered pair (coordinate) : if x = (a,b), $(x)_0 = a, (x)_1 = b$  
n-tuple $(a_1,..,a_n) = ((a_1,...,a_{n-1}),a_n)$  
inverse: $(x)_1^n = (a_1,...,a_{n-1}), (x)_{n-1}^n = a_n$  
Power set P(x)  
Union $\bigcup x = \{a| (\exists y \in x)(a \in y)\}$  
Intersection $\bigcap x = \{a| (\forall y \in x)(a \in y)\}$  

## Relations
Cartesian product $x \times y = \{(a,b)|a \in x \land b \in y\}$  
n-fold cartesian product : $x_1 \times x_2 ... \times x_n = \{(a_1,a_2,...,a_n)|a_i \in x_i for each i fom 1 to n\}$

unary relation on x: a subset of x
n-ary relation on x: a subset of n-fold cartesian product = a unary relation on n-fold product of x

### binary relations 

Very important in set theory

reflexive
symmetric
antisymmetric
transitive

connected : a != b => aRb and bRa

### equivalence relation 

equivalence class $[a] = [a]_R = \{b \in x| aRb \}$

### partial order relation

partial ordering (<=)
poset = (x, <=)
minimal element - no predecessor
well founded : every non-empty subset has a minimal element

Lemma : x is well founded iff there is no infinite monotonically decreasing sequence in x

Proof : TBD

Subsets relation on any collection of sets forms a partial ordering on that set.

Theorem : Upto isomorphism, the subset relation is the only partial order.
Proof : Take the set of all initial segments of x, order by inclusion, and define a map.

total ordering (or linear ordering) - connected partial ordering

toset - totally ordered set

well-ordering = well-founded + totally ordered

woset - well ordered set


## functions

Let R be an n+1-ary relation in x :

$dom(R) = \{a | \exists b[(a,b) \in R]\}$
$ran(R) = \{b | \exists a[(a,b) \in R]\}$

Note that here a is a member of the n-fold cross product of x, and b is a member of x.

n-ary function on a set x is a n+1-ary relation on x, such that for every a in dom(R), there is exactly one b in ran(R) such that (a,b) is in R.

Exercise : A set-theorist is a person for whom all functions are unary :
Every n+1-ary relation is in fact a binary relation - the corresponding function would be therefore unary.

constant function  
identity function $id_x$  
composition $f \circ g(a) = g(f(a))$ 

f:x -> y, u is subset of x, v is subset of y

image of u under f : $f[u] = \{f(a)| a \in u \}$  
pre-image of v under f : $f^{-1}[v] = \{b \in x| f(b) \in v \}$
pre-image is well behaved : always exists, pre-image of union is union of preimages, pre-image of intersection is intersection of pre-images, and preimage of difference is difference of preimages.

retriction of a function f|u

$f[u] = ran(f|u)$  
$f|u = f \cap (u \times ran(f))$

injective
surjective, onto
bijective

inverse function
cartesian product as a set of functions from index to union, such that f(i) in ith set for each function.

if $x_i = x$ for all i in I, in a cartesian product, we say : $x^I$

Exercise:
$x^{1}$ is the set of all functions from {1} to x = {(0,a),(0,b),..(0,..)}

Exercise:
The ordered pair operation (a,b) defines a binary function on sets
f:2 -> A 


## Well-Orderings and Ordinals

Natural numbers are well-ordered - this is what makes induction work. Remember well ordered sets are totally ordered and well founded i.e. every subset has a minimal element. But induction will also work for any well-ordered set.

In fact, this also works for a transfinite well ordered set which is not countable - i.e. enumerable as an integer indexed sequence. 

First, we see that every well-ordered set has a minimum element - 
every well-ordered set is well founded => 
every subset has at least one minimal element =>
the set itself has at least one minimal element being a subset of itself.
But every well ordered set is also totally ordered =>
There is only one minimal element, which is the unique minimum.

This is also true for any non-empty subset of the well-ordered set.

But the difference from natural numbers is that an element may not have a unique predecessor. Note that every element of a well ordered set has a unique successor.
Proof : Take the (unique) minimum element of all elements greater than any given element.

Theorem [Induction on Well Ordering] Let (X,<=>) be a woset. Let E be a subset of X such that
i) smallest element of X is a member of E
ii) for any x in E, if every predecessor of x is in E, then x is in E
Then E = x
Proof: Suppose E != X. Then X-E has a minimum element x since it is non-empty, and this x is not the minimum element of X, which is in E. But any y less than x is in E => x is in E by (ii). 

order isomorphism is a bijective mapping (function) between sets which retains ordering.

Theorem: Let f be an order isomorphism between two wosets X and Y, with Y being a subset of X. Then for all x in X, x <= f(x)
Proof (mine): 
Let E be all elements y of X such that y <= f(y). 
Minimal element of X is in E.
Assume E != X.
Let x = inf X - E, x exists and is not the minimum of X.
Then x > f(x) => x >= f(x)+. If inverse of f(x)+ is in E, then this would be a contradiction. So inverse of f(x)+ must be z > x (cannot be x). Now we have a situation where z > x, but f(z) <= x, which violates order isomorphism. So E = X.

If the sets are tosets, but not wosets, this is not true. For e.g. for integers, consider f(n) = n-1.

Theorem: Any order isomorphism between wosets is unique
Proof:
Let f and g be o.i.s. between X and Y. Let h = f-1 o g.
h is an o.i.
x <= h(x) = f-1 o g(x), for any x => f(x) <= g(x), for any x. 
We can similarly show that g(x) <= f(x).

Note: For tosets, again consider for integers: f(n) = n, g(n) = n+1

segment of a in a poset (devlin defines for woset, halmos calls this strict initial segment) is the set:

$X_a = {x \in X| x < a}$

Theorem: No woset can have an order isomorphism to a segment of X (i.e. to a initial segment of any of its elements). 

Suppose f: X -> initial segment of y in X be an o.i.. Then y > f(y), contradicting earlier theorem.

For totally ordered sets with a maximum element, this is not true : e.g for nonpositive integers, consider f(n) = n-1. In a well ordered set, there is always a minimum element.

Theorem: The set of initial segments of a woset ordered by inclusion is order isomorphic to it.
Proof: This is true for all posets, so wosets as well.

ordinal : any woset (X, <=), such that $X_a = a$ for all a in X.

If X is a woset, then for x, y in X : x < y iff initial segment of x is included in initial segment of y. Further if x is an ordinal, then x itself is a subset of y, since they are equal to their initial segments.

Theorem: Any element of an ordinal is an ordinal.

$(X_a)_b = \{x \in X_a|x < b\} = \{x \in X | x < a \land x < b\}$  
$(X_a)_b = \{x \in X | x < b\} = X_b = b$

Theorem: If a proper subset Y of an ordinal X is an ordinal, it is an element of X

Proof: Let a = inf X - Y. a exists as Y is a proper subset. Then initial segment of a is a subset of Y. Also, any element b of Y has its initial segment in Y. If b > a, then a is in Y, a contradiction. Also, if b = a, then a is in Y, also a conntradiction. So b < a. Thus Y is a subset of the initial segment of a ie the two are equal, and Y = a, since a itself is equal to its initial segment.

Theorem: The intersection of two ordinals is an ordinal. 
Proof: Let Z = X n Y. Given any b in Z, initial segment is in X and in Y, and hence also in Z. 

Theorem: Given two ordinals, they are either equal, or one is a segment of the other, and hence an element of the other

Proof:
Let X,Y be ordinals. If either is a subset of the other, then result follows immediately. Assume this is not true. Then their intersection Z is a proper subset of both X and Y. Let a = inf X - Z, and b = inf Y - Z.

Clearly a,b are not in Z. But Z itself is an ordinal, and hence an element of both X and Y. In fact Z = a, because every element less than a is in Z (by def of a), and every element greater than a cannot be in z, else a would be in Z, and a itself is not in Z => Z is the initial segment of a. Similar Z = b. This implies a and b are equal. But this would mean a belongs to Z - a contradiction.

Theorem: If two ordinals are isomorphic, they are equal
Let X,Y be two ordinals, f is an o.i from X to Y. We need to prove f is the identity map on X.

Let E be the set of all x in X, such that x != f(x). Suppose E is non-empty, and let a be the inf E (since X is woset, every subset has a minimum element). Then for any x < a, f(x) = x, so initial segment of a is the initial segment of f(a) => a = f(a), since every element of X and Y is an ordinal.

**Theorem: Any woset each of whose initial segments are isomorphic to an ordinal is itself isomorphic to an ordinal.**

Proof : Since a is a woset, there is a unique isomorphism from a to an ordinal. In fact we know this ordinal is unique since a is a woset. Hence we can call this ordinal Z(a). Let $g_a$ be the unique isomorphism from a to Z(a).

We can now define Z as a function on X. Let W = ran Z = {Z(a) | $a \in X$} (apparently this uses the Axiom of Replacement). We have to show W is an ordinal isomorphic to X.

Let f: X -> W, s.t. f(a) = Z(a)

Let x and y in X be such that x < y. We want to show Z(x) is a proper subset of Z(y).

Let x,y in X, x < y.

We know $g_x:X_x -> Z(x)$ is an o.i$. 

Also, $X_x = (X_y)_x$.

Thus $(g_y|X_x):X_x -> (Z(y))_{g_y(x)}$ is an o.i. Z(y) is an ordinal. $g_y(x)$ is an element of Z(y) - hence, it is an ordinal and equal to its initial segment i.e $(Z(y))_{g_y(x)}$. Thus the restriction of $g_y$ is in fact an o.i. from $X_x$ to an ordinal. 

Since X_x has an o.i to both Z(x) and to  $(Z(y))_{g_y(x)}$, the two ordinals are o.i. to each other => they are equal. Thus, Z(x) is a proper subset of Z(y).

We see that f is one-to-one : any two x,y in X map to different Z(x), Z(y) - since given any two diferent x,y one is less than the other.

f is onto : by definition, W is just the collection of Z(x) for each x in X. Thus f is bijective.

Also, f preserves order : x < y implies $Z(x) \subset Z(y)$. Thus f is an order isomorphism between X and W.

We now show W is an ordinal.

Let Z(y) be an element of W. Then,

$$\begin{aligned}
W_{Z(y)} & = \{ Z(x) | Z(x) \subset Z(y)\} \\
         & = \{ Z(x) | x < y \} \\
         & = \{ g_y(x) | x < y \} \\
         & = g_y[X_y] \\
         & = g_y[y] \\
         & = Z(y) \\
\end{aligned}
$$

This implies that every element of W is equal to its initial segment in W => W is an ordinal.

**Theorem: Every woset is isomorphic to a unique ordinal**

For existence : We need to prove for every element a of a woset X, $X_a$ is isomorphic to an ordinal. Let E be elements of a not isomorphic to any ordinal. Suppose E is not empty. Let a be the smallest element of E. Thus for x < a, $X_x$ is isomorphic to an ordinal. But this means $X_a$ is isomorphic to an ordinal.

### Musings on Ordinals

If a and b are ordinals, 

$$a \subset b \implies a = b \implies a \in b \implies a = Y_x \text{ for some x in b}$$ 

also, a = { x | x < a} 

The empty set is an ordinal. We can define :

$$\begin{aligned}
0 & = \emptyset \\
1 & = \{0\} \\
2 & = \{0,1\} \\
n & = \{0,1,...,n-1\} \\
\text{the first infinite ordinal } \\
\omega & = \{0,1,2,...,n,n+1,....\} \\
\omega + 1 & = \{0,1,2,...,n,n+1,....,w,\}
\end{aligned}$$

In general, if a is an ordinal, the next ordinal is a U {a}.

An ordinal may be a not be a successor of any ordinal (e.g $\omega$) - it is called a limit ordinal. An ordinal that is the successor of some ordinal is called a successor ordinal.

A sequence is a function whose domain is an ordinal if a = dom(f), we call f an a-sequence and we denote it by :

$\left\langle x_e | e < a \right\rangle$ 

If b < a, the restriction of f to b is
$f|b = \left\langle x_e | e < b \right\rangle$

Thus,
$\{a_n\}_{n=0}^{\infty} = \left\langle a_n | n < \omega \right\rangle$

Exercise 1.7.3 : 
Let E be the set of all ordinals in a, for which condition is true.

Clearly, #\empty set is in E, since it is a limit ordinal#

Assume there is a b in a, such that for all x < b, the statement is true. Then, either b is a limit ordinal, in which case it is in E. Or else b is a successor to some ordinal x. Thus b = x + 1. Now, either x is a limit ordinal, in which case b is in E. Or else, x = c + n, where c is a limit ordinal. Thus b = c + (n+1), and b is in E.

### Problems - Boolean algebras

Boolean algebra has a unary operation (complement), and 2 binary operations meet and join.

meet / join are commutative, associative, distributive over each other.

Absorption : $b \land (b \lor c) = b, b \lor (b \land c) = b$  
Identity : $(b \land -b) \lor a = a, (b \lor -b) \land a = a$

Prove : $b \land -b$ is same and denoted by 0.
Let $b \land -b = z_b$, and $a \land -a = z_a$.  
Then, $z_b \lor a = a$ => $(z_b \lor a) \land z_b = a \land z_b$ => $a \land z_b = z_b$. We can show the same for $z_a$.  
This implies $z_b \land z_a = z_b = z_a = 0$

C. A non-empty set F of subsets of X closed under union, intersection, complement wrt X is a boolean algebra - it is called a field of subsets of X. P(x) is a boolean algebra. Stone's theorem says every boolean algebra is isomorphic to a field of sets.

D. All clopen subsets of a topological space form a field of sets.

F/G/H. b <= c iff $b = b \land c$

$b = b \land c => b \lor c = (b \land c) \lor c = c$

Reflexivity : $(b \land b) \lor b = b => ((b \land b) \lor b) \land b = b \land b => b \land b = b$

Transitivity : $b = b \land c, a = a \land b$  
$a \land b = a \land b \land c => a = a \land c$

Anti-symmetry follows from commutativity of $\land$

$0 \lor b = 0 => (0 \lor b) \land 0 = b \land 0 => 0 = b \land 0$

$1 \lor b = b$

0, 1 are unique min, max

$(b \lor c) \land b = b => b => (b \lor c)$

$(b \land c) \land b = (b \land b) \land c = b \land c => (b \land c) <= b$

**Ideals and Filters**

Nonempty subset I of B is called ideal iff 

b,c in I => (b or c) in I

b in I and c in B => (b and c) in I

A. $b \lor c \in I$

B. $0 \in I$ for every I. Because for any b in I, $0 \land b = 0 \in I$

C. If $b \in B$ => $\{ c \in B | c <= B\}$ is an ideal (principal ideal generated by b)

If a,c in B, then $c \land a = c$ or a. Which is in the ideal.

Note that b is in the ideal. Consider a d in B, such that d > b. Then, $b \land d = b$. Alternatively, assume that neither d < b, nor b < d. Then $d \land b <= b$ is also in I.

D. The set of all finite subsets of an infinite X is a non-prinicipal ideal I. Given any set B of X, it may either for finite, or infinite. If it is finite, there will be a set greater than B in I. If it is infinite, it will not have a finite predecessor. Hence non-ideal.

Measure on a boolean algebra : mu(0) = 0, mu(1) = 1
disjoint union is sum of each

E. If mu is measure on B, then {b|mu(b)} = 0 























