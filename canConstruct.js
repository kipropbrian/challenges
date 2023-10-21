/**
 * Time complexity: O(n^2) or O(2^n)
 * Space complexity: O(n)
 */
const canConstruct = (target, wordBank) => {
	//work out the base case
	if(target == ''){
		return true;
	}
	//recurse
	for (word of wordBank){
		if(target.indexOf(word) == 0){
            let newTarget = target.slice(word.length);
		    let answer = canConstruct(newTarget, wordBank)
            if(answer == true){
                return true;
            }
        }
	}
    return false;
	
}