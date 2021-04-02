import rpi_ws281x as ws
from time import sleep

LED_COUNT = 8
LED_PIN = 12
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

RPM_MIN = 10000
RPM_MAX = 14000


class LED_Bar:
    def __init__(self):
        self.strip = ws.PixelStrip(
            LED_COUNT,
            LED_PIN,
            LED_FREQ_HZ,
            LED_DMA,
            LED_INVERT,
            LED_BRIGHTNESS,
            LED_CHANNEL,
        )
        self.strip.begin()

        self.wave()

    def wave(self):
        for i in range(3):
            for j in range(LED_COUNT):
                if i == 0:
                    self.strip.setPixelColor(j, ws.Color(255, 0, 0))
                elif i == 1:
                    self.strip.setPixelColor(j, ws.Color(0, 255, 0))
                elif i == 2:
                    self.strip.setPixelColor(j, ws.Color(0, 0, 255))

                self.strip.show()
                sleep(0.05)

        for j in range(LED_COUNT):
            self.strip.setPixelColor(j, ws.Color(0, 0, 0))

    def update(self, rpm):
        active_led = int((rpm - RPM_MIN) / (RPM_MAX - RPM_MIN) * LED_COUNT)
        if active_led < 0:
            active_led = 0
        for i in range(LED_COUNT):
            if i < active_led:
                if i < LED_COUNT * 0.44:
                    self.strip.setPixelColor(i, ws.Color(0, 255, 0))
                elif i < LED_COUNT * 0.77:
                    self.strip.setPixelColor(i, ws.Color(255, 255, 0))
                else:
                    self.strip.setPixelColor(i, ws.Color(255, 0, 0))
            else:
                self.strip.setPixelColor(i, ws.Color(0, 0, 0))

        self.strip.show()
