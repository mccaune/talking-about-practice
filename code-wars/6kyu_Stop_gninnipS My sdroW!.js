/*
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples: spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" spinWords( "This is a test") => returns "This is a test" spinWords( "This is another test" )=> returns "This is rehtona test"

*/

function spinWords(text){
  let lst = text.split(' ');
  let finalLst = [];
  for(let i = 0; i < lst.length; i++){
    if(lst[i].length >= 5){
      finalLst.push(lst[i].split('').reverse().join(''));
    } else {
        finalLst.push(lst[i]);
      }
    }
  return finalLst.join(' ');
}
