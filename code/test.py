from thinkdsp import CosSignal, SinSignal
from thinkdsp import decorate
import pyinputplus as pyip
from matplotlib import pyplot

cos_sig = CosSignal(freq=440, amp=1, offset=0)
sin_sig = SinSignal(freq=880, amp=0.5, offset=0)

mix = cos_sig + sin_sig

wave = mix.make_wave(0.5, 0, 11025)

period = mix.period

segment = wave.segment(0, period*3)


segment.plot()
pyplot.show()

