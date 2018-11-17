# A Python implementation of the summarytools R package

This is going to be a slow developping project because 1) I'm a bit rusty in Python and 2) I don't have much free time. So if you'd like to contribute by all means do!

To see what summarytools is all about, see [summarytools: An *R* Package For Descriptive Statistics](https://github.com/dcomtois/summarytools)

### How to install

Just copy the `summarytools.py` file in your `Python/Lib/site-packages` folder.

## Frequency tables with freq

First, a quick setup

```python
import pandas as pd
from summarytools import freq
```

Import a sample dataset:

```python
link = "https://raw.githubusercontent.com/dcomtois/summarytools-python/master/data/tobacco.csv"
tobacco = pd.read_csv(link)
```

### Bare-bones example

```python
freq(tobacco.age_gr)
```
```
         Freq    % Valid    % Valid Cum.    % Total    % Total Cum.
-----  ------  ---------  --------------  ---------  --------------
18-34     258      26.46           26.46      25.80           25.80
35-50     241      24.72           51.18      24.10           49.90
51-70     317      32.51           83.69      31.70           81.60
71 +      159      16.31          100.00      15.90           97.50
NaN        25                                  2.50          100.00
Total    1000     100.00          100.00     100.00          100.00
```

The returned object is a pandas Dataframe, and it is displayed using the [tabulate](https://pypi.org/project/tabulate/) library. 

### Markdown formatting

When switching format to 'pipe', we get pretty formatted markdown tables where mardown is supported, such as here on GitHub.

```python
freq(tobacco.gender, format = 'pipe')
```
```
|       |   Freq |   % Valid |   % Valid Cum. |   % Total |   % Total Cum. |
|:------|-------:|----------:|---------------:|----------:|---------------:|
| F     |    489 |     50.00 |          50.00 |     48.90 |          48.90 |
| M     |    489 |     50.00 |         100.00 |     48.90 |          97.80 |
| NaN   |     22 |           |                |      2.20 |         100.00 |
| Total |    978 |    100.00 |         100.00 |    100.00 |         100.00 |
```

### Fancier console display

When working in a regular Python console or in IPython, the 'fancy_grid' format from tabular produces good results:

```python
freq(tobacco.gender, format = 'fancy_grid')
```
```
╒═══════╤════════╤═══════════╤════════════════╤═══════════╤════════════════╕
│       │   Freq │   % Valid │   % Valid Cum. │   % Total │   % Total Cum. │
╞═══════╪════════╪═══════════╪════════════════╪═══════════╪════════════════╡
│ F     │    489 │     50.00 │          50.00 │     48.90 │          48.90 │
├───────┼────────┼───────────┼────────────────┼───────────┼────────────────┤
│ M     │    489 │     50.00 │         100.00 │     48.90 │          97.80 │
├───────┼────────┼───────────┼────────────────┼───────────┼────────────────┤
│ NaN   │     22 │           │                │      2.20 │         100.00 │
├───────┼────────┼───────────┼────────────────┼───────────┼────────────────┤
│ Total │   1000 │    100.00 │         100.00 │    100.00 │         100.00 │
╘═══════╧════════╧═══════════╧════════════════╧═══════════╧════════════════╛
```

## Parameters

For now, only a few parameters are implemented. We'll store a frequency table to show how we can tweak the display after its creation, using the print() method.

```python
ft = freq(tobacco.gender, format = 'pipe')
```

#### Omit the Total row
```python
ft.print(totals=False)
```
|     |   Freq |   % Valid |   % Valid Cum. |   % Total |   % Total Cum. |
|:----|-------:|----------:|---------------:|----------:|---------------:|
| F   |    489 |     50.00 |          50.00 |     48.90 |          48.90 |
| M   |    489 |     50.00 |         100.00 |     48.90 |          97.80 |
| NaN |     22 |           |                |      2.20 |         100.00 |

#### Omit missing data reporting
```python
ft.print(nans=False)
```
|       |   Freq |   % Valid |   % Valid Cum. |
|:------|-------:|----------:|---------------:|
| F     |    489 |     50.00 |          50.00 |
| M     |    489 |     50.00 |         100.00 |
| Total |    978 |    100.00 |         100.00 |

#### Control number of decimals to show
```python
ft.print(digits=1)
```
|       |   Freq |   % Valid |   % Valid Cum. |   % Total |   % Total Cum. |
|:------|-------:|----------:|---------------:|----------:|---------------:|
| F     |    489 |      50.0 |           50.0 |      48.9 |           48.9 |
| M     |    489 |      50.0 |          100.0 |      48.9 |           97.8 |
| NaN   |     22 |           |                |       2.2 |          100.0 |
| Total |    978 |     100.0 |          100.0 |     100.0 |          100.0 |

#### More to come... In the meantime feel free to chip in and contribute!
