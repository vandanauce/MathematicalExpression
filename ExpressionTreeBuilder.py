import Node as model_nodeLib

def newNode(c):
	n = model_nodeLib.Node(c)
	return n

def buildFromList(expList):

	# Stack to hold nodes
	stN = []

	# Stack to hold chars
	stC = []

	# Prioritising the operators
	p = [0]*(123)
	p[ord('+')] = p[ord('-')] = 1
	p[ord('/')] = p[ord('*')] = 2
	p[ord('^')] = 3
	p[ord(')')] = 0

	for expStr in expList:
		if (expStr == '('):
			# Push '(' in char stack
			stC.append(expStr)

		# Push the operands in node stack
		elif (expStr not in [ '*','/','-','+' ,'^',')']): 
			t = newNode(expStr)
			stN.append(t)
		elif (p[ord(expStr)] > 0):
		
			# If an operator with lower or
			# same associativity appears
			while (len(stC) != 0 and stC[-1] != '(' and ((expStr != '^' and p[ord(stC[-1])] >= p[ord(expStr)])	 or (expStr == '^'and 	p[ord(stC[-1])] > p[ord(expStr)]))):
			
				# Get and remove the top element
				# from the character stack
				t = newNode(stC[-1])
				stC.pop()

				# Get and remove the top element
				# from the node stack
				t1 = stN[-1]
				stN.pop()

				# Get and remove the currently top
				# element from the node stack
				t2 = stN[-1]
				stN.pop()

				# Update the tree
				t.left = t2
				t.right = t1

				# Push the node to the node stack
				stN.append(t)

			# Push s[i] to char stack
			stC.append(expStr)
			
		elif (expStr == ')'):
			while (len(stC) != 0 and stC[-1] != '('):
				t = newNode(stC[-1])
				stC.pop()
				t1 = stN[-1]
				stN.pop()
				t2 = stN[-1]
				stN.pop()
				t.left = t2
				t.right = t1
				stN.append(t)
			stC.pop()
	t = stN[-1]
	return t

