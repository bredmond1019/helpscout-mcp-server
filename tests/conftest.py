"""Test configuration and fixtures."""

import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_helpscout_response():
    """Mock response from HelpScout API."""
    return {
        "_embedded": {
            "conversations": [
                {
                    "id": "123",
                    "subject": "Test Conversation",
                    "status": "active",
                    "type": "email"
                }
            ]
        }
    }


@pytest.fixture
def mock_conversation_detail():
    """Mock detailed conversation response."""
    return {
        "id": "123",
        "subject": "Test Conversation",
        "status": "active",
        "type": "email",
        "createdAt": "2025-01-01T12:00:00Z",
        "assignee": {
            "id": "456",
            "firstName": "John",
            "lastName": "Doe"
        },
        "primaryCustomer": {
            "id": "789",
            "firstName": "Jane",
            "lastName": "Smith",
            "email": "jane@example.com"
        }
    }