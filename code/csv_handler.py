#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-

import csv

class CsvHandler():
    """Handle csv data.
    """

    def read_csv(self, path, configFormat = 'rb', configEncoding = 'utf-8', configDelimiter = ',', configQuotechar = '|', pythonVersion = '3'):
        """Returns the content of a csv document.
        """
        if pythonVersion == '3':
            csvFile = open(path, configFormat, encoding = configEncoding)
        elif pythonVersion == '2':
            csvFile = open(path, configFormat)
        reader = csv.reader(csvFile, delimiter = configDelimiter, quotechar = configQuotechar)

        outputList = []
        for row in reader:
            if len(row) > 0:
                outputList.append(row)
        csvFile.close()
        return outputList

    def create_csv(self, content, path):
        """Creates a new csv document.
        """
        inputList = content
        csvFile = open(path, 'a')
        writer = csv.writer(csvFile)

        for item in inputList:
            if type(item) == list:
                writer.writerow(item)
            else:
                writer.writerow([item])
        csvFile.close()
        return csvFile
