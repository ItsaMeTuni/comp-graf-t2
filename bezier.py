from vec import Vec

def quadratic_curve(vecs, t):
    p0 = Vec((1-t) ** 2 * vecs[0].x, (1-t) ** 2 * vecs[0].y)
    p1 = Vec(2 * (1-t) * t * vecs[1].x, 2 * (1-t) * t * vecs[1].y)
    p2 = Vec(t ** 2 * vecs[2].x, t ** 2 * vecs[2].y)

    return p0 + p1 + p2


