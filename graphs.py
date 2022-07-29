import matplotlib.pyplot as plt
import numpy as np

y = np.array([3, 8, 1, 10])
my_labels = ["candy bars", "apples", "sodas", "beers"]

plt.pie(y, labels = my_labels)
plt.legend(title = "Consumption:")
plt.show()