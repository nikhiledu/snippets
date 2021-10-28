#!/usr/bin/python
import sys

# Returns 6 (buying for $5 and selling for $11)
def get_max_profit(stock_prices_yesterday):
  min_value = 0
  min_index = 0
  max_value = 0
  max_index = 0

  for index, value in enumerate(stock_prices_yesterday):
    if index == 0:
      min_value = value
      max_value = value

    if value <= min_value:
      if max_index >= index:
        min_index = index
        min_value = value
    else:
      if value >= max_value:
        if index >= min_index:
          max_index = index
          max_value = value

  if max_index >= min_index:
    print(min_value)
    print(max_value)
    print(max_value-min_value)

stock_prices_yesterday = [10, 17, 13, 8, 11, 9]

get_max_profit(stock_prices_yesterday)
