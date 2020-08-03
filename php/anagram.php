<?php
/*
 An anagram is a word formed from another by rearranging its letters,
 using all the original letters exactly once;
 for example, orchestra can be rearranged into carthorse.
 Write a function that returns true if two words are each other's anagrams; false otherwise.
 For example, AreAnagrams::areStringsAnagrams('momdad', 'dadmom')
 should return true as arguments are anagrams.

http://www.testdome.com/Questions/PHP/AreAnagrams/3457

 */

class AreAnagrams
{

    public static function areStringsAnagrams($a, $b)
    {
        // not optimal solution cpu-wise and memory-wise for huge strings, OK for small ones.
        $aa = str_split($a, 1);
        sort($aa);
        $bb = str_split($b, 1);
        sort($bb);

        return ($aa === $bb);
        
        // or even shorter:
        // return (count_chars($a, 1) == count_chars($b, 1));
    }
}

// test output

echo AreAnagrams::areStringsAnagrams('momdadee', 'dadmom') ? "\n" . 'True' : "\n" . 'False';
echo AreAnagrams::areStringsAnagrams('momdad', 'dadmom') ? "\n" . 'True' : "\n" . 'False';

?>
