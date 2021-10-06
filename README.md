# pyvec

a simple package for handling vectors of any size.

all* your favorite vector operations are here, and generalized to n-dimensional vectors. want to add three 4D vectors? dot product a 8D and 3D vector together? you can do it!

**\*disclaimer: i still haven't figured out how to implement the cross product in n dimensions, so right now, it only works on vectors <= 3 dimensions. sorry**

# examples
defining a vector is as simple as passing the constructor an n-dimensional array of scalar values!
```python
v = Vector([a, b, c,... y, z])
```
you can also create `Vector`s using magnitude/direction notation:
```python
# using magnitude, and the angle from each axis
v1 = Vector.fromMagnitudeRad(m, [α, β, ɣ,...])

# the vector between two points in n-dimensional space
v2 = Vector.fromTwoPoints([a₁, b₁, c₁,...], [a₂, b₂, c₂,...])

# for the special case of 3D vectors in a spherical coordinate system 
# (note this is NOT the same as Vector.fromMagnitudeRad(r, [θ, φ])
v3 = Vector.fromSpherical(r, θ, φ)
```

from there, you can do all sorts of fun unary and binary operations!
```python
v3 = v1.unitVector()

# returns the sector the vector is in, given as an array made up of either 1, 0, or -1
array = v1.sector()

# x(), y(), and z() are convenience methods to return the 1st, 2nd, or 3rd-dimensional component of a vector
f = v1.x()

v2 = v1.scale(7)

boolean = v1.parallel(v2)
boolean = v1.perpendicular(v2)

# returns the angle between v1 and v2
angle = v1.angleTo(v2)

v3 = v1.dot(v2)
v3 = v1.cross(v2)
```
and more!
you can also access various components of the vectors:
```python
# returns the components of a vector as a list
array = v1.toArray()

# returns the angle the vector makes from the positive axis in the i dimension (x = 0, y = 1, etc)
angle = v1.alphaRad(i)

```

you can also use the good ol' `+` and `-` operators to add and subtract both vectors and scalars!
```python
# v2 is a vector in the same direction as v1 but its length is 5 more
v2 = v1 + 5

# v3 is the difference between v1 and v2
v3 = v1 - v2
```
