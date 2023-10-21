def solution(x, y):
    setX = set(x);
    setY = set(y);

    diff = setX.symmetric_difference(setY);
    print (diff.pop());



solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50])