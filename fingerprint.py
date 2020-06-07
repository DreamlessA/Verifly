# The MIT License (MIT)
#
# Copyright (c) 2017 ladyada for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_fingerprint`
====================================================

This library will let you use an Adafruit Fingerprint sensor on any UART to get, store,
retreive and query fingerprints! Great for adding bio-sensing security to your next build.

* Author(s): ladyada

Implementation Notes
--------------------

**Hardware:**

* `Fingerprint sensor <https://www.adafruit.com/product/751>`_ (Product ID: 751)

**Software and Dependencies:**

* Adafruit CircuitPython firmware (2.2.0+) for the ESP8622 and M0-based boards:
  https://github.com/adafruit/circuitpython/releases
"""

from micropython import const
import time
import math
try:
    import struct
except ImportError:
    import ustruct as struct

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Fingerprint.git"

_STARTCODE = const(0xEF01)
_COMMANDPACKET = const(0x1)
_DATAPACKET = const(0x2)
_ACKPACKET = const(0x7)
_ENDDATAPACKET = const(0x8)

_GETIMAGE = const(0x01)
_UPIMAGE = const(0x0a) #sensor to device
_DOWNIMAGE = const(0x0b) #device to sensor
_IMAGE2TZ = const(0x02)
_MATCH = const(0x03)
_REGMODEL = const(0x05)
_STORE = const(0x06)
_LOAD = const(0x07)
_UPCHAR = const(0x08) #sensor to device
_DOWNCHAR = const(0x09) #device to sensor
_DELETE = const(0x0C)
_EMPTY = const(0x0D)
_HISPEEDSEARCH = const(0x1B)
_VERIFYPASSWORD = const(0x13)
_TEMPLATECOUNT = const(0x1D)
_TEMPLATEREAD = const(0x1F)

# Packet error code
OK = const(0x0)
PACKETRECIEVEERR = const(0x01)
NOFINGER = const(0x02)
IMAGEFAIL = const(0x03)
IMAGEMESS = const(0x06)
FEATUREFAIL = const(0x07)
NOMATCH = const(0x08)
NOTFOUND = const(0x09)
ENROLLMISMATCH = const(0x0A)
BADLOCATION = const(0x0B)
DBRANGEFAIL = const(0x0C)
UPLOADFEATUREFAIL = const(0x0D)
PACKETRESPONSEFAIL = const(0x0E)
UPLOADFAIL = const(0x0F)
DELETEFAIL = const(0x10)
DBCLEARFAIL = const(0x11)
PASSFAIL = const(0x13)
INVALIDIMAGE = const(0x15)
FLASHERR = const(0x18)
INVALIDREG = const(0x1A)
ADDRCODE = const(0x20)
PASSVERIFY = const(0x21)

#other constants
NOSUM_LEN = 6
HEADER_LEN = 9
TEMPLATE_PACKET_COUNT = 12
TEMPLATE_PACKET_DATA_LEN = 128

#Debug
DEBUG_FLAG = False

class Adafruit_Fingerprint:
    """UART based fingerprint sensor."""
    _uart = None

    password = None
    address = [0xFF, 0xFF, 0xFF, 0xFF]
    finger_id = None
    confidence = None
    templates = []
    template_count = None

    def __init__(self, uart, passwd=(0, 0, 0, 0)):
    # Create object with UART for interface, and default 32-bit password
        self.password = passwd
        self._uart = uart
        if self.verify_password() != OK:
            raise RuntimeError('Failed to find sensor, check wiring!')

    def verify_password(self):
        """Checks if the password/connection is correct, returns True/False"""
        self._send_packet([_VERIFYPASSWORD] + list(self.password))
        return self._get_packet()[0]

    def count_templates(self):
        """Requests the sensor to count the number of templates and stores it
        in ``self.template_count``. Returns the packet error code or OK success"""
        self._send_packet([_TEMPLATECOUNT])
        r = self._get_packet()
        self.template_count = struct.unpack('>H', bytes(r[1:3]))[0]
        return r[0]

    def get_image(self):
        """Requests the sensor to take an image and store it memory, returns
        the packet error code or OK success"""
        self._send_packet([_GETIMAGE])
        return self._get_packet()[0]

    def image_2_tz(self, slot):
        """Requests the sensor convert the image to a template, returns
        the packet error code or OK success"""
        self._send_packet([_IMAGE2TZ, slot])
        return self._get_packet()[0]

    def create_model(self):
        """Requests the sensor take the template data and turn it into a model
        returns the packet error code or OK success"""
        self._send_packet([_REGMODEL])
        return self._get_packet()[0]

    def store_model(self, location):
        """Requests the sensor store the model into flash memory and assign
        a location. Returns the packet error code or OK success"""
        self._send_packet([_STORE, 1, location >> 8, location & 0xFF])
        return self._get_packet()[0]

    def delete_model(self, location):
        """Requests the sensor delete a model from flash memory given by
        the argument location. Returns the packet error code or OK success"""
        self._send_packet([_DELETE, location >> 8, location & 0xFF, 0x00, 0x01])
        return self._get_packet()[0]

    def read_templates(self):
        """Requests the sensor to list of all template locations in use and
        stores them in self.templates. Returns the packet error code or OK success"""
        self._send_packet([_TEMPLATEREAD, 0x00])
        r = self._get_packet()
        self.templates = []
        for i in range(32):
            byte = r[i+1]
            for bit in range(8):
                if byte & (1 << bit):
                    self.templates.append(i * 8 + bit)
        return r[0]

    def finger_fast_search(self):
        """Asks the sensor to search for a matching fingerprint template to the
        last model generated. Stores the location and confidence in self.finger_id
        and self.confidence. Returns the packet error code or OK success"""
        # high speed search of slot #1 starting at page 0x0000 and page #0x00A3
        self._send_packet([_HISPEEDSEARCH, 0x01, 0x00, 0x00, 0x00, 0xA3])
        r = self._get_packet()
        self.finger_id, self.confidence = struct.unpack('>HH', bytes(r[1:5]))
        return r[0]

    def get_model(self, idx):
        self._send_packet([_UPCHAR, idx])
        self._get_packet()
        res = []
        for i in range(TEMPLATE_PACKET_COUNT):
            res.extend(self._get_packet())
        return res

    # idx = 0x01 or 0x02
    def load_model(self, data, idx):
        self._send_packet([_DOWNCHAR, idx])
        time.sleep(0.1)
        res = self._get_packet()
        n_packet  = math.ceil(len(data)/TEMPLATE_PACKET_DATA_LEN)
        if res[0] == OK:
            for i in  range(n_packet):      
                if (i < n_packet - 1):
                    self._send_packet(data[TEMPLATE_PACKET_DATA_LEN*i:TEMPLATE_PACKET_DATA_LEN*(i+1)],_DATAPACKET)
                else:
                    self._send_packet(data[TEMPLATE_PACKET_DATA_LEN*i:len(data)],_ENDDATAPACKET)
        return res[0]

    def get_match(self):
        self._send_packet([_MATCH])
        time.sleep(0.1)
        res = self._get_packet()     
        start, confidence = struct.unpack('>BH', bytearray(res))
        return confidence

    # def get_match(self):
    #     self._send_packet([_MATCH])
    #     time.sleep(0.1)
    #     r = self._get_packet()        
    #     # print("r")
    #     # print(r)
    #     confidence = r[0]
    #     #confidence = r[1]
    #     #confidence <<= 8
    #     #confidence |= r[2]
    #     return confidence


##################################################
    def _get_packet(self):
        """ Helper to parse out a packet from the UART and check structure.
        Returns just the data payload from the packet"""
        header = self._uart.read(HEADER_LEN)
        if DEBUG_FLAG :
            print("Header:", header)
        if (not header) or (len(header) != HEADER_LEN):
            raise RuntimeError('Failed to read data from sensor')

        # first two bytes are start code
        start = struct.unpack('>H', header[0:2])[0]

        if start != _STARTCODE:
            raise RuntimeError('Incorrect packet data')
        # next 4 bytes are address
        addr = [i for i in header[2:6]]
        if addr != self.address:
            raise RuntimeError('Incorrect address')

        packet_type, packet_length = struct.unpack('>BH', header[6:9])
        if DEBUG_FLAG :
            print(packet_length)
            print(packet_type)

        res = self._uart.read(packet_length)
        if DEBUG_FLAG :
            print(DEBUG_FLAG )
            print("Content:", res)
        if (not res) or (len(res) != packet_length):
            raise RuntimeError('Failed to read data from sensor')
        
        reply = [i for i in res[:-2]]
        res_sum = sum(header[NOSUM_LEN:]) + sum(reply)
        checksum1, checksum2 = struct.unpack('>BB', res[-2:])
        if (res_sum>>8 != checksum1 or res_sum& 0xFF != checksum2):
            raise RuntimeError('Check sum mismatch')       

        return reply

    def _send_packet(self, data, type=_COMMANDPACKET):
        packet = [_STARTCODE >> 8, _STARTCODE & 0xFF]
        packet = packet + self.address
        packet.append(type)  # the packet type

        length = len(data) + 2
        packet.append(length >> 8)
        packet.append(length & 0xFF)

        packet = packet + data

        checksum = sum(packet[NOSUM_LEN:])
        packet.append(checksum >> 8)
        packet.append(checksum & 0xFF)
        if DEBUG_FLAG :
            print("Sending: ", [hex(i) for i in packet])
        self._uart.write(bytearray(packet))
