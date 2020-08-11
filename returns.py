#!/usr/local/bin/python3.8


stock_list = []
f = open('hdper.txt', 'r')
for line in f:
    stock_list.append(float(line)) 
print(len(stock_list))
counter = 0 
curtotal = 20000
for i in range(len(stock_list)):
    interest = (stock_list[counter]/100 * curtotal)
    curtotal = interest + curtotal 
    counter = counter +1
    print(f' year {counter} \t ${curtotal:,.2f}')
