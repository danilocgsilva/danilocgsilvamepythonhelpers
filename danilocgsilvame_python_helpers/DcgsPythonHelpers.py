class DcgsPythonHelpers:

    def getHashDateFromDate(self, datetime_data):
        return str(datetime_data.year) +\
            '{0:02}'.format(datetime_data.month) +\
            '{0:02}'.format(datetime_data.day) + '-' +\
            '{0:02}'.format(datetime_data.hour) + 'h' +\
            '{0:02}'.format(datetime_data.minute) + 'm' +\
            '{0:02}'.format(datetime_data.second) + 's'