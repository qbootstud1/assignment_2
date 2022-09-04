from src.html_gen import HtmlDoc


class SvgCanvas:
    TAB: str = "   "  # HTML indentation tab (default: three spaces)

    def __init__(self, hd: HtmlDoc, width: int, height: int, t: int = 2) -> None:
        self.__w: int = width
        self.__h: int = height
        self.__t: int = t
        self.__hd: HtmlDoc = hd

    def gen_empty_html_svg(self):
        self.__hd.write_html_head()
        self.write_svg_head()
        self.write_svg_tail()
        self.__hd.write_html_tail()

    def gen_svg_box(self):
        self.write_svg_head()
        self.write_svg_tail()

    def write_svg_line(self, line: str) -> None:
        """draw_circle_line method"""
        ts: str = HtmlDoc.TAB * self.__t
        self.__hd.fd.write(f"{ts}{line}\n")

    def write_svg_head(self) -> None:
        self.write_svg_line(f"<svg width={self.__w} height={self.__h}>")

    def write_svg_tail(self) -> None:
        self.write_svg_line(f"</svg>")
