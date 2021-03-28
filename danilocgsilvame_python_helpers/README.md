# Class `DcgsPythonHelper`

**DcgsPythonHelper.py** holds the object containing all utilities functions:

## `getHashDateFromDate`

Generates a *hash* based on type.

Example:

```
import datetime
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers

datetimeForged = datetime.datetime(2017, 11, 12, 8, 6, 24)
pHelpers = DcgsPythonHelpers()
results = pHelpers.getHashDateFromDate(datetimeForged)
```
The `results` will be `20171112-08h06m24s`.

## `command_line_argument_names`

Returns an `argparse` object containing variables and its values provided by the user.

```
from danilocgsilvame_python_helpers.DcgsPythonHelpers import DcgsPythonHelpers

pHelpers = DcgsPythonHelpers()
argparser = pHelpers.command_line_argument_names('command', 'c', 'template', 't')

print(argparser.command)
print(argparser.template)
```
The user may pass the `command -t myvalue -c commandvalue`, the in the print result you will found `myvalue` as template and `commandvalue` as command.
Not that the user can provies `command --template myvalue --command commandvalue` and the result will be exact the same.
So notice that for this command, you must always pass values as pair, beign the first the argument name and the second its alias, the third beign the next command argument, the fourth its alias, and so forth.
