class Games:
    def __init__(self, speed, size, age):
        self.speed=speed
        self.size=size
        self.age=age
    def moving(self, region):
        print('차량 이동')
        print("{0}으로 이동합니다. 속도: {1}".format(region, self.speed))
    def gasoline(self, oil):
        self.speed+=oil
        print("현재 속도: {0}".format(self.speed))
sonata=Games(90,80,4)
sonata.moving("문경")
sonata.gasoline(32)


