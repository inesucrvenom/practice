
/*

Given the string representations of two integers, return the string representation of the sum
of those integers.

For example:
sumStrings('1','2') // => '3'
C# sumStrings("1","2") // => "3"

A string representation of an integer will contain no characters besides the ten numerals "0" to "9".

hint: big integers!
*/

/* magic number */
var BLOCK_SIZE = 10;

/* sum of small numbers */
function smallIntCase(a, b) {
    return String(Number(a) + Number(b));
}

/* convert string into array of blocks of strings */
function convertToBlocks(inputString) {
    var head = inputString.length % BLOCK_SIZE;
    var blockArray = [];

    // add head first
    if (head > 0) {
        blockArray.push(inputString.slice(0, head));
    }

    // add all other same sized blocks
    for (var i = head, len = inputString.length; i < len; i += BLOCK_SIZE) {
        blockArray.push(inputString.slice(i, BLOCK_SIZE + i));
    }

    return blockArray;
}


/* calculates carry, returns array [carry, rest] */
function calculateCarry(block) {
    var split = convertToBlocks(block);
    var result = [];

    if (split.length > 1) {
        result[0] = split[0];
        result[1] = split[1];
    }
    else {
        result[0] = 0;
        result[1] = split[0];
    }

    return result;
}

/* glue rest of string together at the beginning */
function mergeBlockArray(a, sum, firstCarry) {
    var block;
    while (a.length > 0) {
        block = a.pop();
        if (firstCarry > 0) {
            sum = smallIntCase(block, firstCarry) + sum;
            firstCarry = 0;
        } else {
            sum = block + sum;
        }
    }

    return sum;
}

/* sums given array per block positionwise, returns string */
function sumBlockArray(a1, a2) {
    var sum = "";
    var block1, block2, partialSum, sumSplit;
    var carry = 0;

    while (a1.length > 0 && a2.length > 0) {
        block1 = a1.pop();
        block2 = a2.pop();

        // block1 + block2 + carry
        partialSum = smallIntCase(block1, carry);
        partialSum = smallIntCase(partialSum, block2);

        // next carry
        sumSplit = calculateCarry(partialSum);
        carry = sumSplit[0];
        sum = sumSplit[1] + sum;
    }

    // when numbers aren't of same block array size
    if (a1.length > 0) {
        sum = mergeBlockArray(a1, sum, carry);
    }
    if (a2.length > 0) {
        sum = mergeBlockArray(a2, sum, carry);
    }

    return sum;
}


/* returns string representation of sum result, bigInt version */
function sumStrings(a, b) {

    /* small int case */
    if (a.length <= BLOCK_SIZE && b.length <= BLOCK_SIZE) {
        return smallIntCase(a, b);
    }

    /* big int case */
    var aBlocks = convertToBlocks(a, BLOCK_SIZE);
    var bBlocks = convertToBlocks(b, BLOCK_SIZE);
    var result = sumBlockArray(aBlocks, bBlocks, BLOCK_SIZE);

    return result;
}

// testing output

console.log(sumStrings("1111222233334444555566667777", "5555533333222224444411111"));

console.log(sumStrings("1111111133333333555566666666", "5555599222222229911111111"));


console.log(sumStrings('712569312664357328695151392','8100824045303269669937'));

console.log(sumStrings('123000800','456'));
