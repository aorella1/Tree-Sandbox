

class Node:
	def __init__(self,x):
		self.val = x
		self.left = None
		self.right = None
		self.counter = 1

	
def bstMaker(list):
	root = Node(list[0])
	currentNode = root
	for val in list:
		currentNode = root
		
		while currentNode != None:
			#If currentNode val == list val, add to currentNodes counter
			if currentNode.val == val : #== add to counter
				currentNode.counter+=1 #if it already exists, add 1 to node
				currentNode = None
			elif val > currentNode.val: #if val being inputed is greater than currentNode

				if currentNode.right == None: #if right is nonexistant, 
					currentNode.right = Node(val) #set right to a new node containing a value
					currentNode = None #reset the while loop, thus resetting the for loop
				elif currentNode.right != None: #if right exists, set currentNode to right 
					currentNode = currentNode.right 
							

			elif val < currentNode.val: #Same as above, going left
			
				if currentNode.left == None:
					currentNode.left = Node(val)	
					currentNode = None
				elif currentNode.left != None:
					currentNode = currentNode.left
			

			else: #If not of the requirements are met, set currentNode to none
				currentNode = None
			
	return(root)
			#if val > currentNode.val:
				#currentNode = currentNode.right


def main():
	list = [4,3,7,5,9,1,1,1,1,1,1]


	print(bstMaker(list).left.val)





main()
