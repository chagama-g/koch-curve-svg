import svgwrite
import numpy as np


def rot(v, theta):
    R = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    return np.dot(R, v)


# 終点を除いて、新しく生成した頂点を返す
def unit(p_start, p_end):
    p1 = p_start + (p_end - p_start) / 3
    p2 = p1 + rot(p1 - p_start, -np.pi / 3)
    p3 = p_start + (p_end - p_start) * 2 / 3
    _points = [
        p_start,
        p1, p2, p3
    ]
    return _points


def next_step(points):
    new_points = []
    for i in range(len(points)-1):
        p1 = points.pop(0)
        p2 = points[0]

        new_points += unit(p1, p2)
    new_points.append(points[0])
    return new_points


def main():
    WIDTH = 300 * 6

    N = 6

    points = [np.array([0, 0]), np.array([WIDTH, 0])]

    for step in range(N):
        print(f"step: {step}")

        points_list = [(int(p[0]), int(p[1])) for p in points]

        filename = f"koch-{step}"
        svg_filename = f"{filename}.svg"

        dwg = svgwrite.Drawing(svg_filename)
        dwg.add(dwg.polyline(points_list, stroke="black",
                fill="none", stroke_width=1))
        dwg.save()

        points = next_step(points)


if __name__ == "__main__":
    main()
