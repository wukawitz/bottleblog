#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Unittest code for testing logging functionality
"""

import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from blog.libraries.log import Log

class LogTest(unittest.TestCase):
    """
    Tests application logging functionality
    """
    PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
    INFORMATION_LOG = PATH + "../logs/info.log"
    ERROR_LOG = PATH + "../logs/error.log"
    print "####"
    print INFORMATION_LOG
    print ERROR_LOG

    def test_ilog_functionality(self):
        """
        Determines if able to write to the information log
        Input:
            None
        Returns:
            None
        """
        test_file = LogTest.INFORMATION_LOG
        test_location = "LogTest.test_ilog_functionality()"
        test_message = "This is a test message"
        if os.path.isfile(test_file):
            os.remove(test_file)
        Log.ilog(location=test_location, message=test_message)
        content = self._contents(current_file=test_file)
        result = self._contains(string=content, substring=test_message)
        self.assertTrue(result)
        if os.path.isfile(test_file):
            os.remove(test_file)
    
    def test_elog_functionality(self):
        """
        Determines if able to write to the error log
        Input:
            None
        Returns:
            None
        """
        test_file = LogTest.ERROR_LOG
        test_location = "LogTest.test_elog_functionality()"
        test_message = "This is a test message"
        if os.path.isfile(test_file):
            os.remove(test_file)
        Log.elog(location=test_location, message=test_message)
        content = self._contents(current_file=test_file)
        result = self._contains(string=content, substring=test_message)
        self.assertTrue(result)
        if os.path.isfile(test_file):
            os.remove(test_file)

    def test_write_functionality(self):
        """
        Determines if able to write to any file
        Input:
            None
        Returns:
            None
        """
        test_file = "/tmp/test.log"
        test_message = "This is a test message"
        if os.path.isfile(test_file):
            os.remove(test_file)
        Log.write(current_file=test_file, message=test_message)
        content = self._contents(current_file=test_file)
        result = self._contains(string=content, substring=test_message)
        self.assertTrue(result)
        if os.path.isfile(test_file):
            os.remove(test_file)

    def _contents(self, **kwargs):
        """
        Get the contents of a file
        Input:
            current_file - Current file to get contents from
        Returns:
            str
        """
        contents = ""
        try:
            current_file = kwargs.get("current_file", "")
            with open(current_file, "r") as f_obj:
                contents = f_obj.read().strip()
        except Exception, e_obj:
            print "[-] ERROR - LogTest._contents() - {0}".format(str(e_obj))
        return contents

    def _contains(self, **kwargs):
        """
        Test if string contains substring
        Input:
            string - Test string
            substring - Substring to look for
        Returns:
            bool
        """
        string = kwargs.get("string", "")
        substring = kwargs.get("substring", "")
        if substring in string:
            return True
        return False

if __name__ == "__main__":

    unittest.main()
