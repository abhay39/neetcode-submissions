class Queue:

    def __init__(self) -> None:
        self.list = []

    def enqueue(self, data):
        self.list.append(data)

    def get_top(self):
        if len(self.list) > 0:
            return self.list.pop(0)

    def getSize(self):
        return len(self.list)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = Queue()
        result = []

        queue.enqueue(root)

        while queue.getSize() > 0:

            level = []

            # Number of nodes currently in this level
            level_size = queue.getSize()

            for _ in range(level_size):

                node = queue.get_top()

                level.append(node.val)

                if node.left:
                    queue.enqueue(node.left)

                if node.right:
                    queue.enqueue(node.right)

            result.append(level)

        return result