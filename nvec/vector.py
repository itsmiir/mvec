from math import radians, cos, sin, sqrt, acos, degrees, pi


class Vector(object):
    def __init__(self, d):
        super(Vector, self).__init__()
        self.d = d

    def __str__(self):
        i = self.dimensions()
        f = round(self.magnitude(), 3)
        return(str(i) + "D Vector of length " + str(f))

    def __add__(self, other):
        v = []
        try:
            if self.dimensions() >= other.dimensions():
                for i in range(self.dimensions()):
                    try:
                        v.append(self.d[i] + other.d[i])
                    except Exception:
                        v.append(self.d[i])
            else:
                for i in range(other.dimensions()):
                    try:
                        v.append(self.d[i] + other.d[i])
                    except Exception:
                        v.append(other.d[i])
        except AttributeError:
            m = self.magnitude() + other
            unit = self.unitVector()
            return unit.scale(m)
        return Vector(v)

    def __sub__(self, other):
        v = []
        try:
            if self.dimensions() >= other.dimensions():
                for i in range(self.dimensions()):
                    try:
                        v.append(self.d[i] - other.d[i])
                    except Exception:
                        v.append(self.d[i])
            else:
                for i in range(other.dimensions()):
                    try:
                        v.append(self.d[i] - other.d[i])
                    except Exception:
                        v.append(-other.d[i])
        except AttributeError:
            m = self.magnitude() - other
            unit = self.unitVector()
            return unit.scale(m)
        return Vector(v)

    def __eq__(self, other):
        if self.magnitude() == other.magnitude():
            return (self.scalarProjection(other) == self.magnitude())
        else:
            return False

    def x(self):
        """Helper methods to quickly
        get the first three coordinates of a vector"""
        if self.dimensions() < 1:
            return 0
        else:
            return self.d[0]

    def y(self):
        if self.dimensions() < 2:
            return 0
        else:
            return self.d[1]

    def z(self):
        if self.dimensions() < 3:
            return 0
        else:
            return self.d[2]

    def magnitude(self):
        sum = 0
        for x in self.d:
            sum += x**2
        return sqrt(sum)

    def dimensions(self):
        return (len(self.d))

    def dot(self, other):
        sum = 0
        if self.dimensions() >= other.dimensions():
            for i in range(self.dimensions()):
                try:
                    sum += (self.d[i] * other.d[i])
                except Exception:
                    pass
        else:
            for i in range(other.dimensions()):
                try:
                    sum += (self.d[i] * other.d[i])
                except Exception:
                    pass
        return sum

    def cross(self, other):
        x = self.y() * other.z() - self.z() * other.y()
        y = self.z() * other.x() - self.x() * other.z()
        z = self.x() * other.y() - self.y() * other.x()
        return Vector([x, y, z])

    def scalarProjection(self, other):
        return self.magnitude() * cos(self.anglebetween(other))

    def angleTo(self, other):
        return acos(self.dot(other) / (self.magnitude() * other.magnitude()))

    def toArray(self, rnd=False, r=5):
        if rnd:
            b = []
            for i in self.d:
                b.append(round(i, r))
            return b
        return self.d

    def scale(self, mul):
        c = []
        for i in range(self.dimensions()):
            c.append(self.d[i] * mul)
        return Vector(c)

    def unitVector(self):
        return self.scale(1 / self.magnitude())

    def alphaRad(self, dim):
        try:
            return acos(self.d[dim] / self.magnitude())
        except Exception:
            return 0

    def alphaDeg(self, dim):
        return degrees(self.alphaRad(dim))

    def sector(self):
        """returns the sector in which a vector lies, in the form
        [-1, 1] (for a 2D vector in quadrant II)"""
        sector = []
        for i in range(self.dimensions()):
            if self.d[i] != 0:
                sector.append(abs(self.d[i]) / self.d[i])
            else:
                sector.append(0)
        return sector

    def fromMagnitudeRad(m, alphas):
        v = []
        try:
            for i in alphas:
                v.append(m * cos(i))
            return Vector(v)
        except TypeError:
            try:
                return Vector([m * cos(i), m * sin(i)])
            except Exception as e:
                raise e

    def fromMagnitudeDeg(m, alphas):
        v = []
        try:
            for i in alphas:
                v.append(radians(i))
            return Vector.fromMagnitudeRad(m, v)
        except TypeError:
            return Vector.fromMagnitudeRad(m, [radians(alphas)])

    def fromTwoPoints(a, b, m=0):
        """generates a vector given two points (direction from a to b)
        m = the length of the vector"""
        c = []
        if len(a) >= len(b):
            for i in range(len(a)):
                c.append(b[i] - a[i])
        else:
            for i in range(len(b)):
                c.append(b[i] - a[i])
        d = Vector(c).toMagnitudeAngle()
        if m != 0:
            d[0] = m
        return Vector.fromMagnitudeRad(d[0], d[1])

    def fromSpherical(r, theta, phi):
        """returns a 3D vector in spherical coordinates"""
        return Vector.fromMagnitudeRad(r, [theta, (pi / 2) - theta, phi])

    def toMagnitudeAngle(self):
        alphas = []
        magnitude = self.magnitude()
        for i in self.d:
            alphas.append(acos(i / magnitude))
        return [magnitude, alphas]

    def toMagnitudeAngleDeg(self):
        alphas = []
        magnitude = self.magnitude()
        for i in self.d:
            alphas.append(degrees(acos(i / magnitude)))
        return [magnitude, alphas]

    def directionTo(self, other):
        """returns the unit vector in the direction from self to other"""
        return (other - self).unitVector()

    def parallel(self, other):
        return (self.anglebetween(other) == 0)

    def perpendicular(self, other):
        return (self.anglebetween(other) == (pi / 2))

v = Vector([7, 6])
print(v)
