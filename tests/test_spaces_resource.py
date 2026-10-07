from mcp_server.resources.spaces import read_spaces_resource

# Test cases for the Confluence spaces resource
def test_resource_returns_spaces():
    result = read_spaces_resource()

    assert len(result) == 3

# Test that the resource contains the expected engineering space
def test_resource_contains_engineering_space():
    result = read_spaces_resource()

    engineering = result[0]

    assert engineering["key"] == "ENG"