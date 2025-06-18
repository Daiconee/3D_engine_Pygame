class Vec3d:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def get_py_point(self):
        return (self.x, self.y)
