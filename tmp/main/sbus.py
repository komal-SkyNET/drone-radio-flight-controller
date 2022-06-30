
import readline
import serial
import ctypes
import time


#-------------------------------------------------------------------------------
def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n


#-------------------------------------------------------------------------------
class SBUSEncoder:
    #---------------------------------------------------------------------------
    def __init__(self):
        self.channels = [1024] * 16

    #---------------------------------------------------------------------------
    def set_channel(self, channel, data):
        self.channels[channel] = data & 0x07ff

    #---------------------------------------------------------------------------
    def get_data(self):
        #-----------------------------------------------------------------------
        # Create the header
        #-----------------------------------------------------------------------
        data = bytearray(25)
        data[0] = 0x0f # start byte

        #-----------------------------------------------------------------------
        # Encode channels
        #-----------------------------------------------------------------------
        current_byte = 1
        available_bits  = 8
        for ch in self.channels:
            ch &= 0x7ff
            remaining_bits = 11
            while remaining_bits:
                mask = bit_not(0xffff >> available_bits << available_bits, 16)
                enc = (ch & mask) << (8 - available_bits)
                data[current_byte] |= enc

                encoded_bits = 0
                if remaining_bits < available_bits:
                    encoded_bits = remaining_bits
                else:
                    encoded_bits = available_bits

                remaining_bits -= encoded_bits
                available_bits -= encoded_bits
                ch >>= encoded_bits

                if available_bits == 0:
                    current_byte += 1
                    available_bits = 8

        #-----------------------------------------------------------------------
        # Ignore the flags and end byte
        #-----------------------------------------------------------------------
        data[23] = 0
        data[24] = 0

        return data
