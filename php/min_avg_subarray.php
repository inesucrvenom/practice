<?php
/*

A non-empty zero-indexed array A consisting of N integers is given.
 A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A
 (notice that the slice contains at least two elements). The average of a slice (P, Q)
is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice.
To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:
    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

If there is more than one slice with a minimal average, you should return the smallest
starting position of such a slice.

Assume that:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Complexity:

expected worst-case time complexity is O(N);
expected worst-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).
Elements of input arrays can be modified.

*/

/*
I used condition "use next item only if it's smaller than current average".

However, in case or an array like:
a0 > a1 > a2 > a3 .... >an-1
rule works, but it takes time, so performance goes to O(n^2) territory.
In this case, we see clearly that we only need last 2 for global minimum average.

Also, for subarray a, b, c  where a < c < b, average of such 3-tuple is less than average of
a,b or b,c pairs on its own.
So we also need 3-tuples, in addition to 2-tuples.

I couldn't find out 4-tuple that has less average than it's subtuples, however inequalities are tricky,
so I could mix up something.

However, since rule we started with isn't enough on it's own for edge cases,
limiting by length would increase speed.
Although, we must be aware until we have exact proof, we risk to omit some cases using such limit.

For unlimited, on web it takes several seconds for 100k array (>6 sec).
Ok for correctnes, timeout for large edge cases.

For limit 10, it takes around 0.6 sec and timeout limit is lower than that.

For limit 5 it passes completely, both in accuracy and performance.

*/


define("LENGTH_FOR_SPEED_OPTIMIZATION", 5);

/* return array of prefix sums */
function prefix_sums($a){
    $size = count($a);
    $result = array();
    $result[0] = 0;
    for ($i = 1; $i < $size + 1; $i++){
        $result[$i] = $result[$i-1] + $a[$i-1];
    }
    return $result;
}

/* return sum of given slice */
function slice_sum($prefix_sums, $start, $end){
    return $prefix_sums[$end + 1] - $prefix_sums[$start];
}


function solution($A) {
    $debug = false;

    $A_length = count($A);
    if ($debug == true) { echo PHP_EOL, "given array ", json_encode($A), " len ", $A_length; }

    $prefix_sums = prefix_sums($A);
    if ($debug == true) { echo PHP_EOL, "prefix sums array ", json_encode($prefix_sums); }

    $avg_min = ($A[0]+$A[1])/2;
    $avg_min_start = 0;
    $left_bound = 0;
    $right_bound = 1;

    while ((1 <= $right_bound && $right_bound <= $A_length - 1)
        && (0 <= $left_bound && $left_bound <= $A_length - 2)
        && ($left_bound < $right_bound)) {

        $sum_current = slice_sum($prefix_sums, $left_bound, $right_bound);
        $avg_current = $sum_current / ($right_bound - $left_bound + 1);
        if ($debug == true) {
            echo PHP_EOL, "current <", $left_bound, "..", $right_bound, "> diff ", $right_bound - $left_bound;
            echo " # slice ", json_encode(array_slice($A, $left_bound, $right_bound - $left_bound + 1));
            echo " sum ", $sum_current, " avg ", $avg_current;
        }

        // use first minimum
        if ($avg_current < $avg_min){
            $avg_min = $avg_current;
            $avg_min_start = $left_bound;
            if ($debug == true) { echo "*"; }
        }

        // include next item into current slice only if its value is less than average of the current slice
        if (($right_bound < $A_length - 1) && ($A[$right_bound + 1] < $avg_current)
            && ($right_bound - $left_bound < LENGTH_FOR_SPEED_OPTIMIZATION)){
            $right_bound++;
        }
        else {
            $left_bound++;
            $right_bound = $left_bound + 1;
        }
    }

    if ($debug == true) {
        echo PHP_EOL, "avg is: " . $avg_min . " and start at position ";
    }

    return $avg_min_start;
}
