from typing import Union

from pyray import EPSILON

class Threeple:
    def __init__(self, x: float, y: float, z: float, w: int):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    
    @property
    def is_point(self):
        return self.w == 1
    
    def is_vector(self):
        return self.w == 0
    
    def __add__(self, o):
        if isinstance(o, Threeple):
            ret = Threeple(
                self.x + o.x,
                self.y + o.y,
                self.z + o.z,
                self.w + o.w
            )
            return ret
    
    def __radd__(self, o):
        return self.__add__(o)
    
    def __iadd__(self, o):
        self.x += o.x
        self.y += o.y
        self.z += o.z
        self.w += o.w
    
    def magnitude(self) -> float:
        return magnitude(self)
    
    def norm(self) -> None:
        m = self.magnitude()
        self.x /= m
        self.y /= m
        self.z /= m
        self.w /= m
    
    def dot(self, o) -> float:
        return dot(self, o)
    
    def cross(self, o):
        return cross(self, o)
    
    def __mul__(self, o: float):
        return Threeple(
            self.x * o,
            self.y * o,
            self.z * o,
            self.w * o
        )
    
    def __rmul__(self, o: float):
        return self.__mul__(o)
    
    def __truediv__(self, o: float):
        return self.__mul__(1 / o)
    
    def __neg__(self):
        return Threeple(
            -self.x,
            -self.y,
            -self.z,
            -self.w
        )
        
    def __sub__(self, o):
        return self + -o
    
    def magnitude(self):
        return self.dot(self)**0.5
    
    def __eq__(self, o):
        return (approx(self.x, o.x) and approx(self.y, o.y) and \
            approx(self.z, o.z) and approx(self.w, o.w))
    
    def __unicode__(self) -> str:
        if self.w == 1:
            return f"Point({self.x}, {self.y}, {self.z})"
        elif self.w == 0:
            return f"Vector({self.x}, {self.y}, {self.z})"
        else:
            return f"Threeple({self.x}, {self.y}, {self.z}, {self.w})"
    
    def __str__(self) -> str:
        return self.__unicode__()
    
    def __repr__(self) -> str:
        return f"Threeple({self.x}, {self.y}, {self.z}, {self.w})"

def point(x: float, y: float, z: float) -> Threeple:
    return Threeple(x, y, z, 1)

def vector(x: float, y: float, z: float) -> Threeple:
    return Threeple(x, y, z, 0)

def approx(a: float, b: float) -> bool:
    return abs(a - b) < EPSILON

def dot(a: Threeple, b: Threeple) -> float:
    return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

def magnitude(a: Threeple) -> float:
    return dot(a, a)**0.5

def norm(a: Threeple) -> Threeple:
    return a / magnitude(a)

def cross(a: Threeple, b: Threeple) -> Threeple:
    x = a.y * b.z - a.z * b.y
    y = a.z * b.x - a.x * b.z
    z = a.x * b.y - a.y * b.x
    return vector(x, y, z)
