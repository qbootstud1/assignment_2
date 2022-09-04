import random
from typing import IO, TextIO


class ArtConfig:
    shapes_counter = -1
    shape_range: tuple = tuple((0, 2))
    color_range: tuple = tuple((0, 255))
    rad_range: tuple = tuple((0, 100))
    rx_range: tuple = tuple((10, 30))
    ry_range: tuple = tuple((10, 30))
    width_range: tuple = tuple((10, 100))
    height_range: tuple = tuple((10, 100))
    op_range: tuple = tuple((0.0, 1.0))

    def __init__(self, table_file_name: str, shape: int, x: int, y: int, rad: int, rx: int, ry: int, cx: int, cy: int,
                 width: int, height: int, red: int, green: int, blue: int, opacity: float):
        ArtConfig.shapes_counter += 1
        self.table_file_name = table_file_name
        self.shape = shape
        self.cx = cx
        self.cy = cy
        self.rx = rx
        self.ry = ry
        self.x = x
        self.y = y
        self.rad = rad
        self.height = height
        self.width = width
        self.blue = blue
        self.red = red
        self.green = green
        self.opacity = opacity
        self.fd: IO[str] = self.open_txt_file()

    @classmethod
    def how_many_shapes(cls):
        return cls.shapes_counter

    def gen_table_header(self):
        header_elems = f"{'CNT' : >4}{'SHA' : >4}{'X' : >4}{'Y' : >4}{'RAD' : >4}{'RX' : >4}{'RY' : >4}" \
                       f"{'CX' : >4}{'CY' : >4}{'W' : >4}{'H' : >4}{'R' : >4}{'G' : >4}{'B' : >4}{'OP' : >4}"
        self.fd.write(header_elems)
        self.fd.write('\n')

    def gen_table_elems(self):
        table_elems = f"{ArtConfig.shapes_counter : >4}{self.shape : >4}{self.x : >4}{self.y : >4}{self.rad : >4}" \
                      f"{self.rx : >4}{self.ry : >4}{self.cx : >4}{self.cy : >4}{self.width : >4}{self.height : >4}" \
                      f"{self.red : >4}{self.green : >4}{self.blue : >4}{self.opacity : >4}"
        self.fd.write(table_elems)
        self.fd.write('\n')

    def open_txt_file(self) -> TextIO:
        return open(self.table_file_name, "a")

    def close_txt_file(self) -> None:
        self.fd.close()


class RandomUtil:
    def __init__(self, var_range: tuple):
        self.__below = var_range[0]
        self.__above = var_range[1]

    def gen_int_in_range(self):
        return random.randint(self.__below, self.__above)

    def gen_float_in_range(self):
        return round(random.uniform(self.__below, self.__above), 1)
