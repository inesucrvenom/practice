Train of thoughts / notes

#### ~ 1 Aug
- started

#### 3 Aug
- lost all code (I didn't use the proven methods == offline and git, thinking it will be 'just a few lines')

#### 4 Aug
- it's correctly working, but too slow for those extreme test cases, need to look up further optimisations
- I've been splitting the table and saving intermediary results, but I only took smallest blocks of 8x8

full matrix of 8x8 looks like:
```
    a    a+1  a+2  a+3  a+4  a+5  a+6  a+7
    a+1  a    a+3  a+2  a+5  a+4  a+7  a+6
    a+2  a+3  a    a+1  a+6  a+7  a+4  a+5
    a+3  a+2  a+1  a    a+7  a+6  a+5  a+4
    a+4  a+5  a+6  a+7  a    a+1  a+2  a+3
    a+5  a+4  a+7  a+6  a+1  a    a+3  a+2
    a+6  a+7  a+4  a+5  a+2  a+3  a    a+1
    a+7  a+6  a+5  a+4  a+3  a+2  a+1  a

  smallest element = top left, main diagonal
  biggest element = bottom left, antidiagonal/skew diagonal
```
- I was thinking about using bigger ones, but I stumbled upon that there's formula for m==n==2^k so I'll figure out the formula
- yeah, ok, formula works only for square matrices without nulls (or 0 at the first place and on the diagonal only):  ```dim * 1/2 * dim * (dim + 1)   +  a * dim * dim```
- ```(a + b) mod m == (a mod m + b mod m) mod m```
- ```(a * b) mod m == (a mod m * b mod m) mod m```

#### 5 Aug
- however, when we have element = old_element - LOSS if LOSS <= old_element else 0 then we can't just use modulo properties on any matrix, we need to split the problem into the matrices where LOSS <= first_element and the rest, and then those rest figure out in a different way
- maybe there's some formula that can be invented for those matrices that have nulls at known positions?
- ok, if LOSS >= dim/2 then from four dim/2 x dim/2 blocks we get null matrices for top left and bottom right, that means we don't have to calculate them
```
[0, dim/2] x [0, dim/2]      [0, dim/2] [dim/2+1, dim]
[dim/2+1, dim] x [0, dim/2]    [dim/2+1, dim] x [dim/2+1, dim]

LOSS >= dim/2:
[0] [S]
[S] [0]
```
- and those two S have same values, so we need to do only one
- after LOSS is applied, on square matrices
  - if biggest element isn't zero, then we don't have null matrix
  - but if smallest element isn't zero, then we have full matrix and we can apply the formula
  - specially, on matrixes with zeroes only on diagonal but no more, we can also apply the formula directly - for them the top left corners looks like:
  ```
  0 1 2 ...
  1 0 3 ...
  2 3 0 ...
  ...
  ```
    - so, when right and bottom neighbour of the smallest element are 1
- when LOSS is >=8 but smaller than dim/2 then we only get 8x8 null blocks on  the main diagonal, and for the rest we have to check LOSS value further
  - big LOSS clears up blocks of 8x8 (and smaller, but since I have working solution for 8x8 blocks, they'll be my stopping point for the recursion which will figure out big blocks in the starting matrix)
  - ok, LOSS of type LOSS == 8p will always give full null matrices for 8x8 blocks
  - need to figure out how to get them, skip them better said
  - LOSS of type 2^s will give null matrices of 2^s x 2^s

- it looks like recursion could be:
  every matrix split will be top-left A, top-right B, bottom-left C, bottom-right D, where only A is square matrix unless it's smaller than 8x8
  ```
  A B
  C D
  ```
  (modulo will be applied on every step where possible)

  starting matrix has dimension row x col and LOSS
  find biggest s so that 2^s <= LOSS - that will give 2^s null submatrices in the main one

  rec_split: split the big one into A of dim 2^s and the rest

  A is zero, skip it
  call the same rec_split on D with same s

  for B (and C):
  rec_sum: find biggest k so that dim = 2^k <= smallest dim of B
   split B into new AA, BB, CC, DD where you use formula on AA and call rec_sum on the rest

   if any A, B, C, or D <=8 stop and use old solutions

- with some simple testing, it might have sense to spare some recursion calls and calculate some bigger blocks than 8x8 directly
one candidate is 32x32, another is 64x64
- in any case, for smallest blocks, we want DELTAS_LOSS table and will just sum through the needed part of it

#### 12 Aug
have correctly working using recursions, but still too slow
trying to implement with bigger default block
