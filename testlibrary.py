import numpy as np
import AudiPy

Audi = AudiPy()

# line = StandardScalar(minf=20, maxf=4000)

test = np.linspace(1, 500, 50)
test2 = np.linspace(500, 1, 50)

test4 = np.array([test, test2], dtype=object)

# print(test4)

t = 10
preprocess = Audi.pre_process(filename="C:\\Users\\Cayden\\Downloads\\Save_webP\\parabola.csv")
final = Audi.convert_to_audio(data=preprocess, min_freq=20, max_freq=4000, time=t, mode="Major")

