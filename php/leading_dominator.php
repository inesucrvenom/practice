<?php

/*
The task is to find the value of the leader of the sequence a0,a1,...,an-1, such that
0 <= ai <= 10^9. If there is no leader,the result should be -1

return index of first occurence

*/



function find_leader($A){
    $debug = false;

    $arr_counted = array();
    $leader = $A[0];
    $leader_max = 0;

    $size = count($A);
    $i= 0;
    while ($i < $size){
        if ($debug) {echo PHP_EOL, "i: ", $i, " A[i]: ", $A[$i];}
        if (array_key_exists($A[$i], $arr_counted)){
            $items = $arr_counted[$A[$i]];
            $items["value"] = $items["value"] + 1;
            $arr_counted[$A[$i]] = $items;
            if ($debug) {echo PHP_EOL, "access items: ", json_encode($items);}
            if ($items["value"] > $leader_max){
                if ($debug) {echo PHP_EOL, "max, items", json_encode($items), PHP_EOL;}
                $leader_max = $items["value"];
                $leader = $A[$i];
                if ($debug) {echo PHP_EOL, "modify items: ", json_encode($items), json_encode($arr_counted[$A[$i]]);}
            }
        }
        else {
            $items["value"] = 1;
            $items["index"] = $i;
            if ($debug) {echo PHP_EOL, "create items: ", json_encode($items);}
            $arr_counted[$A[$i]] = $items;
        }
        $i++;
    }

    if ($debug) {echo PHP_EOL, json_encode($A), PHP_EOL, json_encode($arr_counted);}
    if ($debug) {echo PHP_EOL, "leader value ", $leader, " leader max ", $leader_max, PHP_EOL;}

    $result = $arr_counted[$leader];
    if ($result["value"] > $size/2){
        $result_idx = $result["index"];
    }
    else {
        $result_idx = -1;
    }

    if ($debug) {var_dump($arr_counted);}

    return $result_idx;


}

// testing examples

$a1 = array(1, 6, 8, 6, 6, 8, 6, 6);
$a2 = array(1, 2, 8, 4, 3, 5, 6, 7);
$a3 = array(1, 2, 1, 2, 2);

echo find_leader($a3);
