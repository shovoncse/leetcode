/**
 * @param {string} date
 * @return {number}
 */
var dayOfYear = function(date) {
    let arr = date.split('-');
    let year = parseInt(arr[0]);
    let month = parseInt(arr[1]);
    let day = parseInt(arr[2]);
    let days = 0;
    let isLeapYear = false;
    if(year % 4 === 0 && year % 100 !== 0 || year % 400 === 0){
        isLeapYear = true;
    }
    for(let i = 1; i < month; i++){
        if(i === 2){
            if(isLeapYear){
                days += 29;
            }else{
                days += 28;
            }
        }else if(i === 4 || i === 6 || i === 9 || i === 11){
            days += 30;
        }else{
            days += 31;
        }
    }
    days += day;
    return days;
};