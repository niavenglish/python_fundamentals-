import math

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return base * height / 2

def get_number(message):
    while True:
        try:
            number = float(input(message))

            if not math.isfinite(number) or number <= 0:
                print("Please enter a positive, finite number.")
            else:
                return number

        except ValueError:
            print("Invalid input! Please enter a number.")


stop = False
while not stop:
    u_shape = input('Pick a shape: C=circle, R=rectangle, T=triangle: ').strip().upper()
    if u_shape == 'C':
        u_radius = get_number('Enter the radius: ')
        print('The area of the circle is: ' + str(circle_area(u_radius)))

    elif u_shape == 'R':
        u_length = get_number('Enter the length: ')
        u_width = get_number('Enter the width: ')
        r_area = rectangle_area(u_length, u_width)
        print(f'The area of the rectangle is: {r_area}')

    elif u_shape == 'T':
        u_base = get_number('Enter the base: ')
        u_height = get_number('Enter the height: ')
        print('The area of the triangle is: ' + str(triangle_area(u_base, u_height)))

    else:
        print('Invalid input! Try again')

    if u_shape in ('C', 'R', 'T'):
        shape_names = {'C': 'circle', 'R': 'rectangle', 'T': 'triangle'}
        selected_shape = shape_names[u_shape]

        print(f'You selected: {selected_shape.upper()}')
        print(f'The letter "a" appears {selected_shape.count("a")} time(s).')


    yes_no = input('Do you want to quit? y/n: ')
    if yes_no == 'y':
        stop = True

    print('Thank you for using the Area Calculator!')
