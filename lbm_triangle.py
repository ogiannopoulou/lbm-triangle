#%%
import matplotlib.pyplot as plt
import numpy as np
import sys
import subprocess
import os
import csv

"""
Lattice Boltzmann Simulation (With Python)

Simulate flow past a triangle

"""


# Simulation parameters
Nx                     = 400    # resolution x-dir
Ny                     = 100    # resolution y-dir
rho0                   = 1    # average density
tau                    = 0.8    # collision timescale
Nt                     = 5000   # number of timesteps

# Lattice speeds / weights
NL = 9
idxs = np.arange(NL)
cxs = np.array([0, 0, 1, 1, 1, 0,-1,-1,-1])
cys = np.array([0, 1, 1, 0,-1,-1,-1, 0, 1])
weights = np.array([4/9,1/9,1/36,1/9,1/36,1/9,1/36,1/9,1/36]) # sums to 1

# Initial Conditions
F = np.ones((Ny,Nx,NL)) #* rho0 / NL
np.random.seed(42)
F += 0.01*np.random.randn(Ny,Nx,NL)
X, Y = np.meshgrid(range(Nx), range(Ny))
F[:,:,3] += 0.1 #2*(1+0.2*np.cos(2*np.pi*X/Nx*4))
rho = np.sum(F,2)
for i in idxs:
	F[:,:,i] *= rho0 / rho

# triangle boundary
X, Y = np.meshgrid(range(Nx), range(Ny))

 
# Define a triangular triangle (equilateral, pointing up)
# Centered at (3*Nx/4, Ny/2), side length similar to circular triangle diameter
triangle_center_x = Nx / 4
triangle_center_y = Ny / 2
side_length = Ny / 2
height = np.sqrt(3) / 2 * side_length

# Vertices of the triangle
v1 = (triangle_center_x, triangle_center_y - height / 3)
v2 = (triangle_center_x - side_length / 2, triangle_center_y + height * 2 / 3)
v3 = (triangle_center_x + side_length / 2, triangle_center_y + height * 2 / 3)

# Barycentric coordinate method for point-in-triangle test
def point_in_triangle(x, y, v1, v2, v3):
	denom = ((v2[1] - v3[1]) * (v1[0] - v3[0]) + (v3[0] - v2[0]) * (v1[1] - v3[1]))
	a = ((v2[1] - v3[1]) * (x - v3[0]) + (v3[0] - v2[0]) * (y - v3[1])) / denom
	b = ((v3[1] - v1[1]) * (x - v3[0]) + (v1[0] - v3[0]) * (y - v3[1])) / denom
	c = 1 - a - b
	return (a >= 0) & (b >= 0) & (c >= 0)

triangle = point_in_triangle(X, Y, v1, v2, v3)
# Rotate triangle 45 degrees counterclockwise around its center
theta = np.deg2rad(-90)
cos_t, sin_t = np.cos(theta), np.sin(theta)

def rotate_point(x, y, cx, cy, cos_t, sin_t):
	x_shifted, y_shifted = x - cx, y - cy
	x_rot = cos_t * x_shifted - sin_t * y_shifted + cx
	y_rot = sin_t * x_shifted + cos_t * y_shifted + cy
	return x_rot, y_rot

v1_rot = rotate_point(*v1, triangle_center_x, triangle_center_y, cos_t, sin_t)
v2_rot = rotate_point(*v2, triangle_center_x, triangle_center_y, cos_t, sin_t)
v3_rot = rotate_point(*v3, triangle_center_x, triangle_center_y, cos_t, sin_t)

triangle = point_in_triangle(X, Y, v1_rot, v2_rot, v3_rot)


# Prep figure
fig = plt.figure(figsize=(12,6), dpi=80)
print(range(Nt))
# Simulation Main Loop
for it in range(Nt):
	print(it)
	
	# Drift
	for i, cx, cy in zip(idxs, cxs, cys):
		F[:,:,i] = np.roll(F[:,:,i], cx, axis=1)
		F[:,:,i] = np.roll(F[:,:,i], cy, axis=0)
	
	
	# Set reflective boundaries
	bndryF = F[triangle,:]
	bndryF = bndryF[:,[0,5,6,7,8,1,2,3,4]]

	
	# Calculate fluid variables
	rho = np.sum(F,2)
	ux  = np.sum(F*cxs,2) / rho
	uy  = np.sum(F*cys,2) / rho
	
	
	# Apply Collision
	Feq = np.zeros(F.shape)
	for i, cx, cy, w in zip(idxs, cxs, cys, weights):
		Feq[:,:,i] = rho * w * ( 1 + 3*(cx*ux+cy*uy)  + 9*(cx*ux+cy*uy)**2/2 - 3*(ux**2+uy**2)/2 )
	
	F += -(1.0/tau) * (F - Feq)
	
	# Apply boundary 
	F[triangle,:] = bndryF
	
	


	# color 1/2 particles blue, other half red
	#plt.cla()
	ux[triangle] = 0
	uy[triangle] = 0
	vorticity = (np.roll(ux, -1, axis=0) - np.roll(ux, 1, axis=0)) - (np.roll(uy, -1, axis=1) - np.roll(uy, 1, axis=1))
	vorticity[triangle] = np.nan
	vorticity = np.ma.array(vorticity, mask=triangle)
	plt.imshow(vorticity, cmap='bwr')
	plt.imshow(~triangle, cmap='gray', alpha=0.3)
	plt.clim(-.1, .1)
	ax = plt.gca()
	ax.invert_yaxis()
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)	
	ax.set_aspect('equal')	
	plt.pause(0.001)
	plt.show()
	# Save each timestep output in a separate figure
	output_dir = "lbm_figures_triangle"
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)
	if it % 10 == 0:
		fig.savefig(os.path.join(output_dir, f"lbm_triangle_{it:04d}.png"))
	fig.clf()




print("Simulation complete. Consider post-processing for visualization.")
# %%

