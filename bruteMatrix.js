const bruteMatrix = (matrix, target) => {
    let i = matrix[0].length -1;
    let j = 0;

    while (i >= 0 && j < matrix.length){
        if(matrix[j][i] == target){
            return [j,i];
        }
        if(matrix[j][i] < target){
            j++;
        }else{
            i--;
        }
    }
}

console.log(bruteMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 30));