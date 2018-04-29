from unittest import TestCase, mock

from work import work_on


class TestWorkMockingModule(TestCase):

    def test_using_context_manager(self):
        with mock.patch('work.os') as mocked_os:
            work_on()
            mocked_os.getcwd.assert_called_once()

    @mock.patch('work.os')
    def test_using_decorator(self, mocked_os):
        work_on()
        mocked_os.getcwd.assert_called_once()

    def test_using_return_value(self):
        """Note 'as' in the context manager is optional"""
        with mock.patch('work.os.getcwd', return_value='testing'):
            assert work_on() == 'testing'
