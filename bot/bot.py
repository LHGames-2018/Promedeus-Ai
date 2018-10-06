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
        if StorageHelper.read("isInit") is None:
            StorageHelper.write("isInit", True)
            StorageHelper.write("bptr", [Point(0, 1), Point(0, 1),Point(0, 1), Point(0, 1)])
            StorageHelper.write("posInPath", 0)

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        if StorageHelper.read("posInPath") < len(StorageHelper.read("bptr")):
            StorageHelper.write("posInPath", StorageHelper.read("posInPath") + 1)
            return create_move_action(StorageHelper.read("bptr"))


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
        for x in range(0, 20):
            for y in range(0, 20):
                if gameMap.getTileAt(x, y) == TileContent.Resource:
                    return (x, y)

    def find_home(self, gameMap):
        # Find closest resource
        for x in range(0, 20):
            for y in range(0, 20):
                if gameMap.getTileAt(x, y) == TileContent.House:
                    return (x, y)

    def get_resource(self, gameMap):
        # Collect resources
        if gameMap.getTileAt(1, 0) == TileContent.Resource:
            return create_collect_action(Point(1, 0))
        elif gameMap.getTileAt(0, 1) == TileContent.Resource:
            return create_collect_action(Point(0, 1))
        elif gameMap.getTileAt(0, -1) == TileContent.Resource:
            return create_collect_action(Point(0, -1))
        elif gameMap.getTileAt(-1, 0) == TileContent.Resource:
            return create_collect_action(Point(-1, 0))
