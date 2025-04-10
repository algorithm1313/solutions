def solution(dirs):
    visited = set()
    current = (0, 0)
    count = 0
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            before_x, before_y = current
            after_x, after_y = current[0], current[1] + 1
            if after_y > 5:
                after_y = 5
            current = (after_x, after_y)
            path = (before_x, before_y, after_x, after_y)
            reverse_path = (after_x, after_y, before_x, before_y)
            if path not in visited and reverse_path not in visited and (before_x != after_x or before_y != after_y):
                visited.add(path)
                visited.add(reverse_path)
                count += 1
        elif dirs[i] == 'D':
            before_x, before_y = current
            after_x, after_y = current[0], current[1] - 1
            if after_y < -5:
                after_y = -5
            current = (after_x, after_y)
            path = (before_x, before_y, after_x, after_y)
            reverse_path = (after_x, after_y, before_x, before_y)
            if path not in visited and reverse_path not in visited and (before_x != after_x or before_y != after_y):
                visited.add(path)
                visited.add(reverse_path)
                count += 1
        elif dirs[i] == 'R':
            before_x, before_y = current
            after_x, after_y = current[0] + 1, current[1]
            if after_x > 5:
                after_x = 5
            current = (after_x, after_y)
            path = (before_x, before_y, after_x, after_y)
            reverse_path = (after_x, after_y, before_x, before_y)
            if path not in visited and reverse_path not in visited and (before_x != after_x or before_y != after_y):
                visited.add(path)
                visited.add(reverse_path)
                count += 1
        else:  # 'L'
            before_x, before_y = current
            after_x, after_y = current[0] - 1, current[1]
            if after_x < -5:
                after_x = -5
            current = (after_x, after_y)
            path = (before_x, before_y, after_x, after_y)
            reverse_path = (after_x, after_y, before_x, before_y)
            if path not in visited and reverse_path not in visited and (before_x != after_x or before_y != after_y):
                visited.add(path)
                visited.add(reverse_path)
                count += 1
    return count
