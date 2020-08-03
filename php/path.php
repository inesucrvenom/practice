<?php

/* Write a function that provides change directory (cd) function for an abstract file system.

Notes:

Root path is '/'.
Path separator is '/'.
Parent directory is addressable as '..'.
Directory names consist only of English alphabet letters (A-Z and a-z).

For example:

$path = new Path('/a/b/c/d');
echo $path->cd('../x')->currentPath;

should display '/a/b/c/x'.

Note: The evaluation environment uses '\' as the path separator.

*/

/* note to self: 3/4 works, test feedback says: wrong aswer for complex paths, but I didn't manage to
discover what complex paths are :/
*/


class Path
{
    public $currentPath;

    function __construct($path)
    {
        $this->currentPath = $path;
    }

    public function cd($newPath)
    {
        $oldPathArray = explode("/", $this->currentPath);
        $newPathArray = explode("/", $newPath);

        foreach ($newPathArray as $item) {
            if ($item == "..") {
                array_pop($oldPathArray);
            } else {
                array_push($oldPathArray, $item);
            }
        }

        if (count($oldPathArray) <= 1) {
            array_push($oldPathArray, "/");
        }

        $this->currentPath = implode("/", $oldPathArray);
        return $this;
    }

}

// test outputs

$path = new Path('/a/b/c/d');
echo PHP_EOL, "bla1 " . $path->cd('../x')->currentPath;


$path = new Path('/a/b/c/d');
echo PHP_EOL, "bla2 " . $path->cd('../../x')->currentPath;


$path = new Path('/a/b/c/d');
echo PHP_EOL, "bla3 " . $path->cd('y/x')->currentPath;

$path = new Path('/a/b/c/d');
echo PHP_EOL, "bla3 " . $path->cd('y/../x')->currentPath;

$path = new Path('/a/b/c/d');
echo PHP_EOL, "bla31 " . $path->cd('y/..')->currentPath;


$path = new Path('/a/b');
echo PHP_EOL, "bla4 " . $path->cd('../../../..')->currentPath;

?>
