import geopandas as gpd
collisions = gpd.read_file('nyc-collision-factors.geojson')

import sys; sys.path.append('.')
from sync_quadtree import QuadTree
result = QuadTree(collisions).partition(1, 5)