import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams.update({'font.size': 18})

x1 = [3.75,3.79,3.78,3.775,3.755,3.765,3.769]
x2 = [3.76,3.773,3.765,3.766,3.755,3.759,3.750]
x3 = [3.864,3.869,3.861,3.860,3.834,3.83,3.835]
x4 = [3.74,3.743,3.745,3.735,3.720,3.718,3.719]
x5 = [3.791,3.795,3.783,3.783,3.780,3.781,3.783]
y1 = [10,20,30,40,50,60,70]

fig, ax = plt.subplots()

# Using set_dashes() to modify dashing of an existing line
line1, = ax.plot(y1, x1, label='f1')
plt.scatter(y1,x1)
line1.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break
line2, = ax.plot(y1, x2, label='f2')
plt.scatter(y1,x2)
line2.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break
line3, = ax.plot(y1, x3, label='f3')
plt.scatter(y1,x3)
line3.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break
line4, = ax.plot(y1, x4, label='f4')
plt.scatter(y1,x4)
line4.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break
line5, = ax.plot(y1, x5, label='f5')
plt.scatter(y1,x5)
line5.set_dashes([2, 2, 10, 2])  # 2pt line, 2pt break, 10pt line, 2pt break
plt.xlabel("Epoch")
plt.ylabel("Smoothed Reward on Each Fold")
# Using plot(..., dashes=...) to set the dashing when creating a line
#line2, = ax.plot(x, y - 0.2, dashes=[6, 2], label='Using the dashes parameter')

ax.legend(loc='upper right')
plt.tight_layout()
plt.savefig('1_r.pdf', bbox_inches='tight')
plt.show()