import math

def show_error_message(message):
    print('Invalid input. ' + message)

def get_input_parts(message):
    return input(message + ' ').split(' ')

def get_base_and_height():
    message = 'Enter base and height separated by a space:'
    parts = get_input_parts(message)
    while len(parts) != 2 or not all([parts[0].isdigit(), parts[1].isdigit()]):
        show_error_message('Please, enter the correct base and height separated by a space.') 
        parts = get_input_parts(message)
    return { 'base' : int(parts[0]), 'height' : int(parts[1]) }

def get_area_by_base_and_height():
    params = get_base_and_height()
    print_area(params['base'] * params['height'] / 2)

def get_two_sides_and_angle_between_them():
    message = 'Enter 2 sides and angle(degrees) between them separated by a space:'
    parts = get_input_parts(message)    
    while len(parts) != 3 or not all([parts[0].isdigit(), parts[1].isdigit(), parts[2].isdigit()]):
        show_error_message('Please, enter the correct 2 sides and angle(degrees) between them separated by a space.') 
        parts = get_input_parts(message)
    return { 'side_one' : int(parts[0]), 'side_two' : int(parts[1]), 'angle' : int(parts[2]) }

def get_area_by_two_sides_and_angle_betwenn_them():
    params = get_two_sides_and_angle_between_them()
    print_area((params['side_one'] * params['side_two'] / 2) * math.sin(math.radians(int(params['angle']))))

def print_area(area):
    print(f'Area is: {str(round(area))}')

def get_menu_item():
    message = 'Enter a menu item number: '
    menu_item = input(message)
    while menu_item not in ['1', '2', '3']:
        show_error_message('Please, enter a menu item number between 1 and 3.')        
        menu_item = input(message)
    
    if menu_item == "1":
        get_area_by_base_and_height()
    elif menu_item == "2":
        get_area_by_two_sides_and_angle_betwenn_them()        
    else:
        print('Goodbye!')
        return False
    
    return True

print('Welcome to the triangle area calculation tool.')
while True:
    print('\nMenu:\n1. Calculate triangle area by base and height\n2. Calculate triangle area by 2 sides and angle between them\n3. Exit')
    if get_menu_item() == False:
        break
