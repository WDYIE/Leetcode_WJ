

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        def preTravel(node, val):
            global maxd
            maxd = max(abs(val), maxd)
            if node.left:
                cur = node.left.val - node.val
                if cur * val > 0:
                    cur = cur +val
                else:
                    cur = cur if abs(cur)>abs(val) else val
                preTravel(node.left,cur)
            if node.right:
                cur = node.left.val - node.val
                if cur * val > 0:
                    cur = cur +val
                else:
                    cur = cur if abs(cur)>abs(val) else val
                preTravel(node.right, cur)
        maxd = 0
        if root:
            preTravel(root,0)
