#!/usr/bin/env python3

import openpyxl
import pandas as pd
import bar_chart_race as bcr

file = "data/allscores.xlsx"
wb = openpyxl.load_workbook(file, read_only=True)

all_scores = {}

for ws in wb.worksheets:
  for row in ws.iter_rows():
    if row[0].value == "Player":
      continue
    if not row[0].value in all_scores:
      all_scores[row[0].value] = {}
      all_scores[row[0].value]['Day0'] = 0
    all_scores[row[0].value][ws.title] = row[1].value

df = pd.DataFrame(data=all_scores) 

#lol = bcr.load_dataset(df)
out = bcr.bar_chart_race(
  df=df,
  filename=None,
  writer="imagemagick",
  title="World Cup 2022",
  period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
  period_length=2000,
  steps_per_period=10,
  fixed_max=True,
  figsize=(7,6),
  fixed_order=True
)

print(out)



