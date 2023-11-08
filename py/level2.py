import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = self.right = None

def postorder(height, nums):
    if height == 1:
        return Node(nums.pop())
    node = Node()
    node.value = nums.pop()
    node.right = postorder(height - 1, nums)
    node.left = postorder(height - 1, nums)
    return node

def tree_to_array_breadth_first(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        current = queue.pop(0)  # Dequeue the front node
        result.append(current.value)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result

def getParent(children, arrangement):
    order = []
    for child in children:
        loc = arrangement.index(child)
        parent = math.floor((loc -1)/2)
        if parent < 0 :
            order.append(-1)
        else: 
            order.append(arrangement[parent])
    return order

def solution(h, q):
    tree = postorder(h, list(range(1, 2**h)))
    arrangement = tree_to_array_breadth_first(tree)
    parents = getParent(q, arrangement)
    return parents

print(solution(3, [7, 3, 5, 1]))