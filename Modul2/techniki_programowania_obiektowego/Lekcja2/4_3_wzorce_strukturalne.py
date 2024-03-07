'''
Wzorce strukturalne w Pythonie
'''

# FASADA

# Subsystem 1
class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")


# Subsystem 2
class Lights:
    def turn_on(self):
        print("Lights turned on")

    def turn_off(self):
        print("Lights turned off")


# Subsystem 3
class AirConditioning:
    def turn_on(self):
        print("Air conditioning turned on")

    def turn_off(self):
        print("Air conditioning turned off")


# Fasada
class CarSystem:
    def __init__(self):
        self.engine = Engine()
        self.lights = Lights()
        self.air_conditioning = AirConditioning()

    def start_car(self):
        self.engine.start()
        self.lights.turn_on()
        self.air_conditioning.turn_on()

    def stop_car(self):
        self.engine.stop()
        self.lights.turn_off()
        self.air_conditioning.turn_off()


# Client code
# car_system = CarSystem()
# car_system.start_car()
# print("Driving...")
# car_system.stop_car()


# ADAPTER
        
# Istniejący interfejs
class EuropeanSocketInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def earth(self):
        pass


# Implementacja interfejsu istniejącego
class Socket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# Interfejs oczekiwany przez klienta
class USASocketInterface:
    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass


# Adapter
class Adapter(USASocketInterface):
    def __init__(self, socket):
        self.socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.socket.live()

    def neutral(self):
        return self.socket.neutral()


# Klient
class ElectricKettle:
    def __init__(self, power):
        self.power = power

    def boil(self, adapter):
        if adapter.voltage() > 110:
            print("Kettle cannot be used")
        else:
            if adapter.live() == 1 and adapter.neutral() == -1:
                print("Kettle is boiling!")
            else:
                print("Kettle cannot be used")

# socket = Socket()
# adapter = Adapter(socket)
# kettle = ElectricKettle(120)
# kettle.boil(adapter)


# PEŁNOMOCNIK  
# Interfejs Subject
class Subject:
    def request(self):
        pass


# RealSubject
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")


# Proxy
class Proxy(Subject):
    def __init__(self):
        self._real_subject = None

    def request(self):
        if self._real_subject is None:
            self._real_subject = RealSubject()
        self._real_subject.request()


# proxy = Proxy()
# proxy.request()
