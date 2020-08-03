/*
The program uses a data structure where an array can contain items and other arrays of the same type. Write a function countItems that recursively passes through all items and counts the number of occurrences of a given item.
*/

function countItems(arr, item) {
  // Write the code that goes here
    if (arr.length > 0){
      if (arr[0].constructor === Array){
        // go into member that is array
        return countItems(arr[0], item) + countItems(arr.slice(1, arr.length), item);
      } else {
        // ordinary member
        if (item === arr[0]){
          return (1 + countItems(arr.slice(1, arr.length), item));
        } else {
          // rest of the subarray
          return countItems(arr.slice(1, arr.length), item);
        }
      }
    } else {
      return 0;
    }
}

var arr = ["apple",
           ["bananaX", "apple", "strawberryX"],
           "chocolate",
           "apple",
           "milk"
           ];


var arr2 = ["apple",
           "apple",
           "milk"
           ];

var arr3 = ["apple",
           ["bananaX", "apple", "strawberryX"],
           "chocolate",
           "apple",
           ["miki", ["miki", "apple", "maus"], "maus"],
           "milk"
           ];



console.log("final " + countItems(arr3, "apple"));
