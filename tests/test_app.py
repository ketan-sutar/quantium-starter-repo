import sys
from pathlib import Path

# Add project root to Python path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from app import app


def test_header_is_present():
    layout = app.layout
    header = layout.children[0]
    assert "Pink Morsel Sales Visualiser" in header.children[0].children


def test_region_picker_is_present():
    layout = app.layout
    radio = layout.children[1].children[1]
    assert radio.id == "region-filter"


def test_visualisation_is_present():
    layout = app.layout
    graph = layout.children[2].children[0]
    assert graph.id == "sales-line-chart"
