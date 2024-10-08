from serial import PARITY_NONE, STOPBITS_ONE, Serial


class HCS_3300_Interface_Exception(Exception):
    pass

class HCS_3300_INTERFACE():

    def open(self, **kwargs):
        pass

    def send(self, cmd):
        pass

    def recv(self) -> tuple[bool, str]:
        pass

    def close(self):
        pass


class HCS_3300_Serial(HCS_3300_INTERFACE):
    def __init__(self, serial_port=None, baudrate=9600, timeout=5):
        self.serial = None
        self._serial_port = serial_port
        self._baudrate = baudrate
        self._read_timeout = timeout
        if self._serial_port is not None:
            self.open()

    def open(self, **kwargs):
        # def open(self, serial_port=None, baudrate=None):
        serial_port = kwargs.get('serial_port')
        baudrate = kwargs.get('baudrate')

        if serial_port:
            self._serial_port = serial_port
        if baudrate:
            self._baudrate = baudrate

        if (self._serial_port and self._baudrate):
            self.serial = Serial(self._serial_port, self._baudrate, timeout=self._read_timeout, stopbits=STOPBITS_ONE, parity=PARITY_NONE)
        else:
            raise HCS_3300_Interface_Exception("No serial port or baudrate specified: {} {}".format(self._serial_port, self._baudrate))

    def send(self, cmd):
        data = (cmd +'\r').encode()
        wres = self.serial.write(data)
        return (wres > 0)

    def recv(self)-> tuple[bool, str]:
        resp = self.serial.read_until(b'\r')
        if b'OK' not in resp :
            respOK = self.serial.read_until(b'\r')
            if b'OK' not in respOK:
                return (False, None)
            else:
                return (True, resp.decode())
        else:
            return (True, None)

    def close(self):
        if self.serial is not None:
            self.serial.close()
            self.serial = None

