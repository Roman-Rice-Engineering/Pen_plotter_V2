old_filename = "/home/shubh/Pen_plotter_V2/my_flask/static/Image_Storage/Gcodes/pervious.gcode"
logo_filename = "/home/shubh/Pen_plotter_V2/my_flask/mvths engineering (2).gcode"
num_lines = 1  
top_string = """G92 X0 Y0;\n"""
bottom_string = """G1 X0 Y0;\n"""

with open(logo_filename, 'r+') as f:
    data = f.read()
    
with open(old_filename, "a") as f:
    f.write(data+old_filename)