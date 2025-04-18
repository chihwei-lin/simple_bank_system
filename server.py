#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
 Script Name: account.py
 Author:      Calvin C W Lin <chihweilin@163.com>
 Version:     v1.0.0
 Description: handle request from clients
 Created:     2025-04-16
 Last Update: 2025-04-18
 Usage:       python server.py 
 Notes:       
===============================================================================
"""

import time
import socket
import threading
from account import Account

# Loading account information
accounts = Account.load_from_csv()

def handle_client(client_socket):
    while True:
        request = client_socket.recv(1024).decode('utf-8')
        if not request:
            break

        print(f"{time.asctime()} {request}")
        
        parts = request.split()
        response = "Invalid command"
        
        try:
            if parts[0] == 'NEW':
                name, balance = parts[1], float(parts[2])

                # replace comma in name
                name = name.replace(',', ' ')

                print(f"{time.asctime()} Trying to create new account {name}")

                isaccExist = next((acc for acc in accounts if acc.name == name), False)
                if isaccExist:
                    response = f"Account {name} already exists."
                else:
                    newacct = Account(name, balance)
                    accounts.append(newacct)
                    response = f"Account {name} is created successfully."
                        
            elif parts[0] == 'DEPOSIT':
                name, amount = parts[1], float(parts[2])
                
                # replace comma in name
                name = name.replace(',', ' ')

                print(f"{time.asctime()} Trying to deposit {amount} from {name}")

                for acc in accounts:
                    if acc.name == name:
                        acc.deposit(amount)
                        response = f"Deposited {amount} to {name}. New balance: {acc.balance}"
                        break
            
            elif parts[0] == 'WITHDRAW':
                name, amount = parts[1], float(parts[2])

                # replace comma in name
                name = name.replace(',', ' ')

                print(f"{time.asctime()} Trying to withdraw {amount} from {name}")

                for acc in accounts:
                    if acc.name == name:
                        if acc.withdraw(amount):
                            response = f"Withdrew {amount} from {name}. New balance: {acc.balance}"
                        else:
                            response = f"Insufficient funds for {name}."
                        break
            
            elif parts[0] == 'TRANSFER':
                from_name, to_name, amount = parts[1], parts[2], float(parts[3])
                from_name, to_name = from_name.replace(',', ' '), to_name.replace(',', ' ')

                print(f"{time.asctime()} Trying to transfer {amount} from {from_name} to {to_name}")

                from_account = next((acc for acc in accounts if acc.name == from_name), None)
                to_account = next((acc for acc in accounts if acc.name == to_name), None)

                if from_account and to_account:
                    if from_account.transfer(to_account, amount):
                        response = f"Transferred {amount} from {from_name} to {to_name}. New balances: {from_name}: {from_account.balance}, {to_name}: {to_account.balance}"
                    else:
                        response = f"Transfer failed due to insufficient funds or invalid amount."
                else:
                    response = f"Transfer failed due to invalid account."
                
            
            elif parts[0] == 'EXIT':
                break
            
            else:
                response = "Unknown command"
                
        except Exception as e:
            response = str(e)
        
        print(f"{time.asctime()} {response}")
        client_socket.send(response.encode('utf-8'))
    
    # persist account status
    Account.save_to_csv(accounts)
    client_socket.close()

def start_server():
    HOST='localhost'
    PORT=9999
    SEVER_LISTEN_TIME=5

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(SEVER_LISTEN_TIME)
    print(f"Server listening on port {PORT}...")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()