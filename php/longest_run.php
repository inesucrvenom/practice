<?php

/*

Write a function that finds the zero-based index of the longest run in a string.
A run is a consecutive sequence of the same character. If there is more than one run with
the same length, return the index of the first one.

For example, Run::indexOfLongestRun('abbcccddddcccbba') should return 6 as the longest
run is dddd and it first appears on index 6.

*/

class Run
{
    public static function indexOfLongestRun($str)
    {
        $index_of_longest_one = 0;
        $len_of_longest_one = 1;
        $tested_char = $str[0];
        $len_of_tested_one = 1;
        $index_of_tested_one = 0;

        $i = 1;
        $len = strlen($str);
        while ($i < $len) {
            if ($len_of_tested_one > $len_of_longest_one) {
                $len_of_longest_one = $len_of_tested_one;
                $index_of_longest_one = $index_of_tested_one;
            }
            if ($str[$i] == $tested_char) {
                $len_of_tested_one++;
            }
            else {
                $len_of_tested_one = 1;
                $index_of_tested_one = $i;
                $tested_char = $str[$i];
            }
            $i++;
        }
        if ($len_of_tested_one > $len_of_longest_one) {
            $len_of_longest_one = $len_of_tested_one;
            $index_of_longest_one = $index_of_tested_one;
        }

        return $index_of_longest_one;
    }
}

// test output

echo "\n<br>(1, " . Run::indexOfLongestRun('abbcccddddcccbba');
echo "\n<br>(2, " . Run::indexOfLongestRun('baaaa');
echo "\n<br>(3, " . Run::indexOfLongestRun('aaaab');
echo "\n<br>(4, " . Run::indexOfLongestRun('bacc');
