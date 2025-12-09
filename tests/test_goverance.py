import pytest
import os
import sys

# Add scripts directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../scripts")))

import scan
import tag
import log

def test_scan_runs_without_error(capfd):
    scan.scan_repos()
    out, err = capfd.readouterr()
    assert "Scanning repos" in out
    assert err == ""

def test_tag_runs_without_error(capfd):
    tag.apply_tags()
    out, err = capfd.readouterr()
    assert "Applying multidimensional tags" in out
    assert err == ""

def test_log_runs_without_error(capfd):
    log.log_results()
    out, err = capfd.readouterr()
    assert "Logging audit results" in out
    assert err == ""