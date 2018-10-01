"""
Sample case for building it up
Only for testing!
"""

# Rectangles for initial testing. x1, y1, x2, y2. Corner points
TARGETS =[
    [14, 20, 7, 10],
    [3, 5, 7, 8],
    [0, 0, 3, 3],
    [4, 4, 8, 8]
]


# probablities, x1, x2, y1, y2
ESTIMATES =[
    [20, 14, 20, 7, 10],
    [30, 100, 100, 200, 200],
    [80, 3, 5, 7, 8],
    [70, 100, 100, 200, 200],
    [60, 0, 0, 3, 3],
    [65, 0, 0, 3, 3],
    [50, 100, 100, 200, 200],
    [30, 4, 4, 8, 8]
]


def quad_corners_to_coords(corners):
    """ Rectangle endpoints to 8 values"""
    # For testing only. This won't be pretty. Especially the input
    return [(corners[0], corners[1]),
            (corners[2], corners[1]),
            (corners[2], corners[3]),
            (corners[0], corners[3])]


def sample_estimates():
    """ Returns a list of estimates for testing, [[prob, 8 values], ... ] """
    return list(map(lambda x: (x[0], quad_corners_to_coords(x[1:])), ESTIMATES))


def sample_targets():
    """ Sample targets for testing, list of 8 values each """
    return list(map(quad_corners_to_coords, TARGETS))
