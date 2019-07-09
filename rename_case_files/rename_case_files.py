import os
import re

base_directory = "C:\\Users\\Nathan\\Dropbox\\business\\2019\\Evan Seamone\\nathan-wailes-upwork-evan-seamone\\full"
file_names = os.listdir(base_directory)

for file_name in file_names:
    full_path_to_file = os.path.join(base_directory, file_name)
    try:

        try:
            with open(full_path_to_file, 'r', encoding='utf16') as infile:
                file_contents_as_a_string = infile.read()
        except:
            with open(full_path_to_file, 'r', encoding='ISO-8859-1') as infile:
                file_contents_as_a_string = infile.read()

        # (?<=Citation Nr: )(\d+)
        # Citation Nr: (\d+)
        citation_number_matches = re.match('Citation Nr: (\d+)', file_contents_as_a_string)
        citation_number = citation_number_matches[1]
        print(citation_number)

        new_file_name = citation_number + '.txt'
        new_full_path = os.path.join(base_directory, new_file_name)
        os.rename(full_path_to_file, new_full_path)
    except:
        print("Error with file: %s" % full_path_to_file)
