/**
 * @param {string[]} bank
 * @return {number}
 */
var numberOfBeams = function(bank) {
  let arr = [];
  for(let i = 0; i < bank.length; i++) {
    let beams = bank[i].split("1").length - 1;
    if(beams > 0) arr.push(beams);
  }
  if(arr.length < 2) return 0;
  const sum = arr.reduce((accumulator, currentValue, index, array) => {
    if (index < array.length - 1) {
      return accumulator + currentValue * array[index + 1];
    }
    return accumulator;
  }, 0);

  return sum;
};