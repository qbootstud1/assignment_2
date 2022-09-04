from src.html_gen import HtmlDoc


class Circle:
    def __init__(self, hd: HtmlDoc, cx: int, cy: int, rad: int, red: int, green: int, blue: int, op: float = 0.0,
                 t: int = 3) -> None:
        self.__cx: int = cx
        self.__cy: int = cy
        self.__rad: int = rad
        self.__red: int = red
        self.__green: int = green
        self.__blue: int = blue
        self.__op: float = op
        self.__t: int = t
        self.__hd: HtmlDoc = hd

    def draw_circle_line(self) -> None:
        ts: str = HtmlDoc.TAB * self.__t
        line1: str = f'<circle cx="{self.__cx}" cy="{self.__cy}" r="{self.__rad}" '
        line2: str = f'fill="rgb({self.__red}, {self.__green}, {self.__blue})" fill-opacity="{self.__op}"></circle>'
        self.__hd.fd.write(f"{ts}{line1 + line2}\n")


class Rectangle:
    def __init__(self, hd: HtmlDoc, x: int, y: int, height: int, width: int, red: int, green: int,
                 blue: int, op: float = 0.0, rx: int = 0, ry: int = 0, t: int = 3) -> None:
        self.__rx: int = rx
        self.__ry: int = ry
        self.__h: int = height
        self.__w: int = width
        self.__x = x
        self.__y = y
        self.__red: int = red
        self.__green: int = green
        self.__blue: int = blue
        self.__op: float = op
        self.__t: int = t
        self.__hd: HtmlDoc = hd

    def draw_rectangle_line(self) -> None:
        ts: str = HtmlDoc.TAB * self.__t
        line1: str = f'<rect x="{self.__x}" y="{self.__y}" width="{self.__w}" height="{self.__h}" '
        line2: str = f'rx="{self.__rx}" ry="{self.__ry}" '
        line3: str = f'fill="rgb({self.__red}, {self.__green}, {self.__blue})" fill-opacity="{self.__op}"></rect>'
        self.__hd.fd.write(f"{ts}{line1 + line2 + line3}\n")


class Ellipse:
    def __init__(self, hd: HtmlDoc, cx: int, cy: int, rx: int, ry: int, red: int, green: int, blue: int,
                 op: float = 0.0, t: int = 3) -> None:
        self.__rx: int = rx
        self.__ry: int = ry
        self.__cx: int = cx
        self.__cy: int = cy
        self.__red: int = red
        self.__green: int = green
        self.__blue: int = blue
        self.__op: float = op
        self.__t: int = t
        self.__hd: HtmlDoc = hd

    def draw_ellipse_line(self) -> None:
        ts: str = HtmlDoc.TAB * self.__t
        line1: str = f'<ellipse cx="{self.__cx}" cy="{self.__cy}" rx="{self.__rx}" ry="{self.__ry}" '
        line2: str = f'fill="rgb({self.__red}, {self.__green}, {self.__blue})" fill-opacity="{self.__op}"></ellipse>'
        self.__hd.fd.write(f"{ts}{line1 + line2}\n")
