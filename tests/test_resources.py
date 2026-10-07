from unittest import result

from mcp_server.resources.spaces import read_spaces_resource

# Tests for the read_spaces_resource function in mcp_server.resources
def test_spaces_resource_returns_list():
    result = read_spaces_resource()

    assert isinstance(result, list)

def test_spaces_resource_contains_three_spaces():
    result = read_spaces_resource()
    assert len(result) == 3

def test_spaces_resource_contains_eng():
    result = read_spaces_resource()
    
    assert any(
        space["key"] == "ENG"
        for space in result
    )

def test_spaces_resource_contains_hr():
    result = read_spaces_resource()
    
    assert any(
        space["key"] == "HR"
        for space in result
    )

def test_spaces_resource_contains_ops():
    result = read_spaces_resource()
    
    assert any(
        space["key"] == "OPS"
        for space in result
    )

# Test that the resource returns a list
def test_spaces_resource_contains_data():
    result = read_spaces_resource()

    assert len(result) > 0

# Test the first record in the resource data
def test_spaces_resource_first_record():
    result = read_spaces_resource()

    first = result[0]

    assert first["id"] == "1"
    assert first["key"] == "ENG"
    assert first["name"] == "Engineering"