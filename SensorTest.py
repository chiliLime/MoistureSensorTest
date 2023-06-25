import spidev
import time

# Create a SpiDev object
spi = spidev.SpiDev()

# Open SPI device
spi.open(0, 0)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

def readadc(channel):
    if ((channel > 7) or (channel < 0)):
        return -1
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

try:
    while True:
        value = readadc(0)
        print("ADC Value: ", value)
        time.sleep(1)

except KeyboardInterrupt:
    spi.close()
