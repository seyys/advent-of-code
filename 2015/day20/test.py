from matplotlib import pyplot as plt

factors = []
lims = 100

# for i in range(665080,666080):
for i in range(lims):
    factors.append(sum(x for x in range(1,i+1) if i % x == 0))

plt.plot(range(lims), factors, ':')
# plt.plot(range(665080,666080), factors)
plt.show()