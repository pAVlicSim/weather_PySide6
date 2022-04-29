def y_axis_range(ls: list):
    full_axes = []
    # for i in y_axes:
    #     full_axes.extend(i)
    full_axes = sum(ls, [])
    return [int(min(set(full_axes))), int(max(set(full_axes)))]


print(y_axis_range([[-3.5, 6, 3], [5, 10, 3.3], [11.7, 7, 8]]))
