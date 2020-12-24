from time import sleep
class TrafficLight():

    def running(self):
        self.__color = ['red', 'yellow', 'green']
        light = 0
        while light !=3:
            print(self.__color[light])
            if light == 0:
                sleep(7)
            elif light == 1:
                sleep(2)
            elif light == 2:
                sleep(17)
            light += 1

t = TrafficLight()
t.running()