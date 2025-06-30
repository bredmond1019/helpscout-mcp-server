"""Configuration settings for HelpScout MCP Server."""

from pydantic import HttpUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    helpscout_api_token: str = ""
    helpscout_api_url: HttpUrl = "https://api.helpscout.net"  # type: ignore