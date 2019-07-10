import argparse
import os
import re
from shutil import copyfile


def separate_cases_based_on_whether_they_only_have_a_remand_section(base_path, every_nth_case):
    path_to_input_cases = os.path.join(base_path, '02 case files converted to utf-8')
    base_path_for_output = os.path.join(base_path, '03 case files separated based on whether they have an ORDER section')
    path_to_where_cases_with_an_order_section_should_go = os.path.join(base_path_for_output, 'has an ORDER section')
    path_to_where_cases_without_an_order_section_should_go = os.path.join(base_path_for_output, 'does not have an ORDER section')

    for path in [path_to_where_cases_with_an_order_section_should_go, path_to_where_cases_without_an_order_section_should_go]:
        if not os.path.exists(path):
            os.makedirs(path)

    for index, filename in enumerate(os.listdir(path_to_input_cases)):
        path_to_file = os.path.join(path_to_input_cases, filename)
        if index % every_nth_case == 0:
            pass
        else:
            continue

        with open(path_to_file, 'r', encoding='utf-8') as infile:
            case_text = infile.read()

            if re.findall('(\n\s*ORDERS?\s*\n)', case_text):
                path_to_output_file = os.path.join(path_to_where_cases_with_an_order_section_should_go, filename)
                copyfile(path_to_file, path_to_output_file)
            else:
                path_to_output_file = os.path.join(path_to_where_cases_without_an_order_section_should_go, filename)
                copyfile(path_to_file, path_to_output_file)

    path_to_done_file = os.path.join(base_path_for_output, 'done.txt')
    with open(path_to_done_file, 'w') as outfile:
        outfile.write("Done")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Separate the case files based on whether they only have a remand '
                                                 'section or not.')
    parser.add_argument('--base_path', type=str,
                        help='the path to the parent folder of the folder containing the input images')
    parser.add_argument('--every_nth_case', type=int,
                        help='If not specified, the program will only consider every 1000th case, which is useful'
                             ' for testing.')

    args = parser.parse_args()
    base_path = args.base_path if args.base_path else 'C:\\Users\\Nathan\\Desktop'
    every_nth_case = args.every_nth_case if args.every_nth_case else 1000
    separate_cases_based_on_whether_they_only_have_a_remand_section(base_path, every_nth_case)
