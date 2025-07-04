# HelpScout MCP Server

A Model Context Protocol (MCP) server that provides AI assistants with access to HelpScout's Mailbox API for customer support workflows.

## Features

- **List Conversations**: Retrieve and filter conversations from HelpScout
- **Get Conversation Details**: Access detailed conversation information including threads
- **OAuth2 Authentication**: Secure API access using Bearer tokens
- **MCP Protocol**: Standard interface for AI tool integration

## Installation

```bash
# Clone and navigate to directory
cd helpscout-mcp-server

# Install dependencies
uv sync --extra dev

# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/helpscout_mcp --cov-report=term-missing
```

## Configuration

Set the required environment variable:

```bash
export HELPSCOUT_API_TOKEN="your-helpscout-oauth-token"
```

Optional configuration:
```bash
export HELPSCOUT_API_URL="https://api.helpscout.net"  # Default value
```

## Usage

The server exposes two MCP tools:

### list_conversations
```python
# List all conversations
await list_conversations()

# Filter by mailbox and status
await list_conversations(mailbox="123", status="active", limit=10)
```

### get_conversation
```python
# Get conversation details
await get_conversation("conversation-id")

# Include conversation threads
await get_conversation("conversation-id", embed_threads=True)
```

## Development

This project follows Test-Driven Development (TDD) principles:

1. **Red**: Write failing tests first
2. **Green**: Implement minimal code to pass tests
3. **Refactor**: Improve code quality while maintaining green tests

### Project Structure

```
src/helpscout_mcp/
├── __init__.py
├── server.py          # MCP server with @mcp.tool() decorators
├── client.py          # HelpScout API client with HTTPX
└── config.py          # Configuration management with Pydantic

tests/unit/
├── test_config.py     # Configuration tests
├── test_client.py     # HTTP client tests
├── test_server.py     # MCP server tests
└── test_project_structure.py  # Package structure tests
```

### Running Tests

```bash
# All tests
uv run pytest

# Specific test file
uv run pytest tests/unit/test_client.py -v

# With coverage
uv run pytest --cov=src/helpscout_mcp --cov-report=html
```

## License

MIT License