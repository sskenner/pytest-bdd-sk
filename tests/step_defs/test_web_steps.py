"""
This module contains step definitions for web.feature.
It  uses Selenium WebDriver fro browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project, 
use Page Object Model or Screenplay Pattern to model web interactions.

Prerequisites:
 - Firefox must be installed
 - geckodriver must be installed and accessible on the system path.
"""

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import keys

# Constants