from helper import *


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

    def execute_turn(self, gameMap, visiblePlayers):
        """
        This is where you decide what action to take.
            :param gameMap: The gamemap.
            :param visiblePlayers:  The list of visible players.
        """

        if StorageHelper.read("posInPath") < len(self.path):
            StorageHelper.write("posInPath", StorageHelper.read("posInPath") + 1)
            return create_move_action(self.path[self.index])


        # Write your bot here. Use functions from aiHelper to instantiate your actions.
        if self.PlayerInfo.carriedResources < self.PlayerInfo.carryingCapacity:
            self.get_ressource()
            #dest = find_closest_resource(gameMap)
        else:
            pass
            #dest = find_home(gameMap)

        return create_move_action(Point(1, 0))


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
