event = rank(ts_sum(vec_avg(nws12_afterhsz_sl),252)) > 0.5;
alpha_1 = 1;
alpha_2 = rank(-ts_delta(close,2));
if_else(event, alpha_1, alpha_2)
