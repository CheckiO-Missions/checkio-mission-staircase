"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["100123"],
            "answer": 4,
        },
        {
            "input": ["503715"],
            "answer": 4,
        },
        {
            "input": ["0425494220946"],
            "answer": 6,
        },
        {
            "input": ["04414952075836"],
            "answer": 7,
        },
        {
            "input": ["1234567891011213"],
            "answer": 12,
        },
    ],
    "Extra": [
        {
            "input": ["1011101110121013"],
            "answer": 6,
        },
        {
            "input": ["007304517931223832"],
            "answer": 9,
        },
        {
            "input": ["78219236133269344741"],
            "answer": 9,
        },
    ]
}
