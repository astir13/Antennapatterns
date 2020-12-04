# Python Program to plot Antenna pattern APENST807 v01 found at ITU's space antenna pages
# calculates coefficients A, B, C, D for the formula given in document
# http://www.itu.int/en/ITU-R/software/Documents/ant-pattern/APL_DOC_BY_PATTERN_NAME/APENST807V01.pdf
# 
# G = G_max                        for 0 deg. <= phi < 1 deg.
# G = coefA - coefB * log (phi)    for 1 <= phi <= phi1
# G = coefC - coefD * log (phi)    for phi1 < phi <= 180 deg.
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
g1 = 8 # Gmax [dBi]
phi1 = 100  # angle where the attenuation is highest
g_phi1 = -18 # [dBi] at highest attenuation points
g_phi180 = -4 # [dBi] at 180 point
phi180 = 180 # kind of a constant
coefA = 8 # G [dBi] at 1 degree
coefB = (coefA - g_phi1)/np.log(phi1) # calculated coefB
print("coefB = " + str(coefB) + "\n")
coefC = (g_phi1 - (g_phi180 * np.log(phi1) / np.log(phi180))) / (1 - (np.log(phi1) / np.log(phi180)))
print("coefC = " + str(coefC) + "\n")
coefD = (coefC - g_phi180)/np.log(phi180) 
print("coefD = " + str(coefD) + "\n")
x1 = np.arange(-1, 1, .1) # main lobe Gmax
x2 = np.arange(1, phi1, .1) # main lobe courve
x3 = np.arange(phi1, 180, .1) # secondary courve

#linear diagram
if (False):
  fig=plt.figure()
  axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
  #axes2 = fig.add_axes([0.55, 0.55, 0.3, 0.3]) # inset axes
  #axes3 = fig.add_axes([0.2, 0.3, 0.2, 0.3]) # inset axes
  axes1.plot(x1, g1 * np.ones(len(x1)), 'r')
  axes1.plot(x2, coefA - (coefB * np.log(x2)), 'b')
  axes1.plot(x3, coefC - (coefD * np.log(x3)), 'g')
  #axes2.plot(x,np.cos(x),'r')
  #axes3.plot(x,np.tan(x),'g')
  axes1.set_title('VDE Antenna ref. pattern')
  #axes2.set_title("cosine")
  #axes3.set_title("tangent")
  plt.show()

# polar diagram
ax = plt.subplot(111, projection='polar', theta_offset=np.pi/2, rlabel_position=-110)
ax.set_thetalim(thetamin=-180, thetamax=180)
ax.set_thetagrids([-135, -90, -45, 0, 45, 90, 135, 180])
ax.plot(x1/180*np.pi, g1 * np.ones(len(x1)))
ax.plot(x2/180*np.pi, coefA - (coefB * np.log(x2)), 'b')
ax.plot(x3/180*np.pi, coefC - (coefD * np.log(x3)), 'b')
ax.plot(-x1/180*np.pi, g1 * np.ones(len(x1)), 'b')
ax.plot(-x2/180*np.pi, coefA - (coefB * np.log(x2)), 'b')
ax.plot(-x3/180*np.pi, coefC - (coefD * np.log(x3)), 'b')
ax.set_rmax(8)
ax.set_rticks([-20,-15,-10,-5, 0, 5, 8])  # less radial ticks
ax.set_xlabel("Phi (degrees) vs. Gain (dBi)")
ax.grid(True)

ax.set_title("Antenna reference pattern ITU APENST807 V01", va='bottom')
plt.show()
