print("hello problem invert tree")



class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data 

   def invertree( root):
       print("function")
       node1 = root.left
       node2 = root.right
       stack1 , stack2 = [node1], [node2]
       while(stack1 or stack2):
           node1 = stack1.pop()
           node2 = stack2.pop()
           if node1.right :
               stack1.append(node1.right)
           if node2.left:
               stack2.append(node2.left)
           if node1.left:
               stack1.append(node1.left)
           if node2.right:
               stack2.append(node2.right)
           print("node 1 is",node1.data)
           print("node 2 is", node2.data)
           node1.data , node2.data = node2.data , node1.data
           print("node 1 a is",node1.data)
           print("node 2  a is", node2.data)
    
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(20)
# root.left.left.left = Node(7)
root.left.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(1)
# root.right.right.right = Node(1)
print(root.left.right.data)
print(root.invertree())
print(root.left.right.data)
print(root.left.left.data)