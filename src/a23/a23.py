from src.html_gen import HtmlDoc
from src.svg_canvas import SvgCanvas
from src.svg_geometries import Circle, Rectangle, Ellipse
from src.art_config import ArtConfig, RandomUtil
from src.utils import print_my_art


# Instantiate all the (random) ArtConfig attributes with a pre-defined range for a possible svg canvas
random_shape = RandomUtil(ArtConfig.shape_range)
random_rad = RandomUtil(ArtConfig.rad_range)
random_rx = RandomUtil(ArtConfig.rx_range)
random_ry = RandomUtil(ArtConfig.ry_range)
random_width = RandomUtil(ArtConfig.width_range)
random_height = RandomUtil(ArtConfig.height_range)
random_red = RandomUtil(ArtConfig.color_range)
random_green = RandomUtil(ArtConfig.color_range)
random_blue = RandomUtil(ArtConfig.color_range)
random_opacity = RandomUtil(ArtConfig.op_range)

# Generate three different, random greeting cards

svg_dimensions_range = (100, 10000)  # Choose the min and max values for the shape of the svg files
number_shapes_range = (1, 1000)  # Choose the min and max values for the number of shapes in the svg files

for greeting_card in range(3):
    # Instantiate the html object, defining its file name and title
    html = HtmlDoc(f'a2-3{greeting_card+1}.html', f'My Greeting Card {greeting_card+1}')

    # Instantiate the corresponding svg canvas object, defining its shape
    svg_width = RandomUtil(svg_dimensions_range).gen_int_in_range()
    svg_height = RandomUtil(svg_dimensions_range).gen_int_in_range()
    svg = SvgCanvas(width=svg_width, height=svg_height, hd=html)

    # Instantiate the (random) ArtConfig attributes with a svg-file-dimensions-dependent range
    random_x = RandomUtil((0, svg_width))
    random_y = RandomUtil((0, svg_height))
    random_cx = RandomUtil((0, svg_width))
    random_cy = RandomUtil((0, svg_height))

    # Instantiate the random shapes to be shown
    number_shapes_a23 = RandomUtil(number_shapes_range).gen_int_in_range()
    shapes_vector = []

    for num_shape in range(number_shapes_a23):
        shape_type = random_shape.gen_int_in_range()

        red = random_red.gen_int_in_range()
        green = random_green.gen_int_in_range()
        blue = random_blue.gen_int_in_range()
        op = random_opacity.gen_float_in_range()

        if shape_type == 0:
            cx = random_cx.gen_int_in_range()
            cy = random_cy.gen_int_in_range()
            rad = random_rad.gen_int_in_range()
            shape = Circle(hd=html, cx=cx, cy=cy, rad=rad, red=red, green=green, blue=blue, op=op)

        elif shape_type == 1:
            x = random_x.gen_int_in_range()
            y = random_y.gen_int_in_range()
            height = random_height.gen_int_in_range()
            width = random_width.gen_int_in_range()
            rx = random_rx.gen_int_in_range()
            ry = random_ry.gen_int_in_range()
            shape = Rectangle(hd=html, x=x, y=y, height=height, width=width, rx=rx, ry=ry, red=red, green=green,
                              blue=blue, op=op)
        elif shape_type == 2:
            cx = random_cx.gen_int_in_range()
            cy = random_cy.gen_int_in_range()
            rx = random_rx.gen_int_in_range()
            ry = random_ry.gen_int_in_range()
            shape = Ellipse(hd=html, cx=cx, cy=cy, rx=rx, ry=ry, red=red, green=green, blue=blue, op=op)

        shapes_vector.append(shape)

    # Print those shapes in html file
    print_my_art(html, svg, shapes_vector)
