const grid = (m, n) =>  {
    //Flesh out base case
    //0 rows or cols
    if(m == 0 || n == 0){
        return 0;
    }
    if(m == 1 && n == 1){
        return 1;
    }
    return grid(m-1, n) + grid(m, n-1);
}

console.log(grid(3,3));