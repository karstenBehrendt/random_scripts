#!/usr/bin/env python3
"""
Calculate mean average precision for evaluating
object detection models

"""

import polygon_iou


def precision(tp, fp):
    return tp / (tp + fp)


def recall(tp, fn):
    return tp / (tp + fn)


def pr_values(targets, estimates, required_iou=.5):
    estimates = sorted(estimates, key=lambda x: x[0], reverse=True)

    precisions = []
    recalls = []
    false_positives = 0
    true_positives = 0
    for estimate in estimates:
        target_ious = list(map(
            lambda x: polygon_iou.polygon_iou(estimate[1], x), targets))

        # false positive / smaller than required_iou
        if not any(map(lambda x: x >= required_iou, target_ious)):
            false_positives += 1
            continue

        # remove largest overlap from targets to not count it twice
        true_positives += 1
        max_index = target_ious.index(max(target_ious))
        del target_ious[max_index]

        precisions.append(precision(true_positives, false_positives))
        recalls.append(recall(true_positives, len(targets)))
    return precisions, recalls


def average_precision(precisions, recalls):
    precisions = [precisions[0]] + precisions
    recalls = [0] + recalls

    ap = 0
    for i in range(1, len(precisions)):
        ap += precisions[i] * (recalls[i] - recalls[i - 1])
    return ap
