const openLock = (target) => {
  let start = "0000";

  const queue = [start];
  const visited = new Set();
  let count = 0;

  while (queue.length > 0) {
    let current = queue.pop();

    if (current === target) {
      console.log(current);
      break;
    }

    if (!visited.has(current)) {
      count = count + 1;
      visited.add(current);

      for (let i = 0; i < 4; i++) {
        let added = (parseInt(current[i]) + 1) % 10;
        let combination = current.slice(0, i) + added + current.slice(i + 1);
        queue.push(combination);

        let sub = (parseInt(current[i]) + 9) % 10;
        let subcombination = current.slice(0, i) + sub + current.slice(i + 1);

        queue.push(subcombination);
      }
    }
  }
  console.log(count);
};

openLock("0202");
