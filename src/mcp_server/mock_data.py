"""
Mock Confluence data.

Phase 0:
Development only.
No external systems involved.
"""

# Function to get mock Confluence spaces
def get_spaces() -> list:

    # This simulates what will eventually come from Confluence.
    # Later we want: confluence://spaces
    return [
        {
            "id": "1",
            "key": "ENG",
            "name": "Engineering",
        },
        {
            "id": "2",
            "key": "HR",
            "name": "Human Resources",
        },
        {
            "id": "3",
            "key": "OPS",
            "name": "Operations",
        },
    ]