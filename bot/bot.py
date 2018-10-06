from helper import *

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
		if(playerInfo.carriedResources < playerInfo.carryingCapacity)
			dest = find_closest_resource(gameMap)
		else
			dest = find_home(gameMap)

		return create_move_action(Point(1, 0))

    def after_turn(self):
        """
        Gets called after executeTurn
        """
        pass

	def find_closest_resource(self, gameMap):
		# Find closest resource
		for x in range (0,20):
			for y in range (0,20):
				if (gameMap.getTileAt(x,y) == Resource)
					return = (x,y)


	def find_home(self, gameMap):
		# Find closest resource
		for x in range (0,20):
			for y in range (0,20):
				if (gameMap.getTileAt(x,y) == House)
					return = (x,y)
	def map_to_graph(gameMap):
		vertices = []
		edges = [()]

		
