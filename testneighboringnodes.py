import unittest
from neighboringnodes import NeighboringNodes, NeighborhoodShape


class TestNeighboringNodes(unittest.TestCase):
    def setUp(self):
        self.nn_instance = NeighboringNodes(6, False)

    def test_invalid_idx_on_get_position(self):
        self.assertRaises(ValueError, self.nn_instance.get_position, 52)

    def test_valid_idx_on_get_position(self):
        assert self.nn_instance.get_position(3) == (3, 0)

    def test_grid_values(self):
        expected_grid = [
            [0, 1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10, 11],
            [12, 13, 14, 15, 16, 17],
            [18, 19, 20, 21, 22, 23],
            [24, 25, 26, 27, 28, 29],
            [30, 31, 32, 33, 34, 35]
        ]
        assert self.nn_instance.grid == expected_grid

    def test_get_neighbors_coordinates_square_with_i(self):
        m = 2
        target_node = 14
        expected_values = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2),
                           (1, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4),
                           (3, 4), (4, 4)]

        assert self.nn_instance.get_neighbors_coordinates(m, NeighborhoodShape.SQUARE, i=target_node) == expected_values

    def test_get_neighbors_coordinates_square_with_x_y(self):
        m = 2
        x, y = 2, 2
        expected_values = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (0, 2),
                           (1, 2), (3, 2), (4, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (0, 4), (1, 4), (2, 4),
                           (3, 4), (4, 4)]

        assert self.nn_instance.get_neighbors_coordinates(m, NeighborhoodShape.SQUARE, x=x, y=y) == expected_values

    def test_get_neighbors_coordinates_square_with_m_equals_1(self):
        m = 1
        target_node = 14
        expected_values = [(1, 1), (2, 1), (3, 1), (1, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

        assert self.nn_instance.get_neighbors_coordinates(m, NeighborhoodShape.SQUARE, i=target_node) == expected_values

    def test_get_neighbors_coordinates_cross(self):
        m = 2
        target_node = 15
        expected_values = [(3, 0), (3, 1), (1, 2), (2, 2), (4, 2), (5, 2), (3, 3), (3, 4)]

        assert self.nn_instance.get_neighbors_coordinates(m, NeighborhoodShape.CROSS, i=target_node) == expected_values

    def test_get_neighbors_coordinates_diamond(self):
        m = 2
        target_node = 14
        expected_values = [(0, 2), (1, 3), (1, 2), (1, 1), (2, 4), (2, 3), (2, 2), (2, 1), (2, 0), (3, 3),
                           (3, 2), (3, 1), (4, 2)]

        assert self.nn_instance.get_neighbors_coordinates(m, NeighborhoodShape.DIAMOND, i=target_node) == expected_values

    def test_get_neighbors_by_edge(self):
        m = 3
        target_node = 13
        expected_values = [(1, 0), (1, 1), (0, 2), (2, 2), (3, 2), (4, 2), (1, 3), (1, 4), (1, 5)]

        assert self.nn_instance.get_neighbors_coordinates(m, NeighborhoodShape.CROSS, i=target_node) == expected_values


if __name__ == '__main__':
    unittest.main()
