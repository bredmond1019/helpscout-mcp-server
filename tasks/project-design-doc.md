# HelpScout MCP Server - Project Design Document

## Project Overview

The HelpScout MCP Server is a Python-based Model Context Protocol server that provides AI assistants with structured access to HelpScout's Mailbox API. This enables AI tools to help with customer support workflows by retrieving and analyzing conversation data.

## Goals

### Primary Goals
1. **Secure API Access**: Provide OAuth2-authenticated access to HelpScout's API
2. **Conversation Management**: Enable listing and retrieving individual conversations
3. **MCP Integration**: Follow MCP protocol standards for AI tool interactions
4. **Customer Support Focus**: Support common customer service workflows

### Secondary Goals
1. **Performance**: Low-latency API responses with proper caching
2. **Extensibility**: Architecture that supports additional HelpScout endpoints
3. **Developer Experience**: Clear documentation and easy setup process

## Architecture

### Core Components

#### 1. MCP Server (`helpscout_mcp.server`)
- **Purpose**: Main MCP server using FastMCP Python SDK
- **Responsibilities**:
  - Handle MCP protocol communication
  - Register and execute MCP tools
  - Coordinate between authentication and API client

#### 2. HelpScout API Client (`helpscout_mcp.client`)
- **Purpose**: Handle all HTTP interactions with HelpScout API
- **Responsibilities**:
  - Execute authenticated HTTP requests
  - Handle API rate limiting and retries
  - Parse and validate API responses
  - Cache conversation data appropriately

#### 3. OAuth2 Authentication (`helpscout_mcp.auth`)
- **Purpose**: Manage HelpScout OAuth2 authentication flow
- **Responsibilities**:
  - Handle OAuth2 token management
  - Refresh expired tokens automatically
  - Secure credential storage
  - Generate proper authorization headers

#### 4. Configuration Management (`helpscout_mcp.config`)
- **Purpose**: Centralized configuration with validation
- **Responsibilities**:
  - Load settings from environment variables
  - Validate configuration values
  - Provide sensible defaults
  - Handle different deployment environments

#### 5. Data Models (`helpscout_mcp.models`)
- **Purpose**: Pydantic models for type safety and validation
- **Responsibilities**:
  - Define conversation and customer data structures
  - Validate API responses
  - Serialize/deserialize data for MCP protocol

## Technology Stack

### Core Dependencies
- **MCP SDK**: Official Python MCP server implementation
- **HTTPX**: Modern async HTTP client for API calls
- **Pydantic**: Data validation and settings management
- **Pydantic-Settings**: Environment variable configuration

### Development Dependencies
- **Pytest**: Testing framework with async support
- **Pytest-Mock**: Mocking utilities for testing
- **Black**: Code formatting
- **Ruff**: Fast Python linting
- **MyPy**: Static type checking

## API Integration

### HelpScout Endpoints
1. **List Conversations**: `GET /v2/conversations`
   - Query parameters: mailbox, status, tag, assigned_to, query
   - Pagination support
   - Advanced search capabilities

2. **Get Conversation**: `GET /v2/conversations/{conversationId}`
   - Detailed conversation information
   - Optional thread embedding
   - Customer and assignee details

### Authentication Flow
1. OAuth2 Client Credentials flow
2. Bearer token authentication
3. Automatic token refresh
4. Rate limit handling (429 responses)

## MCP Tools Design

### Tool 1: List Conversations
```python
@mcp.tool()
async def list_conversations(
    mailbox: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 25
) -> List[ConversationSummary]:
    """List HelpScout conversations with optional filtering."""
```

### Tool 2: Get Conversation
```python
@mcp.tool()
async def get_conversation(
    conversation_id: str,
    embed_threads: bool = False
) -> ConversationDetail:
    """Get detailed information about a specific conversation."""
```

## Data Flow

1. **AI Assistant Request**: Send MCP request with tool name and parameters
2. **Parameter Validation**: Validate input using Pydantic models
3. **Authentication**: Apply OAuth2 bearer token
4. **API Request**: Execute HTTP request to HelpScout API
5. **Response Processing**: Parse and validate API response
6. **Data Transformation**: Convert to MCP-compatible format
7. **MCP Response**: Return structured data to AI assistant

## Security Considerations

### API Security
- OAuth2 token secure storage
- Rate limiting compliance
- Request/response logging (excluding sensitive data)
- API error handling and user-friendly messages

### Data Privacy
- No persistent storage of customer data
- Minimal data exposure in logs
- Secure handling of authentication credentials
- Compliance with HelpScout's API terms

## Development Approach

### Test-Driven Development
1. **Red**: Write failing test for each feature
2. **Green**: Implement minimal code to pass test
3. **Refactor**: Improve code quality while maintaining green tests

### Testing Strategy
- **Unit Tests**: Test individual components with mocks
- **Integration Tests**: Test component interactions
- **HTTP Mocking**: Use recorded responses for predictable testing
- **Coverage Target**: 95% line coverage

## Implementation Phases

### Phase 1: Foundation ✅
- Project structure and dependencies
- Basic MCP server setup
- Configuration management
- OAuth2 authentication framework

### Phase 2: Core API Integration
- HTTP client implementation
- List conversations endpoint
- Get conversation endpoint
- Error handling and validation

### Phase 3: MCP Tools
- MCP tool registration
- Parameter validation
- Response formatting
- Tool documentation

### Phase 4: Polish & Production
- Comprehensive error handling
- Performance optimization
- Documentation and examples
- CI/CD setup

## Success Metrics

### Functionality
- Both MCP tools working correctly
- Successful OAuth2 authentication
- Proper error handling for all scenarios

### Performance
- API response times < 1 second
- Memory usage < 50MB
- Handles rate limiting gracefully

### Quality
- 95%+ test coverage
- All linting and type checking passes
- Clear documentation and examples