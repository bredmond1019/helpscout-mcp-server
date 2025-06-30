"""Test basic project structure and imports."""

import pytest


def test_helpscout_mcp_package_imports():
    """Test that the helpscout_mcp package can be imported."""
    # This should fail initially - Red phase
    import helpscout_mcp
    assert helpscout_mcp.__name__ == "helpscout_mcp"


def test_server_module_imports():
    """Test that the server module can be imported."""
    # This should fail initially - Red phase
    from helpscout_mcp import server
    assert hasattr(server, 'mcp')


def test_client_module_imports():
    """Test that the client module can be imported."""
    # This should fail initially - Red phase
    from helpscout_mcp import client
    assert hasattr(client, 'HelpScoutClient')


def test_config_module_imports():
    """Test that the config module can be imported."""
    # This should fail initially - Red phase
    from helpscout_mcp import config
    assert hasattr(config, 'Settings')