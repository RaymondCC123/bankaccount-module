from tkinter import *
import pandas as pd
import datetime
from random import choice
from string import ascii_uppercase
import os

cwd = os.getcwd()
now = datetime.datetime.now()


def deposit():
    id_client = str(e1.get())
    amount = float(e2.get())
    try:
        df = pd.read_csv(cwd + "/" + id_client + ".csv", sep=';',
                         header=0)
        balance = float(df['balance'].iloc[-1])
    except:
        df = pd.DataFrame(columns=['id_client', 'date', 'operation_number', 'operation_type', 'amount', 'balance'])
        balance = float(0)

    dict1 = {'id_client': id_client, 'date': now,
             'operation_number': ''.join(choice(ascii_uppercase) for i in range(12)),
             'operation_type': 'deposit', 'amount': amount, 'balance': balance + amount}
    df = df.append(dict1, ignore_index=True)
    df.to_csv(cwd + "/" + id_client + ".csv", sep=';', index=False,
              mode='w')


def withdraw():
    id_client = str(e1.get())
    amount = float(e2.get())
    try:
        df = pd.read_csv(cwd + "/" + id_client + ".csv", sep=';',
                         header=0)
        balance = float(df['balance'].iloc[-1])
    except:
        df = pd.DataFrame(columns=['id_client', 'date', 'operation_number', 'operation_type', 'amount', 'balance'])
        balance = float(0)

    if balance < amount:
        print("\n Insufficient balance  ")
    else:
        balance -= amount
        dict1 = {'id_client': id_client, 'date': now,
                 'operation_number': ''.join(choice(ascii_uppercase) for i in range(12)),
                 'operation_type': 'withdraw', 'amount': amount, 'balance': balance}
        df = df.append(dict1, ignore_index=True)
        df.to_csv(cwd + "/" + id_client + ".csv", sep=';',
                  index=False,
                  mode='w')


def display():
    id_client = str(e1.get())
    try:
        df = pd.read_csv(cwd + "/" + id_client + ".csv", sep=';',
                         header=0)
        from tabulate import tabulate
        print(tabulate(df, headers='keys', tablefmt='psql'))
    except:
        print("Client doesn't exist")


master = Tk()
Label(master, text="id client").grid(row=0)
Label(master, text="amount").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Deposit', command=deposit).grid(row=4, column=0, sticky=W, pady=4)
Button(master, text='Withdraw', command=withdraw).grid(row=4, column=1, sticky=W, pady=4)
Button(master, text='Display historic', command=display).grid(row=5, column=0, sticky=W, pady=4)

mainloop()
