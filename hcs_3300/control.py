from serial import Serial
from time import sleep
from hcs_3300.interfaces import HCS_3300_INTERFACE
import logging


class HCS_3300_Exception(Exception):
    pass

class HCS_3300():
    def __init__(self, interface: HCS_3300_INTERFACE,  logLevel=logging.DEBUG):
        self.connection = interface
        self.logger = logging.getLogger('HCS-3300')
        self.logger.setLevel(logLevel)

    def open(self, **kwargs):
        self.logger.debug('open')
        self.connection.open(**kwargs)

    def close(self):
        self.logger.debug('close')
        self.connection.close()

    def __del__(self):
        self.close()

    def send(self, cmd: str) -> tuple[bool, str]:
        """
        :param cmd: python string without CR
        :return: (result: bool, response: str)
        """
        self.logger.debug('send: {}'.format(cmd))
        self.connection.send(cmd)
        ret = self.connection.recv()
        self.logger.debug('recv: {}'.format(ret))
        return ret


    def getUI(self) -> tuple[float, float]:
        res, resp = self.send('GETD')
        if not res or resp is None:
            return 0,0
        u = resp[0:4]
        i = resp[4:8]
        mode = resp[8:9]
        self.logger.debug('U: {}, I: {}, Mode: {}'.format(u, i, "CV" if mode == '0' else "CC"))
        return (int(u)/100, int(i)/100)

    def getU(self) -> float:
        u,_ = self.getUI()
        return u

    def getI(self):
        _,i = self.getUI()
        return i

    def setOut(self, state:bool) -> bool:
        """
        Turning on or off the output
        :param state:
        :return:
        """
        s = 0 if state else 1
        res, _ = self.send('SOUT{}'.format(s))
        return res

    def getOut(self) -> bool:
        """Get Output Status
        return state of the power supply
        :return: True if power is on
        """
        res, resp = self.send('GOUT')
        if not res or resp is None:
            raise HCS_3300_Exception("no response")
        return '0' in resp

    def setU(self, voltage):
        """Set output Voltage
        :param voltage - float
        """
        v = int(voltage*10)
        res, _ = self.send('VOLT{:03}'.format(v))
        return res

    def setI(self, current:float):
        """Set output Current
        :param current - float
        total power <= 80W
        """
        i = int(current * 10)
        res, _ = self.send('CURR{:03}'.format(i))
        return res


