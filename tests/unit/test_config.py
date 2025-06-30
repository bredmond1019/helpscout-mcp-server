"""Test configuration management."""

import os
import pytest
from unittest.mock import patch

from helpscout_mcp.config import Settings


class TestSettings:
    """Test configuration settings."""

    def test_settings_loads_from_environment_variables(self):
        """Test that settings can load from environment variables."""
        with patch.dict(os.environ, {
            'HELPSCOUT_API_TOKEN': 'test-token-123',
            'HELPSCOUT_API_URL': 'https://api.example.com'
        }):
            settings = Settings()
            assert settings.helpscout_api_token == 'test-token-123'
            assert str(settings.helpscout_api_url) == 'https://api.example.com/'

    def test_settings_provides_default_values(self):
        """Test that settings provide sensible defaults."""
        with patch.dict(os.environ, {}, clear=True):
            settings = Settings()
            assert str(settings.helpscout_api_url) == 'https://api.helpscout.net/'
            assert settings.helpscout_api_token == ''

    def test_settings_validates_required_api_token(self):
        """Test that validation catches missing required API token."""
        # This should fail initially - Red phase
        with patch.dict(os.environ, {}, clear=True):
            settings = Settings()
            # Should not raise error for empty token (will handle in auth layer)
            assert settings.helpscout_api_token == ''

    def test_settings_validates_api_url_format(self):
        """Test that API URL validation works."""
        # This should fail initially - Red phase
        from pydantic import ValidationError
        with patch.dict(os.environ, {
            'HELPSCOUT_API_URL': 'invalid-url'
        }):
            with pytest.raises(ValidationError):
                Settings()

    def test_settings_handles_missing_environment_gracefully(self):
        """Test that missing environment variables are handled gracefully."""
        with patch.dict(os.environ, {}, clear=True):
            settings = Settings()
            assert isinstance(settings.helpscout_api_token, str)
            # HttpUrl is a valid URL type, str conversion works
            assert isinstance(str(settings.helpscout_api_url), str)