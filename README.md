# Project: Develop a Simple Banking System

# Features
Users can create a new bank account with a name and starting balance
Users can deposit money to their accounts
Users can withdraw money from their accounts
Users are not allowed to overdraft their accounts
Users can transfer money to other accounts in the same banking system
Save and load system state to CSV

# Expectations
- Use any programming language of your choice
- Provide steps to set up and run your project
- No UI is needed
- Remember the KISS principle
- High code quality
- Good test coverage

Please follow deploy.txt to run the application

# Use case
1.    I am a new user with no bank account, wish to create a new one
2.    I have a bank account with no money, wish to deposit 
2.1   I have a bank account with money, wish to deposit
3.    I have a bank account with money, wish to withdraw
3.1   I have a bank account with no money, wish to withdraw
4.    I have a bank account with money, wish to transfer money to other accounts
4.1   I have a bank account with no money, wish to transfer money to other accounts

# Test
Please run test.py for unitest result

python test.py

# Enhancement
Business - Users are able to have multiple account under the same username / uid
Business - More user information should be collected for fraud analysis
Techincal - All constants can be stored in a configuration file / files
Technical - Using username / uid to access the bank system, name can be duplicate
Technical - RDBS can be used to replace csv as a data storage (faster and powerful)
Technical - Assign response code for each return status
Techincal - Adding log for each operation for investigation 
Security - Adding authentication to verify identity
Security - User will be logged out if idle for certain time
Security - SQL injection needs to be check if there is a SQL statement

