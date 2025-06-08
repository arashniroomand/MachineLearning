# mean_shift_core.py

def get_neighbors(point, data, bandwidth):
    return [other for other in data if abs(point - other) <= bandwidth]

def shift_point(point, data, bandwidth, tol=1e-3, max_iter=100):
    for _ in range(max_iter):
        neighbors = get_neighbors(point, data, bandwidth)
        if not neighbors:
            break
        new_point = sum(neighbors) / len(neighbors)
        shift = abs(new_point - point)
        point = new_point
        if shift < tol:
            break
    return point

def mean_shift(data, bandwidth, max_iter=100, tol=1e-3):
    shifted_points = data.copy()
    iterations = [0] * len(data)
    
    for i, point in enumerate(shifted_points):
        count = 0
        while count < max_iter:
            neighbors = get_neighbors(point, data, bandwidth)
            if not neighbors:
                break
            new_point = sum(neighbors) / len(neighbors)
            shift = abs(new_point - point)
            point = new_point
            count += 1
            if shift < tol:
                break
        shifted_points[i] = point
        iterations[i] = count
    
    return shifted_points, iterations

def group_clusters(shifted_points, tol=0.5):
    clusters = []
    cluster_ids = []

    for point in shifted_points:
        found = False
        for i, center in enumerate(clusters):
            if abs(point - center) < tol:
                cluster_ids.append(i)
                found = True
                break
        if not found:
            clusters.append(point)
            cluster_ids.append(len(clusters) - 1)

    return cluster_ids, clusters
