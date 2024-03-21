import numpy as np
#import laspy
#import h5py
# Visualization
import open3d as o3d
import pptk # works with Python 3.6

pc_txt = np.loadtxt('./data/modelnet40_airplane_0001.txt', delimiter=',')
print('Shape of the point cloud:', pc_txt.shape)
points = pc_txt[:,:3]
colors = pc_txt[:,3:]
#vis = pptk.viewer(points, colors) # Start the interactive visualization

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors)

o3d.visualization.draw_geometries([pcd])
