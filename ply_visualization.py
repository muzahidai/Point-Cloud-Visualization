import open3d as o3d

# Path to your point cloud file
file_path = "path_to_your_point_cloud_file.ply"

# Load the point cloud data
point_cloud = o3d.io.read_point_cloud(file_path)

# Visualize the point cloud
o3d.visualization.draw_geometries([point_cloud])