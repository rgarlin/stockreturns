#!/usr/local/bin/python3.8
import yfinance as yf
import pandas as pd
import openpyxl
import os
from yahoo_fin import stock_info as si

class Stock:
    
    def __init__(self, ticker, shares, basis_per_share):
        self.ticker = ticker
        self.shares = shares
        self.basis_per_share = basis_per_share
          
    def total_cost(self):
        return(round(self.shares * self.basis_per_share, 2))

    def current_value(self):
        current_price = si.get_live_price(self.ticker)
        total_gain = self.shares * current_price
        return(round(total_gain,2))
    
    def current(self):
        current_price = si.get_live_price(self.ticker)
        return(round(current_price, 2))

    def current_value(self):
        current_price = si.get_live_price(self.ticker)
        return(round(current_price * self.shares, 2))

    def per_gain(self):
        current_price = si.get_live_price(self.ticker)
        return((round(((current_price - self.basis_per_share)/self.basis_per_share)*100, 2)))

    def dollar_gain(self):
        current_price = si.get_live_price(self.ticker)
        return(round(current_price*self.shares - self.shares * self.basis_per_share,2))

def values(lst, name):
    lst.append(name.ticker)
    lst.append(name.shares)
    lst.append(name.basis_per_share)
    lst.append(name.total_cost())
    lst.append(name.current())
    lst.append(name.current_value())
    lst.append(name.per_gain())
    lst.append(name.dollar_gain())    
    return(lst)

amznlst = []
msftlst = []
applelst =[]
msftbglst = []
googllst = []
cmglst= []
vlst = []
nvdalst = []
atvilst = []
shwlst = []


amazon = Stock('amzn', 1,2760.69)
microsoft = Stock('msft', 15,198.3)
apple = Stock('aapl', 66, 152.20)
msftbg = Stock('msft', 102, 97.70)
googl = Stock('googl', 10, 1024.02)
cmg = Stock('cmg', 35,757.6)
visa = Stock('v',164,183.61)
nvda = Stock('nvda',110,358.20)
atvi = Stock('atvi',465,77.21)
shw = Stock('shw',65,621.20)

values(amznlst,amazon)
values(msftlst,microsoft)


values(applelst,apple)
values(msftbglst,msftbg)
values(googllst,googl)
values(cmglst,cmg)
values(vlst,visa)
values(nvdalst,nvda)
values(atvilst,atvi)
values(shwlst,shw)


print(amznlst)
print(msftlst)
print(applelst)
print(msftbglst)
print(googllst)
print(cmglst)
print(vlst)
print(nvdalst)
print(atvilst)
print(shwlst)
two_sp = "<td>&emsp;</td> <td>&emsp;</td>" 

with open("index.html", "w") as text_file:
    text_file.write('Charlie\n')
    text_file.write('<br>\n')
    text_file.write('=========================================================\n')
    text_file.write('<table>\n')
    text_file.write('<tr>\n')
    text_file.write('<td>Stock</td> {} <td>Shares </td>{} <td>Cost Per Share </td>{} <td>Cost Basis</td> {}<td>Current Share Price</td></td> {}<td>Current Value</td> {}<td> Per Gain</td> {} <td>Dollar Gain</td>\n'.format(two_sp,two_sp,two_sp,two_sp,two_sp,two_sp,two_sp))
    text_file.write('</tr>\n')
    text_file.write('<tr>\n')
    text_file.write('<td>{}</td> {} <td>{}</td> {} <td>${:,.2f}</td> {} <td>${:,.2f}</td>{}<td>${:,.2f}</td>{}<td>${:,.2f}</td>{}<td>%{}</td>{}<td>${:,.2f}</td>\n'.format(amznlst[0],two_sp,amznlst[1],two_sp,amznlst[2],two_sp,amznlst[3],two_sp,amznlst[4],two_sp,amznlst[5],two_sp,amznlst[6],two_sp,amznlst[7]))
    text_file.write('</tr>\n')
    text_file.write('<table>\n')
    text_file.write('</br>\n')
    text_file.write('<br>\n')
    text_file.write('Tyler\n')
    text_file.write('<br>\n')
    text_file.write('=========================================================\n')
    text_file.write('<table>\n')
    text_file.write('<tr>\n')
    text_file.write('<td>Stock</td> {} <td>Shares </td>{} <td>Cost Per Share </td>{} <td>Cost Basis</td> {}<td>Current Share Price</td></td> {}<td>Current Value</td> {}<td> Per Gain</td> {} <td>Dollar Gain</td>\n'.format(two_sp,two_sp,two_sp,two_sp,two_sp,two_sp,two_sp))
    text_file.write('</tr>\n')
    text_file.write('<tr>\n')
    text_file.write('<td>{}</td> {} <td>{}</td> {} <td>${:,.2f}</td> {} <td>${:,.2f}</td>{}<td>${:,.2f}</td>{}<td>${:,.2f}</td>{}<td>%{}</td>{}<td>${:,.2f}</td>\n'.format(msftlst[0],two_sp,msftlst[1],two_sp,msftlst[2],two_sp,msftlst[3],two_sp,msftlst[4],two_sp,msftlst[5],two_sp,msftlst[6],two_sp,msftlst[7]))
    text_file.write('</tr>\n')
    text_file.write('<table>\n')
    text_file.write('</br>\n')
    text_file.write('<br>\n')
    text_file.write('Bob and Lisa\n')
    text_file.write('<br>\n')
    text_file.write('=========================================================\n')
    text_file.write('<table>\n')
    text_file.write('<tr>\n')
    text_file.write('<td>Stock</td> {} <td>Shares </td>{} <td>Cost Per Share </td>{} <td>Cost Basis</td> {}<td>Current Share Price</td></td> {}<td>Current Value</td> {}<td> Per Gain</td> {} <td>Dollar Gain</td>\n'.format(two_sp,two_sp,two_sp,two_sp,two_sp,two_sp,two_sp))
    text_file.write('</tr>\n')
    text_file.write('<tr>\n')
    text_file.write('<td>{}</td> {} <td>{}</td> {} <td>${:,.2f}</td> {} <td>${:,.2f}</td>{}<td>${:,.2f}</td>{}<td>${:,.2f}</td>{}<td>%{}</td>{}<td>${:,.2f}</td>\n'.format(applelst[0],two_sp,applelst[1],two_sp,applelst[2],two_sp,applelst[3],two_sp,applelst[4],two_sp,applelst[5],two_sp,applelst[6],two_sp,applelst[7]))
    text_file.write('</tr>\n')
    text_file.write('<tr>\n')
    text_file.write('<td>{}</td> {} <td>{}</td> {} <td>${:,.2f}</td> {} <td>${:,.2f}</td>{}<td>${:,.2f}</td>{}<td>${:,.2f}</td>{}<td>%{}</td>{}<td>${:,.2f}</td>\n'.format(msftbglst[0],two_sp,msftbglst[1],two_sp,msftbglst[2],two_sp,msftbglst[3],two_sp,msftbglst[4],two_sp,msftbglst[5],two_sp,msftbglst[6],two_sp,msftbglst[7]))
    text_file.write('</tr>\n')
    text_file.write('<tr>\n')
    text_file.write('<td>{}</td> {} <td>{}</td> {} <td>${:,.2f}</td> {} <td>${:,.2f}</td>{}<td>${:,.2f}</td>{}<td>${:,.2f}</td>{}<td>%{}</td>{}<td>${:,.2f}</td>\n'.format(googllst[0],two_sp,googllst[1],two_sp,googllst[2],two_sp,googllst[3],two_sp,googllst[4],two_sp,googllst[5],two_sp,googllst[6],two_sp,googllst[7]))
    text_file.write('</tr>\n')
    text_file.write('</table>\n')
    text_file.write('<br>\n')


    ##print("<td> Stock </td>" two_ <td> Shares </td> <td>&emsp;</td> <td>&emsp;</td> <td> Cost per Share </td><td>&emsp;</td> <td>&emsp;</td> <td>Total Value</td>",file=text_file)
    ##print('</tr>', file=text_file)
    ##print('<tr>', file=text_file)
    ##print("<td> Amazon </td>", file=text_file)
    ##print("<td>&emsp;</td>", file=text_file)
    ##print("<td>&emsp;</td>", file=text_file)
    ##print("<td> ${} </td> <td>&emsp;</td> <td>&emsp;</td> <td> {}% </td>".format(round(amzn_cur_gain, 2),round(amzn_per_gain, 2)), file=text_file)
    ##print('<td> &emsp;</td> <td>&emsp;</td> <td>${:,.2f} </td>'.format(amzn_tot_val), file=text_file)
    ##print('</tr>', file=text_file)
    ##print('</table>', file=text_file)
    ##print('<br>', file=text_file)
    ##print('<br>', file=text_file)
tickerlst = [apple, msftbg, googl]

