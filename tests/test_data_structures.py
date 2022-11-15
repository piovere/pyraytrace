import pytest

from pyray.structs import *

@pytest.fixture
def threeples():
    return Threeple(3, -2, 5, 1), Threeple(-2, 3, 1, 0)

@pytest.fixture
def points():
    return point(4.3, -4.2, 3.1), point(3, 2, 1), point(5, 6, 7)

@pytest.fixture
def vectors():
    return vector(4.3, -4.2, 3.1), vector(3, 2, 1), vector(5, 6, 7)

def test_a_tuple_with_w_one_is_a_point(threeples, points, vectors):
    a, b = threeples
    assert a.is_point
    assert b.is_vector
    assert all(p.is_point for p in points)
    assert all(v.is_vector for v in vectors)

def test_adding_threeples(threeples):
    a, b = threeples
    assert a + b == Threeple(1, 1, 6, 1)

def test_subtracting_points(points):
    _, a, b = points
    assert a - b == vector(-2, -4, -6)

def test_subtracting_vectors(vectors):
    _, a, b = vectors
    assert a - b == vector(-2, -4, -6)

def test_subtracting_vector_from_point(vectors, points):
    _, p, _ = points
    _, _, v = vectors
    assert p - v == point(-2, -4, -6)

def test_scalar_multiplication():
    a = Threeple(1, -2, 3, -4)
    assert a * 3.5 == Threeple(3.5, -7, 10.5, -14)

def test_scalar_division():
    a = Threeple(1, -2, 3, -4)
    assert a / 2 == Threeple(0.5, -1, 1.5, -2)

def test_magnitude():
    v = vector(1, 0, 0)
    assert approx(magnitude(v), 1)
    
    v = vector(0, 1, 0)
    assert approx(magnitude(v), 1)
    
    v = vector(0, 0, 1)
    assert approx(magnitude(v), 1)
    
    v = vector(1, 2, 3)
    assert approx(magnitude(v), 14**0.5)
    
    v = vector(-1, -2, -3)
    assert approx(magnitude(v), 14**0.5)

def test_normalization():
    v = vector(4, 0, 0)
    v.norm()
    assert v == vector(1, 0, 0)
    
    v = vector(1, 2, 3)
    assert norm(v) == vector(0.26726, 0.53452, 0.80178)
    
    n = norm(v)
    assert approx(magnitude(n), 1.0)

def test_dot_product():
    a = vector(1, 2, 3)
    b = vector(2, 3, 4)
    
    assert approx(dot(a, b), 20)
    assert approx(a.dot(b), 20)

def test_cross_product():
    a = vector(1, 2, 3)
    b = vector(2, 3, 4)
    
    assert cross(a, b) == vector(-1, 2, -1)
    assert cross(b, a) == vector(1, -2, 1)
    
    assert a.cross(b) == vector(-1, 2, -1)
    assert b.cross(a) == vector(1, -2, 1)
