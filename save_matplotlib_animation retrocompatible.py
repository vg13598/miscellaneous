"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!

# MODIFICATION: extra_args save it so that it is compatible with Windows Media Player, no need for more ffmpeg
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import os
# First set up the figure, the axis, and the plot element we want to animate
fig,axs = plt.subplots()
d = [np.random.rand(256,256) for i in range(200)]
img = axs.imshow(d[0])

# initialization function: plot the background of each frame
def init():
    img.set_data(d[0])
    return img, axs

# animation function.  This is called sequentially


def update(j):
    img.set_data(d[j])
    return img, axs

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, update, init_func=init,
                               frames=200, interval=20, blit=True)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
anim.save('video.mp4', fps=10, extra_args=['-vcodec', 'libx264',"-pix_fmt","yuv420p"])


plt.show()
