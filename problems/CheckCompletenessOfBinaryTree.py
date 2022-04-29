import collections


class Solution:
    def isCompleteTree(self, root) -> bool:
        queue = collections.deque([])

        queue.append(root)
        flag = False  # has empty node

        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if node.left:
                    if flag:
                        return False
                    queue.append(node.left)
                else:
                    flag = True

                if node.right:
                    if flag:
                        return False
                    queue.append(node.right)
                else:
                    flag = True

        return True
