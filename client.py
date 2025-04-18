#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
===============================================================================
 Script Name: account.py
 Author:      Calvin C W Lin <chihweilin@163.com>
 Version:     v1.0.0
 Description: sending input request to server
 Created:     2025-04-16
 Last Update: 2025-04-18
 Usage:       python client.py 
 Notes:       
===============================================================================
"""

import socket

def main():
    HOST='127.0.0.1'
    PORT=9999

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a TCP Socket instance
        client.connect((HOST, PORT))     # define send message to localhost port 9999

        print("Welcome to Bank System (BS)!")

        # looping to detect user's activity
        while True:
            commandInstructionStr = """
Please enter a command, format can be referred as below
Create a new bank account: NEW <name> <balance>
Deposit money to an account: DEPOSIT <name> <amount> 
Withdraw cash from an account: WITHDRAW <name> <amount>
Transfer money to another account: TRANSFER <from_name> <to_name> <amount>
Enter: """

            command = input(commandInstructionStr)
            if command.upper() == 'EXIT':
                break
            
            client.send(command.encode('utf-8'))
            response = client.recv(1024).decode('utf-8')
            print(response)

        client.close()
    except ConnectionRefusedError:
        print("Connection is refused, please confirm server address and port number")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()