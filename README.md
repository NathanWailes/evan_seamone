## Summary of the steps I took:
1. Downloaded the case files
   - Code is in `/download_cases/`
1. Renamed the case files to be their citation numbers.
   - Code is in `/rename_case_files/`
1. Used UTFCast to convert all of them to UTF-8 format.
   - Two had some unknown encoding that couldn't be converted to UTF-8 and 
     couldn't be read by Notepad, so those cases 
     were discarded / ignored going forward.
   - There was no code written for this step.
1. Separated the cases that only had a "Remand" section from the cases that had
   an "Order" section so that it'd be quicker
   to run regexes against the former.
   - Code is in
     `/separate_cases_based_on_whether_they_only_have_a_remand_section.py`
