# Python XLSX tryout

## Purpose

The purpose of this (mostly AI-generated) short script is to demonstrate how to handle Excel files with Python.

The script loads the contents of the file `existing.xlsx`, reads two values within it, sums them, and finally
generates an output file named `generated.xsls` containing the sum of the two values.

## Usage

### Prerequisites

The script relies on package `openpyxl`, which must be installed:

```bash
python -m pip install -r requirements.txt
```

### Execution

In its raw form, the script takes no input parameters; therefore, execution boils down to:

```bash
python ./read_and_write.py
```