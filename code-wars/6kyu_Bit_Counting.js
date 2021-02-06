/*
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
*/

var countBits = function(n) {
  let lst = [];
  count = 0;
    while (n > 0) {
    a = n % 2
    b = n >> 1
    n = b
    lst.push(a);
  }
  for (let i = 0; i < lst.length; i++){
    if(lst[i] == 1){
      count += 1;
    }
  }
  return count;
};
