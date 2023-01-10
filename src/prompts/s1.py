"""
write a python program that generates a random list of 50000 fake, but reasonable-looking academic papers.
 - There are 50 possible journals.
 - Use faker to  create names for 10000 possible authors.
 - Each paper shall have a year, journal, pages, title, authors and optionally may have references to other papers in this list.
 - References are to be in academic format.
 - Any references must be to papers in this list.
 - A paper must not reference itself.
"""

import faker
from random import shuffle, randint

faker_gen = faker.Faker()

papers = []

# Create 50 possible journals
journals = ["Journal of Applied Mathematics", "Journal of Biomedical Science", "Computer Science Journal",
"Journal of Analytical Chemistry", "International Journal of Microbiology", "Journal of Chemical Physics",
"Journal of Geoscience", "Journal of Meteorology", "Journal of Astronomy", "Journal of Neuroscience",
"Journal of Geology", "Journal of Statistics", "Journal of Molecular Biology", "Journal of Economics",
"Journal of Genetics", "Journal of History", "Journal of Ecology", "Journal of Geography",
"Journal of Physics", "Journal of Psychology", "Journal of Sociology", "Journal of Education",
"Journal of Engineering", "Journal of Law", "Journal of Medicine", "Journal of Technology",
"Journal of Computer Science", "Journal of Chemistry", "Journal of Biochemistry",
"Journal of Organic Chemistry", "Journal of Nuclear Chemistry", "Journal of Physics A",
"Journal of Physics B", "Journal of Physics C", "Journal of Mathematics",
"Journal of Probability Theory", "Journal of Mathematical Analysis", "Journal of Algebra",
"Journal of Differential Equations", "Journal of Topology", "Journal of Geometric Analysis",
"Journal of Number Theory", "Journal of Combinatorics", "Journal of Group Theory",
"Journal of Representation Theory", "Journal of Graph Theory", "Journal of Logic",
"Journal of Set Theory", "Journal of Philosophy", "Journal of Political Science",
"Journal of Anthropology", "Journal of Art History", "Journal of Linguistics",
"Journal of Literary Studies", "Journal of Musicology", "Journal of Cultural Studies",
"Journal of Film Studies", "Journal of Theatre Studies", "Journal of Gender Studies",
"Journal of Media Studies", "Journal of Religion Studies", "Journal of Popular Culture"]

# Create 10000 possible authors
authors = []
for i in range(10000):
    authors.append(faker_gen.name())

# Generate 50000 papers
for i in range(50000):
    # Generate a random year between 1950 and 2020
    year = randint(1950, 2020)
    # Select a random journal
    journal = journals[randint(0, len(journals)-1)]
    # Generate a random number of pages
    pages = randint(1, 400)
    # Generate a random title
    title = faker_gen.sentence(nb_words=5, variable_nb_words=True)
    # Generate a random number of authors (up to 5)
    n_authors = randint(1, 5)
    authors_list = []
    for j in range(n_authors):
        authors_list.append(authors[randint(0, len(authors)-1)])
    # Generate a random number of references (up to 5)
    refs = []
    while len(refs) < 5 and len(papers) > 0:
        r = randint(0, len(papers)-1)
        if papers[r]["title"] != title:
            refs.append(papers[r]["title"])
    # Create the paper
    paper = {"year": year,
             "journal": journal,
             "pages": pages,
             "title": title,
             "authors": authors_list,
             "refs": refs}
    # Add the paper to the list
    papers.append(paper)

# Print the papers
for paper in papers:
    print("Title: {}\nYear: {}\nJournal: {}\nPages: {}\nAuthors: {}\nReferences: {}".format(paper["title"], paper["year"], paper["journal"], paper["pages"], ", ".join(paper["authors"]), ", ".join(paper["refs"])))
