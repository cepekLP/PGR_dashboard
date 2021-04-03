import rpi_ws281x as ws
from time import sleep
from PyQt5.QtCore import QTimer

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
        self.timer = QTimer()
        self.timer.setInterval(250)
        self.timer.timeout.connect(self.blink)
        self.timer_work = False
        self.blink_status = False

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
        self.strip.show()

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

    def update_2(self, rpm):
        active_led = int((rpm - RPM_MIN) / (RPM_MAX - RPM_MIN) * LED_COUNT)
        if active_led < 0:
            active_led = 0
        if active_led > LED_COUNT:
            self.timer.start()
            self.timer_work = True
        else:
            if self.timer_work is True:
                self.timer_work = False
            for i in range(LED_COUNT):
                if i < active_led:
                    if i < LED_COUNT * 0.4:
                        self.strip.setPixelColor(i, ws.Color(0, 255, 0))
                    elif i < LED_COUNT * 0.7:
                        self.strip.setPixelColor(i, ws.Color(255, 255, 0))
                    else:
                        self.strip.setPixelColor(i, ws.Color(255, 0, 0))
                else:
                    self.strip.setPixelColor(i, ws.Color(0, 0, 0))

            self.strip.show()

    def blink(self):
        if self.blink_status is True:
            for i in range(LED_COUNT):
                self.strip.setPixelColor(i, ws.Color(0, 0, 0))
            self.blink_status = False
        else:
            for i in range(LED_COUNT):
                self.strip.setPixelColor(i, ws.Color(255, 0, 0))
            self.blink_status = True
