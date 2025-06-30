"""HelpScout MCP Server implementation."""

import os
from typing import Optional, List, Dict, Any
from mcp.server.fastmcp import FastMCP

from .client import HelpScoutClient
from .config import Settings

# Create FastMCP server instance
mcp = FastMCP("HelpScout MCP Server")

# Initialize settings
settings = Settings()


@mcp.tool()
async def list_conversations(
    mailbox: Optional[str] = None,
    status: Optional[str] = None,
    limit: Optional[int] = 25
) -> List[Dict[str, Any]]:
    """
    List conversations from HelpScout.
    
    Args:
        mailbox: Optional mailbox ID to filter conversations
        status: Optional status to filter conversations (active, closed, etc.)
        limit: Maximum number of conversations to return
    
    Returns:
        List of conversation summaries
    """
    if not settings.helpscout_api_token:
        raise ValueError("HelpScout API token not configured")
    
    async with HelpScoutClient(settings.helpscout_api_token) as client:
        result = await client.list_conversations(mailbox=mailbox, status=status)
        conversations = result.get("_embedded", {}).get("conversations", [])
        return conversations[:limit] if limit else conversations


@mcp.tool()
async def get_conversation(
    conversation_id: str,
    embed_threads: bool = False
) -> Dict[str, Any]:
    """
    Get detailed information about a specific conversation.
    
    Args:
        conversation_id: The ID of the conversation to retrieve
        embed_threads: Whether to include conversation threads in the response
    
    Returns:
        Detailed conversation information
    """
    if not settings.helpscout_api_token:
        raise ValueError("HelpScout API token not configured")
    
    async with HelpScoutClient(settings.helpscout_api_token) as client:
        return await client.get_conversation(conversation_id, embed_threads=embed_threads)