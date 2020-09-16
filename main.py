from tkinter import *
from functools import partial

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

a="a"
b="b"
def login(username, password):
        global a
        global b
        a=username.get()
        b=password.get()
        #return

flag=0
tkWindow = Tk()  
tkWindow.geometry('400x100')  
tkWindow.title('Login information')


label_name = Label(tkWindow, text="E-MAIL")
label_name.grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

password_name = Label(tkWindow,text="PASSWORD")
password_name.grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  


login = partial(login, username, password)
loginButton = Button(tkWindow, text="LOGIN", command=login).grid(row=6, column=1)  

tkWindow.mainloop()
print(a)
print(b)

# Check for credentials

if (a=="tejashwini@gmail.com" and b=="switchon"):
        flag=1
print(flag)

if flag==1:
        #real time data
        np.random.seed(1)

        N = 10
        random_x = np.linspace(1900, 2020, N)
        random_y0 = np.random.randn(N) 
        random_y1 = np.random.randn(N)+15
        

        fig = go.Figure()
      
        fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines+markers',
                    name='Vegeterian food '))
        
        fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='Non-Vegeterian food'))
        fig.update_layout(
           title="Food Consumption",
           xaxis_title="Years(yrs)",
           yaxis_title="Consumption",
          )
        

        fig.show()
        plot(fig)
        #login to dashboard
        my_dboard = dashboard.Dashboard()
        my_dboard.insert(box_c)
        my_dboard.get_preview()
        my_dboard.insert(box_c, 'left', 1, fill_percent=30)
        my_dboard.get_box(1)
        py.dashboard_ops.upload(my_dboard , 'Dashboard of consumption of food ')

        dboard_names = my_dboard()
        first_dboard = dashboard(my_dboard[0])
 
        first_dboard.get_preview()
   
        
else:
        print("Invalid credentials")
        
