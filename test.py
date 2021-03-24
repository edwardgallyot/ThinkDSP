from thinkdsp import CosSignal, SinSignal
from thinkdsp import decorate

cos_sig = CosSignal(freq=440, amp=1, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)

cos_sig.plot()
decorate(xlabel='Time (s)')

