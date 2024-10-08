# HCS-3300
Python control over Manson HCS-3300 Power Source


# Installation
```
git clone git@github.com:maslovw/HCS-3300.git
cd HCS-3300
pip install -e .
```

## Update

`git pull`

# Usage

## command line
```bash
hcs3300 --help
usage: hcs3300 [-h] [-p PORT] [-u SETU] [-i SETI] [-on] [-off] [--waitU WAITU] [--getU] [--getI] [--getOut] [--verbose]

Script to control HCS_3300 via serial(USB) interface hcs3300 --off -u=12 --on: will turnoff the output, set 12V and turn the power on

options:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Serial port name, default is taken from ENV_VAR "HCS_3300"
  -u SETU, --setU SETU  Set Voltage (float value)
  -i SETI, --setI SETI  Set Current (float value)
  -on, --on             set to turn on the power, last action to execute
  -off, --off           set to turn off the power, first action to execute if specified
  --waitU WAITU         wait for the setU action to be applied with timeout, --waitU=0 to wait without timeout
  --getU                print Voltage
  --getI                print Current
  --getOut              print if the power is on or off
  --verbose             DEBUG Logging
```

### Configuration
#### Linux example

- find which port is assigned to HCS-3302 and add this to your .bashrc

```
export HCS_3300="/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0"
```

#### Windows example

- find which port is assigned to HCS-3302 and add this to your Environment Variables

```
HCS_3300="COM3"
```


### Example:

```bash
>> hcs3300 --setU=12 --on
setU(12.0V):  True
setOn:  True

>> hcs3300 --off --setU=6.5 --setI=2 --on
setOff:  True
setI(2.0A):  True
setU(6.5V):  True
setOn:  True

>> hcs3300 --getU
getU:  6.51

>> hcs3300 --getI
getI:  1.456
```

## Python

```python
import hcs_3300
from hcs_3300.interfaces import hcs_3300_Serial
from hcs_3300 import hcs_3300

com = hcs_3300_Serial('COM3')
power = hcs_3300(com)

power.setU(12.) # set voltage 12V
power.setOut(True) # turn it on

print(power.getUI())
print(power.getPower())
```
