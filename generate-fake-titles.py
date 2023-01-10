#!/usr/bin/python3

# Generate 'fake' academic paper titles
"""
Prompt:

Write python code to generate a list of complex titles for simulated academic papers.
Each title should include a proposed experiment and a set of experimental subjects.
Include 250 kinds of experiments and 250 kinds of subjects.
The output should have 50000 titles, one per line.
Title shall be proper-cased.
The experiments do not need to make real-world sense, but be creative.

Using the two title patterns below, and create 10 additional title patterns of your own.
Hint: 'A Study of THING' can also be expressed as 'Studying THING'
Use 'A' or 'An' appropriately depending on whether BLANK1 starts with a vowel.

Example 1: Abstract Pattern: A BLANK1 of QUALIFIER1 BLANK2 in QUALIFIER2 BLANK4
Example: A study of non-deterministic prose generation in hamster communities.

Example 2: Abstract Pattern: BLANK1ing the QUALIFIER1 BLANK2 of QUALIFIER2 BLANK3 in QUALIFIER3 BLANK4
Example: Analyzing the effects of  amino acid variations in lunar lettuce management.

"""

# approximately 10 generations of tuning the prompt above yielded this:

import random

experiments = ["Study", "Analysis", "Observation", "Investigation", "Test", "Examination", "Evaluation", "Inspection", "Survey", "Research", "Assessment", "Investigation", "Assay", "Audit", "Scrutiny", "Inquiry", "Analysis", "Analysis", "Experiment"]

subjects = ["Bacteria", "Ants", "Mice", "Cats", "Beetles", "Bees", "Flies", "Frogs", "Fish", "Insects", "Crickets", "Birds", "Lizards", "Rats", "Snakes", "Spiders", "Squirrels", "Turtles", "Hamsters", "Horses", "Rabbits"]

qualifier1 = ["Non-Deterministic", "Deterministic", "Randomized", "Structured", "Unstructured", "Decentralized", "Centralized", "Organic", "Synthetic", "Natural", "Artificial", "Atomic", "Composite", "Robotic", "Self-Organizing", "Adaptive", "Dynamic", "Static", "Quantum", "Digital", "Analog"]

qualifier2 = ["Grammatical", "Syntactical", "Mathematical", "Mechanical", "Structural", "Aerodynamic", "Biochemical", "Neurological", "Linguistic", "Psychological", "Social", "Cognitive", "Molecular", "Cellular", "Organic", "Environmental", "Atmospheric", "Astronomical", "Quantum", "Nuclear", "Geological"]

qualifier3 = ["Resource", "Population", "Management", "Culture", "Organization", "Behavior", "Development", "Evolution", "Interaction", "Structure", "Function", "Process", "Systems", "Ecosystems", "Networks", "Scale", "Dynamics", "Cooperation", "Competition", "Adaptation", "Integration"]

titles = []

patterns = ["A {0} of {3} {1} in {4} {2}",
            "Analyzing the {3} of {2} {1} in {5} {4}",
            "Analyzing the {3} of {2} {1} and {5} {4}",
            "Observing the {3} of {2} {1} in {5} {4}",
            "Studying the {3} of {2} {1} in {5} {4}",
            "Experimenting the {3} of {2} {1} in {5} {4}",
            "Examining the {3} of {2} {1} in {5} {4}",
            "Researching the {3} of {2} {1} in {5} {4}",
            "Testing the {3} of {2} {1} in {5} {4}",
            "Investigating the {3} of {2} {1} in {5} {4}",
            "Assessing the {3} of {2} {1} in {5} {4}",
            "Inspecting the {3} of {2} {1} in {5} {4}",
            "Scrutinizing the {3} of {2} {1} in {5} {4}",
            "Inquiring the {3} of {2} {1} in {5} {4}",
            "The {3} of {2} {1} in {5} {4}",
            "A Study of the {3} of {2} {1} in {5} {4}",
            "Studying {2} {1} in {5} {4}",
            "Experimenting {2} {1} in {5} {4}"]

for _ in range(50000):
    exp = experiments[random.randint(0, len(experiments)-1)]
    sub = subjects[random.randint(0, len(subjects)-1)]
    q1 = qualifier1[random.randint(0, len(qualifier1)-1)]
    q2 = qualifier2[random.randint(0, len(qualifier2)-1)]
    q3 = qualifier3[random.randint(0, len(qualifier3)-1)]
    pattern = patterns[random.randint(0, len(patterns)-1)]
    if sub[0] in 'AEIOUaeiou':
        article = 'An'
    else:
        article = 'A'
    title = pattern.format(exp, article, sub, q1, q2, q3)
    titles.append(title)

for title in titles:
    print(title.title())