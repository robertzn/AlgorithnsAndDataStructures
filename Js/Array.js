// index      [0, 1, 2, 3, 4, 5]
const numArr = [1, 5, 2, 8, 7, 3];
console.log(numArr); //output the elements of the array before modifying the array
console.log(numArr[4]); //methods to find the position of an element in an array.
const addArray = numArr.splice(4, 0, 15); //add element in the array
console.log(numArr); //the new elements in the array after adding num 15 in position 7 of the array
const deletedArray = numArr.splice(2, 0, 7); // Delete the element from Array
console.log(numArr); // value in the array
console.log(numArr); //output the values of the array

// 1,  5, 7, 2, 8, 15, 7, 3
//using a for loop to add/delete element in an array
const numArray = [1, 5, 2, 8, 7, 3];
let ArrRemove = 8;
for (var i = 0; i < numArray.length; i++) {
  if (numArray[i] === ArrRemove) {
    numArray.splice(i, 1); // remove the array
  }
}

console.log(numArray);

//using a for loop to add/delete element in an array

for (var i = 0; i < arr.length; i++) {
  if (numArray[i] === ArrRemove) {
    numArray.splice(i, 1);
    i--;
  }
}
console.log(numArray);
//=> [1, 2, 3, 4, 6, 7, 8, 9, 0]
