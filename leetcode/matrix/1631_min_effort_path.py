def min_effort_path(heights):
    right_path = sub_min_effort_path(heights, 0, 1, 100000)
    down_path = sub_min_effort_path(heights, 1, 0, 100000)


def sub_min_effort_path(heights, row_index, column_index, effort):
    if len(heights) - 1 == row_index and len(heights[0]) - 1 == column_index: return effort

    effort = min([abs(heights[row_index][column_index] - heights[row_index + 1][column_index]),
                  abs(heights[row_index][column_index] - heights[row_index][column_index + 1]), effort])

    right_path = sub_min_effort_path(heights, row_index, column_index + 1, effort)
    down_path = sub_min_effort_path(heights, row_index + 1, column_index, effort)

    return min(right_path, down_path)
