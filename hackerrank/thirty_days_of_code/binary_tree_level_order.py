#### BINARY TREE  Level Order

import sys

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

    def levelOrder(self,root):

        # def getHeight(self, root):
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
        height_tree =  (1 + max(x, y))
        # print(height_tree)

        def children(node):
            ans = []
            curr = node
            ans.append(curr.left)
            ans.append(curr.right)
            return ans  #list

        def final(root):
            lvl_order = [root.data]
            curr = root
            x = children(curr)
            lvl = 0
            while lvl != height_tree:
                temp = []
                for j in x:
                    if type(j) != list:
                        if j != None:
                            lvl_order.append(j.data)
                            p = children(j)
                            temp.append(p)
                        elif j == None:
                            pass
                    elif type(j) == list:
                        for k in j:
                            if k != None:
                                lvl_order.append(k.data)
                                p = children(k)
                                temp.append(p)
                            elif k == None:
                                pass
                x = temp
                lvl += 1
            return lvl_order

        check = final(root)
        print(*check)

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)