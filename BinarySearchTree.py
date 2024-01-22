class BSTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data


class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        self.sum_height = 0
        self.difference_list = []

    def insert(self, x):
        node = BSTNode(x)
        if self.root.value is None:
            self.root = node
        else:
            cur = self.root
            while True:
                # Go to right subtree
                if x > cur.value:
                    if cur.right is None:
                        cur.right = node
                        break
                    else:
                        cur = cur.right
                # Go to left subtree
                else:
                    if cur.left is None:
                        cur.left = node
                        break
                    else:
                        cur = cur.left

    def getNodeHeight(self, node):
        if node is None:
            return -1
        # Compute the height of each subtree
        left_height = self.getNodeHeight(node.left)
        right_height = self.getNodeHeight(node.right)

        # Find the maximum height of left and right subtree
        height = 1 + max(left_height, right_height)
        self.sum_height += height
        return height

    def getTotalHeight(self, node):
        self.getNodeHeight(node)
        return self.sum_height

    def getBalanceFactor(self, node):
        if node is None:
            return 0
        # Compute the height of each subtree
        left_subtree = self.getBalanceFactor(node.left)
        right_subtree = self.getBalanceFactor(node.right)

        # Find the maximum height of left and right subtree
        height = 1 + max(left_subtree, right_subtree)

        # Find and store the weight balance factor to a list
        difference = abs(left_subtree - right_subtree)
        self.difference_list.append(difference)
        return height

    def getWeightBalanceFactor(self, node):
        self.getBalanceFactor(node)
        return max(self.difference_list)


COUNT = [10]


# Print binary tree in 2D
def print2DUtil(node, space):
    if (node == None):
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(node.right, space)

    # Print current node after space count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(node.value)

    # Process left child
    print2DUtil(node.left, space)


# Wrapper over print2DUtil()
def print2D(node):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(node, 0)


if __name__ == '__main__':
    print("<Test the case if tree is empty>")
    root1 = BSTNode(None)
    tree_test = BinarySearchTree(root1)
    print("The sum of the heights of all nodes is",
          tree_test.getTotalHeight(root1))

    print("The weight balance factor of the binary tree "
          "is", tree_test.getWeightBalanceFactor(root1))
    print("=====================================")
    print("Then we insert some nodes")
    tree_test.insert(5)
    tree_test.insert(3)
    tree_test.insert(9)
    print2D(tree_test.root)
    print()
    print("=====================================")
    print("<Test the normal case>")
    """ The tree we will construct
              6
          /       \
         /         \
        4           9
        \           /
         \         /
          5       8     
                 /
                /
               7
    """
    print("The tree before inserting a new node")
    root = BSTNode(6)
    root.left = BSTNode(4)
    print2D(root)
    print()
    print("=====================================")
    print("The tree after inserting a new node")
    test_tree = BinarySearchTree(root)
    test_tree.insert(5)
    print2D(root)
    print("=====================================")
    print("The tree after inserting 3 more nodes")
    test_tree.insert(9)
    test_tree.insert(8)
    test_tree.insert(7)
    print2D(root)
    print("=====================================")
    print("The sum of the heights of all nodes is",
          test_tree.getTotalHeight(root))
    print("=====================================")
    print("The weight balance factor of the binary tree "
          "is", test_tree.getWeightBalanceFactor(root))
