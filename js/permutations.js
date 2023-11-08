function getPermutations(str) {
    const permutations = [];
  
    function generate(current, remaining) {
      if (remaining.length === 0) {
        permutations.push(current);
      } else {
        for (let i = 0; i < remaining.length; i++) {
          const nextChar = remaining[i];
          const updatedCurrent = current + nextChar;
          const updatedRemaining = remaining.slice(0, i) + remaining.slice(i + 1);
          generate(updatedCurrent, updatedRemaining);
        }
      }
    }
  
    generate('', str);
    return permutations;
  }
  
  // Example usage:
  const inputString = 'abc';
  const result = getPermutations(inputString);
  console.log(result);