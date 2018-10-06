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

        upgradePriority = [UpgradeType.CollectingSpeed, UpgradeType.CarryingCapacity, UpgradeType.AttackPower]
        upgradePrices = [10000, 15000, 25000, 50000, 100000]
        itemPrice = 30000

        if self.PlayerInfo.Position == self.PlayerInfo.HouseLocation:
            currentLevel = 0
            for upgrade in upgradePriority:
                if currentLevel > self.PlayerInfo.getUpgradeLevel(upgrade):
                    if self.PlayerInfo.TotalResources >= upgradePrices[self.PlayerInfo.getUpgradeLevel(upgrade) + 1]:
                        return create_upgrade_action(upgrade)
                currentLevel = self.PlayerInfo.getUpgradeLevel(upgrade) 
        
        dropoff = False

        if self.PlayerInfo.CarriedResources < self.PlayerInfo.CarryingCapacity:
            closestResource = self.find_closest(gameMap, self.PlayerInfo.Position, TileContent.Resource)
            closestPlayer = self.find_closest(gameMap, self.PlayerInfo.Position, TileContent.Player)
            closestHouse = self.find_closest(gameMap, self.PlayerInfo.Position, TileContent.House) 
            closestShop = self.find_closest(gameMap, self.PlayerInfo.Position, TileContent.Shop)

            pointsOfInterest = list(filter(lambda p : p != None, [closestResource, closestPlayer, closestHouse]))
            if not pointsOfInterest:
                return self.randomMove()
            else:
                distances = list(map(lambda p : Point.Distance(p, self.PlayerInfo.Position), pointsOfInterest))
                dest = pointsOfInterest[distances.index(min(distances))]

            # Remove after
            if closestShop != None:
                if self.PlayerInfo.Position == closestShop:
                    return create_purchase_action(PurchasableItem.Sword)
                else:
                    dest = closestShop
            else:
                return self.move(gameMap, Point(0,1))

        else:
            dropoff = True
            dest = self.PlayerInfo.HouseLocation
 
        print(self.PlayerInfo.Position)
        print(dest)
        print(self.PlayerInfo.CarriedResources)
        print(self.PlayerInfo.TotalResources)
 
        if Point.Distance(dest, self.PlayerInfo.Position) == 1 and not dropoff:
            print("Collecting")
            return create_collect_action(dest - self.PlayerInfo.Position)

        """
        data = StorageHelper.read("path")
        if data == None:
            path = self.generate_path(gameMap, dest)
            return self.move_along(gameMap, path)
        else:
            return self.move_along(gameMap, self.get_queue_from_path_data(data))
        

        """	
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
        elif gameMap.getTileAt(self.PlayerInfo.Position + direction) == TileContent.Player:
            return create_attack_action(direction)
        elif gameMap.getTileAt(self.PlayerInfo.Position + direction) == TileContent.Resource:
            return create_move_action(Point(direction.y, direction.x))
        else:
            return create_move_action(direction)
    
    def random_move(self):
        r = randint(0,3)
        if r == 0:
            return create_move_action(Point(1, 0))
        elif r == 1:
            return create_move_action(Point(-1, 0))
        elif r == 2:
            return create_move_action(Point(0, 1))
        elif r == 3:
            return create_move_action(Point(0, -1))

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
                    # Ignore ourself when looking for player to kill
                    if tileType == TileContent.Player and start == Point(x,y):
                        continue
                    # Ignore our house when looking for house to steal
                    elif tileType == TileContent.House and self.PlayerInfo.HouseLocation == Point(x,y):
                        continue
                    else:
                        points.append(Point(x,y))

        if not points:
            return None
        
        closest = points[0]
        for p in points:
            if Point.Distance(start, p) < Point.Distance(start, closest):
                closest = p

        return closest



    def generate_path(self, gameMap, dest):
        # Using A*

        print("Generating path")

        current_pos = self.PlayerInfo.Position
        path = queue.Queue()
        path.put(current_pos)

        while(not (current_pos == dest)):
            p = Point(0,0)
            if dest.x - current_pos.x < 0:
                p = Point(-1, 0) 
            elif dest.x - current_pos.x > 0:
                p = Point(1, 0) 
            elif dest.y - current_pos.y < 0:
                p = Point(0, -1) 
            elif dest.y - current_pos.y > 0:
                p = Point(0, 1) 

            path.put(p)
            current_pos += p

        return path

    def serialize_path_queue_for_data(self, path):
        tuple_path = []
        while not path.empty():
            point = path.get()
            tuple_path.append((point.x, point.y))

        return tuple_path

    def get_queue_from_path_data(self, data):
        path = queue.Queue()
        for tuple in data:
            path.put(Point(tuple[0], tuple[1]))
        
        return path

    def move_along(self, gameMap, path):
        print(path)
        next_move = path.get()
        StorageHelper.write("path", self.serialize_path_queue_for_data(path))

        return self.move(gameMap, next_move)

