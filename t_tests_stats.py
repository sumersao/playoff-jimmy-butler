import numpy as np
import pandas as pd
from scipy.stats import ttest_rel

adv_stats_reg = pd.read_csv('data/advanced_stats.csv')
adv_stats_playoffs = pd.read_csv('data/advanced_stats_playoffs.csv')

reg_stats_reg = pd.read_csv('data/regular_stats.csv')
reg_stats_playoffs = pd.read_csv('data/regular_stats_playoffs.csv')

# jimmy butler was on 2 teams in 2019 so there are 2 regular season rows. Drop the second one
adv_stats_reg = adv_stats_reg.drop(adv_stats_reg.index[(adv_stats_reg['Player'] == 'Jimmy Butler') & (adv_stats_reg['Year'] == 2019)].tolist()[1])
reg_stats_reg = reg_stats_reg.drop(reg_stats_reg.index[(reg_stats_reg['Player'] == 'Jimmy Butler') & (reg_stats_reg['Year'] == 2019)].tolist()[1:])

# only look at Jimmy's stats
jimmy_butler = adv_stats_reg.loc[adv_stats_reg['Player'] == 'Jimmy Butler']
jimmy_butler_playoffs = adv_stats_playoffs.loc[adv_stats_playoffs['Player'] == 'Jimmy Butler']

jimmy_butler = jimmy_butler.sort_values(by='Year')
jimmy_butler_playoffs = jimmy_butler_playoffs.sort_values(by='Year')

# drop the 4th row of the jimmy_butler dataframe
jimmy_butler = jimmy_butler.drop(jimmy_butler.index[3])

# copy the PTS column over from reg_stats_reg to adv_stats_reg but match the years
jimmy_butler = jimmy_butler.merge(reg_stats_reg[['Year', 'Player', 'PTS']], on=['Year', 'Player'])
jimmy_butler_playoffs = jimmy_butler_playoffs.merge(reg_stats_playoffs[['Year', 'Player', 'PTS']], on=['Year', 'Player'])

# Perform t-tests for each of the 4 stats and print out the results and each null hypothesis
# T-test for PTS
t_stat_pts, p_value_pts = ttest_rel(jimmy_butler['PTS'], jimmy_butler_playoffs['PTS'])
print("T-statistic value for PTS: ", t_stat_pts)  
print("P-Value for PTS: ", p_value_pts)

# T-test for BPM
t_stat_bpm, p_value_bpm = ttest_rel(jimmy_butler['BPM'], jimmy_butler_playoffs['BPM'])
print("T-statistic value for BPM: ", t_stat_bpm)  
print("P-Value for BPM: ", p_value_bpm)

# T-test for WS/48
t_stat_ws48, p_value_ws48 = ttest_rel(jimmy_butler['WS/48'], jimmy_butler_playoffs['WS/48'])
print("T-statistic value for WS/48: ", t_stat_ws48)  
print("P-Value for WS/48: ", p_value_ws48)


# now do the all star years
t_stat_pts, p_value_pts = ttest_rel(jimmy_butler['PTS'][3:], jimmy_butler_playoffs['PTS'][3:])
print("T-statistic value for PTS (All Star): ", t_stat_pts)  
print("P-Value for PTS (All Star): ", p_value_pts)

t_stat_bpm, p_value_bpm = ttest_rel(jimmy_butler['BPM'][3:], jimmy_butler_playoffs['BPM'][3:])
print("T-statistic value for BPM (All Star): ", t_stat_bpm)  
print("P-Value for BPM (All Star): ", p_value_bpm)

t_stat_ws48, p_value_ws48 = ttest_rel(jimmy_butler['WS/48'][3:], jimmy_butler_playoffs['WS/48'][3:])
print("T-statistic value for WS/48 (All Star): ", t_stat_ws48)  
print("P-Value for WS/48 (All Star): ", p_value_ws48)


# now do the miami heat years
t_stat_pts, p_value_pts = ttest_rel(jimmy_butler['PTS'][6:], jimmy_butler_playoffs['PTS'][6:])
print("T-statistic value for PTS (Heat): ", t_stat_pts)  
print("P-Value for PTS (Heat): ", p_value_pts)

t_stat_bpm, p_value_bpm = ttest_rel(jimmy_butler['BPM'][6:], jimmy_butler_playoffs['BPM'][6:])
print("T-statistic value for BPM (Heat): ", t_stat_bpm)  
print("P-Value for BPM (Heat): ", p_value_bpm)

t_stat_ws48, p_value_ws48 = ttest_rel(jimmy_butler['WS/48'][6:], jimmy_butler_playoffs['WS/48'][6:])
print("T-statistic value for WS/48 (Heat): ", t_stat_ws48)  
print("P-Value for WS/48 (Heat): ", p_value_ws48)
