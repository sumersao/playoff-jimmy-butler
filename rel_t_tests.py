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

reg_stats_reg['PTS_Rank'] = reg_stats_reg.groupby('Year')['PTS'].rank(ascending=False)
reg_stats_playoffs['PTS_Rank'] = reg_stats_playoffs.groupby('Year')['PTS'].rank(ascending=False)

adv_stats_reg['BPM_Rank'] = adv_stats_reg.groupby('Year')['BPM'].rank(ascending=False)
adv_stats_playoffs['BPM_Rank'] = adv_stats_playoffs.groupby('Year')['BPM'].rank(ascending=False)

# win shares per 48 minutes
adv_stats_reg['WS/48_Rank'] = adv_stats_reg.groupby('Year')['WS/48'].rank(ascending=False)
adv_stats_playoffs['WS/48_Rank'] = adv_stats_playoffs.groupby('Year')['WS/48'].rank(ascending=False)

# VORP
adv_stats_reg['VORP_Rank'] = adv_stats_reg.groupby('Year')['VORP'].rank(ascending=False)
adv_stats_playoffs['VORP_Rank'] = adv_stats_playoffs.groupby('Year')['VORP'].rank(ascending=False)


# copy the PTS_Rank column over from reg_stats_reg to adv_stats_reg but match the years
adv_stats_reg = adv_stats_reg.merge(reg_stats_reg[['Year', 'Player', 'PTS_Rank']], on=['Year', 'Player'])
adv_stats_playoffs = adv_stats_playoffs.merge(reg_stats_playoffs[['Year', 'Player', 'PTS_Rank']], on=['Year', 'Player'])

# get the rows for jimmy butler
jimmy_butler = adv_stats_reg.loc[adv_stats_reg['Player'] == 'Jimmy Butler']
jimmy_butler_playoffs = adv_stats_playoffs.loc[adv_stats_playoffs['Player'] == 'Jimmy Butler']

jimmy_butler = jimmy_butler.sort_values(by='Year')
jimmy_butler_playoffs = jimmy_butler_playoffs.sort_values(by='Year')

# drop the 4th row of the jimmy_butler dataframe
jimmy_butler = jimmy_butler.drop(jimmy_butler.index[3])

# Perform t-tests for each of the 4 stats and print out the results and each null hypothesis
# T-test for PTS_Rank
t_stat_pts, p_value_pts = ttest_rel(jimmy_butler['PTS_Rank'], jimmy_butler_playoffs['PTS_Rank'])
print("T-statistic value for PTS_Rank: ", t_stat_pts)  
print("P-Value for PTS_Rank: ", p_value_pts)

# T-test for BPM_Rank
t_stat_bpm, p_value_bpm = ttest_rel(jimmy_butler['BPM_Rank'], jimmy_butler_playoffs['BPM_Rank'])
print("T-statistic value for BPM_Rank: ", t_stat_bpm)  
print("P-Value for BPM_Rank: ", p_value_bpm)

# T-test for WS/48_Rank
t_stat_ws48, p_value_ws48 = ttest_rel(jimmy_butler['WS/48_Rank'], jimmy_butler_playoffs['WS/48_Rank'])
print("T-statistic value for WS/48_Rank: ", t_stat_ws48)  
print("P-Value for WS/48_Rank: ", p_value_ws48)

# T-test for VORP_Rank
t_stat_vorp, p_value_vorp = ttest_rel(jimmy_butler['VORP_Rank'], jimmy_butler_playoffs['VORP_Rank'])
print("T-statistic value for VORP_Rank: ", t_stat_vorp)  
print("P-Value for VORP_Rank: ", p_value_vorp)

# now do the all star years
t_stat_pts, p_value_pts = ttest_rel(jimmy_butler['PTS_Rank'][3:], jimmy_butler_playoffs['PTS_Rank'][3:])
print("T-statistic value for PTS_Rank (All Star): ", t_stat_pts)  
print("P-Value for PTS_Rank (All Star): ", p_value_pts)

t_stat_bpm, p_value_bpm = ttest_rel(jimmy_butler['BPM_Rank'][3:], jimmy_butler_playoffs['BPM_Rank'][3:])
print("T-statistic value for BPM_Rank (All Star): ", t_stat_bpm)  
print("P-Value for BPM_Rank (All Star): ", p_value_bpm)

t_stat_ws48, p_value_ws48 = ttest_rel(jimmy_butler['WS/48_Rank'][3:], jimmy_butler_playoffs['WS/48_Rank'][3:])
print("T-statistic value for WS/48_Rank (All Star): ", t_stat_ws48)  
print("P-Value for WS/48_Rank (All Star): ", p_value_ws48)

t_stat_vorp, p_value_vorp = ttest_rel(jimmy_butler['VORP_Rank'][3:], jimmy_butler_playoffs['VORP_Rank'][3:])
print("T-statistic value for VORP_Rank (All Star): ", t_stat_vorp)
print("P-Value for VORP_Rank (All Star): ", p_value_vorp)

# now do the miami heat years
t_stat_pts, p_value_pts = ttest_rel(jimmy_butler['PTS_Rank'][6:], jimmy_butler_playoffs['PTS_Rank'][6:])
print("T-statistic value for PTS_Rank (Heat): ", t_stat_pts)  
print("P-Value for PTS_Rank (Heat): ", p_value_pts)

t_stat_bpm, p_value_bpm = ttest_rel(jimmy_butler['BPM_Rank'][6:], jimmy_butler_playoffs['BPM_Rank'][6:])
print("T-statistic value for BPM_Rank (Heat): ", t_stat_bpm)  
print("P-Value for BPM_Rank (Heat): ", p_value_bpm)

t_stat_ws48, p_value_ws48 = ttest_rel(jimmy_butler['WS/48_Rank'][6:], jimmy_butler_playoffs['WS/48_Rank'][6:])
print("T-statistic value for WS/48_Rank (Heat): ", t_stat_ws48)  
print("P-Value for WS/48_Rank (Heat): ", p_value_ws48)

t_stat_vorp, p_value_vorp = ttest_rel(jimmy_butler['VORP_Rank'][6:], jimmy_butler_playoffs['VORP_Rank'][6:])
print("T-statistic value for VORP_Rank (Heat): ", t_stat_vorp)
print("P-Value for VORP_Rank (Heat): ", p_value_vorp)
