import bs4
import requests
import os
import re
import unittest


def get_soup_from_file(filename):
    """
    Opens the passed file (assumes it is in the same folder as this script)
    and constructs a BeautifulSoup object. Returns the BeautifulSoup object.
    """

    full_path = os.path.join(os.path.dirname(__file__), filename)
    f = open(full_path, 'r')
    data = f.read()
    f.close()
    soup = bs4.BeautifulSoup(data, features='lxml')
    return soup


def get_soup_from_url(url):
    """
    Makes a request to the url and constructs a BeautifulSoup object from the
    response. Returns the BeautifulSoup object.
    """

    headers = {'user-agent': 'This is a user agent'}
    r = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(r.text, features='lxml')
    return soup


def get_headlines_from_search_results(filename):
    """
    Write a function that calls get_soup_from_file() on "article1.html". Parse
    through the BeautifulSoup object and return a list of headlines for each
    search result in the following format:

    ['Headline 1', 'Headline 2'...]
    """

    pass


def get_most_read(url):
    """
    Write a function that calls get_soup_from_url() on
    the passed url. Parse through the BeautifulSoup object
    and return a list of URLs for each article in the "Most Read" section in
    the following format:

    ['https://somelink.com', 'https://anotherlink.com'...]
    """

    pass


def get_most_read_data(url_list):
    """
    Write a function that takes in a list of URLs (i.e. the one returned by
    get_most_read()). For each URL in the list, call get_soup_from_url(),
    parse through the BeautifulSoup object, and capture the article title,
    author, and date. Make sure to .strip() any whitespace from the date.

    This function should return a list of tuples in the following format:
    (url, title, author, date)

    For example:
    [('https://one.com', 'A Great Title', 'Some Author', 'Thursday, October 17, 2019 - 6:14pm')]

    HINT: Using BeautifulSoup's select() method may help you here.
    You can easily capture CSS selectors with your browser's inspector window.
    """

    pass


def get_names_and_years(filename):
    """
    Write a function to get the names and attending years of the alumni
    mentioned in "article2.html". You will need to use regex to accomplish
    this. This function should call get_soup_from_file(). You should return a
    list of (Name, Year) tuples. If there are multiple years, add additional
    elements to the end of the tuple for each year.

    For example, if the article contains: "Matt Whitehead, attended in 2018
    and 2019", you should append ("Matt Whitehead", "2018", "2019") to your
    list of tuples.
    """

    pass


def write_csv(data, filename):
    """
    Write a function that takes in a list of tuples called data (i.e. the one
    that is returned by get_names_and_years()), writes the data to a csv file,
    and saves it to the passed filename.

    The first row of the csv should contain "Name" and
    "Year" respectively. For each tuple in data, write a new row to
    the csv, placing each element of the tuple in the correct column.
    If the tuple has multiple years, you should write them both into the year
    column separated like so: "2018 & 2012".

    When you are done your CSV file should look like this:

    Name,Year
    Some Student,2019 & 2018
    Another Student,2012
    Yetanother Student,2010


    This function should not return anything.
    """

    pass


def main():
    """
    This function is excecuted then the script runs.
    Starts the unit tests.
    """

    unittest.main(verbosity=2)


class TestCases(unittest.TestCase):
    """
    For each function you wrote above you should write a non-trivial test case
    with at least one additional assert statement to make sure that your
    function works properly.

    Remember that websites are dynamic and their content can change at any
    time, any function that calls get_soup_from_url() should not use
    assertEqual statements with hard coded values. You don't want to write a
    test case that passes today and fails tomorrow.
    """
    def setUp(self):
        """
        Use these instance variables in your test cases below rather than
        calling any of these 3 functions again. There is no reason to fetch
        data that we already have.
        """

        self.url_list = get_most_read('https://www.michigandaily.com')
        self.data_list = get_most_read_data(self.url_list)
        write_csv(get_names_and_years('article2.html'), 'results.csv')

    def test_get_headlines_from_search_results(self):
        self.assertEqual(
            get_headlines_from_search_results('article1.html')[0],
            'Technology executives address School of Information members'
        )
        pass

    def test_get_most_read(self):
        self.assertEqual(len(self.url_list), 5)
        pass

    def test_get_most_read_data(self):
        for i in self.data_list:
            self.assertTrue(i[0].startswith('https'))
        pass

    def get_names_and_years(self):
        self.assertEqual(get_names_and_years('article2')[-1], ('Jack Warner', '2010'))
        pass

    def test_write_csv(self):
        # use csv_data for your test case
        # you shouldn't need to read in the file again
        csv = open(os.path.join(os.path.dirname(__file__), 'results.csv'))
        csv_data = csv.readlines()
        csv.close()
        self.assertEqual(len(csv_data), 8)
        pass


if __name__ == '__main__':
    main()
