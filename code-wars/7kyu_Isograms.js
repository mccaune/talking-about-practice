/*
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

isIsogram("Dermatoglyphics") == true
isIsogram("aba") == false
isIsogram("moOse") == false // -- ignore letter case
*/

function isIsogram(str){
  let lower = str.toLowerCase();
  let obj = {};
  for(let i = 0; i < lower.length; i++){
    if (obj.hasOwnProperty(lower[i])) {
            obj[lower[i]] += 1;
    } else {
            obj[lower[i]]  = 1;
    } 
  }
  return Object.values(obj).every(check = (value) => value <= 1);
}
