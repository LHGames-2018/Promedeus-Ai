from helper import *
from StorageHelper import *

class Bot:
    def __init__(self):
        pass

    def before_turn(self, playerInfo):
        """
        Gets called before ExecuteTurn. This is where you get your bot's state.
            :param playerInfo: Your bot's current state.
        """
        self.PlayerInfo = playerInfo
        if read("isInit") == None:
            write("isInit", True) 
            write("bptr", [Point(-1,0),Point(-1,0),Point(-1,0),Point(-1,0)])
            write("posInPath") = 0

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        if read("posInPath") < len(read("bptr")):
            return create_move_action(read("bptr"))
            write("posInPath", read("posInPath") + 1)
            
        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        """ 
        if(playerInfo.carriedResources < playerInfo.carryingCapacity)
			dest = find_closest_resource(gameMap)
		else
			dest = find_home(gameMap)

		return create_move_action(Point(1, 0))
        """

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

    def find_closest_resource(self, gameMap):
        # Find closest resource
        for x in range (0, 20):
            for y in range (0, 20):
                if gameMap.getTileAt(x, y) == TileContent.Resource:
                    return (x, y)

    def find_home(self, gameMap):
        # Find closest resource
        for x in range (0, 20):
            for y in range (0, 20):
                if gameMap.getTileAt(x, y) == TileContent.House:
                    return (x, y)


	def find_home(self, gameMap):
		# Find closest resource
		for x in range (0,20):
			for y in range (0,20):
				if (gameMap.getTileAt(x,y) == House)
					return = (x,y)

    def get_resource(self, gameMap)
        #Collect resources
        if gameMap.getTileAt(1,0) == Resource
            return create_collect_action(Point(1,0))
        else if gameMap.getTileAt(0,1) == Resource
            return create_collect_action(Point(0,1))
        else if gameMap.getTileAt(0,-1) == Resource
            return create_collect_action(Point(0,-1))
        else if gameMap.getTileAt(-1,0) == Resource
            return create_collect_action(Point(-1,0))


		
