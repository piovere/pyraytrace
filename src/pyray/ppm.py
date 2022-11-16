from typing import Union
from pathlib import Path

from .color import Color

class PPM:
    def __init__(self, data: list[list[Color]]):
        self.data: list[list[Color]] = data
        self.height: int = len(data)
        self.width: int = len(data[0])
    
    def write(self, p: Path):
        with open(p, "w") as f:
            f.write(f"P3\n{self.width} {self.height}\n255")
            
            for line in self.data:
                outstr = " ".join([str(l) for l in line])
                
                while len(outstr) > 70:
                    # find the last space
                    i = 69
                    while outstr[i] != " ":
                        i -= 1
                    f.write(outstr[:i+1])
                    f.write("\n")
                    outstr = outstr[i+i:]
                
                f.write(outstr)
                f.write("\n")
