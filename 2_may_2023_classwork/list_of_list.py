chart = [['dele', 300, 1, 300, 80884443],
         ['sultan', 200, 2, 400, 9044444],
         ['esther', 50, 5, 2500, 9064747],
         ['sza', 500,  2, 1000, 903494040]]
chart[0][0] = 'mariam'
chart[1][0] = 'daniel'
chart[2][0] = 'summer'
chart[3][0] = 'chris'
print(chart)
chart[0][4] = 90440985
add = ['mary', 373, 84, 990990988]
chart.append(add)
print(chart)
adds = ['mary', 373, 84, 86, 990990988]
chart.insert(0, add)
print(chart)
