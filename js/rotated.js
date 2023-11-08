const junction = (arr) => {
    //check which is the lowest point
    //use binary search. start with looking for midpoint
    //check which half is bigger. ignore other half

    let b = 0;
    let e = arr.length -1;
    
    while(b < e){
        
        let midpoint = Math.floor((b + e)/2);
        
        if(arr[midpoint] > arr[e]){
            b = midpoint +1;
        }
        else {
            e = midpoint;
        }
    }
    console.log(b, e);
}

junction([7,0,1,2,4,5,6]);