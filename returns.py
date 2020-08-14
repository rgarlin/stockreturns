#!/usr/local/bin/python3.8

## take a file of stock annual percent gains 
## and calculates the dollar gain with a start value 
## of 20,000 
import argparse
parser = argparse.ArgumentParser(description='Input file names: file1.csv')
parser.add_argument('file1')

args = parser.parse_args()

stock_list = []
f = open(args.file1, 'r')
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
