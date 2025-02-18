"""Top-level package for firstcomfynode."""

__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    "WEB_DIRECTORY",
]

__author__ = """ChenPenghui"""
__email__ = "924898127cph@gmail.com"
__version__ = "0.0.1"

from .src.firstcomfynode.nodes import NODE_CLASS_MAPPINGS
from .src.firstcomfynode.nodes import NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./web"
