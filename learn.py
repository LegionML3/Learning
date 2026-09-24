class Node:
    def __init__(self, data, right=None, left=None) -> None:
        self.data = data
        self.right = right
        self.left = left

def BFS(root):
    if root is None:
        return []

    queue = [root]
    ans = []

    while len(queue) > 0:
        level_size = len(queue)
        current_lvl_nodes = []

        for _ in range(level_size):
            current = queue.pop(0)

            current_lvl_nodes.append(current.data)

            if current.left:    queue.append(current.left)
            if current.right:   queue.append(current.right)


        ans.append(current_lvl_nodes)
    print(ans)
        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

BFS(root)
