"""Test HelpScout API client."""

import pytest
from unittest.mock import Mock, patch
import httpx

from helpscout_mcp.client import HelpScoutClient


class TestHelpScoutClient:
    """Test HelpScout API client functionality."""

    def test_client_initialization_requires_api_token(self):
        """Test that client initialization requires an API token."""
        # This should fail initially - Red phase
        with pytest.raises(TypeError):
            HelpScoutClient()  # Missing required api_token parameter

    def test_client_initialization_with_token(self):
        """Test that client initializes properly with API token."""
        # This should fail initially - Red phase
        client = HelpScoutClient(api_token="test-token")
        assert client.api_token == "test-token"
        assert client.base_url == "https://api.helpscout.net"

    def test_client_creates_httpx_client(self):
        """Test that client creates an HTTPX client instance."""
        # This should fail initially - Red phase
        client = HelpScoutClient(api_token="test-token")
        assert hasattr(client, 'http_client')
        assert isinstance(client.http_client, httpx.AsyncClient)

    def test_client_sets_proper_headers(self):
        """Test that client sets proper authorization headers."""
        # This should fail initially - Red phase
        client = HelpScoutClient(api_token="test-token")
        headers = client.http_client.headers
        assert headers.get("Authorization") == "Bearer test-token"
        assert headers.get("Content-Type") == "application/json"

    def test_client_sets_timeout_configuration(self):
        """Test that client configures proper timeouts."""
        # This should fail initially - Red phase
        client = HelpScoutClient(api_token="test-token")
        timeout = client.http_client.timeout
        assert timeout.connect == 10.0
        assert timeout.read == 30.0

    @pytest.mark.asyncio
    async def test_client_context_manager_support(self):
        """Test that client supports async context manager."""
        async with HelpScoutClient(api_token="test-token") as client:
            assert isinstance(client, HelpScoutClient)
            assert not client.http_client.is_closed

    @pytest.mark.asyncio
    async def test_list_conversations_method_exists(self):
        """Test that list_conversations method exists."""
        # This should fail initially - Red phase
        client = HelpScoutClient(api_token="test-token")
        assert hasattr(client, 'list_conversations')
        assert callable(getattr(client, 'list_conversations'))

    @pytest.mark.asyncio 
    async def test_list_conversations_makes_get_request(self):
        """Test that list_conversations makes a GET request to correct endpoint."""
        # This should fail initially - Red phase
        with patch.object(httpx.AsyncClient, 'get') as mock_get:
            mock_get.return_value = Mock(status_code=200, json=lambda: {"_embedded": {"conversations": []}})
            
            async with HelpScoutClient(api_token="test-token") as client:
                await client.list_conversations()
                
            mock_get.assert_called_once_with("/v2/conversations", params={})

    @pytest.mark.asyncio
    async def test_list_conversations_with_parameters(self):
        """Test that list_conversations supports query parameters."""
        # This should fail initially - Red phase
        with patch.object(httpx.AsyncClient, 'get') as mock_get:
            mock_get.return_value = Mock(status_code=200, json=lambda: {"_embedded": {"conversations": []}})
            
            async with HelpScoutClient(api_token="test-token") as client:
                await client.list_conversations(mailbox="123", status="active")
                
            mock_get.assert_called_once_with("/v2/conversations", params={"mailbox": "123", "status": "active"})

    @pytest.mark.asyncio
    async def test_get_conversation_method_exists(self):
        """Test that get_conversation method exists."""
        # This should fail initially - Red phase
        client = HelpScoutClient(api_token="test-token")
        assert hasattr(client, 'get_conversation')
        assert callable(getattr(client, 'get_conversation'))

    @pytest.mark.asyncio
    async def test_get_conversation_makes_get_request(self):
        """Test that get_conversation makes a GET request to correct endpoint."""
        # This should fail initially - Red phase
        with patch.object(httpx.AsyncClient, 'get') as mock_get:
            mock_get.return_value = Mock(status_code=200, json=lambda: {"id": "123", "subject": "Test"})
            
            async with HelpScoutClient(api_token="test-token") as client:
                await client.get_conversation("123")
                
            mock_get.assert_called_once_with("/v2/conversations/123", params={})

    @pytest.mark.asyncio
    async def test_get_conversation_with_embed_threads(self):
        """Test that get_conversation supports embed threads parameter."""
        # This should fail initially - Red phase
        with patch.object(httpx.AsyncClient, 'get') as mock_get:
            mock_get.return_value = Mock(status_code=200, json=lambda: {"id": "123", "subject": "Test"})
            
            async with HelpScoutClient(api_token="test-token") as client:
                await client.get_conversation("123", embed_threads=True)
                
            mock_get.assert_called_once_with("/v2/conversations/123", params={"embed": "threads"})