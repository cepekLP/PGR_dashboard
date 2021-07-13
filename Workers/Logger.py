import logging
import json
from time import gmtime, strftime
from threading import Timer


class Logger:
    def __init__(self, bolide_info):
        self.bolide_info = bolide_info
        logging.basicConfig(
            format="%(asctime)s | %(levelname)s: %(message)s",
            filename="log/" + strftime("%d-%m-%y_%H%M%S", gmtime()) + ".log",
            level=logging.INFO,
        )
        logging.info("Started...")
        self.rt = RepeatedTimer(0.25, self.log)

    def log(self) -> None:
        logging.info(json.dumps(self.bolide_info))

    def warning_log(self, error: str) -> None:
        logging.critical(error)


class RepeatedTimer:
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
