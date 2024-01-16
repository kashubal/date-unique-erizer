# date-unique-erizer

date-unique-erizer is a utility that allows a user to provide a list of dates and generate a normalized, sorted list of unique date values.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed at least Python 3.12.1.
* You have read this README.

## Installing date-unique-erizer

To set up date-unique-erizer, follow these steps:

1. <>Code > Download ZIP > Open cmd in that location
2. Run this command: pip install -r requirements.txt

## Using date-unique-erizer

To use date-unique-erizer, follow these steps:

```
python dateunique.py

The application will prompt for the following inputs:
1. a complete or relative path to an input file.  This file should exist and be populated with date values.  Date value format is flexible per https://dateutil.readthedocs.io/en/stable/parser.html.  Example:  SAMPLE_INPUT_FILE.txt
2. a complete or relative path to an output file.  If the file exists at time of execution, it will be overwritten with updated results.  Example:  SAMPLE_OUTPUT_FILE.txt
```

## Contributing to 
To contribute to date-unique-erizer, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin date-unique-erizer/main`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* me!
