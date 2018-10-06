from helper import *
import math
import queue
from random import randint

class Bot: 
    def __init__(self):
        self.path = []
        self.index = 0

    def before_turn(self, playerInfo):
        """
		Gets called before ExecuteTurn. This is where you get your bot's state.
		    :param playerInfo: Your bot's current state.
        """
        
        self.PlayerInfo = playerInfo
        
        """
        test = [Point(0, 1), Point(0, 1), Point(0, 1), Point(0, 1)]

        if StorageHelper.read("isInit") == None:
            print("initialized")
            StorageHelper.write("isInit", True)
            StorageHelper.write("bptr", json.dumps(test))
            StorageHelper.write("posInPath", 0)

        print(StorageHelper.read("isInit"))
        print(StorageHelper.read("bptr"))
        for tuple in json.loads(StorageHelper.read("bptr")):
            self.path.append(Point(tuple[0], tuple[1]))

        self.index = StorageHelper.read("posInPath")
        """
        pass

    def execute_turn(self, gameMap, visiblePlayers):
        """
		This is where you decide what action to take.
			:param gameMap: The gamemap.
			:param visiblePlayers:  The list of visible players.
        """
        """
        if StorageHelper.read("posInPath") < len(self.path):
            StorageHelper.write("posInPath", StorageHelper.read("posInPath") + 1)
            return create_move_action(self.path[self.index])
        """

        if StorageHelper.read("house") == None:
            house = self.find_closest(gameMap, self.PlayerInfo.Position, TileContent.House)   
            StorageHelper.write("house", (house.x, house.y))

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        dropoff = False
        if self.PlayerInfo.CarriedResources < self.PlayerInfo.CarryingCapacity:
            dest = self.find_closest(gameMap, self.PlayerInfo.Position, TileContent.Resource)
        else:
            dropoff = True
            dest = self.find_closest(gameMap, self.PlayerInfo.Position, TileContent.House)

        print(self.PlayerInfo.Position)
        print(dest)
        print(self.PlayerInfo.CarriedResources)

        if dest == None:
            r = randint(0,3)
            if r == 0:
                return create_move_action(Point(1, 0))
            elif r == 1:
                return create_move_action(Point(-1, 0))
            elif r == 2:
                return create_move_action(Point(0, 1))
            elif r == 3:
                return create_move_action(Point(0, -1))
 
        if Point.Distance(dest, self.PlayerInfo.Position) == 1 and not dropoff:
            return create_collect_action(dest - self.PlayerInfo.Position)
 
        if dest.x - self.PlayerInfo.Position.x < 0:
            return self.move(gameMap, Point(-1,0))
        elif dest.x - self.PlayerInfo.Position.x > 0:
            return self.move(gameMap, Point(1,0))
        elif dest.y - self.PlayerInfo.Position.y < 0:
            return self.move(gameMap, Point(0,-1))
        elif dest.y - self.PlayerInfo.Position.y > 0:
            return self.move(gameMap, Point(0,1))

    def move(self, gameMap, direction):
        if gameMap.getTileAt(self.PlayerInfo.Position + direction) == TileContent.Wall:
            return create_attack_action(direction)
        else:
            return create_move_action(direction)
    
    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

    def find_closest(self, gameMap, start, tileType):
        points = []
        for x in range (start.x - 10, start.x + 10):
            for y in range (start.y - 10, start.y + 10):
                if gameMap.getTileAt(Point(x,y)) == tileType:
                    points.append(Point(x,y))

        if not points:
            return None
        
        closest = points[0]
        for p in points:
            if Point.Distance(start, p) < Point.Distance(start, closest):
                closest = p

        return closest

    def find_resource(self, gameMap):
        for x in range (0,20):
            for y in range (0,20):
                if gameMap.getTileAt(Point(x,y)) == TileContent.Resource:
                    return (x,y)
        
        return (10,10)

    def map_to_graph(gameMap):
        vertices = []
        edges = [()]


    def generate_path(self, gameMap, dest):
        # Using A*

        start = (10,10)
        nodes = []
        for x in range (0,20):
            for y in range (0,20):
                nodes.append((x,y))

        # Set of nodes already evaluated
        closedSet = Set()

        # Set of currently discovered nodes that have not been evaluated
        openSet = Set([start])

        # List of tuples which contain two nodes (node a, node b 
        # that can be most efficiently reached from node).
        # Empty at the beginning.
        cameFrom = []

        # For each tile, total cost of getting from the start tile to that node
        gScore = []
        gScore.append((start, 0))	# Going from start to start is zero

        # For each node, the total cost of getting from the start node to the goal
        # by passing by that node. That value is partly known, partly heuristic.
        fScore = []
        for node in nodes:
            fScore.append(node, math.inf)	

        for fscore in fScore:
            if fscore[0] == start:
                fscore[1] = 0

    def heuristic(a, b):
        (x1, y1) = a
        (x2, y2) = b
        return abs(x1 - x2) + abs(y1 - y2)

    def get_ressource(self, gameMap):
        # Collect resources
        if gameMap.getTileAt(1, 0) == TileContent.Resource:
            return create_collect_action(Point(1, 0))
        elif gameMap.getTileAt(0, 1) == TileContent.Resource:
            return create_collect_action(Point(0, 1))
        elif gameMap.getTileAt(0, -1) == TileContent.Resource:
            return create_collect_action(Point(0, -1))
        elif gameMap.getTileAt(-1, 0) == TileContent.Resource:
            return create_collect_action(Point(-1, 0))
