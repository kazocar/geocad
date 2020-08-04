import vtk

class CAD(object):
    """
    TODO Description
    """
    def __init__(self):
        pass

    def import(file_name):
        pass

class Surface(CAD):
    """
    TODO Description
    """
    def __init__(self):
        pass

    def rotate(self, origin, axis, rotation_angle):
        """
        :param origin:
        :param axis:
        :param rotation_angle:
        :return:
        """
        pass

    def translate(self, x, y, z):
        pass

    def clip(self):
        pass

    def convex_crop(self):
        pass

    def fill_holes(self):
        pass

    def cut_section(self, dxf_output=None):
        pass

    def convert(self, file_type):
        pass

    def check_triangulation_quality(self):
        pass

class Polyline(CAD):
    """
    TODO Description
    """
    def __init__(self, pts=None, cad_file=None):
        pass

    def rotate(self, origin, axis, rotation_angle):
        pass

    def translate(self):
        pass

    def to_xy(self, to_origin=False):
        pass

    def get_azimuth(self):
        pass

    def clip_x(self):
        pass

    def clip_y(self):
        pass

    def clip_z(self):
        pass

    def save_dxf(self):
        pass