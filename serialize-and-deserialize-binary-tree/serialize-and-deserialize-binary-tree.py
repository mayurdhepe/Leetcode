# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        ret_str = ''
        if not root:
            return ret_str
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node:
                ret_str += str(node.val) + ','
                stack.append(node.left)
                stack.append(node.right)
            else:
                ret_str += 'N' + ','
                
        return ret_str
    
    

    def deserialize(self, data):
        if data == '':
            return None
        
        data_list = data.split(',')
        start_node = TreeNode(int(data_list.pop(0)))
        node_list = [start_node]
        
        while data_list and node_list:
            node = node_list.pop(0)
            left_val = data_list.pop(0)
            if left_val != 'N':
                node.left = TreeNode(int(left_val))
                node_list.append(node.left)
            else:
                node.left = None
            if data_list:
                right_val = data_list.pop(0)
                if right_val != 'N':
                    node.right = TreeNode(int(right_val))
                    node_list.append(node.right)
                else:
                    node.right = None
    
        return start_node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))