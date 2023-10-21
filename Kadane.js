const maxsubarray = (arr) => {
    //dp
  let maxSum = 0;

  for (let i = 0; i < arr.length; i++) {
    let currentSum = 0;
    for (let j = i; j < arr.length; j++) {
      currentSum +=arr[j];
      maxSum = Math.max(maxSum, currentSum);
    }
  }
  return maxSum;
};
console.log(maxsubarray([-6, 1, 5, -2]));
