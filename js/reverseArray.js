const reverseArray = (arr) => {
    for(let i = 0; i < arr.length/2; i++){
        let end = arr.length - i - 1;
        let temp1 = arr[end];

        let temp2 = arr[i];

        arr[i] = temp1;
        arr[end] = temp2;
    }
    console.log(arr);
}

reverseArray([1,2,3,4,5,6,7,8,9]);