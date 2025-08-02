import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from dash import Dash
from app import app


# Dash test fixture automatically provided by Dash’s test framework
@pytest.mark.parametrize("dash_duo", [app], indirect=True)
def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Visualiser"

def test_graph_is_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_radio_items_present(dash_duo):
    dash_duo.start_server(app)
    radio = dash_duo.find_element("#region-selector")
    assert radio is not None