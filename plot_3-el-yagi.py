# Python Program to plot Antenna reference pattern of a 3-element X-yagi for VDE-SAT
# 
# G = G_min + (G_max - G_min) * sqrt(cos(pi * phi * phi1 / 2))                     for -phi1 <= phi <= phi1
# G = G_min + (G_back - G_min) * sin( (abs(phi) - phi1) / (180 - phi1) / 2 * pi)   for phi1 < abs(phi) <= 180
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

g = 8 # Gmax [dBi]
phi1 = 110  # angle where the attenuation is highest
g_phi1 = -18 # [dBi] at highest attenuation points
g_phi180 = -5 # [dBi] at 180 point
phi180 = 180 # kind of a constant

print("G_max = " + str(g) + " dBi at 0 degrees")
print("G_min = " + str(g_phi1) + " dBi at " + str(phi1) + "degrees")
print("G_back = " + str(g_phi180) + " dBi at 180 degrees")
x1 = np.arange(-phi1, phi1, .1) # main lobe
x2 = np.concatenate((np.arange(phi1, 180, .1), np.arange(-180, -phi1, .1)), axis = 0) # back lobe

# polar diagram
ax = plt.subplot(111, projection='polar', theta_offset=np.pi/2, rlabel_position=-110)
ax.set_thetalim(thetamin=-180, thetamax=180)
ax.set_thetagrids([-150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180])
ax.plot(x1/180*np.pi, g_phi1 + (g - g_phi1) * np.sqrt(np.cos(x1/phi1/2*np.pi)), 'b')
ax.plot(x2/180*np.pi, g_phi1 + (g_phi180 - g_phi1) * np.sin((np.abs(x2)-phi1)/(180-phi1)/2*np.pi), 'b')

ax.set_rmax(8)
ax.set_rticks([-15,-10,-5, 0, 5, 8])  # less radial ticks
# ax.set_xlabel("Phi (degrees) vs. Gain (dBi)")
ax.grid(True)

plt.show()
