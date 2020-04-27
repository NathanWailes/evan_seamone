import csv
import pkgutil
import re

import scrapy
from scrapy.selector import SelectorList


def get_citation_numbers():
    citation_numbers = []

    csv_file_data = pkgutil.get_data("download_cases", "citation_numbers.csv")

    reader = csv.DictReader(csv_file_data.decode('utf-8-sig').splitlines(),
                            delimiter=',')
    for index, row in enumerate(reader):
        citation_numbers.append(row['citation_number'])

    assert isinstance(citation_numbers, list)
    return citation_numbers


class DownloadCasesSpider(scrapy.Spider):
    name = "download_cases"

    # I'm appending "&SPC=false" to the end of the URL to avoid the
    # autosuggestions.
    base_url = 'https://www.index.va.gov/search/va/bva_search.jsp?QT=&EW=%s' \
               '&AT=&ET=&RPP=10&DB=2019&DB=2018&DB=2017&DB=2016&DB=2015' \
               '&DB=2014&DB=2013&DB=2012&DB=2011&DB=2010&DB=2009&DB=2008' \
               '&DB=2007&DB=2006&DB=2005&DB=2004&DB=2003&DB=2002&DB=2001' \
               '&DB=2000&DB=1999&DB=1998&DB=1997&DB=1996&DB=1995&DB=1994' \
               '&DB=1993&DB=1992&SPC=false'

    citation_numbers = get_citation_numbers()

    def start_requests(self):
        assert isinstance(self.citation_numbers, list)
        for citation_number in self.citation_numbers:
            assert isinstance(citation_number, str)
            url = self.base_url % citation_number
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        result = response.xpath('//*[@id="results-area"]/div[1]/a/@href')
        if isinstance(result, SelectorList):
            result = result[0]
        case_url = result.extract()

        citation_number = re.findall('EW=(\d+)', response.url)[0]
        yield {
            'file_urls': [case_url],
            'citation_number': citation_number
        }
