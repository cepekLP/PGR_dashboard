import can
import time
from gpiozero import Button

# from datetime import datetime

SWITCH_GPIO = 22


def main():
    can0 = can.interface.Bus(channel="can0", bustype="socketcan_ctypes")
    msg = can.Message(
        arbitration_id=2, data=[255, 0, 0, 0, 0, 0, 0, 0], is_extended_id=False
    )

    button = Button(SWITCH_GPIO)

    truth_position = button.is_pressed()
    last_switch_position = button.is_pressed()

    while True:
        current_state = button.is_pressed()
        if current_state != last_switch_position:
            print("Change!" + str(current_state))
            last_switch_position = current_state
            if current_state == truth_position:
                msg.data[0] = 255
                can0.send(msg)
            elif current_state != truth_position:
                msg.data[0] = 0
                can0.send(msg)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
