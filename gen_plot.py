"""
Description: Generate a brain activity plot from the data
Author: Triskelion <info@mlwave.com>
Kaggle contest description, rules and data: 
http://www.kaggle.com/c/decoding-the-human-brain/
Code description:
http://mlwave.com/predict-visual-stimuli-from-human-brain-activity/
"""

import matplotlib.pyplot as plt
from scipy.io import loadmat

data = loadmat("d:\\traindata\\train_subject01.mat", squeeze_me=True)

fig = plt.figure()
fig.suptitle('Top: activity series for channel 0 and channel 3\n Bottom: activity series for channel 1')

ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.plot([f for f in xrange(375)],data['X'][0][0])
ax1.plot([f for f in xrange(375)],data['X'][0][3])
ax2.plot([f for f in xrange(375)],data['X'][0][1])

plt.savefig("activity_plot.png")
plt.show()