
/*
You are writing a function that takes two sets of arguments of arbitrary length. The return value will be the sum of the values of all of the arguments.

The function should contain at least 1 argument per set.

calculate(1)(1) // should return 2
calculate(1,1)(1) // should return 3
calculate(1,1)(1,-1) // should return 2
calculate(2,4)(3,7,1) // should return 17
*/

/* uses closure */
function calculate() {

    var sum = 0;

    function sumThem(args) {
      for (var i = 0; i < args.length; i++) {
        sum += args[i];
      }
    }

    function subarguments() {
      sumThem(arguments);
      return sum;
    }

  // sum arguments of initial call
  sumThem(arguments);
  // call again for another set of arguments
  return subarguments;
}
