# Python Program to plot a 4dBi patch Antenna pattern
# Inspiration from ITU-R M.1528
# 
# G = G_max - (|phi/phi_b/alpha|)^alpha                        for -180 <= phi <= 180
# 
# Copyright December 2020, Stefan Pielmeier
# Usage under the 2-clause BSD License:
#
# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, 
#    this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, 
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, 
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, 
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import matplotlib.pyplot as plt
import numpy as np
import math
G_max = 4 # Gmax [dBi]
alpha = 3.2  # angle where the attenuation is highest
phi_b = np.sqrt(1200)/2 # = 69˚ for a patch antenna with 4dBi
x1 = np.arange(-180, 0, .1) # main lobe right
x2 = np.arange(0, 180, .1) # main lobe left
y1 = G_max - np.power(np.abs(x1/phi_b/alpha), alpha)
y2 = G_max - np.power(np.abs(x2/phi_b/alpha), alpha)

#linear diagram
if (True):
  fig=plt.figure()
  axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
  axes1.plot(x1, y1, 'r')
  axes1.plot(x2, y2, 'b')
  axes1.grid(True, 'major', 'both')
  axes1.set_yticks([4, 1, -2, -7, -12, -17, -22, -27, -32])
  plt.show()

# polar diagram
if (True):
  ax = plt.subplot(111, projection='polar', theta_offset=np.pi/2, rlabel_position=-155)
  ax.set_thetalim(thetamin=-180, thetamax=180)
  ax.set_thetagrids([-135, -90, -45, 0, 45, 90, 135, 180])
  ax.plot(x1/180*np.pi, y1, 'b')
  ax.plot(x2/180*np.pi, y2, 'b')
  ax.set_rmax(G_max)
  ticks = np.arange(np.ceil(G_max), np.floor(min(y1)), -np.ceil((np.ceil(G_max) - np.floor(min(y1)))/5))
  print("ticks in polar diagram at " + str(ticks) + " dBi")
  ax.set_rticks(ticks)  # less radial ticks
#  ax.set_xlabel("Phi (degrees) vs. Gain (dBi)")
  ax.grid(True)

#  ax.set_title("Antenna reference pattern ITU-R M.1528", va='bottom')
  plt.show()
