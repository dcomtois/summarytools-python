# A Python implementation of the summarytools R package

This is going to be a slow developping project because 1) I'm a bit rusty in Python and 2) I don't have much free time. So if you'd like to contribute by all means do!

To see what summarytools is all about, see [summarytools: An *R* Package For Descriptive Statistics](https://github.com/dcomtois/summarytools)

### Frequency tables with freq

```
import pandas as pd
import numpy as np
tobacco = pd.read_csv("data/tobacco.csv", encoding='ansi')

freq(tobacco.age_gr)

# 
#          Freq    % Valid    % Valid Cum.    % Total    % Total Cum.
# -----  ------  ---------  --------------  ---------  --------------
# 18-34     258      26.46           26.46      25.80           25.80
# 35-50     241      24.72           51.18      24.10           49.90
# 51-70     317      32.51           83.69      31.70           81.60
# 71 +      159      16.31          100.00      15.90           97.50
# NaN        25                                  2.50          100.00
# Total    1000     100.00          100.00     100.00          100.00

freq(tobacco.age_gr, totals = False)

#          Freq    % Valid    % Valid Cum.    % Total    % Total Cum.
# -----  ------  ---------  --------------  ---------  --------------
# 18-34     258      26.46           26.46      25.80           25.80
# 35-50     241      24.72           51.18      24.10           49.90
# 51-70     317      32.51           83.69      31.70           81.60
# 71 +      159      16.31          100.00      15.90           97.50
# NaN        25                                  2.50          100.00

ft = freq(tobacco.gender, format = 'fancy_grid')
ft.print(digits=1)

# ╒═══════╤════════╤═══════════╤════════════════╤═══════════╤════════════════╕
# │       │   Freq │   % Valid │   % Valid Cum. │   % Total │   % Total Cum. │
# ╞═══════╪════════╪═══════════╪════════════════╪═══════════╪════════════════╡
# │ F     │    489 │      50.0 │           50.0 │      48.9 │           48.9 │
# ├───────┼────────┼───────────┼────────────────┼───────────┼────────────────┤
# │ M     │    489 │      50.0 │          100.0 │      48.9 │           97.8 │
# ├───────┼────────┼───────────┼────────────────┼───────────┼────────────────┤
# │ NaN   │     22 │           │                │       2.2 │          100.0 │
# ├───────┼────────┼───────────┼────────────────┼───────────┼────────────────┤
# │ Total │   1000 │     100.0 │          100.0 │     100.0 │          100.0 │
# ╘═══════╧════════╧═══════════╧════════════════╧═══════════╧════════════════╛

ft.print(nans=False)

# ╒═══════╤════════╤═══════════╤════════════════╕
# │       │   Freq │   % Valid │   % Valid Cum. │
# ╞═══════╪════════╪═══════════╪════════════════╡
# │ F     │    489 │     50.00 │          50.00 │
# ├───────┼────────┼───────────┼────────────────┤
# │ M     │    489 │     50.00 │         100.00 │
# ├───────┼────────┼───────────┼────────────────┤
# │ Total │    978 │    100.00 │         100.00 │
# ╘═══════╧════════╧═══════════╧════════════════╛
```

### Markdown compatible? You bet!

### Markdown compatible? You bet!

`ft.print(format = 'pipe')`

|       |   Freq |   % Valid |   % Valid Cum. |   % Total |   % Total Cum. |
|:------|-------:|----------:|---------------:|----------:|---------------:|
| F     |    489 |     50.00 |          50.00 |     48.90 |          48.90 |
| M     |    489 |     50.00 |         100.00 |     48.90 |          97.80 |
| NaN   |     22 |           |                |      2.20 |         100.00 |
| Total |    978 |    100.00 |         100.00 |    100.00 |         100.00 |


