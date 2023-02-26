#### BINARY TREE - FIND HEIGHT OF THE BINARY TREE 

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self, root):
        a = root.left
        b = root.right

        def path(node):
            curr = node
            count = 0
            alpha = True
            while alpha:
                if (curr.left != None) and (curr.right == None):
                    count += 1
                    curr = curr.left
                elif (curr.left == None) and (curr.right != None):
                    count += 1
                    curr = curr.right
                elif (curr.left != None) and (curr.right != None):
                    p = path(curr.left)
                    q = path(curr.right)
                    count += max(p + 1, q + 1)
                    alpha = False
                elif (curr.left == None) and (curr.right == None):
                    alpha = False

            return count

        x = path(a) #left sub tree
        y = path(b) # right sub tree
        return (1 + max(x, y))


T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)