from math import sin

import dearpygui.dearpygui as dpg

# # from dearpygui import
# from dearpygui._dearpygui
# from dearpygui.demo import show_demo, add_additional_font

dpg.create_context()

sindatax = []
sindatay = []
for i in range(0, 500):
    sindatax.append(i / 1000)
    sindatay.append(0.5 + 0.5 * sin(50 * i / 1000))

# add a font registry
with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    # font = dpg.add_font(file="fonts/Montserrat-ExtraLight.ttf", size=14,
    #              # glyph_ranges='cyrillic'
    #              )
    with dpg.font("fonts/Montserrat-ExtraLight.ttf", 16) as font1:
        # add the default font range
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)

        # helper to add range of characters
        # Options:
        # mvFontRangeHint_Japanese
        # mvFontRangeHint_Korean
        # mvFontRangeHint_Chinese_Full
        # mvFontRangeHint_Chinese_Simplified_Common
        # mvFontRangeHint_Cyrillic
        # mvFontRangeHint_Thai
        # mvFontRangeHint_Vietnamese
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

with dpg.window(label="Tutorial", width=(width_ := 900)):
    # configuration set when button is created
    with dpg.group(width=(gr_width_ := 400)):
        dpg.add_text(label="title_text", track_offset=0.5,
                     default_value="Виды сортировок".center(gr_width_ // 4, " "), )
        dpg.add_button(label="Аплай", width=300)

        # user data and callback set any time after button has been created
        btn = dpg.add_button(label="Apply 2")
        dpg.set_item_label(btn, "Button 57")
        dpg.set_item_width(btn, 200)

    with dpg.group(width=(gr2_width_ := width_ - gr_width_ - 10), pos=(gr_width_, 0)):
        with dpg.plot(label="Line Series", height=(gr2_height_:=400), width=gr2_width_):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

            # series belong to a y axis
            dpg.add_line_series(sindatax, sindatay, label="0.5 + 0.5 * sin(x)", parent="y_axis")

    with dpg.group(width=(gr3_width_ := width_ - 10), pos=(10, gr2_height_ + 30)):
        with dpg.table(header_row=False):

            # use add_table_column to add columns to the table,
            # table columns use child slot 0
            dpg.add_table_column()
            dpg.add_table_column()
            dpg.add_table_column()

            # add_table_next_column will jump to the next row
            # once it reaches the end of the columns
            # table next column use slot 1
            for i in range(0, 4):
                with dpg.table_row():
                    for j in range(0, 3):
                        dpg.add_text(f"Row{i} Column{j}")


    dpg.bind_font(font1)

dpg.create_viewport(title='Custom Title', width=width_ + 15, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
