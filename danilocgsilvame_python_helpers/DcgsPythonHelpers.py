import datetime
import argparse

class DcgsPythonHelpers:

    def getHashDateFromDate(self, datetime_data = None):

        if datetime_data == None:
            datetime_data = datetime.datetime.now()

        return str(datetime_data.year) +\
            '{0:02}'.format(datetime_data.month) +\
            '{0:02}'.format(datetime_data.day) + '-' +\
            '{0:02}'.format(datetime_data.hour) + 'h' +\
            '{0:02}'.format(datetime_data.minute) + 'm' +\
            '{0:02}'.format(datetime_data.second) + 's'

    def command_line_argument_names(self, *args):
        
        command_alias_pairs = self.__get_command_alias_pairs_from_all_args(args)

        parser = argparse.ArgumentParser()
        
        for argument in command_alias_pairs:
            parser.add_argument(
                "--" + argument[0],
                "-" + argument[1],
                type=str,
                required=False
            )

    def __get_command_alias_pairs_from_all_args(self, args) -> list:

        if len(args) % 2 != 0:
            raise Exception("You can only provides a number of arguments that is even.")
        
        even_iteration = True
        iteration_count = 0
        command_alias_pair = []
        iteration_pair = []
        for argument in args:
            if even_iteration:
                iteration_pair = []
                iteration_pair.append(argument)
            else:
                iteration_pair.append(argument)
                command_alias_pair.append(iteration_pair)
            iteration_count += 1
            even_iteration = iteration_count % 2 == 0
        return command_alias_pair