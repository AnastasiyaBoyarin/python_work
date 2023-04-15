from time import sleep


class TrafficLight:
    __color = 'Red'

    def running(self):
        self.__color = 'Red'
        print(f'Color: {self.__color}')
        sleep(7)

        self.__color = 'Yellow'
        print(f'Color: {self.__color}')
        sleep(2)

        self.__color = 'Green'
        print(f'Color: {self.__color}')
        sleep(7)

        while True:
            self.running()


print("*****Simulating traffic light*****")
obj = TrafficLight()
obj.running()
