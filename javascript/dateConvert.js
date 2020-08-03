/*
Convert given M/D/YYYY into YYYYMMDD date format string.
*/
function myDate(inputDate) {
    var someDate = new Date(inputDate);
    var year = someDate.getFullYear()
    var month = someDate.getMonth() + 1
    var day = someDate.getDate();
    
    var outputDate = ""+ year 
    outputDate += (month<10 ? "0"+month : ""+month)
    outputDate += (day<10 ? "0"+day : ""+day);
    return outputDate;
  }
