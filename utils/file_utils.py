import pathlib
import re

def natural_key(string_):
    """See http://www.codinghorror.com/blog/archives/001018.html"""
    return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_)]

def load_folder(folder):
    paths = pathlib.Path(folder).glob('*')
    paths = [str(path) for path in paths]
    paths.sort(key = natural_key)

    return paths

class SimpleMesh:
    def __init__(self, v, f):
        self.points = v
        self.triangles = f
    
    @property
    def v(self):
        return self.points

    @property
    def f(self):
        return self.triangles