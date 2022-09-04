from src.html_gen import HtmlDoc
from src.svg_canvas import SvgCanvas
from src.svg_geometries import Circle, Rectangle, Ellipse
from src.utils import print_my_art


# Instantiate the html object, defining its file name and title
html = HtmlDoc('a21.html', 'My Art')

# Instantiate the corresponding svg canvas object, defining its shape
svg = SvgCanvas(width=300, height=500, hd=html)

# Define the shapes to be shown
left_eye_circle = Circle(hd=html, cx=50, cy=50, rad=50, red=255, green=0, blue=0, op=0.7)
left_eye_rectangle = Rectangle(hd=html, x=25, y=25, height=50, width=50, rx=20, ry=20, red=0, green=255, blue=0,
                               op=0.2)
mouth_ellipse = Ellipse(hd=html, cx=150, cy=150, rx=100, ry=25, red=0, green=0, blue=255, op=0.3)
right_eye_circle = Circle(hd=html, cx=250, cy=50, rad=50, red=255, green=0, blue=0, op=0.7)
right_eye_rectangle = Rectangle(hd=html, x=225, y=25, height=50, width=50, rx=20, ry=20, red=0, green=255, blue=0,
                                op=0.2)

# Print those shapes in html file
shapes_vector = [left_eye_circle, left_eye_rectangle, mouth_ellipse, right_eye_circle, right_eye_rectangle]
print_my_art(html, svg, shapes_vector)
