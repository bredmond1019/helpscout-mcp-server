# Quick Start Guide

Get the HelpScout MCP Server running with Claude Desktop or Claude Code in minutes.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager
- HelpScout OAuth2 API token

## Getting Your HelpScout API Token

1. Log into your HelpScout account
2. Go to **Your Profile** → **My Apps**
3. Create a new OAuth2 application
4. Use the **Client Credentials** flow for server-to-server integration
5. Copy your access token

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd helpscout-mcp-server

# Install dependencies
uv sync

# Verify installation works
uv run pytest
```

## Configuration

### Option 1: Environment Variables
```bash
export HELPSCOUT_API_TOKEN="your-oauth-token-here"
export HELPSCOUT_API_URL="https://api.helpscout.net"  # Optional
```

### Option 2: .env File
Create a `.env` file in the project root:
```bash
HELPSCOUT_API_TOKEN=your-oauth-token-here
HELPSCOUT_API_URL=https://api.helpscout.net
```

## Claude Desktop Setup

### 1. Install in Claude Desktop

```bash
# Install the MCP server for Claude Desktop
uv run mcp install src/helpscout_mcp/server.py:mcp --name "HelpScout Support"
```

### 2. Verify Installation

Open Claude Desktop and you should see "HelpScout Support" in the MCP tools section.

### 3. Test the Tools

In Claude Desktop, try:
```
List my recent HelpScout conversations
```

or

```
Get details for HelpScout conversation ID 12345
```

## Claude Code Setup

### 1. Configure MCP in settings.json

Add to your Claude Code configuration:

```json
{
  "mcpServers": {
    "helpscout": {
      "command": "uv",
      "args": ["run", "python", "-m", "helpscout_mcp.server"],
      "cwd": "/path/to/helpscout-mcp-server",
      "env": {
        "HELPSCOUT_API_TOKEN": "your-oauth-token-here"
      }
    }
  }
}
```

### 2. Restart Claude Code

Restart Claude Code to load the new MCP server.

### 3. Test the Integration

Claude Code should now have access to HelpScout tools. Try:
```
Show me conversations in mailbox 123 with status "active"
```

## Development Mode

For development and testing:

```bash
# Run in development mode with hot reload
uv run mcp dev src/helpscout_mcp/server.py:mcp

# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/helpscout_mcp --cov-report=term-missing
```

## Available Tools

### `list_conversations`
Lists conversations from HelpScout with optional filtering.

**Parameters:**
- `mailbox` (optional): Mailbox ID to filter conversations
- `status` (optional): Status filter (active, closed, etc.)
- `limit` (optional): Maximum number of conversations (default: 25)

**Example:**
```python
await list_conversations(mailbox="123", status="active", limit=10)
```

### `get_conversation`
Gets detailed information about a specific conversation.

**Parameters:**
- `conversation_id` (required): The conversation ID
- `embed_threads` (optional): Include conversation threads (default: false)

**Example:**
```python
await get_conversation("456", embed_threads=True)
```

## Troubleshooting

### Common Issues

**"HelpScout API token not configured"**
- Ensure `HELPSCOUT_API_TOKEN` environment variable is set
- Verify the token is valid and has proper permissions

**"Connection failed"**
- Check your internet connection
- Verify the HelpScout API is accessible
- Confirm your API token hasn't expired

**"Tool not found in Claude"**
- Restart Claude Desktop/Code after installation
- Check MCP server logs for errors
- Verify the installation path is correct

### Enable Debug Logging

```bash
export LOG_LEVEL=DEBUG
uv run mcp dev src/helpscout_mcp/server.py:mcp
```

### Test API Connection

```bash
# Quick test to verify your token works
curl -H "Authorization: Bearer YOUR_TOKEN" \
     https://api.helpscout.net/v2/conversations
```

## Next Steps

- Explore the [full documentation](README.md)
- Check out example workflows in the `tests/` directory
- Contribute improvements via pull requests

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review server logs for error messages
3. Verify your HelpScout API token permissions
4. Open an issue with detailed error information