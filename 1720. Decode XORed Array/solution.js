/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
var decode = function(encoded, first) {
    let ans = [first];
    for (let i of encoded) {
        ans.push(ans[ans.length - 1] ^ i);
    }
    return ans;
};