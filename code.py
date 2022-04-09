import random
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import pandas as pd 

df = pd.read_csv('studentMarks.csv')
data = df['Math_score'].tolist()

mean = sum(data) / len(data)
std_deviation = statistics .stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation 
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation) 
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

fig = ff.create_distplot([data],["reading scores :"],show_hist=False)

fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode='lines',name="first standard deviation starts"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode='lines',name="first standard deviation end"))

fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode='lines',name="second standard deviation starts"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode='lines',name="second standard deviation end"))

thin_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end] 
thin_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end] 
thin_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end]

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode='lines',name="MEAN"))
fig.show()

#first_std_start, first_std_end = mean-std_dev, mean+std_dev
#list_between_1_std = [x for x in dice_result if x>first_std_start and x<first_std_end] first_std_percent= len(list_between_1_std)*100/len (dice_result)
print("mean is {}".format(mean))
print("median is {}".format(median))
print("mode is {}".format(mode))
print("std is {}".format(std_deviation))

print("{}% of data lies within our first standard deviation". format (len(thin_1_std_deviation)*100/len (data)))
print("{}% of data lies within our second standard deviation". format (len(thin_2_std_deviation)*100/len (data)))
print("{}% of data lies within our third standard deviation". format (len(thin_3_std_deviation)*100/len (data)))
