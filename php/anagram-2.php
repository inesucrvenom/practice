<?php namespace StringUtils;

class Anagram
{
    /**
     * This method takes two string parameters that are then checked if they are anagrams.
     *
     * @param string $a First string
     * @param string $b Second string
     *
     * @return bool True if the two strings are anagrams, false otherwise
     *
     * Notes about other ways I did before:
     * php, with sort: https://gist.github.com/inesucrvenom/038abed298fa36004ce1
     * Java, can be done similarly in php: https://gist.github.com/inesucrvenom/c3651bc24d608117c580
     */
    public static function areStringsAnagrams($a, $b){
        return (count_chars($a, 1) == count_chars($b, 1));
    }

}

// test

echo "test1 " . var_export(Anagram::areStringsAnagrams("miki", "kiki"), true) . PHP_EOL;
echo "test2 " . var_export(Anagram::areStringsAnagrams("miki", "kimi"), true) . PHP_EOL;
