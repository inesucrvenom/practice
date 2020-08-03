
/*
 Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
 Input to the function is guaranteed to be a single string.

 Examples of valid inputs: 1.2.3.4 123.45.67.89

 Examples of invalid inputs: 1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089
 */

function isValidIP(str) {
    // check for failing, if not failed then pass

    var strArray = str.split('.');
    console.log(str, strArray);

    // not IPv4
    if (strArray.length != 4) {
        return false;
    }

    for (var i = 0, len = strArray.length; i < len; i++){
        // not a number
        if (isNaN(Number(strArray[i]))){
            return false;
        }

        // out of range
        if (Number(strArray[i]) < 0 || Number(strArray[i]) > 255){
            return false;
        }

        // has leading zeros
        if (Number(strArray[i]) !== 0 && strArray[i][0] === 0){
            return false;
        }

        // has whitespaces
        if (strArray[i].indexOf(' ') >= 0){
            return false;
        }
    }

    return true;
}

// testing

var str;
//str = "127.0.0.1";
str = "127.0.0.1 2";
console.log(isValidIP(str));
