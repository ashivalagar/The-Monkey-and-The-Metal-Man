import random 
class agentP:
    def __init__(self,*args):
        # print(args)
        pass
    def step(self,state):
        # print(state)
        vals = [[0,1],[0,-1],[1,0],[-1,0]]
        spotter_postion = state['spotter location']
        spotter_dir = state['spotter direction']
        assasin_postion = state['assasin location']
        assasin_dir = state['assasin direction']
        board = state['board']
        # print('spotter_position',spotter_postion)
        # print('spotter_dir',spotter_dir)
        print('assasin_position', assasin_postion)
        print('assasin_dir', assasin_dir)
        if (spotter_postion[0] in [7,8,9,10,11] and spotter_postion[1] in [7,8,9,10,11]):
            # spotter_moves=[[0,0], [0,0]]
            # spotter_direction = [1,0]
            spotter_moves = [random.choice(vals),random.choice(vals)]
            spotter_direction = random.choice(vals)
        else:
            if (spotter_postion[0] < len(board)/2 and spotter_postion[1]< len(board[0])/2):
                if (spotter_dir[0] == -1 or spotter_dir[1]==-1):
                    spotter_direction = [0,1]
                    spotter_moves=[[0,0], [0,0]]
                elif (spotter_dir[0] == 1):
                    count = 0
                    for i in range(5):
                        if (board[spotter_postion[0]+1+i][spotter_postion[1]] != -1 and board[spotter_postion[0]+1+i][spotter_postion[1]] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        spotter_direction = [0,1]
                        spotter_moves = [[0,1], [0,1]]
                    elif (count > 0 and count < 2):
                        spotter_direction = [0,1]
                        spotter_moves = [[1,0], [0,1]]
                    elif (count == 2):
                        spotter_direction = [1,0]
                        spotter_moves = [[1,0], [1, 0]]
                    else:
                        spotter_direction = [1,0]
                        spotter_moves = [[1,0], [1, 0]]
                elif (spotter_dir[1]==1):
                    count = 0
                    for i in range(5):
                        if (board[spotter_postion[0]][spotter_postion[1]+1+i] != -1 and board[spotter_postion[0]][spotter_postion[1]+1+i] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        spotter_direction = [1,0]
                        spotter_moves = [[1,0], [1,0]]
                    elif (count > 0 and count < 2):
                        spotter_direction = [1,0]
                        spotter_moves = [[0,1], [1,0]]
                    elif (count == 2):
                        spotter_direction = [0,1]
                        spotter_moves = [[0,1], [0, 1]]
                    else:
                        spotter_direction = [0,1]
                        spotter_moves = [[0,1], [0, 1]]
            if (spotter_postion[0] < len(board)/2 and spotter_postion[1] > len(board[0])/2):
                if (spotter_dir[0] == -1 or spotter_dir[1]==1):
                    spotter_direction = [0,-1]
                    spotter_moves=[[0,0], [0,0]]
                elif (spotter_dir[0] == 1):
                    count = 0
                    for i in range(5):
                        if (board[spotter_postion[0]+1+i][spotter_postion[1]] != -1 and board[spotter_postion[0]+1+i][spotter_postion[1]] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        spotter_direction = [0,-1]
                        spotter_moves = [[0,-1], [0,-1]]
                    elif (count > 0 and count < 2):
                        spotter_direction = [0,-1]
                        spotter_moves = [[1,0], [0,-1]]
                    elif (count == 2):
                        spotter_direction = [1,0]
                        spotter_moves = [[1,0], [1, 0]]
                    else:
                        spotter_direction = [1,0]
                        spotter_moves = [[1,0], [1, 0]]
                elif (spotter_dir[1]==-1):
                    count = 0
                    for i in range(5):
                        if (board[spotter_postion[0]][spotter_postion[1]-i] != -1 and board[spotter_postion[0]][spotter_postion[1]-i] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        spotter_direction = [1,0]
                        spotter_moves = [[1,0], [1,0]]
                    elif (count > 0 and count < 2):
                        spotter_direction = [1,0]
                        spotter_moves = [[0,-1], [1,0]]
                    elif (count == 2):
                        spotter_direction = [0,-1]
                        spotter_moves = [[0,-1], [0, -1]]
                    else:
                        spotter_direction = [0,-1]
                        spotter_moves = [[0,-1], [0, -1]]
            if (spotter_postion[0] > len(board)/2 and spotter_postion[1] > len(board[0])/2):
                if (spotter_dir[0] == 1 or spotter_dir[1]==1):
                    spotter_direction = [0,-1]
                    spotter_moves=[[0,0], [0,0]]
                elif (spotter_dir[0] == -1):
                    count = 0
                    for i in range(5):
                        if (board[spotter_postion[0]-i][spotter_postion[1]] != -1 and board[spotter_postion[0]-i][spotter_postion[1]] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        spotter_direction = [0,-1]
                        spotter_moves = [[0,-1], [0,-1]]
                    elif (count > 0 and count < 2):
                        spotter_direction = [0,-1]
                        spotter_moves = [[-1,0], [0,-1]]
                    elif (count == 2):
                        spotter_direction = [-1,0]
                        spotter_moves = [[-1,0], [-1, 0]]
                    else:
                        spotter_direction = [-1,0]
                        spotter_moves = [[-1,0], [-1, 0]]
                elif (spotter_dir[1]==-1):
                    count = 0
                    for i in range(5):
                        if (board[spotter_postion[0]][spotter_postion[1]-i] != -1 and board[spotter_postion[0]][spotter_postion[1]-i] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        spotter_direction = [-1,0]
                        spotter_moves = [[-1,0], [-1,0]]
                    elif (count > 0 and count < 2):
                        spotter_direction = [-1,0]
                        spotter_moves = [[0,-1], [-1,0]]
                    elif (count == 2):
                        spotter_direction = [0,-1]
                        spotter_moves = [[0,-1], [0, -1]]
                    else:
                        spotter_direction = [0,-1]
                        spotter_moves = [[0,-1], [0, -1]]

            if (spotter_postion[0]>len(board)/2 and spotter_postion[1]<len(board[0])/2):
                if (spotter_dir[0] == 1 or spotter_dir[1]==-1):
                    spotter_direction = [0,1]
                    spotter_moves=[[0,0], [0,0]]
                elif (spotter_dir[0] == -1):
                    count = 0
                    for i in range(5):
                        if (board[spotter_postion[0]-i][spotter_postion[1]] != -1 and board[spotter_postion[0]-i][spotter_postion[1]] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        spotter_direction = [0,1]
                        spotter_moves = [[0,1], [0,1]]
                    elif (count > 0 and count < 2):
                        spotter_direction = [0,1]
                        spotter_moves = [[-1,0], [0,1]]
                    elif (count == 2):
                        spotter_direction = [-1,0]
                        spotter_moves = [[-1,0], [-1, 0]]
                    else:
                        spotter_direction = [-1,0]
                        spotter_moves = [[-1,0], [-1, 0]]
                elif (spotter_dir[1]==1):
                    print("here")
                    count = 0
                    for i in range(5):
                        if (board[spotter_postion[0]][spotter_postion[1]+1+i] != -1 and board[spotter_postion[0]][spotter_postion[1]+1+i] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        spotter_direction = [-1,0]
                        spotter_moves = [[-1,0], [-1,0]]
                    elif (count > 0 and count < 2):
                        spotter_direction = [-1,0]
                        spotter_moves = [[0,1], [-1,0]]
                    elif (count == 2):
                        spotter_direction = [0,1]
                        spotter_moves = [[0,1], [0, 1]]
                    else:
                        spotter_direction = [0,1]
                        spotter_moves = [[0,1], [0, 1]]    

        if (assasin_postion[0] in [7,8,9,10,11] and assasin_postion[1] in [7,8,9,10,11]):
            # assasin_moves=[[0,0], [0,0]]
            # assasin_direction = [1,0]
            assasin_moves = [random.choice(vals),random.choice(vals)]
            assasin_direction = random.choice(vals)
        else:
            if (assasin_postion[0] < len(board)/2 and assasin_postion[1]< len(board[0])/2):
                if (assasin_dir[0] == -1 or assasin_dir[1]==-1):
                    assasin_direction = [0,1]
                    assasin_moves=[[0,0], [0,0]]
                elif (assasin_dir[0] == 1):
                    count = 0
                    for i in range(5):
                        if (board[assasin_postion[0]+1+i][assasin_postion[1]] != -1 and board[assasin_postion[0]+1+i][assasin_postion[1]] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        assasin_direction = [0,1]
                        assasin_moves = [[0,1], [0,1]]
                    elif (count > 0 and count < 2):
                        assasin_direction = [0,1]
                        assasin_moves = [[1,0], [0,1]]
                    elif (count == 2):
                        assasin_direction = [1,0]
                        assasin_moves = [[1,0], [1, 0]]
                    else:
                        assasin_direction = [1,0]
                        assasin_moves = [[1,0], [1, 0]]
                elif (assasin_dir[1]==1):
                    count = 0
                    for i in range(5):
                        if (board[assasin_postion[0]][assasin_postion[1]+1+i] != -1 and board[assasin_postion[0]][assasin_postion[1]+1+i] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        assasin_direction = [1,0]
                        assasin_moves = [[1,0], [1,0]]
                    elif (count > 0 and count < 2):
                        assasin_direction = [1,0]
                        assasin_moves = [[0,1], [1,0]]
                    elif (count == 2):
                        assasin_direction = [0,1]
                        assasin_moves = [[0,1], [0, 1]]
                    else:
                        assasin_direction = [0,1]
                        assasin_moves = [[0,1], [0, 1]]
            if (assasin_postion[0] < len(board)/2 and assasin_postion[1] > len(board[0])/2):
                if (assasin_dir[0] == -1 or assasin_dir[1]==1):
                    assasin_direction = [0,-1]
                    assasin_moves=[[0,0], [0,0]]
                elif (assasin_dir[0] == 1):
                    count = 0
                    for i in range(5):
                        if (board[assasin_postion[0]+1+i][assasin_postion[1]] != -1 and board[assasin_postion[0]+1+i][assasin_postion[1]] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        assasin_direction = [0,-1]
                        assasin_moves = [[0,-1], [0,-1]]
                    elif (count > 0 and count < 2):
                        assasin_direction = [0,-1]
                        assasin_moves = [[1,0], [0,-1]]
                    elif (count == 2):
                        assasin_direction = [1,0]
                        assasin_moves = [[1,0], [1, 0]]
                    else:
                        assasin_direction = [1,0]
                        assasin_moves = [[1,0], [1, 0]]
                elif (assasin_dir[1]==-1):
                    count = 0
                    for i in range(5):
                        if (board[assasin_postion[0]][assasin_postion[1]-i] != -1 and board[assasin_postion[0]][assasin_postion[1]-i] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        assasin_direction = [1,0]
                        assasin_moves = [[1,0], [1,0]]
                    elif (count > 0 and count < 2):
                        assasin_direction = [1,0]
                        assasin_moves = [[0,-1], [1,0]]
                    elif (count == 2):
                        assasin_direction = [0,-1]
                        assasin_moves = [[0,-1], [0, -1]]
                    else:
                        assasin_direction = [0,-1]
                        assasin_moves = [[0,-1], [0, -1]]
            if (assasin_postion[0] > len(board)/2 and assasin_postion[1] > len(board[0])/2):
                if (assasin_dir[0] == 1 or assasin_dir[1]==1):
                    assasin_direction = [0,-1]
                    assasin_moves=[[0,0], [0,0]]
                elif (assasin_dir[0] == -1):
                    count = 0
                    for i in range(5):
                        if (board[assasin_postion[0]-i][assasin_postion[1]] != -1 and board[assasin_postion[0]-i][assasin_postion[1]] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        assasin_direction = [0,-1]
                        assasin_moves = [[0,-1], [0,-1]]
                    elif (count > 0 and count < 2):
                        assasin_direction = [0,-1]
                        assasin_moves = [[-1,0], [0,-1]]
                    elif (count == 2):
                        assasin_direction = [-1,0]
                        assasin_moves = [[-1,0], [-1, 0]]
                    else:
                        assasin_direction = [-1,0]
                        assasin_moves = [[-1,0], [-1, 0]]
                elif (assasin_dir[1]==-1):
                    count = 0
                    for i in range(5):
                        if (board[assasin_postion[0]][assasin_postion[1]-i] != -1 and board[assasin_postion[0]][assasin_postion[1]-i] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        assasin_direction = [-1,0]
                        assasin_moves = [[-1,0], [-1,0]]
                    elif (count > 0 and count < 2):
                        assasin_direction = [-1,0]
                        assasin_moves = [[0,-1], [-1,0]]
                    elif (count == 2):
                        assasin_direction = [0,-1]
                        assasin_moves = [[0,-1], [0, -1]]
                    else:
                        assasin_direction = [0,-1]
                        assasin_moves = [[0,-1], [0, -1]]

            if (assasin_postion[0]>len(board)/2 and assasin_postion[1]<len(board[0])/2):
                if (assasin_dir[0] == 1 or assasin_dir[1]==-1):
                    assasin_direction = [0,1]
                    assasin_moves=[[0,0], [0,0]]
                elif (assasin_dir[0] == -1):
                    count = 0
                    for i in range(5):
                        if (board[assasin_postion[0]-i][assasin_postion[1]] != -1 and board[assasin_postion[0]-i][assasin_postion[1]] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        assasin_direction = [0,1]
                        assasin_moves = [[0,1], [0,1]]
                    elif (count > 0 and count < 2):
                        assasin_direction = [0,1]
                        assasin_moves = [[-1,0], [0,1]]
                    elif (count == 2):
                        assasin_direction = [-1,0]
                        assasin_moves = [[-1,0], [-1, 0]]
                    else:
                        assasin_direction = [-1,0]
                        assasin_moves = [[-1,0], [-1, 0]]
                elif (assasin_dir[1]==1):
                    print("here")
                    count = 0
                    for i in range(5):
                        if (board[assasin_postion[0]][assasin_postion[1]+1+i] != -1 and board[assasin_postion[0]][assasin_postion[1]+1+i] != 0):
                            count+=1
                    print(count)
                    if (count==0):
                        assasin_direction = [-1,0]
                        assasin_moves = [[-1,0], [-1,0]]
                    elif (count > 0 and count < 2):
                        assasin_direction = [-1,0]
                        assasin_moves = [[0,1], [-1,0]]
                    elif (count == 2):
                        assasin_direction = [0,1]
                        assasin_moves = [[0,1], [0, 1]]
                    else:
                        assasin_direction = [0,1]
                        assasin_moves = [[0,1], [0, 1]]
        if (assasin_moves and assasin_direction):
            print("True has move")
        else:
            print("No Move")
            assasin_moves = [random.choice(vals),random.choice(vals),random.choice(vals),random.choice(vals)]
            assasin_direction = random.choice(vals)
        if (spotter_moves and spotter_direction):
            print('Spot has move')
        else:
            spotter_moves = [random.choice(vals),random.choice(vals)]
            spotter_direction = random.choice(vals)
        
        # print({
        #     "Spotter":{
        #         "direction":spotter_direction, # or [-1,0],[0,1],[0,-1]
        #         "moves":spotter_moves # max length 2, 
        #         # if you input more than 2, truncated to first 2
        #         # if you dont input any, no move made
        #         # input [1,0] makes the bot move from (x,y) to (x+1,y)
        #         # other inputs include [-1,0],[0,1],[0,-1]
        #         # if you hit a wall/ edge of the map, that move is ignored and one of your 2 moves is used up
        #         # landing on an opponent kills them
        #     },
        #     "Assasin":{
        #         "direction":assasin_direction, # or [-1,0],[0,1],[0,-1]
        #         "moves":assasin_moves # max length 4, 
        #         # if you input more than 4, truncated to first 4
        #         # if you dont input any, no move made
        #         # input [1,0] makes the bot move from (x,y) to (x+1,y)
        #         # other inputs include [-1,0],[0,1],[0,-1]
        #         # if you hit a wall/ edge of the map, that move is ignored and one of your 4 moves is used up
        #         # landing on an opponent kills them
        #     }
        # })
        return {
            "Spotter":{
                "direction":spotter_direction, # or [-1,0],[0,1],[0,-1]
                "moves":spotter_moves # max length 2, 
                # if you input more than 2, truncated to first 2
                # if you dont input any, no move made
                # input [1,0] makes the bot move from (x,y) to (x+1,y)
                # other inputs include [-1,0],[0,1],[0,-1]
                # if you hit a wall/ edge of the map, that move is ignored and one of your 2 moves is used up
                # landing on an opponent kills them
            },
            "Assasin":{
                "direction":assasin_direction, # or [-1,0],[0,1],[0,-1]
                "moves":assasin_moves # max length 4, 
                # if you input more than 4, truncated to first 4
                # if you dont input any, no move made
                # input [1,0] makes the bot move from (x,y) to (x+1,y)
                # other inputs include [-1,0],[0,1],[0,-1]
                # if you hit a wall/ edge of the map, that move is ignored and one of your 4 moves is used up
                # landing on an opponent kills them
            },
            "Debug":"ASdasdasdas"
        }