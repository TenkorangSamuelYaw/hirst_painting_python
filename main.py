#  import colorgram
import turtle as turtle_module
import random
turtle_module.colormode(255)  # I want to use rgb colors.
timmy = turtle_module.Turtle()
turtle_module.title("HIRST PAINTING")
timmy.speed("fastest")
timmy.penup()  # Move without a trace.
timmy.hideturtle()

#  Use the commented code to generate the colors from hirst_spot.jpeg
# color_list = []
# colors = colorgram.extract("hirst_spot.jpeg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple = (r, g, b)
#     color_list.append(color_tuple)
# print(color_list)
color_list = [(204, 156, 106), (60, 106, 126), (123,
                                                80,
                                                95),
              (166, 83, 42), (126, 158, 171), (192, 139, 41), (128, 174, 160), (221, 197, 140), (16, 43, 53),
              (186, 136, 148), (47, 31, 17), (188, 90, 110), (59, 124, 113), (56, 161, 128), (147, 24, 32),
              (208, 94, 79), (49, 31, 35), (234, 168, 163), (86, 142, 161), (146, 29, 22), (9, 23, 22), (24, 79, 91),
              (224, 174, 179), (106, 127, 152), (165, 207, 195), (9, 107, 102)]


def hirst_spot_painting():
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    total_dots = 100
    for dot_count in range(1, total_dots + 1):  # You can't start at zero, because 0 % 10 is 0
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
        if dot_count % 10 == 0:
            timmy.setheading(90)
            timmy.forward(50)
            timmy.setheading(180)
            timmy.forward(500)
            timmy.setheading(0)


hirst_spot_painting()
# timmy.setheading(225)
# timmy.forward(300)
# timmy.setheading(0)
# total_dots = 100
# for dot_count in range(1, total_dots + 1):
#     timmy.dot(20, random.choice(color_list))
#     timmy.forward(50)
#     if dot_count % 10 == 0:
#         timmy.setheading(90)
#         timmy.forward(50)
#         timmy.setheading(180)
#         timmy.forward(500)
#         timmy.setheading(0)
turtle_module.Screen().exitonclick()
