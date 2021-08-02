"""
Unit and regression test for the molecool_test package.
"""

# Import package, test suite, and other packages as needed
import molecool_test
import pytest
import sys

def test_molecool_test_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "molecool_test" in sys.modules
