class EnvTargetMap:
    def __init__(self):
        self.values = {
            "Breakout": 90,
            "Seaquest": 1150,
            "Qbert": 14000,
            "Pong": 20,
            "Alien": 200,
            "Amidar": 190,
            "Assault": 140,
            "Asterix": 220,
            "Asteroids": 29,
            "BankHeist": 90,
            "BattleZone": 32,
            "BeamRider": 144,
            "Bowling": 10,
            "Boxing": 89,
            "CrazyClimber": 743,
            "Freeway": 34,
            "Frostbite": 201,
            "Gravitar": 5,
            "Kangaroo": 75,
            "MsPacman": 394,
            "PrivateEye": 8,
            "SpaceInvaders": 242
        }

    def __getitem__(self, key):
        if key not in self.values:
            raise NotImplementedError()
        return self.values[key]

    def IsReady(name):
        #Environments that have issues
        if (name == "Alien"):
            return False
        return True