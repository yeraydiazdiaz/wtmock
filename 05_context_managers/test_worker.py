from io import StringIO
from unittest import TestCase, mock

from worker import size_of

class TestContextManager(TestCase):

    def test_context_manager(self):
        with mock.patch('worker.open') as mock_open:
            mock_open.return_value.__enter__.return_value = StringIO('testing')
            self.assertEqual(size_of(), 7)
