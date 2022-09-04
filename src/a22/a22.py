from src.art_config import ArtConfig, RandomUtil


# Instantiate all the (random) ArtConfig attributes for a possible svg canvas of width=500 and height=500
svg_width = 500
svg_height = 500
random_shape = RandomUtil(ArtConfig.shape_range)
random_x = RandomUtil((0, svg_width))
random_y = RandomUtil((0, svg_height))
random_rad = RandomUtil(ArtConfig.rad_range)
random_rx = RandomUtil(ArtConfig.rx_range)
random_ry = RandomUtil(ArtConfig.ry_range)
random_cx = RandomUtil((0, svg_width))
random_cy = RandomUtil((0, svg_width))
random_width = RandomUtil(ArtConfig.width_range)
random_height = RandomUtil(ArtConfig.height_range)
random_red = RandomUtil(ArtConfig.color_range)
random_green = RandomUtil(ArtConfig.color_range)
random_blue = RandomUtil(ArtConfig.color_range)
random_opacity = RandomUtil(ArtConfig.op_range)

# Generate a table of random values for all the ArtConfig attributes
number_shapes = 10

for shape in range(number_shapes):
    art = ArtConfig('a22.txt', random_shape.gen_int_in_range(), random_x.gen_int_in_range(),
                    random_y.gen_int_in_range(), random_rad.gen_int_in_range(), random_rx.gen_int_in_range(),
                    random_ry.gen_int_in_range(), random_cx.gen_int_in_range(), random_cy.gen_int_in_range(),
                    random_width.gen_int_in_range(), random_height.gen_int_in_range(), random_red.gen_int_in_range(),
                    random_green.gen_int_in_range(), random_blue.gen_int_in_range(),
                    random_opacity.gen_float_in_range())
    if art.shapes_counter == 0:
        art.gen_table_header()
        art.gen_table_elems()
    else:
        art.gen_table_elems()

art.close_txt_file()
