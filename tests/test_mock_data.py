from mcp_server.mock_data import get_spaces

# Tests for the mock Confluence data functions
def test_get_spaces_returns_list():
    spaces = get_spaces()
    
    # Ensure that the list is not empty for further tests
    assert isinstance(spaces, list)

# Test that the list of spaces contains at least one record
def test_get_spaces_contains_records():
    spaces = get_spaces()

    # Ensure that each space has the required fields for further tests
    assert len(spaces) > 0

# Test that a space has the required fields
def test_space_has_required_fields():
    space = get_spaces()[0]

    assert "id" in space
    assert "key" in space
    assert "name" in space