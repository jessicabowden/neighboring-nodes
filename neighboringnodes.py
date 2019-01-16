from enum import Enum


def divide_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


class NeighborhoodShape(Enum):
    SQUARE = "square"
    CROSS = "cross"
    DIAMOND = "diamond"


class NeighboringNodes:
    def __init__(self, size, debug):
        self.size = size
        self.debug = debug
        self.grid = self.construct_grid()

        if self.debug:
            for current_y, inner_list in enumerate(self.grid):
                for current_x, i in enumerate(inner_list):
                    print(current_x, current_y, i)

    def construct_grid(self):
        i_values = list(range(self.size*self.size))
        split_list = list(divide_list(i_values, self.size))
        return split_list

    def get_position(self, idx):
        if (idx > (self.size * self.size - 1)) or (idx < 0):
            raise ValueError('ID out of bounds')

        for current_y, inner_list in enumerate(self.grid):
            for current_x, i in enumerate(inner_list):
                if i == idx:
                    return current_x, current_y

    def get_neighbors_coordinates(self, m, n_type, x=None, y=None, i=None):
        if not isinstance(n_type, NeighborhoodShape):
            raise TypeError('Parameter n_type must be an instance of NeighborhoodShape')

        if n_type == NeighborhoodShape.SQUARE:
            return self._get_neighbors_coordinates_square(m, x, y, i)
        if n_type == NeighborhoodShape.CROSS:
            return self._get_neighbors_coordinates_cross(m, x, y, i)
        if n_type == NeighborhoodShape.DIAMOND:
            return self._get_neighbors_coordinates_diamond(m, x, y, i)

    def _get_neighbors_coordinates_square(self, m, x=None, y=None, i=None):
        if i:
            target_node_x, target_node_y = self.get_position(i)
        elif x and y:
            target_node_x = x
            target_node_y = y

        neighbors = []

        for current_y, inner_list in enumerate(self.grid):
            for current_x, val in enumerate(inner_list):
                distance_x = target_node_x - current_x
                distance_y = target_node_y - current_y

                if distance_x == 0 and distance_y == 0:
                    continue
                if distance_x < -m or distance_x > m:
                    continue
                elif distance_y < -m or distance_y > m:
                    continue
                else:
                    neighbors.append((current_x, current_y))

        return neighbors

    def _get_neighbors_coordinates_cross(self, m, x=None, y=None, i=None):
        neighbors = []

        if i:
            target_node_x, target_node_y = self.get_position(i)
        else:
            target_node_x = x
            target_node_y = y

        for current_y, inner_list in enumerate(self.grid):
            for current_x, val in enumerate(inner_list):
                distance_x = target_node_x - current_x
                distance_y = target_node_y - current_y

                if distance_x == 0 and distance_y == 0:
                    continue
                if current_y == target_node_y and distance_x in list(range(-m, m+1)):
                    neighbors.append((current_x, current_y))
                if current_x == target_node_x and distance_y in list(range(-m, m+1)):
                    neighbors.append((current_x, current_y))
        return neighbors

    def _get_neighbors_coordinates_diamond(self, m, x=None, y=None, i=None):
        neighbors = []

        if i:
            target_node_x, target_node_y = self.get_position(i)
        else:
            target_node_x = x
            target_node_y = y

        for j, inner_list in enumerate(self.grid):
            distance_x = target_node_x - j
            if distance_x < 0:
                range_width = distance_x + m
                x_ranges = list(range(-range_width, range_width+1))
            elif distance_x >= 0:
                range_width = m - distance_x
                x_ranges = list(range(-range_width, range_width+1))

            for x_range in x_ranges:
                neighbor_on_current_row = target_node_x - x_range
                neighbor_indices = (j, neighbor_on_current_row)
                neighbors.append(neighbor_indices)

        return neighbors
