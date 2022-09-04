from src.svg_geometries import Circle, Rectangle, Ellipse
from typing import List, Union


def print_my_art(html_file, svg_file, vec_shapes: List[Union[Circle, Rectangle, Ellipse]]) -> None:
    html_file.write_html_head()
    svg_file.write_svg_head()
    for elem in vec_shapes:
        if isinstance(elem, Circle):
            elem.draw_circle_line()
        if isinstance(elem, Rectangle):
            elem.draw_rectangle_line()
        if isinstance(elem, Ellipse):
            elem.draw_ellipse_line()
    svg_file.write_svg_tail()
    html_file.write_html_tail()
    html_file.close_html_file()
