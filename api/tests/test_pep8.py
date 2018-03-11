import glob
import pep8

from django.test import TestCase


class Pep8TestCase(TestCase):

    """Test all the files for PEP8

    Attributes:
        path (str): the base path for the files
        pep8style (pep8): the checker
    """

    def setUp(self):
        """Initialize the vars for the test
        """
        self.path = '/app/'
        self.pep8style = pep8.StyleGuide(quiet=True)

    def test_pep8(self):
        """Should not show any erros"""

        for file in glob.glob('./' + '/**/*.py', recursive=True):
            if '/app/env/' not in file and '/migrations/' not in file:
                print(file)
                fchecker = pep8.Checker(file, show_source=True)
                file_errors = fchecker.check_all()
                self.assertEqual(file_errors, 0)
