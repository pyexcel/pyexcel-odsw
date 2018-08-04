"""
    pyexcel_odsw
    ~~~~~~~~~~~~~~~~~~~
    The lower level ods file format handler
    :copyright: (c) 2018 by Onni Software Ltd. & its contributors
    :license: NEW BSD License
"""
from pyexcel_io.book import BookWriter
from pyexcel_io.sheet import SheetWriter


class ODSSheetWriter(SheetWriter):
    """
    ods sheet writer
    """
    def set_sheet_name(self, name):
        self.current_row = 0

    def write_row(self, array):
        """
        write a row into the file
        """
        pass


class ODSWriter(BookWriter):
    """
    ods writer
    """
    def __init__(self):
        BookWriter.__init__(self)
        self._native_book = None

    def open(self, file_name, **keywords):
        """
        Open a file for writing
        """
        pass

    def create_sheet(self, name):
        return ODSSheetWriter(self._native_book,
                              self._native_book.add_worksheet(name), name)

    def close(self):
        """
        This call actually save the file
        """
        pass
