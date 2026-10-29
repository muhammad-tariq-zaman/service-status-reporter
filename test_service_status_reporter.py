import os, sys, socket, threading
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import check


class TestServiceStatus(unittest.TestCase):
    def test_open_port_is_up(self):
        srv = socket.socket(); srv.bind(("127.0.0.1", 0)); srv.listen(1)
        port = srv.getsockname()[1]
        try:
            self.assertTrue(check("127.0.0.1", port))
        finally:
            srv.close()

    def test_closed_port_is_down(self):
        srv = socket.socket(); srv.bind(("127.0.0.1", 0))
        port = srv.getsockname()[1]; srv.close()
        self.assertFalse(check("127.0.0.1", port))
