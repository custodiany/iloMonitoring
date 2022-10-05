import time
import pybithumb
from PyQt5.QtCore import QThread, pyqtSignal

class PriceWorker(QThread):
    dataSent = pyqtSignal(float)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True
    def run(self):
        while self.alive:
            data = pybithumb.get_current_price(self.ticker)
            time.sleep(1)
            slef.dataSent.emit(data)

    def close(self):
            self.alive = False