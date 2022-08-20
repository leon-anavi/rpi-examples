# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Example to send a packet periodically between addressed nodes
# Author: Leon Anavi <leon@anavi.org>
# Modified to work directly on the MaPIE Lora RP2040 boards.
#
import time
import board
import busio
import digitalio
import adafruit_rfm9x

# set the time interval (seconds) for sending packets
transmit_interval = 5

# Define radio parameters.
RADIO_FREQ_MHZ = 868.0  # Frequency of the radio in Mhz. Must match your
# module! Can be a value like 915.0, 433.0, etc.

# Define pins connected to the chip.
CS = digitalio.DigitalInOut(board.GP17)
RESET = digitalio.DigitalInOut(board.GP20)

# Initialize SPI bus.
rfm95x_spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)
# Initialze RFM radio
rfm9x = adafruit_rfm9x.RFM9x(rfm95x_spi, CS, RESET, RADIO_FREQ_MHZ)

# set node addresses
# When trying this out with two boards, one board should have the reverse settings
rfm9x.node = 1
rfm9x.destination = 2
# initialize counter
counter = 0
# send a broadcast message from my_node with ID = counter
rfm9x.send(
    bytes("Startup message {} from node {}".format(counter, rfm9x.node), "UTF-8")
)

# Wait to receive packets.
print("Node: ", rfm9x.node)
print("Waiting for packets...")
now = time.monotonic()
while True:
    # Look for a new packet: only accept if addresses to my_node
    packet = rfm9x.receive(with_header=True)
    # If no packet was received during the timeout then None is returned.
    if packet is not None:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print("Received (raw header):", [hex(x) for x in packet[0:4]])
        print("Received (raw payload): {0}".format(packet[4:]))
        print("Received RSSI: {0}".format(rfm9x.last_rssi))
    if time.monotonic() - now > transmit_interval:
        now = time.monotonic()
        counter = counter + 1
        # send a  mesage to destination_node from my_node
        rfm9x.send(
            bytes(
                "message number {} from node {}".format(counter, rfm9x.node), "UTF-8"
            ),
            keep_listening=True,
        )
        button_pressed = None
