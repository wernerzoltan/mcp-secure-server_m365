from pathlib import Path


def test_resource_module_exists():
    assert Path(
        "src/mcp_server/resources/spaces.py"
    ).exists()


def test_data_module_exists():
    assert Path(
        "src/mcp_server/data/mock_data.py"
    ).exists()