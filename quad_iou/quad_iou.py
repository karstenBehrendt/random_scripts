#!/usr/bin/env python3
"""
A quadrilateral to quadrilateral IOU shapely API simplification
for this special case with a couple of extra dimension checks
"""

import numpy
from shapely.geometry import Polygon


def quad_iou(poly1, poly2):
    """ IOU for quadrilaterals with some checks
    Calculates the intersection over union between quadrilaterals, e.g. boxes.
    Is optimized to catch a few input errors rather than runtime efficiency.
    Use case is object detection network output evaluation (not only boxes).
    Args:
        poly1: iterable, dimension of shape 4,2
        poly2: iterable, dimension of shape 4,2
    Returns: IOU between to quads
    Raises: ValueError for self-intersecting quads or non-box polygons
    """
    try:
        poly1_array = numpy.array(poly1)
        poly2_array = numpy.array(poly2)
    except:
        print('quad_iou input could not be turned into numpy.array')
        raise

    if poly1_array.shape != (4,2):
        raise ValueError('poly1 of wrong dimensions: {}'.format(poly1))
    if poly2_array.shape != (4,2):
        raise ValueError('poly2 of wrong dimensions: {}'.format(poly2))

    poly1 = Polygon(numpy.array(poly1_array))
    poly2 = Polygon(numpy.array(poly2_array))

    # Mainly for self-intersection
    if not poly1.is_valid:
        raise ValueError('poly1 is invalid, likely self-intersecting: {}'.
                         format(poly1_array))
    if not poly2.is_valid:
        raise ValueError('poly2 is invalid, likely self-intersecting: {}'.
                         format(poly2_array))

    intersection_area = poly1.intersection(poly2).area
    union_area = poly1.union(poly2).area

    return intersection_area / union_area


if __name__ == '__main__':
    poly1 = [(0, 0), (0, 1), (1, 1), (1, 0)]
    poly2 = [[val / 2 for val in coord] for coord in poly1]
    print('Running sample case:')
    print('Poly1:', poly1)
    print('Poly2:', poly2)
    print('Intersection over union:', quad_iou(poly1, poly2))
