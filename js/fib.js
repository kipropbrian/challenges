const fib = (n, memo = {}) => {
    //base case
    if(n in memo){
        return memo[n];
    }
    if(n == 0){
        return 0;
    }
    if(n < 1){
        return 1;
    }

    memo[n] =  fib(n-1, memo) + fib(n-2, memo);
    console.log(JSON.stringify(memo))
    return memo[n];
}

console.debug(fib(8));