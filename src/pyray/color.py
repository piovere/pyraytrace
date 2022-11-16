class Color:
    def __init__(self, r: float, g: float, b: float):
        self.r: float = r
        self.g: float = g
        self.b: float = b
    
    def channels(self) -> list[float]:
        return [self.r, self.g, self.b]
    
    def scale(self) -> list[int]:
        return [int(255.999 * c) for c in self.channels()]
    
    def __str__(self):
        r, g, b = self.scale()
        return f"{r} {g} {b}"
    
    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"
