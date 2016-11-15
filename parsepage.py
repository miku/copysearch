#!/usr/bin/env python
# coding: utf-8

"""
Scratchpad for getting data out of a single wiki page.

Pages have:

* Abstract (p)
* Main Results of the Study (p)
* Policy Implications as Stated By Author (p)
* Coverage of Study (tables)
* Dataset (tables)

Additional infoboxes:

* Paper (top)
* About the data (bottom)

"""

from bs4 import BeautifulSoup
import json

def abstract(soup):
    """
    Return abstract.
    """
    ps = soup.find('span', {'class': 'mw-headline', 'id': 'Abstract'}).parent.find_next_siblings('p')
    return ' '.join([s.get_text() for s in ps]).strip()

def main_results_of_study(soup):
    """
    Main results of study.
    """
    ps = soup.find('span', {'class': 'mw-headline', 'id': 'Main_Results_of_the_Study'}).parent.find_next_siblings('p')
    return ' '.join([s.get_text() for s in ps]).strip()

def policy_implications_as_stated_by_author(soup):
    """
    Policy Implications as Stated By Author.
    """
    ps = soup.find('span', {'class': 'mw-headline', 'id': 'Policy_Implications_as_Stated_By_Author'}).parent.find_next_siblings('p')
    return ' '.join([s.get_text() for s in ps]).strip()


if __name__ == '__main__':
    path = 'mirror/www.copyrightevidence.org/evidence-wiki/index.php/Acilar_(2010).html'

    with open(path) as handle:
        html = handle.read()

    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify().encode('utf-8'))

    # <h3>
    #  <span class="mw-headline" id="Abstract">
    #   Abstract
    #  </span>
    # </h3>
    # <p>
    #  The widespread use of computers and ....
    # </p>
    # <p>
    #  The main purpose of the present ...
    # </p>

    print(json.dumps({
        'abstract': abstract(soup),
        'results': main_results_of_study(soup),
        'implications': policy_implications_as_stated_by_author(soup),
    }))

    # h3s = soup.find_all('h3')
    # for h3 in h3s:
    #     print(h3)
    #     print(h3.find_next_siblings('p'))
