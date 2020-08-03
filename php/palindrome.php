<?php
/*
A palindrome is a word, phrase, verse, or sentence that reads the same backward
or forward. Only the order of English alphabet letters (A-Z and a-z) should be considered,
other characters should be ignored. Write a function that returns true if a given sentence
is a palindrome; false otherwise.

For example, Palindrome::isPalindrome(‘Noel sees Leon.’) should return true
as spaces, period, and case should be ignored resulting with 'noelseesleon'
which is a palindrome since it reads same backward and forward.


*/


class Palindrome
{
    public static function isPalindrome($str)
    {
        $str = strtolower($str);
        // leave only a-z chars
        $str = preg_replace("/[^a-z]+/", "", $str);
        // reverse string
        $str2 = strrev($str);
        return $str === $str2;
    }
}

// test output

echo Palindrome::isPalindrome('Noel sees Leon.');

?>
