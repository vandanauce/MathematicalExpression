def evaluateExpressionTree(root):
 
    # empty tree
    if root is None:
        return 0
 
    # leaf node
    if root.left is None and root.right is None:
        return int(root.key)
 
    # evaluate left tree
    left_sum = evaluateExpressionTree(root.left)
 
    # evaluate right tree
    right_sum = evaluateExpressionTree(root.right)
 
    # check which operation to apply
    if root.key == '+':
        return left_sum + right_sum
 
    elif root.key == '-':
        return left_sum - right_sum
 
    elif root.key == '*':
        return left_sum * right_sum
 
    else:
        return left_sum / right_sum