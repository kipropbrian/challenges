const allConstruct = (target, wordBank, memo={}) => {
    if(target in memo) return memo[target];
    if (target === "") return [[]];

  const results = [];

  for (word of wordBank) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length);

      const suffixWays = allConstruct(suffix, wordBank, memo);
      const targetWays = suffixWays.map((way) => [word, ...way]);
      results.push(...targetWays);
    }
  }

  
  return results;
};

console.log(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]));
