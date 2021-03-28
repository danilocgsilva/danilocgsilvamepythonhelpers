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


