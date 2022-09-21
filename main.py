def to_cumulative(stream: list):
  all_list = []
  # sort the list according to timestamp
  for i in stream:
    this_list = i.split(",")
    all_list.append(this_list)
  all_list.sort(key = lambda x:(x[0], x[1]))

  output = []
  time = all_list[0][0]
  ticker_set = {}

  for i in all_list:
    this_time = i[0]
    # if the timestamp is new, print cumulative quantity and cumulative notional for each ticker up till the timestamp
    if this_time != time:
      this_output = time
      for ticker in sorted(ticker_set.keys()):
        this_output += "," + ticker + "," + str(ticker_set[ticker][0]) + "," + str(ticker_set[ticker][1])
      output.append(this_output)
      # update timestamp
      time = this_time

    # update cumulative quantity and cumulative notional
    quantity = int(i[2])
    price = float(i[3])
    if i[1] not in ticker_set.keys():
      ticker_set[i[1]] = [quantity, quantity * price]
    else:
      ticker_set[i[1]][0] += quantity
      ticker_set[i[1]][1] += quantity * price

  # print cumulatvie values at final timestamp
  this_output = time
  for ticker in sorted(ticker_set.keys()):
    this_output += "," + ticker + "," + str(ticker_set[ticker][0]) + "," + str(ticker_set[ticker][1])
  output.append(this_output)

  return output


def to_cumulative_delayed(stream: list, quantity_block: int):
  all_list = []
  # sort the list according to timestamp
  for i in stream:
    this_list = i.split(",")
    all_list.append(this_list)
  all_list.sort(key = lambda x:(x[0], x[1]))

  output = []
  ticker_set = {}

  for i in all_list:
    time = i[0]
    quantity = int(i[2])
    price = float(i[3])
    new_quantity = quantity
    # when the ticker does not appear before
    if i[1] not in ticker_set.keys():
      # print cumulatvie values every multiple of quantity_block
      while new_quantity >= quantity_block:
        output.append(time + "," + i[1] + "," + str(quantity_block) + "," + str(quantity_block * price))
        new_quantity -= quantity_block
      # update cumulative values, including leftover quantity
      ticker_set[i[1]] = [quantity, quantity * price]

    # when ticker appears before
    else:
      # find the required quantity for the ticker to reach next multiple of quantity_block
      difference = quantity_block - ticker_set[i[1]][0]%quantity_block
      # fill the required quantity, and print cumulative values
      if new_quantity >= difference and difference != 0:
        ticker_set[i[1]][0] += difference
        ticker_set[i[1]][1] += difference * price
        output.append(time + "," + i[1] + "," + str(ticker_set[i[1]][0]) + "," + str(ticker_set[i[1]][1]))
        new_quantity -= difference
      while new_quantity >= quantity_block:
        ticker_set[i[1]][0] += quantity_block
        ticker_set[i[1]][1] += quantity_block * price
        output.append(time + "," + i[1] + "," + str(ticker_set[i[1]][0]) + "," + str(ticker_set[i[1]][1]))
        new_quantity -= quantity_block
      # update cumulative values with leftover quantity
      ticker_set[i[1]][0] += new_quantity
      ticker_set[i[1]][1] += new_quantity * price

  return output