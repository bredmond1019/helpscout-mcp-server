"""HelpScout API client implementation."""

import httpx
from typing import Optional


class HelpScoutClient:
    """Client for HelpScout API interactions."""
    
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.base_url = "https://api.helpscout.net"
        
        # Create HTTPX client with proper configuration
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        timeout = httpx.Timeout(connect=10.0, read=30.0, write=30.0, pool=10.0)
        
        self.http_client = httpx.AsyncClient(
            base_url=self.base_url,
            headers=headers,
            timeout=timeout
        )
    
    async def __aenter__(self):
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.http_client.aclose()
    
    async def list_conversations(self, mailbox: Optional[str] = None, status: Optional[str] = None, **kwargs):
        """List conversations from HelpScout API."""
        params = {}
        if mailbox:
            params["mailbox"] = mailbox
        if status:
            params["status"] = status
        params.update(kwargs)
        
        response = await self.http_client.get("/v2/conversations", params=params)
        response.raise_for_status()
        return response.json()
    
    async def get_conversation(self, conversation_id: str, embed_threads: bool = False):
        """Get a specific conversation from HelpScout API."""
        params = {}
        if embed_threads:
            params["embed"] = "threads"
        
        response = await self.http_client.get(f"/v2/conversations/{conversation_id}", params=params)
        response.raise_for_status()
        return response.json()