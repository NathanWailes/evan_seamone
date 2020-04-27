### How to use it

1. Start a terminal session using the Miniconda virtual environment.
   1. Go to Start (in Windows) and type "Anaconda" and select the "Anaconda 
   Prompt" program.
1. Run `conda activate C:\Users\Nathan\Miniconda3\envs\categorize_court_cases\venv`
to activate the virtual environment.
  1. Run `conda env list` to see a list of all environments.  You can specify 
  the environment by name or by path.
1. Run `cd C:\Users\Nathan\Documents\Upwork\2019\06\categorize_court_cases` to 
switch to the directory of the project.
   1. To create a new scrapy project, run `scrapy startproject project_name`
1. To run the crawler *locally*:
   1. `cd` into the project's directory and run `scrapy crawl name_of_crawler`.
        - The name of the crawler is defined in a file within `project_name/spiders/`
        directory.
1. To run the crawler *on ScrapingHub*:
    1. Deploy the spider to ScrapingHub: ([Source](
    https://www.youtube.com/watch?v=JYch0zRmcgU))
       1. `pip install shub`
       1. `shub login`
       1. `shub deploy`
    1. In the ScrapingHub Job dashboard, click "Run" and select the name of the
    spider you created.
1. To download the case files stored on Google Cloud Storage:
    1. Start a Google Cloud SDK Shell.
    1. Run `gsutil -m cp -R gs://nathan-wailes-upwork-evan-seamone/ .`



### Notes
- Example URL for a case: https://www.va.gov/vetapp19/files3/a19000160.txt
- You can't search for a case on the BVA website with the case's docket number
as it appears in the Excel workbook, 
because the format doesn't match.  The BVA website expects a format like
'95-38 222'.
- Example URL to search across all years for a particular citation number
("0918001" in this case):
https://www.index.va.gov/search/va/bva_search.jsp?QT=&EW=0918001&AT=&ET=&RPP=10&DB=2019&DB=2018&DB=2017&DB=2016&DB=2015&DB=2014&DB=2013&DB=2012&DB=2011&DB=2010&DB=2009&DB=2008&DB=2007&DB=2006&DB=2005&DB=2004&DB=2003&DB=2002&DB=2001&DB=2000&DB=1999&DB=1998&DB=1997&DB=1996&DB=1995&DB=1994&DB=1993&DB=1992

- [Using Crawlera with Scrapy](https://support.scrapinghub.com/support/solutions/articles/22000188399-using-crawlera-with-scrapy)
