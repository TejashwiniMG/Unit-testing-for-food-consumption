# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 19:57:16 2020

@author: SONY
"""
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dashboard

import plotly.graph_objects as go
import numpy as np
from plotly.offline import plot


box_c = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': None,
    'title': 'box-for-dashboard',
    'shareKey': None,
}

#a=''
#b=''
global flag
def check1(a,b):
    if (a=="tejashwini@gmail.com" and b=="switchon"):
            flag=1
            print("TEST PASSED( Logged In)")

            #if flag==1:
        #real time data
              # np.random.seed(1)

              #  N = 10
              #  random_x = np.linspace(1900, 2020, N)
              #  random_y0 = np.random.randn(N) 
              #  random_y1 = np.random.randn(N)+15
        

              #  fig = go.Figure()
                
              #  fig.add_trace(go.Scatter(x=random_x, y=random_y0,
              #      mode='lines+markers',
                 #   name='Vegeterian food '))
        
             #   fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                 #   mode='lines+markers',
                 #   name='Non-Vegeterian food'))
               # fig.update_layout(
                #    title="Food Consumption",
                 #   xaxis_title="Years(yrs)",
                 #   yaxis_title="Consumption",
                 #   )
                

              #  fig.show()
              #  plot(fig)
        #login to dashboard
               # my_dboard = dashboard.Dashboard()
              ##  my_dboard.insert(box_c)
               # my_dboard.get_preview()
              #  my_dboard.insert(box_c, 'left', 1, fill_percent=30)
              #  my_dboard.get_box(1)
              #  py.dashboard_ops.upload(my_dboard , 'Dashboard of consumption of food ')
            
               # dboard_names = my_dboard()
               # first_dboard = dashboard(my_dboard[0])
                 #  print(flag)
               # first_dboard.get_preview()
    else:
               print("TEST PASSED(Invalid credentials)")
               flag=0
              # print(flag)
    return(flag)
        
