"""
solution for day 14 part 1 and 2
"""
from day10_2 import hash_knot

TEST_INPUT = "flqrgnkx"
DAY14_INPUT = "nbysizxe"

def build_hash_knot_grid(input_data):
    """
    builds 128x128 grid for binary representation of hash knots
    """
    rows = []
    for i in range(128):
        hash_knot_value = hash_knot(input_data + "-" + str(i))
        rows.append(bin(int(hash_knot_value, 16))[2:].zfill(128))
    return rows

GRID_DIMENSION = 128

class GridPoint(object):
    """
    a point in the region grid
    """
    row = 0
    column = 0
    region = 0

    def __init__(self, row=0, column=0):
        self.row = row
        self.column = column

def solve(input_data):
    """
    solve day 14 part 1 and 2
    """
    hash_knot_grid = build_hash_knot_grid(input_data)

    return count_ones(hash_knot_grid), count_regions(hash_knot_grid)

def count_ones(hash_knot_grid):
    """
    part 1
    """
    count = 0
    for row in hash_knot_grid:
        count += row.count('1')
    return count

def count_regions(hash_knot_grid):
    """
    part 2
    """
    number_of_regions = 0
    regions = 0
    region_grid = build_region_grid()

    for row_index, row in enumerate(hash_knot_grid):
        for column_index, column in enumerate(row):
            grid_point = region_grid[row_index][column_index]
            if grid_point.region == 0:
                if column == '1':
                    north, east, south, west = get_cardinal_points(grid_point, region_grid)
                    max_region = max(\
                        north.region, east.region, south.region, west.region)
                    if max_region == 0:
                        regions += 1
                        number_of_regions += 1
                        region_grid[row_index][column_index].region = regions
                    else:
                        min_region = min([r for r in [north.region, east.region, south.region, west.region] if r > 0])
                        if min_region == max_region:
                            region_grid[row_index][column_index].region = max_region
                        else:
                            region_grid[row_index][column_index].region = min_region
                            reregioned = set()
                            if north.region != 0 and north.region != min_region:
                                reregioned.add(north.region)
                                reregion(north, region_grid, min_region)
                            if east.region != 0 and east.region != min_region:
                                reregioned.add(east.region)
                                reregion(east, region_grid, min_region)
                            if south.region != 0 and south.region != min_region:
                                reregioned.add(south.region)
                                reregion(south, region_grid, min_region)
                            if west.region != 0 and west.region != min_region:
                                reregioned.add(west.region)
                                reregion(west, region_grid, min_region)
                            number_of_regions -= len(reregioned)
    return number_of_regions

def build_region_grid():
    """
    builds a grid of points for storing region info
    """
    region_grid = []
    for row in range(128):
        region_grid.append([])
        for column in range(128):
            region_grid[row].append(GridPoint(row, column))
    return region_grid

def reregion(grid_point, region_grid, new_region):
    """
    reregion a point in the region_grid as well as it's neighbours
    """
    north, east, south, west = get_cardinal_points(grid_point, region_grid)
    old_region = grid_point.region
    grid_point.region = new_region
    if north.region == old_region:
        reregion(north, region_grid, new_region)
    if east.region == old_region:
        reregion(east, region_grid, new_region)
    if south.region == old_region:
        reregion(south, region_grid, new_region)
    if west.region == old_region:
        reregion(west, region_grid, new_region)

def get_cardinal_points(grid_point, region_grid):
    """
    get the cardinal points for given point in grid
    """
    north = GridPoint()
    east = GridPoint()
    south = GridPoint()
    west = GridPoint()
    row_index = grid_point.row
    column_index = grid_point.column
    if row_index > 0:
        north = region_grid[row_index - 1][column_index]
    if row_index < 127:
        south = region_grid[row_index + 1][column_index]
    if column_index > 0:
        west = region_grid[row_index][column_index - 1]
    if column_index < 127:
        east = region_grid[row_index][column_index + 1]
    return north, east, south, west

print solve(TEST_INPUT)
print solve(DAY14_INPUT)
