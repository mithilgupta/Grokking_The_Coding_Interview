#################################
###    987. Vertical Order Traversal of a Binary Tree : LEETCODE
#################################
# It is submitting but failing for some test cases.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def top_view_recur(node, x, dict_):
    # print(node)
    if node is None:
        return
        
    # print(node)
    
    # If dict[y] has a value, pass, otherwise add to dict.
    if x in dict_.keys():
        dict_[x].append(node.val)
    else:
        dict_[x] = [node.val]
        
        
    top_view_recur(node.left, x-1, dict_)
    top_view_recur(node.right, x+1, dict_)


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        dict_ = {}
        # print(root)

        output = []

        top_view_recur(root, 0, dict_)
        
        
        # print(dict_) # check if ordere
        
        output = [v for k,v in sorted(dict_.items())] # i think there is some issue here.

        return output          

#------------------------------------------------------------------------------------------------------------------------

#################################
###    Bottom View of Binary Tree : GFG
#################################

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None


def bottom_view_recur(node, x, dict_):
    if node is None:
        return None
        
    dict_[x] = node.data # Because we want to overwrite the new node with the same x position.
        
    bottom_view_recur(node.left, x-1, dict_)
    bottom_view_recur(node.right, x+1, dict_)

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def bottomView(self,root):
        
        dict_ = {}
        
        bottom_view_recur(root,0 , dict_)
        
        return [v for k,v in sorted(dict_.items())]
        # code here

#------------------------------------------------------------------------------------------------------------------------

#################################
###    Top View of Binary Tree : GFG
#################################

#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None


def top_view_recur(node, x, dict_):
    if node is None:
        return None
        
    if x in dict_.keys():
        pass
    else:
        dict_[x] = node.data
        
    top_view_recur(node.left, x-1, dict_)
    top_view_recur(node.right, x+1, dict_)

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        dict_ = {}
        
        top_view_recur(root,0 , dict_)
        
        return [v for k,v in sorted(dict_.items())]
        # code here


#------------------------------------------------------------------------------------------------------------------------

#################################
###    Tree Boundary Traversal : GFG
#################################

#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
def left_view_recur(node, y, dict_l_):
    # print(node)
    if node is None:
        return
        
    # print(node)
    
    # If dict[y] has a value, pass, otherwise add to dict.
    if y in dict_l_.keys():
        pass
    else:
        dict_l_[y] = node.data
        
        
    left_view_recur(node.left, y+1, dict_l_)
    left_view_recur(node.right, y+1, dict_l_)
    
def root_node_recur(node,  root_leaves):
    # print(node)
    if node is None:
        return
        
    # print(node)
    # Checking the condition for leaf nodes. Append to list if Yes.
    if node.left is None and node.right is None:
        root_leaves.append(node.data)
        
        
    root_node_recur(node.left,  root_leaves)
    root_node_recur(node.right, root_leaves)    
    
def right_view_recur(node, y, dict_r_):
    # print(node)
    if node is None:
        return
        
    # print(node)
    
    # If dict[y] has a value, pass, otherwise add to dict.
    dict_r_[y] = node.data
        
        
    right_view_recur(node.left, y+1, dict_r_)
    right_view_recur(node.right, y+1, dict_r_)




class Solution:
    def printBoundaryView(self, root):
        # Code here

        dict_l_ = {}
        root_leaves = []
        dict_r_ = {}
        
        
        left_view_recur(root, 0, dict_l_)
        root_node_recur(root,  root_leaves)
        right_view_recur(root, 0, dict_r_)
        
        print(dict_l_)
        print(root_leaves)
        print(dict_r_)
        
        







