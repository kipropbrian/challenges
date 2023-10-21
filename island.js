/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function (grid) {
  const island = new Set();
  let islandCount = 0;
  const queue = [];

  //Search and mark
  const bfsMark = (queue) => {
    while (queue.length > 0) {
      let key = queue.pop();
      if (
        key[0] >= 0 &&
        key[1] >= 0 &&
        key[0] < grid.length &&
        key[1] < grid[0].length &&
        grid[key[0]][key[1]] == "1" &&
        !island.has(key.toString())
      ) {
        island.add(key.toString());

        let right = [key[0], key[1] + 1];
        let down = [key[0] + 1, key[1]];
        let back = [key[0], key[1] - 1];
        let up = [key[0] - 1, key[1]];

        queue.push(down);
        queue.push(right);
        queue.push(back);
        queue.push(up);
      }
    }
  };

  for (let r = 0; r < grid.length; r++) {
    for (let c = 0; c < grid[r].length; c++) {
      if (grid[r][c] == "1" && !island.has([r, c].toString())) {
        queue.push([r, c]);

        bfsMark(queue);
        //if new encounter increment else continue
        console.log(r,c, island)
        islandCount++;
      }
    }
  }
  return islandCount;
};

const param = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"],
];

let res = numIslands(param);
console.log(res);
