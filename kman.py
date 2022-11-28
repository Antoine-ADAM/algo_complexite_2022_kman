from typing import Tuple, List

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __getitem__(self, i):
        if i == 0:
            return self.x
        elif i == 1:
            return self.y
        else:
            raise Exception

    @staticmethod
    def from_list(points: List[Tuple[float, float]]):
        return [Point(e[0], e[1]) for e in points]

def kman(points: List[Point], n_cluster: int):
    clusters = [(e, [e]) for e in points]
    if n_cluster < 1 or n_cluster >= len(points):
        raise Exception("n_cluster invalid")
    for i in range(len(points)-n_cluster):
        min_a = -1
        min_b = -1
        min_value = pow(clusters[0][0][0] - clusters[1][0][0], 2) + pow(clusters[0][0][1] - clusters[1][0][1], 2) + 1
        for a in clusters:
            for b in clusters:
                if a != b:
                    distance = pow(a[0][0] - b[0][0], 2) + pow(a[0][1] - b[0][1], 2)
                    if min_value > distance:
                        min_a = a
                        min_b = b
                        min_value = distance
        clusters.remove(min_a)
        clusters.remove(min_b)
        somme_x = 0
        somme_y = 0
        for e in min_a[1]:
            somme_x += e[0]
            somme_y += e[1]
        for e in min_b[1]:
            somme_x += e[0]
            somme_y += e[1]
        len_all = len(min_a[1]) + len(min_b[1])
        clusters.append((Point(somme_x/len_all, somme_y/len_all), min_a[1] + min_b[1]))
    return clusters
