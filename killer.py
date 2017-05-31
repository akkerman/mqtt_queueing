import signal

class Killer:
    cont = True
    def __init__(self):
        signal.signal(signal.SIGINT, self.handler)
        signal.signal(signal.SIGTERM, self.handler)
    def handler(self, signum, frame):
        self.cont = False

