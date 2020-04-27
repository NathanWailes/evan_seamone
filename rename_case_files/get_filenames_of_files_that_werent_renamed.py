import os

path_to_cases = 'C:\\Users\\<Username>>\\Desktop\\full'

cases_we_didnt_find_the_order_section_for = []

for index, filename in enumerate(os.listdir(path_to_cases)):
    if len(filename) > 12:
        print(filename)
