import pytest
import unittest

from modules.sfp_grep_app import sfp_grep_app
from sflib import SpiderFoot


@pytest.mark.usefixtures
class TestModuleGrepApp(unittest.TestCase):

    def test_opts(self):
        module = sfp_grep_app()
        self.assertEqual(len(module.opts), len(module.optdescs))

    def test_setup(self):
        sf = SpiderFoot(self.default_options)
        module = sfp_grep_app()
        module.setup(sf, dict())

    def test_watchedEvents_should_return_list(self):
        module = sfp_grep_app()
        self.assertIsInstance(module.watchedEvents(), list)

    def test_producedEvents_should_return_list(self):
        module = sfp_grep_app()
        self.assertIsInstance(module.producedEvents(), list)
