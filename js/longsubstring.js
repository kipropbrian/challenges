var lengthOfLongestSubstring = function(s) {
    if (!s) {
        return 0;
    }
    // Starting index of the window
    let start = 0;
    // Ending index of the window
    let end = 0;
    // Maximum length of the substring
    let maxLength = 0;
    // Set to store the unique characters
    const uniqueCharacters = new Set();
    // Loop for each character in the string
    while (end < s.length) {
        if (!uniqueCharacters.has(s[end])) {
            uniqueCharacters.add(s[end]);
            end++;
            maxLength = Math.max(maxLength, uniqueCharacters.size);
        } else {
            uniqueCharacters.delete(s[start]);
            start++;
        }
    }
    return maxLength;
    // if(s.length == 0){
    //     return '';
    // }
    // if(s.length == 1){
    //     return s;
    // }


    // //count unique substring and place in array.
    // let substr = new Set(s[0]);
    
    // let start = 1;
    // let end = 2;

    // let maxLen  = 0;

    // while(end < s.length ){
        
    //     if (!substr.has(s[end])){
    //         substr.add(s[end]);
    //         end++;
    //         maxLen = Math.max(maxLen, substr.size);
    //     } else {
    //         start++;
    //     }
    // }
};


console.log(lengthOfLongestSubstring('pwwkew'));

/**
 * Check if length is or 2 and return empty or the one string. 
 * 
 * create two pointers, b and e. Move the e pointer forward while checking to see no repeating letters are found. 
 * 
 * Create a new var called unq, which counts the length of substr
 * 
 * If none are found (unique letters) store the substring in a set which is unique and takes Log ON to search through. 
 * 
 * If we find a duplicate char, stop e pointer and move b pointer to e - 1. Create new set, and insert first character e-1
 * then start moving e. Increment unq only if count is larger than unq.
 * 
 * At end of count, return unq. 
 */