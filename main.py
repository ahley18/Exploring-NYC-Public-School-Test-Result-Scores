# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
print(schools.columns)
print('\n')

# Start coding here...
# Add as many cells as you like...

#Which NYC schools have the best math results?
best_math_schools = schools[schools['average_math']>(800*.8)][['school_name','average_math']].sort_values('average_math', ascending = False)
print(best_math_schools)
print('\n')

#What are the top 10 performing schools based on the combined SAT scores?
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['school_name', 'total_SAT']].sort_values('total_SAT', ascending = False).head(10)
print(top_10_schools)
print('\n')

#Which single borough has the largest standard deviation in the combined SAT score?
borough = schools.groupby('borough')['total_SAT'].agg(['count', 'mean','std'])
largest_std_dev = borough[borough['std'] == borough['std'].max()].rename(columns = {'count':'num_schools', 'mean':'average_SAT', 'std':'std_SAT'}).round(2)
print(largest_std_dev)
