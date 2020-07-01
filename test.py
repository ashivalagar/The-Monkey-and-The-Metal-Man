if (assasin_postion[0] in [7,8,9,10,11] and assasin_postion[1] in [7,8,9,10,11]):
            # assasin_moves=[[0,0], [0,0]]
            # assasin_direction = [1,0]
            assasin_moves = [random.choice(vals),random.choice(vals)]
            assasin_direction = random.choice(vals)
        else:
            if (assasin_postion[0] < len(board)/2 and assasin_postion[1]< len(board[0])/2):
                if (assasin_dir[0] == -1 or assasin_dir[1]==-1):
                    assasin_direction = [0,1]
                    assasin_postion=[[0,0], [0,0]]
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
                    assasin_postion=[[0,0], [0,0]]
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
                    assasin_postion=[[0,0], [0,0]]
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
                    assasin_postion=[[0,0], [0,0]]
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