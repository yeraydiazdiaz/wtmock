from unittest import TestCase, mock

from worker import work_on_env

class TestBuiltin(TestCase):

    def test_patch_builtin_dict(self):
        with mock.patch('worker.print') as mock_print:
            with mock.patch('os.getcwd', return_value='/home/'):
                with mock.patch.dict('os.environ', {'MY_VAR': 'testing'}):
                    self.assertEqual(work_on_env(), '/home/testing')
                    mock_print.assert_called_once_with('Working on /home/testing')

    @mock.patch('os.getcwd', return_value='/home/')
    @mock.patch('worker.print')
    @mock.patch.dict('os.environ', {'MY_VAR': 'testing'})
    def test_patch_builtin_dict_decorators(self, mock_print, mock_getcwd):
        self.assertEqual(work_on_env(), '/home/testing')
        mock_print.assert_called_once_with('Working on /home/testing')
