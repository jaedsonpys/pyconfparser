# PyConfParser

`pyconfparser` is a library that lets you easily get and create configuration files with Python.

## Instalation

Use the [**PyPacking**](https://github.com/jaedsonpys/pypacking) package manager to install this package. Download the last package version file in [dist/ directory](https://github.com/jaedsonpys/pyconfparser/tree/master/dist), and run the following command to install the package:

```
pypacking install pyconfparser-version.zip
```

Ready! Your package has been **installed successfully**

## How to use

For now, `pyconfparser` can **only read** configuration files, which are in the style described below:

```text
section:

option1 = value1
option2 = value2
```

You can skip lines, use **uppercase** or **lowercase** words, *snake_case* or *camelCase* style. You can create as **many sections** as you like and you can also set **global options**. See an example:

```text
globalOption = test // global option

section:
option1 = value1
option2 = value2

section2:
option1 = value
```

### Reading a configuration file

Let's read this example file:

```text
globalOption = test

section:
option1 = value1
option2 = value2

section2:
option1 = value
```

There are two methods available to get the settings:

1. `PyConfigParser.read_file`: This method is used to read files, just pass the name of the file as a argument;
2. `PyConfigParser.read_string`: This method is used to read the settings of a string, just pass the string as an argument.

All the **configuration** of the file is in a **dictionary**, so you can get the sections, and the options of the sections.

With these two you can read the settings, let's use the `read_file` method:

```python
from pyconfparser import PyConfigParser

parser = PyConfigParser()
parser.read_file('config.txt')

print(parser['section']['option1']) # output: value1
```

Now the `read_string` method:

```python
from pyconfparser import PyConfigParser

config = """section:
option1 = value1
"""

parser = PyConfigParser()
parser.read_string(config)

print(parser['section']['option1']) # output: value1
```

### Creating a configuration file

Here's how to create a configuration file using `pyconfparser`:

```python
from pyconfparser import PyConfigParser

parser = PyConfigParser()

parser['global'] = 'global option'

parser['project'] = {
    'name': 'test',
    'version': '0.1.0'
}

config = parser.create_config()
```

At the end, use the `create_config` method to generate the configuration file. You can also use this to update your current options:

```python
from pyconfparser import PyConfigParser

parser = PyConfigParser()
parser.read_file('config.txt')

parser['project']['name'] = 'name'
```

# License

```
MIT License © 2022 Jaedson Silva
```

This project use the **MIT** license.