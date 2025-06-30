"""Test MCP server implementation."""

import pytest
from unittest.mock import Mock, patch
from mcp.server.fastmcp import FastMCP

from helpscout_mcp.server import mcp


class TestMCPServer:
    """Test MCP server functionality."""

    def test_mcp_server_exists(self):
        """Test that MCP server instance exists."""
        assert mcp is not None
        assert isinstance(mcp, FastMCP)

    def test_mcp_server_has_correct_name(self):
        """Test that MCP server has the correct name."""
        # This will help us verify server identity
        assert mcp.name == "HelpScout MCP Server"

    def test_list_conversations_function_exists(self):
        """Test that list_conversations function exists."""
        from helpscout_mcp.server import list_conversations
        assert callable(list_conversations)

    def test_get_conversation_function_exists(self):
        """Test that get_conversation function exists."""
        from helpscout_mcp.server import get_conversation
        assert callable(get_conversation)

    @pytest.mark.asyncio
    async def test_list_conversations_requires_api_token(self):
        """Test that list_conversations requires API token."""
        from helpscout_mcp.server import list_conversations
        
        # Mock settings with empty API token
        with patch('helpscout_mcp.server.settings') as mock_settings:
            mock_settings.helpscout_api_token = ""
            
            with pytest.raises(ValueError, match="HelpScout API token not configured"):
                await list_conversations()

    @pytest.mark.asyncio
    async def test_get_conversation_requires_api_token(self):
        """Test that get_conversation requires API token."""
        from helpscout_mcp.server import get_conversation
        
        # Mock settings with empty API token
        with patch('helpscout_mcp.server.settings') as mock_settings:
            mock_settings.helpscout_api_token = ""
            
            with pytest.raises(ValueError, match="HelpScout API token not configured"):
                await get_conversation("123")