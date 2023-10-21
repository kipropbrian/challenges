var findJudge = function(n, trust) {

    const trustCount = new Array(n+1).fill(0)


    for (const [a, b] of trust) {
       trustCount[a]--;
       trustCount[b]++;
    }
    for (let i =0; i <=n; i++){
        if(trustCount[i] == n-1){
            return i;
        }
    }
    return -1;
}

let params = [[1,3],[2,3],[4,3]];

console.log(findJudge(4, params));