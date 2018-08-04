"""
    pyexcel_odsw
    ~~~~~~~~~~~~~~~~~~~

    The lower level ods file format handler

    :copyright: (c) 2018 by Onni Software Ltd. & its contributors
    :license: NEW BSD License
"""
import types

from pyexcel_io.book import BookWriter
from pyexcel_io.sheet import SheetWriter
from pyexcel_io._compact import text_type

import entrouvert_odsw as ods


class ODSSheetWriter(SheetWriter):
    """
    ods sheet writer
    """
    def __init__(self, native_book, name, **keywords):
        super(ODSSheetWriter, self).__init__(
            native_book, None, name, **keywords)
        self.sheet_name = name

    def set_sheet_name(self, name):
        self.current_row = 0

    def write_array(self, table):
        to_write_data = table
        if isinstance(to_write_data, types.GeneratorType):
            to_write_data = list(table)
        rows = len(to_write_data)
        if rows < 1:
            return
        columns = max([len(row) for row in to_write_data])
        self._native_book.start_sheet(columns,
                                      self.sheet_name)
        super(ODSSheetWriter, self).write_array(to_write_data)
        self._native_book.end_sheet()

    def write_row(self, array):
        """
        write a row into the file
        """
        import pdb; pdb.set_trace()
        cells = []
        for cell in array:
            try:
                cell = text_type(cell, errors="ignore")
            except TypeError:
                pass
            cells.append(cell)
        self._native_book.add_row(cells)

        self.current_row = 1


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
        self._native_book = ods.ODSWorkbook(file_name)

    def create_sheet(self, name):
        return ODSSheetWriter(self._native_book,
                              name)

    def close(self):
        """
        This call actually save the file
        """
        self._native_book.close()
