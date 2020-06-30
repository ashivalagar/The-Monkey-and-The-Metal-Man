import matplotlib
import matplotlib.pyplot as plt
import copy
from agent import HBDagent
from archer import archer
class Board:
    def __init__(self,height,width,walls,highPoints,history_file,agent_classes =[]):

        # define the possible spawn points as the 4 corners
        # default map
        spawn_points = [((0,0),(0,1)),((0,width-1),(1,width-1)),((height-1,width-1),(height-1,width-2)),((height-1,0),(height-2,0))]
        spawn_directions = [((1,0),(1,0)),((0,-1),(0,-1)),((-1,0),(-1,0)),((0,1),(0,1))]

        #board_tourney1_1
        # spawn_points = [((4,8),(4,7)),((8,14),(7,14)),((14,10),(14,11)),((10,4),(11,4))]
        # spawn_directions = [((1,0),(1,0)),((0,-1),(0,-1)),((-1,0),(-1,0)),((0,1),(0,1))]
        initialising_vals = [[*spawn_points[x],*spawn_directions[x]] for x in range(4)]
        # print(initialising_vals)
        # store size of the board
        self.size = (width,height)
        self.f = open(history_file,'w')
        # create the board
        self.walls = walls
        self.highPoints = highPoints
        board = [[1 for x in range(self.size[0])]for x in range(self.size[1])]
        for wall in walls:
            board[wall[0]][wall[1]] = 0
        
        for highPoint in highPoints:
            board[highPoint[0]][highPoint[1]] = 2
        self.board = board
        self.writeToHistory(str(board))
        # instantiate the pieces of each player
        self.agents = []
        for ind,initialising_val in enumerate(initialising_vals):
            self.agents.append((ind,*initialising_val,1,1,agent_classes[ind](*initialising_val)))
            pass
        self.writeToHistory(self.getStateStr())
        # self.agents stores agent data as an array:
        #   self.agents = [(agent ID, spotter point, assasin point, spotter direction,
        #                       assasin direction, spotter alive, assasin alive, agent object) ]

        # Collapsing map
        self.circles = 0
        self.timer = 5

        self.done = False

    def collapseMap(self):
        for x in range(len(self.board)):
            self.board[x][self.circles] = 0
            
        for x in range(len(self.board)):
            self.board[x][-self.circles-1] = 0

        for x in range(len(self.board[0])):
            self.board[self.circles][x] = 0

        for x in range(len(self.board[0])):
            self.board[-1-self.circles][x] = 0
        
        for agent in self.agents:
            (agent_id, spotter_point, assasin_point, spotter_direction, assasin_direction, spotter_alive, assasin_alive, agent_object) = agent
            if self.board[assasin_point[0]][assasin_point[1]] == 0:
                if assasin_alive:
                    self.agents[agent_id] = (agent_id, spotter_point, assasin_point, spotter_direction, assasin_direction, spotter_alive, 0, agent_object)
                    print("ASSASIN ID #{} just died to storm!".format(agent_id))

            (agent_id, spotter_point, assasin_point, spotter_direction, assasin_direction, spotter_alive, assasin_alive, agent_object) = self.agents[agent_id]
            if self.board[spotter_point[0]][spotter_point[1]] == 0:
                if spotter_alive:
                    self.agents[agent_id] = (agent_id, spotter_point, assasin_point, spotter_direction, assasin_direction, 0, assasin_alive, agent_object)
                    print("SPOTTER ID #{} just died to storm!".format(agent_id))

    def displayBoard(self):
        colors = 'black grey orange lime green'.split()
        board_copy = copy.deepcopy(self.board)


        for ind,other_agent in enumerate(self.agents):
                (other_agent_id, other_spotter_point, other_assasin_point, other_spotter_direction, other_assasin_direction, other_spotter_alive, other_assasin_alive, other_agent_object) = other_agent
                if other_spotter_alive:
                    board_copy[other_spotter_point[0]][other_spotter_point[1]] = 4
                if other_assasin_alive:
                    board_copy[other_assasin_point[0]][other_assasin_point[1]] = 3

        cmap = matplotlib.colors.ListedColormap(colors, name='colors', N=None)
        plt.imshow(board_copy, cmap=cmap)
        plt.show()

    def displayLOS(self,board):
        colors = 'black grey orange lime green red'.split()
        cmap = matplotlib.colors.ListedColormap(colors, name='colors', N=None)
        board_copy = copy.deepcopy(board)
        for ind,row in enumerate(board_copy):
            for ind2, element in enumerate(row):
                if isinstance(element,dict):
                    board_copy[ind][ind2] = 5
        plt.imshow(board_copy, cmap=cmap)
        plt.show()

    def writeToHistory(self,inp):
        self.f.write(inp+'\n')

    def calculatePercepts(self,agentId):

        agent_deets = self.agents[agentId]
        (_, spotter_point, assasin_point, spotter_direction, assasin_direction, spotter_alive, assasin_alive, agent_object) = agent_deets
        board = [[-1 for x in range(self.size[0])] for x in range(self.size[1])]
        all_points = []
        if spotter_alive:
            if spotter_point in self.highPoints:
                points = self.calculateLineOfSightHighground(spotter_point)
            else:
                points = self.calculateLineOfSightSpotter(spotter_point,spotter_direction)
            all_points += points
        if assasin_alive:
            points = self.calculateLineOfSightAssasin(assasin_point,assasin_direction)
            all_points += points

        for point in all_points:
            board[point[0]][point[1]] = self.board[point[0]][point[1]]

        for other_agent in self.agents[:agentId]+self.agents[agentId+1:]:
            (other_agent_id, other_spotter_point, other_assasin_point, other_spotter_direction, other_assasin_direction, other_spotter_alive, other_assasin_alive, _) = other_agent
            if other_spotter_alive:
                if board[other_spotter_point[0]][other_spotter_point[1]]!=-1:
                    board[other_spotter_point[0]][other_spotter_point[1]] = {
                        "playerId":other_agent_id,
                        "direction":other_spotter_direction,
                        "type":"spotter",
                        "square":board[other_spotter_point[0]][other_spotter_point[1]]
                    }
            if other_assasin_alive:
                if board[other_assasin_point[0]][other_assasin_point[1]]!=-1:
                    board[other_assasin_point[0]][other_assasin_point[1]] = {
                        "playerId":other_agent_id,
                        "direction":other_assasin_direction,
                        "type":"assasin",
                        "square":board[other_assasin_point[0]][other_assasin_point[1]]
                    }
        percepts = {
            "board":board,
            "timer":self.timer,
            "circles collapsed":self.circles,
            "spotter location":spotter_point,
            "assasin location":assasin_point,
            "spotter alive":spotter_alive,
            "assasin alive":assasin_alive,
            "spotter direction":spotter_direction,
            "assasin direction":assasin_direction
        }
        # print(percepts)
        # self.displayLOS(board)
        return percepts

    def gameStep(self):
        num_alive = 0
        for agent_deets in self.agents:
            (_, spotter_point, assasin_point, spotter_direction, assasin_direction, spotter_alive, assasin_alive, agent_object) = agent_deets
            if spotter_alive or assasin_alive:
                num_alive+=1

        if num_alive<=1:
            self.done = True
            self.writeToHistory(self.getStateStr())
            print("GAME OVER")
            return
            
        for ind,agent_deets in enumerate(self.agents):
            (_, spotter_point, assasin_point, spotter_direction, assasin_direction, spotter_alive, assasin_alive, agent_object) = agent_deets
            percepts = self.calculatePercepts(ind)
            if percepts["assasin alive"] or percepts["spotter alive"]:
                action = agent_object.step(percepts)
                self.agentStep(ind,action)
                self.writeToHistory(self.getStateStr())
        
        num_alive = 0
        for agent_deets in self.agents:
            (_, spotter_point, assasin_point, spotter_direction, assasin_direction, spotter_alive, assasin_alive, agent_object) = agent_deets
            if spotter_alive or assasin_alive:
                num_alive+=1

        if num_alive<=1:
            self.done = True
            self.writeToHistory(self.getStateStr())

            print("GAME OVER")
            return

        self.timer -= 1
        if self.timer == 0:
            self.timer = 5
            self.collapseMap()
            self.writeToHistory("0")
            self.writeToHistory(str(self.board))
            self.writeToHistory(self.getStateStr())
            self.circles += 1

    def agentStep(self,agentId,action):
        agent_deets = self.agents[agentId]
        (_, spotter_point, assasin_point, spotter_direction, assasin_direction, spotter_alive, assasin_alive, agent_object) = agent_deets
        spotter_move = action["Spotter"]
        assasin_move = action["Assasin"]
        current_assasin_point = assasin_point
        current_spotter_point = spotter_point
        current_spotter_direction = spotter_move["direction"]
        current_assasin_direction = assasin_move["direction"]

        if spotter_alive:
            moves = spotter_move["moves"]
            for x in range(2):
                if not moves:
                    break
                move = moves.pop(0)
                if self.checkBounds((current_spotter_point[0]+move[0],current_spotter_point[1]+move[1])) and self.board[current_spotter_point[0]+move[0]][current_spotter_point[1]+move[1]]!=0 and (current_spotter_point[0]+move[0],current_spotter_point[1]+move[1]) != current_assasin_point:
                    current_spotter_point = (current_spotter_point[0]+move[0],current_spotter_point[1]+move[1])
            
            for ind,other_agent in enumerate(self.agents[:agentId]+self.agents[agentId+1:]):
                (other_agent_id, other_spotter_point, other_assasin_point, other_spotter_direction, other_assasin_direction, other_spotter_alive, other_assasin_alive, other_agent_object) = other_agent
                if other_spotter_alive:
                    if other_spotter_point == current_spotter_point:
                        self.agents[other_agent_id] = (other_agent_id, other_spotter_point, other_assasin_point, other_spotter_direction, other_assasin_direction, 0, other_assasin_alive, other_agent_object)
                        print("SPOTTER ID #{} was killed!".format(other_agent_id))
                if other_assasin_alive:
                    if other_assasin_point == current_spotter_point:
                        self.agents[other_agent_id] = (other_agent_id, other_spotter_point, other_assasin_point, other_spotter_direction, other_assasin_direction, other_spotter_alive, 0, other_agent_object)
                        print("ASSASIN ID #{} was killed!".format(other_agent_id))

        if assasin_alive:
            moves = assasin_move["moves"]
            for x in range(4):
                if not moves:
                    break
                move = moves.pop(0)
                if self.checkBounds((current_assasin_point[0]+move[0],current_assasin_point[1]+move[1])) and self.board[current_assasin_point[0]+move[0]][current_assasin_point[1]+move[1]]!=0 and current_spotter_point != (current_assasin_point[0]+move[0],current_assasin_point[1]+move[1]):
                    current_assasin_point = (current_assasin_point[0]+move[0],current_assasin_point[1]+move[1])
            
            for ind,other_agent in enumerate(self.agents[:agentId]+self.agents[agentId+1:]):
                (other_agent_id, other_spotter_point, other_assasin_point, other_spotter_direction, other_assasin_direction, other_spotter_alive, other_assasin_alive, other_agent_object) = other_agent
                if other_spotter_alive:
                    if other_spotter_point == current_assasin_point:
                        self.agents[other_agent_id] = (other_agent_id, other_spotter_point, other_assasin_point, other_spotter_direction, other_assasin_direction, 0, other_assasin_alive, other_agent_object)
                        print("SPOTTER ID #{} was killed!".format(other_agent_id))
                if other_assasin_alive:
                    if other_assasin_point == current_assasin_point:
                        self.agents[other_agent_id] = (other_agent_id, other_spotter_point, other_assasin_point, other_spotter_direction, other_assasin_direction, other_spotter_alive, 0, other_agent_object)
                        print("ASSASIN ID #{} was killed!".format(other_agent_id))
        
        self.agents[agentId] = (agentId, current_spotter_point, current_assasin_point, current_spotter_direction, current_assasin_direction, spotter_alive, assasin_alive, agent_object)
    # check if the point is within the bound of the board
    def checkBounds(self,point):
        if point[0]<self.size[0] and point[0]>=0 and point[1]>=0 and point[1]<self.size[1]:
            return True
        return False

    def getStateStr(self):
        agents_state = ""
        for agent_deets in self.agents:
            agents_state+=str(agent_deets[:-1])+','
        return "["+agents_state[:-1]+"]"

    def calculateLineOfSightHighground(self,point):
        points = []
        for x in range(-5,6):
            limit = 5-abs(x)
            for y in range(-limit,limit+1):
                cur_point = (point[0]+x,point[1]+y)
                if self.checkBounds(cur_point):
                    points.append(cur_point)

        return points

    def calculateLineOfSightSpotter(self,point,direction):
        # self.board[point[0]][point[1]] = 4

        # initialising the different directions in consideration
        forward = []
        diagonal_counter_clock =[]
        diagonal_clock = []
        angled_counter_clock =[]
        angled_clock = []

        # check whether the direction being faced is one of the x directions
        if direction[0]:

            # generate the progressive points in the forward and diagonal directions
            forward = [(point[0]+x*direction[0],point[1])for x in range(1,6)]
            diagonal_counter_clock = [(point[0]+x*direction[0],point[1]+x*direction[0]) for x in range(1,4)]
            diagonal_clock = [(point[0]+x*direction[0],point[1]-x*direction[0]) for x in range(1,4)]

            # get all possibly viewable points between the forward line and diagonals

            # generate theses points as slices along the forward direction
            angled_counter_clock_1 = [(point[0]+x*direction[0],point[1]+direction[0]*1)for x in range(2,6)]
            angled_counter_clock_2 = [(point[0]+x*direction[0],point[1]+direction[0]*2)for x in range(3,6)]
            angled_counter_clock_3 = [(point[0]+x*direction[0],point[1]+direction[0]*3)for x in range(4,5)]
            angled_counter_clock = angled_counter_clock_1+angled_counter_clock_2+angled_counter_clock_3

            angled_clock_1 = [(point[0]+x*direction[0],point[1]-direction[0]*1)for x in range(2,6)]
            angled_clock_2 = [(point[0]+x*direction[0],point[1]-direction[0]*2)for x in range(3,6)]
            angled_clock_3 = [(point[0]+x*direction[0],point[1]-direction[0]*3)for x in range(4,5)]
            angled_clock = angled_clock_1+angled_clock_2+angled_clock_3
        else:
            
            # generate the progressive points in the forward and diagonal directions
            forward = [(point[0],point[1]+x*direction[1])for x in range(1,6)]
            diagonal_counter_clock = [(point[0]+x*direction[1],point[1]+x*direction[1]) for x in range(1,4)]
            diagonal_clock = [(point[0]-x*direction[1],point[1]+x*direction[1]) for x in range(1,4)]
            
            # get all possibly viewable points between the forward line and diagonals

            # generate theses points as slices along the forward direction
            angled_counter_clock_1 = [(point[0]+direction[1]*1,point[1]+x*direction[1])for x in range(2,6)]
            angled_counter_clock_2 = [(point[0]+direction[1]*2,point[1]+x*direction[1])for x in range(3,6)]
            angled_counter_clock_3 = [(point[0]+direction[1]*3,point[1]+x*direction[1])for x in range(4,5)]
            angled_counter_clock = angled_counter_clock_1+angled_counter_clock_2+angled_counter_clock_3

            angled_clock_1 = [(point[0]-direction[1]*1,point[1]+x*direction[1])for x in range(2,6)]
            angled_clock_2 = [(point[0]-direction[1]*2,point[1]+x*direction[1])for x in range(3,6)]
            angled_clock_3 = [(point[0]-direction[1]*3,point[1]+x*direction[1])for x in range(4,5)]
            angled_clock = angled_clock_1+angled_clock_2+angled_clock_3

        boundary = []
        viewable = set()

        # mark the points that are viewable along the forward direction
        for sq in forward:
            if not self.checkBounds(sq):
                break
            
            if self.board[sq[0]][sq[1]] == 0:
                boundary.append(sq)
                # self.board[sq[0]][sq[1]]= 3
                break
            viewable.add(sq)
            # self.board[sq[0]][sq[1]]= 3

        # mark the points that are viewable along the clockwise diagonal
        for sq in diagonal_clock:
            if not self.checkBounds(sq):
                break
            
            if self.board[sq[0]][sq[1]] == 0:
                boundary.append(sq)
                # self.board[sq[0]][sq[1]]= 3
                break
            viewable.add(sq)
            # self.board[sq[0]][sq[1]]= 3

        # mark the points that are viewable along the anti clockwise diagonal
        for sq in diagonal_counter_clock:
            if not self.checkBounds(sq):
                break
            
            if self.board[sq[0]][sq[1]] == 0:
                boundary.append(sq)
                # self.board[sq[0]][sq[1]]= 3
                break
            viewable.add(sq)
            # self.board[sq[0]][sq[1]]= 3

        # mark the points that are viewable along the angled clockwise direction
        # mark as viewable if the point has two pre requisite points - one "behind" it and the appropriately "diagonally behind it"
        for sq in angled_clock:
            if not self.checkBounds(sq):
                continue
            if direction[0]:
                if (sq[0]-direction[0],sq[1]) in viewable and (sq[0]-direction[0],sq[1]+direction[0]) in viewable:
                    if self.board[sq[0]][sq[1]] == 0:
                        boundary.append(sq)
                        # self.board[sq[0]][sq[1]]= 3
                    else:
                        viewable.add(sq)
                        # self.board[sq[0]][sq[1]]= 3
            else:
                if (sq[0],sq[1]-direction[1]) in viewable and (sq[0]+direction[1],sq[1]-direction[1]) in viewable:
                    if self.board[sq[0]][sq[1]] == 0:
                        boundary.append(sq)
                        # self.board[sq[0]][sq[1]]= 3
                    else:
                        viewable.add(sq)
                        # self.board[sq[0]][sq[1]]= 3

        # mark the points that are viewable along the angled counter clockwise direction
        # mark as viewable if the point has two pre requisite points - one "behind" it and the appropriately "diagonally behind it"
        for sq in angled_counter_clock:
            if not self.checkBounds(sq):
                continue
            if direction[0]:
                if (sq[0]-direction[0],sq[1]) in viewable and (sq[0]-direction[0],sq[1]-direction[0]) in viewable:
                    if self.board[sq[0]][sq[1]] == 0:
                        boundary.append(sq)
                        # self.board[sq[0]][sq[1]]= 3
                    else:
                        viewable.add(sq)
                        # self.board[sq[0]][sq[1]]= 3
            else:
                if (sq[0],sq[1]-direction[1]) in viewable and (sq[0]-direction[1],sq[1]-direction[1]) in viewable:
                    if self.board[sq[0]][sq[1]] == 0:
                        boundary.append(sq)
                        # self.board[sq[0]][sq[1]]= 3
                    else:
                        viewable.add(sq)
                        # self.board[sq[0]][sq[1]]= 3

        return list(viewable)+boundary+[point]

    def calculateLineOfSightAssasin(self,point,direction):
        # self.board[point[0]][point[1]] = 4

        # initialising the different directions in consideration
        forward = []
        diagonal_counter_clock =[]
        diagonal_clock = []
        angled_counter_clock =[]
        angled_clock = []

        # check whether the direction being faced is one of the x directions
        if direction[0]:

            # generate the progressive points in the forward and diagonal directions
            forward = [(point[0]+x*direction[0],point[1])for x in range(1,3)]
            diagonal_counter_clock = [(point[0]+x*direction[0],point[1]+x*direction[0]) for x in range(1,2)]
            diagonal_clock = [(point[0]+x*direction[0],point[1]-x*direction[0]) for x in range(1,2)]

            # get all possibly viewable points between the forward line and diagonals

            # generate theses points as slices along the forward direction
            angled_counter_clock = [(point[0]+x*direction[0],point[1]+direction[0]*1)for x in range(2,3)]
            angled_clock = [(point[0]+x*direction[0],point[1]-direction[0]*1)for x in range(2,3)]
        else:
            
            # generate the progressive points in the forward and diagonal directions
            forward = [(point[0],point[1]+x*direction[1])for x in range(1,3)]
            diagonal_counter_clock = [(point[0]+x*direction[1],point[1]+x*direction[1]) for x in range(1,2)]
            diagonal_clock = [(point[0]-x*direction[1],point[1]+x*direction[1]) for x in range(1,2)]
            
            # get all possibly viewable points between the forward line and diagonals

            # generate theses points as slices along the forward direction
            angled_counter_clock = [(point[0]+direction[1]*1,point[1]+x*direction[1])for x in range(2,3)]
            angled_clock = [(point[0]-direction[1]*1,point[1]+x*direction[1])for x in range(2,3)]

        boundary = []
        viewable = set()

        # mark the points that are viewable along the forward direction
        for sq in forward:
            if not self.checkBounds(sq):
                break
            
            if self.board[sq[0]][sq[1]] == 0:
                boundary.append(sq)
                # self.board[sq[0]][sq[1]]= 3
                break
            viewable.add(sq)
            # self.board[sq[0]][sq[1]]= 3

        # mark the points that are viewable along the clockwise diagonal
        for sq in diagonal_clock:
            if not self.checkBounds(sq):
                break
            
            if self.board[sq[0]][sq[1]] == 0:
                boundary.append(sq)
                # self.board[sq[0]][sq[1]]= 3
                break
            viewable.add(sq)
            # self.board[sq[0]][sq[1]]= 3

        # mark the points that are viewable along the anti clockwise diagonal
        for sq in diagonal_counter_clock:
            if not self.checkBounds(sq):
                break
            
            if self.board[sq[0]][sq[1]] == 0:
                boundary.append(sq)
                # self.board[sq[0]][sq[1]]= 3
                break
            viewable.add(sq)
            # self.board[sq[0]][sq[1]]= 3

        # mark the points that are viewable along the angled clockwise direction
        # mark as viewable if the point has two pre requisite points - one "behind" it and the appropriately "diagonally behind it"
        for sq in angled_clock:
            if not self.checkBounds(sq):
                continue
            if direction[0]:
                if (sq[0]-direction[0],sq[1]) in viewable and (sq[0]-direction[0],sq[1]+direction[0]) in viewable:
                    if self.board[sq[0]][sq[1]] == 0:
                        boundary.append(sq)
                        # self.board[sq[0]][sq[1]]= 3
                    else:
                        viewable.add(sq)
                        # self.board[sq[0]][sq[1]]= 3
            else:
                if (sq[0],sq[1]-direction[1]) in viewable and (sq[0]+direction[1],sq[1]-direction[1]) in viewable:
                    if self.board[sq[0]][sq[1]] == 0:
                        boundary.append(sq)
                        # self.board[sq[0]][sq[1]]= 3
                    else:
                        viewable.add(sq)
                        # self.board[sq[0]][sq[1]]= 3

        # mark the points that are viewable along the angled counter clockwise direction
        # mark as viewable if the point has two pre requisite points - one "behind" it and the appropriately "diagonally behind it"
        for sq in angled_counter_clock:
            if not self.checkBounds(sq):
                continue
            if direction[0]:
                if (sq[0]-direction[0],sq[1]) in viewable and (sq[0]-direction[0],sq[1]-direction[0]) in viewable:
                    if self.board[sq[0]][sq[1]] == 0:
                        boundary.append(sq)
                        # self.board[sq[0]][sq[1]]= 3
                    else:
                        viewable.add(sq)
                        # self.board[sq[0]][sq[1]]= 3
            else:
                if (sq[0],sq[1]-direction[1]) in viewable and (sq[0]-direction[1],sq[1]-direction[1]) in viewable:
                    if self.board[sq[0]][sq[1]] == 0:
                        boundary.append(sq)
                        # self.board[sq[0]][sq[1]]= 3
                    else:
                        viewable.add(sq)
                        # self.board[sq[0]][sq[1]]= 3

        return list(viewable)+boundary+[point]

if __name__ == "__main__":
    height = 19
    width = 19
    walls = []
    highPoints = []
    f = open("./board1")
    for x in range(width):
        stuff = f.readline()
        # print(len(stuff))
        for ind,letters in enumerate(stuff):
            if letters == "W":
                walls.append((x,ind))
            elif letters =="O":
                highPoints.append((x,ind))
    f.close()
    board = Board(height,width,walls,highPoints,'history.hbd',agent_classes=[archer,archer,archer,archer])
    while not board.done:
        board.gameStep()
        # board.displayBoard()