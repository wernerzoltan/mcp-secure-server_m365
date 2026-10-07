import importlib


def test_mcp_installed():
    assert importlib.import_module("mcp")


def test_pytest_installed():
    assert importlib.import_module("pytest")