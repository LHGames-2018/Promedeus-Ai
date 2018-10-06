from helper import *
import math

class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        if self.PlayerInfo.CarriedResources < self.PlayerInfo.CarryingCapacity:
            dest = find_closest(gameMap, (11,11), Resource)
        else:
            dest = find_closest(gameMap, (11,11), Home)

        print(dest)
        return create_move_action(Point(1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

    def find_closest(gameMap, start, tileType):
        frontier = Queue()
        frontier.put(start)

        came_from = {}
        came_from[start] = None

        # While there are tiles to search
        while not frontier.empty():
            current = frontier.get()

            # Check if tile is what we are looking for
            if gameMap.getTileAt(current) == tileType:
                break

            (x,y) = current
            neighbors = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
            neighbors = filter(lambda x,y : x >= 0 and x <= 20 and y >= 0 and y <= 20, neighbors)

            for n in neighbors:
                if n not in came_from:
                    frontier.put(n)
                    came_from[n] = current

        return came_from

    def map_to_graph(gameMap):
        vertices = []
        edges = [()]


    def generate_path(self, gameMap, dest):
        # Using A*

        start = (11,11)
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

