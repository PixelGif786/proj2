from .common import *

class CwndControl:
    '''Interface for the congestion control actions'''

    def __init__(self):
        self.cwnd = 1.0 * MTU
        self.ssthresh = INIT_SSTHRESH

    def on_ack(self, ackedDataLen):
        # TCP Tahoe algorithm
        if self.cwnd < self.ssthresh:
            self.cwnd += 412
        else:
            self.cwnd += (412 * 412) / self.cwnd
    
    def on_timeout(self):
        # TCP Tahoe algorithm
        self.ssthresh = self.cwnd / 2
        self.cwnd = 412
    
    def __str__(self):
        return f"cwnd:{self.cwnd} ssthresh:{self.ssthresh}"
