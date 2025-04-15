# Clase principal Robot
class Robot:
    def _init_(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.sensores = []  # Lista para almacenar sensores
        self.motores = []   # Lista para almacenar motores

    def agregar_sensor(self, sensor):
        self.sensores.append(sensor)

    def agregar_motor(self, motor):
        self.motores.append(motor)

    def mostrar_info(self):
        print(f"Robot: {self.nombre}, Modelo: {self.modelo}")
        print("Sensores:")
        for sensor in self.sensores:
            print(f" - {sensor.tipo}")
        print("Motores:")
        for motor in self.motores:
            print(f" - {motor.tipo}")

# Clase Sensor
class Sensor:
    def _init_(self, tipo):
        self.tipo = tipo

# Clase Motor
class Motor:
    def _init_(self, tipo):
        self.tipo = tipo

