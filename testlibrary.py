import numpy as np
import AudiPy

Audi = AudiPy()

test = np.linspace(1, 50, 50)
test2 = np.linspace(50, 1, 50)

test4 = np.array([test, test2], dtype=object)

t = 15
final = Audi.convert_to_audio(data=test4, min_freq=20, max_freq=4000,  time=t)

