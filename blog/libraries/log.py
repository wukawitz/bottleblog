#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module performs all logging functions for the application
"""

import datetime
import os

class Log(object):
    """
    Class used for all loging functionality
    """

    PATH = os.path.dirname(os.path.abspath(__file__))
    INFORMATION_LOG = PATH + "/../logs/info.log"
    ERROR_LOG = PATH + "/../logs/error.log"

    @staticmethod
    def ilog(**kwargs):
        """
        Information log
        Input:
            location - The location of the log call
            message - The message to log
        Returns:
            None
        """
        location = kwargs.get("location", "").strip()
        message = kwargs.get("message", "").strip()
        message = "{0} - {1}".format(location, message)
        Log.write(current_file=Log.INFORMATION_LOG, message=message)

    @staticmethod
    def elog(**kwargs):
        """
        Error log
        Input:
            location - The location of the log call
            message - The message to log
        Returns:
            None
        """
        location = kwargs.get("location", "").strip()
        message = kwargs.get("message", "").strip()
        message = "{0} - {1}".format(location, message)
        Log.write(current_file=Log.ERROR_LOG, message=message)

    @staticmethod
    def write(**kwargs):
        """
        Write to a file
        Input:
            current_file - The full path to the file to be written to
            message - The message to be written
        Returns:
            None
        """
        try:
            current_file = kwargs.get("current_file", "")
            message = kwargs.get("message", "").strip()
            current_time = datetime.datetime.now() \
                                   .strftime('%Y-%m-%d %H:%M:%S')
            log = "{0} {1}\n".format(current_time, message)
            with open(current_file, "a+") as f_obj:
                f_obj.write(log)
        except Exception, e_obj:
            print "[!] ERROR - Log.write() - {0}".format(str(e_obj))
