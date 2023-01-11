"""
write a python program that generates a random list of 50000 fake, but reasonable-looking academic papers.
 - Each paper shall have a year, journal, pages, title, authors and optionally may have references to other papers in this list.
 - There are 50 possible journals with realistic-looking names.
 - Use faker to  create names for 10000 possible authors.
 - A paper may have up to 4 authors.
 - Do not use faker for titles.
 - Provide a minimum of 30 title sentence structures.
 - References are to be in academic format.
 - Any references must be to papers in this list.
 - A paper must not reference itself.
 - Analyze for index out of range errors.
 - print the first 10 records in YAML format
"""


import random
import yaml
from faker import Faker

# Generate 50 Journals
journals= [
    'Journal of Computer Science',
    'Journal of Applied Mathematics',
    'Journal of Data Science',
    'Journal of Machine Learning',
    'Journal of Statistics',
    'Journal of Artificial Intelligence',
    'Journal of Software Engineering',
    'Journal of Information Technology',
    'Journal of Robotics',
    'Journal of Computational Science',
    'Journal of Analytical Science',
    'Journal of Numerical Analysis',
    'Journal of Algorithm Theory',
    'Journal of Network Security',
    'Journal of Computer Graphics',
    'Journal of Database Management',
    'Journal of Image Processing',
    'Journal of Computer Architecture',
    'Journal of Computer Networks',
    'Journal of Web Technologies',
    'Journal of Operating Systems',
    'Journal of Security and Privacy',
    'Journal of Cloud Computing',
    'Journal of Computer Vision',
    'Journal of Natural Language Processing',
    'Journal of Data Mining',
    'Journal of Distributed Systems',
    'Journal of System Administration',
    'Journal of Embedded Systems',
    'Journal of Automated Reasoning',
    'Journal of Cryptography',
    'Journal of Mobile Computing',
    'Journal of Grid Computing',
    'Journal of Autonomous Systems',
    'Journal of Bioinformatics',
    'Journal of Simulation Modeling',
    'Journal of Parallel Computing',
    'Journal of Pattern Recognition',
    'Journal of Network Analysis',
    'Journal of Intelligent Systems',
    'Journal of Data Warehousing',
    'Journal of Internet of Things',
    'Journal of Computational Biology',
    'Journal of Virtual Reality',
    'Journal of Scientific Computing',
    'Journal of Knowledge Representation',
    'Journal of Expert Systems',
    'Journal of Electronic Commerce',
    'Journal of Quantitative Analysis',
    'Journal of Knowledge Management',
    'Journal of Human Computer Interaction',
    'Journal of System Dynamics',
    'Journal of Computational Intelligence'
]

# Generate 10000 authors
fake = Faker()
authors = []

for _ in range(10000):
    authors.append(fake.name())

# Generate 30 title structures
title_structures = [
    "Analysis of {noun} for {noun}",
    "A {adjective} {noun} System for {noun}",
    "Design of {noun} for {noun}",
    "A {adjective} Model of {noun}",
    "A {adjective} Framework for {noun}",
    "Exploring {noun} in {noun}",
    "The {adjective} Impact of {noun}",
    "The {adjective} Role of {noun}",
    "The {adjective} Use of {noun}",
    "A Survey of {noun} in {noun}",
    "The {adjective} Nature of {noun}",
    "The {adjective} Characteristics of {noun}",
    "The {adjective} Dynamics of {noun}",
    "The {adjective} Structure of {noun}",
    "The {adjective} Implications of {noun}",
    "The {adjective} Significance of {noun}",
    "The {adjective} Potential of {noun}",
    "The {adjective} Impact of {noun} on {noun}",
    "The {adjective} Relationship between {noun} and {noun}",
    "The {adjective} Design of {noun} for {noun}",
    "The {adjective} Use of {noun} for {noun}",
    "The {adjective} Analysis of {noun} for {noun}",
    "The {adjective} Application of {noun} for {noun}",
    "The {adjective} Integration of {noun} in {noun}",
    "The {adjective} Development of {noun} for {noun}",
    "The {adjective} Evaluation of {noun} for {noun}",
    "The {adjective} Implications of {noun} for {noun}",
    "The {adjective} Role of {noun} in {noun}",
    "The {adjective} Potential of {noun} for {noun}",
    "The {adjective} Challenges of {noun} for {noun}"
]

# Generate 50000 papers
papers = []
for _ in range(50000):
    year = random.randint(2000, 2020)
    journal = random.choice(journals)
    pages = random.randint(1, 100)
    authors_num = 1
    if len(authors) > 25:
        authors_num = random.randint(1, 4)
    paper_authors = [random.choice(authors) for _ in range(authors_num)]
    title_structure = random.choice(title_structures)
    title = title_structure.format(
        adjective=fake.word(ext_word_list=['adjective']),
        noun=fake.word(ext_word_list=['noun'])
    )
    references = []
    while True:
        if len(papers) == 0:
            break
        ref_paper = random.choice(papers)
        if ref_paper['title'] != title and ref_paper not in references:
            ref_string = f'{ref_paper["authors"][0]}, {ref_paper["title"]}, {ref_paper["journal"]}, {ref_paper["year"]}, {ref_paper["pages"]}'
            references.append(ref_string)
        if len(references) == 3:
            break

    paper = {
        'year': year,
        'journal': journal,
        'pages': pages,
        'title': title,
        'authors': paper_authors,
        'references': references
    }
    papers.append(paper)

# Print first 10 records in YAML format
for paper in papers[:10]:
    print(yaml.dump(paper))

