import argparse
import os
import re
from collections import defaultdict


def extract_the_orders_into_new_files_in_a_new_directory(base_path,
                                                         every_nth_case,
                                                         debug=False):
    path_to_input_cases = os.path.join(base_path,
                                       '03 case files separated based on '
                                       'whether they have an ORDER section',
                                       'has an ORDER section')
    base_path_for_output = os.path.join(base_path,
                                        '04 isolated orders sections')
    if not os.path.exists(base_path_for_output):
        os.makedirs(base_path_for_output)

    cases_we_didnt_find_the_order_section_for = []
    matches_against_the_regex = defaultdict(list)
    cases_without_the_string_ORDER_in_it = []
    cases_with_multiple_matches = []

    number_of_cases_considered = 0

    for index, filename in enumerate(os.listdir(path_to_input_cases)):
        path_to_file = os.path.join(path_to_input_cases, filename)
        if index % every_nth_case == 0:
            number_of_cases_considered += 1
            pass
        else:
            continue
        with open(path_to_file, 'r', encoding='utf-8') as infile:
            case_text = infile.read()
            regex_matches = get_order_section(case_text)

            if len(regex_matches) >= 1:
                output_orders_section_to_a_new_file(base_path_for_output,
                                                    filename, regex_matches)

                if len(regex_matches) > 1:
                    cases_with_multiple_matches.append(filename)
            else:
                cases_we_didnt_find_the_order_section_for.append(filename)

            if debug:
                if 'ORDER' not in case_text:
                    cases_without_the_string_ORDER_in_it.append(filename)
                for match in regex_matches:
                    matches_against_the_regex[filename].append(match)

    output_the_list_of_cases_that_we_didnt_find_an_order_section_for(base_path,
                                                                     cases_we_didnt_find_the_order_section_for)

    if debug:
        print_results(cases_we_didnt_find_the_order_section_for,
                      matches_against_the_regex,
                      cases_without_the_string_ORDER_in_it,
                      cases_with_multiple_matches, number_of_cases_considered)


def get_order_section(case_text):
    regex_to_find_order_section = r"\n" \
                                  r"\s*ORDERS?\s*\n" \
                                  r"\s*(.+?)\s*\n" \
                                  r"\s*(?:" \
                                      r"(?:" \
                                          r"(?:[^\n]+\n)?" \
                                          r"[^\n]+\n[^\n]+" \
                                          r"Board\sof\sVeterans['’]\sAppeals" \
                                      r")" \
                                      r"|(?:______)" \
                                      r"|(?:[A-Z\ \.\:]{3,}?\s*\n)" \
                                  r")"
    regex_matches = re.findall(regex_to_find_order_section, case_text,
                               re.DOTALL)
    return regex_matches


def output_orders_section_to_a_new_file(base_path_for_output, filename,
                                        regex_matches):
    path_to_output_file = os.path.join(base_path_for_output, filename)
    case_text_to_output = "\n\n".join(regex_matches)
    with open(path_to_output_file, 'w') as outfile:
        outfile.write(case_text_to_output)


def output_the_list_of_cases_that_we_didnt_find_an_order_section_for(base_path,
                                                                     cases_we_didnt_find_the_order_section_for):
    path_to_output_file = os.path.join(base_path,
                                       '04 cases we didnt find the order '
                                       'section for.txt')
    with open(path_to_output_file, 'w') as outfile:
        for filename in cases_we_didnt_find_the_order_section_for:
            outfile.write(filename + '\n')


def print_results(cases_we_didnt_find_the_order_section_for,
                  matches_against_the_regex,
                  cases_without_the_string_ORDER_in_it,
                  cases_with_multiple_matches, number_of_cases_considered):
    print("\n\n***\n")
    print("Number of cases considered: %d" % number_of_cases_considered)
    print("\n***\n\n")

    print("\n\n***\n")
    print("Cases we didn't find the order section for:")
    print("\n***\n\n")
    for case_filename in cases_we_didnt_find_the_order_section_for:
        print(case_filename)

    print("\n\n***\n")
    print("Cases with multiple matches:")
    print("\n***\n\n")
    for case_filename in cases_with_multiple_matches:
        print(case_filename)

    print("\n\n***\n")
    print("Matches against the regex:")
    print("\n***\n\n")

    for case_filename in sorted(matches_against_the_regex.keys()):
        for match in matches_against_the_regex[case_filename]:
            print(case_filename)
            print('\n\n')
            print(match)
            print("\n\n<<<<<<<<<<<<<>>>>>>>>>>>>>>\n\n")

    print("\n\n***\n")
    print("Cases without the string 'ORDER' in them:")
    print("\n***\n\n")

    for filename in cases_without_the_string_ORDER_in_it:
        print(filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Extract the orders sections from cases into new files in a'
                    ' separate directory.')
    parser.add_argument('--base_path', type=str,
                        help='the path to the parent folder of the folder '
                             'containing the input case files')
    parser.add_argument('--every_nth_case', type=int,
                        help='If not specified, the program will only consider '
                             'every 1000th case, which is useful for testing.')
    parser.add_argument('--debug', type=int,
                        help='This will print information about what was done '
                             '/ found.  1 for True, default is False')

    args = parser.parse_args()
    base_path = args.base_path if args.base_path else 'C:\\Users\\<Username>\\Desktop'
    every_nth_case = args.every_nth_case if args.every_nth_case else 1000
    debug = args.debug if args.debug else False
    extract_the_orders_into_new_files_in_a_new_directory(base_path,
                                                         every_nth_case, debug)
