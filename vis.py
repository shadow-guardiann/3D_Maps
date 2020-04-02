# VISUALIZATION TECHNIQUES FOR XYZ POINTCLOUDS

# Uncomment section as per requirement


import open3d as o3d
import trimesh, pandas as pd
import numpy as np
import mcubes
import matplotlib.pyplot as plt
from pyntcloud import PyntCloud
from pprint import pprint

def draw_geometries_with_back_face(geometries):
    visualizer = o3d.visualization.Visualizer()
    visualizer.create_window()
    render_option = visualizer.get_render_option()
    render_option.mesh_show_back_face = True
    for geometry in geometries:
        visualizer.add_geometry(geometry)
    visualizer.run()
    visualizer.destroy_window()

pcd = o3d.io.read_point_cloud("data/chair.xyz")
pcd.estimate_normals()

# estimate radius for rolling ball
distances = pcd.compute_nearest_neighbor_distance()
avg_dist = np.mean(distances)
radius = 1.5 * avg_dist   

# Ball pivoting

# mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(
#            pcd,
#            o3d.utility.DoubleVector([radius, radius * 2]))

# trimesh = trimesh.Trimesh(np.asarray(mesh.vertices), np.asarray(mesh.triangles), vertex_normals=np.asarray(mesh.vertex_normals))

# trimesh.show()

# Tetrahederal/Delaunay

# mesh = o3d.geometry.TetraMesh.create_from_point_cloud(pcd)

# o3d.visualization.draw_geometries([mesh[0]]) # Visualization for tetrahedral

# Alpha

# o3d.utility.set_verbosity_level(o3d.utility.Debug)
# o3d.visualization.draw_geometries([pcd])
# print("compute tetra mesh only once")
# tetra_mesh, pt_map = o3d.geometry.TetraMesh.create_from_point_cloud(pcd)
# print("done with tetra mesh")
# for alpha in np.logspace(np.log10(0.5), np.log10(0.01), num=4):
#     print("alpha={}".format(alpha))
#     mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_alpha_shape(
#         pcd, alpha, tetra_mesh, pt_map)
#     mesh.compute_vertex_normals()
#     draw_geometries_with_back_face([mesh])

# Poisson reconstruction

# o3d.utility.set_verbosity_level(o3d.utility.VerbosityLevel.Debug)

# # o3d.visualization.draw_geometries([pcd])

# print('run Poisson surface reconstruction')
# mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
#     pcd, depth=8)
# print(mesh)
# # o3d.visualization.draw_geometries([mesh])

# print('visualize densities')
# densities = np.asarray(densities)
# density_colors = plt.get_cmap('plasma')(
#     (densities - densities.min()) / (densities.max() - densities.min()))
# density_colors = density_colors[:, :3]
# density_mesh = o3d.geometry.TriangleMesh()
# density_mesh.vertices = mesh.vertices
# density_mesh.triangles = mesh.triangles
# density_mesh.triangle_normals = mesh.triangle_normals
# density_mesh.vertex_colors = o3d.utility.Vector3dVector(density_colors)
# # o3d.visualization.draw_geometries([density_mesh])

# print('remove low density vertices')
# vertices_to_remove = densities < np.quantile(densities, 0.1)
# mesh.remove_vertices_by_mask(vertices_to_remove)
# print(mesh)
# o3d.visualization.draw_geometries([mesh])

# Marching cubes

# cloud = PyntCloud.from_file("eiffel.xyz", sep=" ")

# voxelgrid_id = cloud.add_structure("voxelgrid", n_x=32, n_y=32, n_z=32)

# voxelgrid = cloud.structures[voxelgrid_id]

# x_cords = voxelgrid.voxel_x
# y_cords = voxelgrid.voxel_y
# z_cords = voxelgrid.voxel_z

# voxel = np.zeros((32, 32, 32))

# for x, y, z in zip(x_cords, y_cords, z_cords):
#     voxel[x][y][z] = 1

# # smooth = mcubes.smooth(voxel)

# vertices, triangles = mcubes.marching_cubes(voxel, 0)

# mcubes.export_mesh(vertices, triangles, "scene.dae", "MyScene")

# Write mesh to file

# o3d.io.write_triangle_mesh("outputs/output.ply", mesh) 

