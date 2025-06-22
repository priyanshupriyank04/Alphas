event = volume/adv20 > 1;
alpha = - ts_delta(close, 3);
exit_condition = - 1;
trade_when(event, alpha, exit_condition) 
