/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var findMatrix = function(nums) {
  const result = [];

      for (const num of nums) {
          let found = false;

          // Check if the current element is already in the result matrix
          for (const row of result) {
              if (!row.includes(num)) {
                  row.push(num);
                  found = true;
                  break;
              }
          }

          // If the element is not in any existing row, create a new row
          if (!found) {
              result.push([num]);
          }
      }

      return result;
};