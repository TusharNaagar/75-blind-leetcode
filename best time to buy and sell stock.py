def best_time_to_buy_and_sell_stock(price):
  min_price=float('inf)
  max_profit=0

  for current_price in range(price):
    if min_price > current_price:
      min_price=current_price
    else:
      max_proft=max(max_proft,current_price-min_price)
  return max_profit
