# time: O(log(n)) space: O(log(n))
#worst O(n) both time and space
def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelpler(tree, target, float("inf"))

def findClosestValueInBstHelpler( tree, target, closest):
    if tree is None:
        return closest
    if abs(target- closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelpler(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelpler(tree.right, target, closest)
    else:
        return closest

#____________________________________________________________________________
# time: O(log(n)) space: O(1)
#worst O(n) time and O(1) space

def findClosestValueInBst(tree, target):
    return findClosestValueInBstHelpler(tree, target, float("inf"))

def findClosestValueInBstHelpler( tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target- closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break  
    return closest