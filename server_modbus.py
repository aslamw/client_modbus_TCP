from pyModbusTCP.server import DataBank, ModbusServer
import random, os
from time import sleep

class ServerModbus:
    def __init__(self, host_ip, port):
        self._server = ModbusServer(host=host_ip,port=port, no_block=True)
        self._db = DataBank
        
    def run(self):
        try:
            self._server.start()
            print("servidor Moddbus rodando")
            while True:
                self._db.set_words(1000,[random.randrange(int(0.95*400),int(1.05*400))])
                
                #os.system('cls')
                
                print("="*8)
                print("Tabela Modbus")
                print(f"Holding Register \r\n R1000: {self._db.get_words(1000)} \r\n R2000: {self._db.get_words(2000)}")
                
                print(f"coil \r\n R1000: {self._db.get_bits(1000)}")
                sleep(2)
        except Exception as e:
            
            print(f"erro: {e.args}")
        