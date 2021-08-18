from board import board

def alphabeta_opening(pos,depth=3,move=1):
        input_position = board(pos)
        print("**********************************************************************************")
        print("*                                Input Position                                  *")
        print("**********************************************************************************")
        print("\n")
        input_position.display_position()
        print("************* Please wait..... computer is thinking hard to beat you *************")

        root_position = input_position
        root_position.depth=0

        max_min(root_position,-1000000,1000000,depth,move)
            

        print("**********************************************************************************")
        print("*                                  computer plays                                *")
        print("**********************************************************************************")
        print("**********************************************************************************"+"\n\n")
        root_position.ai_move.display_position()
        print("Static Estimate : ",root_position.static_estimate)
        print("Nodes Evaluated : ",dfs(root_position,c=1),"\n")
        print("**********************************************************************************")
        print("**********************************************************************************")
        return root_position.ai_move



###################################################################################
# Input:
# Output:
###################################################################################
def max_min(node,a,b,depth=3,move=1):
    if move==1:
        max_color=1
        min_color=2
    else:
        max_color=2
        min_color=1

    if node.depth == depth:
        if max_color==1:
            node.static_estimate =  node.static_estimation()
        else:
            node.static_estimate =  node.static_estimation_black()        
        return node.static_estimate

    v = float('-inf')

    child_positions = node.generate_moves(player=max_color)
    # print(len(child_positions))
    if len(child_positions)==0:
        if max_color==1:
            node.static_estimate =  node.static_estimation()
        else:
            node.static_estimate =  node.static_estimation_black()        
        return node.static_estimate

    for c in child_positions:
        child = board(c)
        child.parent = node

        if node.depth is None:
            node.depth=0
        child.depth = node.depth+1
        node.child_positions.append(child)

        temp = min_max(child,a,b,depth,move=min_color)
        if v<temp :
            v=temp
            node.ai_move = child
            node.static_estimate = v            
        if v>=b:
            return v

        a = max(v,a)

    return v



###################################################################################
# Input:
# Output:
###################################################################################
def min_max(node,a,b,depth=3,move=2):
    if move==2:
        min_color=2
        max_color=1
    else:
        min_color=1
        max_color=2

    if node.depth == depth:
        if min_color==2:
            node.static_estimate =  node.static_estimation()
        else:
            node.static_estimate =  node.static_estimation_black()
        return node.static_estimate

    v = float('inf')

    child_positions = node.generate_moves(player=min_color)  
    # print(len(child_positions))
    if len(child_positions)==0:
        if min_color==2:
            node.static_estimate =  node.static_estimation()
        else:
            node.static_estimate =  node.static_estimation_black()
        return node.static_estimate

    for c in child_positions:
        child = board(c)
        child.parent = node

        if node.depth is None:
            node.depth=0
        child.depth = node.depth+1
        node.child_positions.append(child)

        temp = max_min(child,a,b,depth,move=max_color)
        if v>temp :
            v=temp
            node.ai_move = child
            node.static_estimate = v  
        if v<=a:
            return v

        b = min(v,b)

    return v    



###################################################################################
# Input: Node in search tree and count of nodes evaluated till given node
# Output: Count of total nodes evaluated
###################################################################################
def dfs(node,c):
    if node.child_positions ==[]:
        return c

    for child in node.child_positions:
        c=dfs(child,c+1)
    return c
    

