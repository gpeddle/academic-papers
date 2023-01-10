"""
write a python program that generates a random list of fake, but reasonable-looking academic papers.
 - Each paper shall have a year, journal, pages, title, authors and optionally may have references to other papers in this list.
 - References are to be in academic format.
 - Any references must be to papers in this list.
 - A paper must not reference itself.
"""

import random

# Define papers
papers = []

# Generate a list of random papers
for i in range(10):
    # Generate a random year
    year = random.randint(1990, 2018)

    # Generate a random journal
    journals = ['Nature', 'Science', 'PLOS', 'Journal of Applied Physics', 'IEEE Transactions on Image Processing']
    journal = random.choice(journals)

    # Generate a random page number
    pages = random.randint(1, 200)

    # Generate a random title
    title = 'A Study of the Impact of ' + random.choice(
        ['Climate Change', 'Artificial Intelligence', 'Quantum Computing', 'Advanced Robotics']) + ' on Modern Society'

    # Generate a random set of authors
    authors = [random.choice(
        ['John Smith', 'Jane Doe', 'Steven Johnson', 'Anna Baker', 'George Smith', 'Maria Lopez', 'Richard Anderson',
         'Stephanie Walker'])
               for i in range(random.randint(1, 5))]

    # Generate a random set of references
    references = []
    if len(papers) > 0:
        num_references = random.randint(0, len(papers))
        for i in range(num_references):
            reference = random.choice(papers)
            if reference['year'] != year:
                references.append("{}, {}, {}, {}".format(reference['authors'], reference['year'], reference['journal'],
                                                          reference['title']))

    # Create the paper
    paper = {
        'year': year,
        'journal': journal,
        'pages': pages,
        'title': title,
        'authors': ", ".join(authors),
        'references': ", ".join(references)
    }

    # Add the paper to the list
    papers.append(paper)

# Print out the papers
for paper in papers:
    print("{}: {}. {}. {}, {}-{}. {}".format(paper['year'], paper['authors'], paper['title'], paper['journal'],
                                             paper['pages'], paper['pages'] + 1, paper['references']))