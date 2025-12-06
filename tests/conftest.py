import pytest
import shutil
import tempfile
from pathlib import Path

@pytest.fixture
def temp_workspace():
    """Provides a clean temporary directory for file operations."""
    temp_dir = tempfile.mkdtemp()
    yield Path(temp_dir)
    shutil.rmtree(temp_dir)
