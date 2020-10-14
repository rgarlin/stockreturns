#!/usr/local/bin/python3.8

## take a file of stock annual percent gains 
## and calculates the dollar gain with a start value 
## of 20,000 
## annual return formula annual = ((total return / initial investment)**(1/years)) -1


import argparse
parser = argparse.ArgumentParser(description='Input file names: file1.csv')
parser.add_argument('file1')
parser.add_argument('year')
args = parser.parse_args()

stock_list = []
f = open(args.file1, 'r')
for line in f:
    stock_list.append(float(line)) 
##stock_list.reverse()
print(stock_list)
stocklen = (len(stock_list))
counter = 0
year = int(args.year) 
curtotal = 20000
for i in range(len(stock_list)):
    interest = (stock_list[counter]/100 * curtotal)
    curtotal = interest + curtotal 
    counter = counter +1
    year = year +1
    annual_return = ((((int(curtotal) / 20000)**(1/counter)) -1) *100)
    print(f' year {year} \t ${curtotal:,.2f} \t\t {round(annual_return,2)}')
ave_annual_return = ((((int(curtotal) / 20000)**(1/stocklen)) -1) *100)
print("Annual return is %" + str(round(ave_annual_return,2)))
