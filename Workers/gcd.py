import can
import RPi.GPIO as GPIO
import time

# from datetime import datetime


def main():
    # currentTime = datetime.now().microsecond

    can0 = can.interface.Bus(channel="can0", bustype="socketcan_ctypes")

    msg = can.Message(
        arbitration_id=2, data=[255, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False
    )

    switchGpio = 22

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(switchGpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    truthPosition = GPIO.input(switchGpio)
    lastSwitchPosition = GPIO.input(switchGpio)

    while True:
        currentState = GPIO.input(switchGpio)
        if currentState != lastSwitchPosition:
            print("Change!" + str(currentState))
            lastSwitchPosition = currentState
            if currentState == truthPosition:
                msg.data[0] = 255
                can0.send(msg)
            elif currentState != truthPosition:
                msg.data[0] = 0
                can0.send(msg)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
