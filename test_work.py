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


class TestWorkMockingFunction(TestCase):

    def test_using_return_value(self):
        """Note 'as' in the context manager is optional"""
        with mock.patch('work.os.getcwd', return_value='testing'):
            assert work_on() == 'testing'

    def test_using_patch_object(self):
        """We import os above and patch the target function inside it"""
        import os
        with mock.patch.object(os, 'getcwd', return_value='testing'):
            # note 'as' in the context manager is optional
            assert work_on() == 'testing'

