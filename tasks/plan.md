# HelpScout MCP Server - TDD Implementation Plan

## Overview
This document outlines the Test-Driven Development approach for building a HelpScout MCP server that provides AI tools with access to HelpScout's API for conversation management.

## TDD Phases Complete

### ✅ Phase 1: Project Structure Setup
- **Test**: `test_project_structure.py` - Basic package imports
- **Implementation**: Created `helpscout_mcp` package with basic modules
- **Status**: COMPLETE ✅

## TDD Phases In Progress

### 🔄 Phase 2: Configuration Management
- **Red**: Write failing test for configuration loading
- **Green**: Implement basic Pydantic settings
- **Refactor**: Add validation and environment variable support

### 🔄 Phase 3: OAuth2 Authentication
- **Red**: Write failing test for OAuth2 token handling
- **Green**: Implement basic authentication
- **Refactor**: Add token refresh and error handling

### 🔄 Phase 4: HTTP Client Setup
- **Red**: Write failing test for HTTPX client initialization
- **Green**: Create basic HTTP client with HelpScout base URL
- **Refactor**: Add timeout, retry logic, proper headers

### 🔄 Phase 5: List Conversations Tool
- **Red**: Write failing test for empty conversations list
- **Green**: Implement basic GET request to `/v2/conversations`
- **Refactor**: Add query parameters, pagination, filtering

### 🔄 Phase 6: Get Conversation Tool
- **Red**: Write failing test for conversation not found
- **Green**: Implement basic GET request to `/v2/conversations/{id}`
- **Refactor**: Add thread embedding, error handling

### 🔄 Phase 7: MCP Server Integration
- **Red**: Write failing test for server initialization
- **Green**: Basic FastMCP server setup
- **Refactor**: Add tool registration and error handling

### 🔄 Phase 8: MCP Tools Registration
- **Red**: Write failing tests for missing MCP tools
- **Green**: Register `@mcp.tool()` decorators for both tools
- **Refactor**: Add parameter validation and response formatting

## Implementation Rules

1. **Red-Green-Refactor**: Always follow TDD cycle
2. **One Test at a Time**: Write one failing test, make it pass, then refactor
3. **Minimal Implementation**: Write just enough code to make tests pass
4. **Separate Commits**: Structural changes separate from behavioral changes
5. **Fast Tests**: All unit tests should run in < 100ms each

## Current Status

- ✅ Project structure created
- ✅ Basic package imports working
- ⏳ Starting configuration management tests

## Next Steps

1. Write failing test for configuration loading from environment
2. Implement minimal Settings class to make test pass
3. Refactor to add validation and proper defaults
4. Continue with OAuth2 authentication tests