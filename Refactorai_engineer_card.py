"""
Problem Statement
As an aspiring AI Engineer, you want a simple command-line application that collects personal information and displays it in a clean, professional format.
This project introduces user interaction, variables, formatting, and project organization.
Ask the user for:

Full Name
Age
Country
State
Dream Company
Dream AI Role
Favorite Programming Language
"""
#Programme to Develop AI Engineer profile
print("**" * 20)
print("       AI ENGINEER PROFILE ")
print("**" * 20)

name = input("Enter your name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")
state = input("Enter your state: ")
dream_company = input("Your dream company: ")
role = input("Your Dream Role: ")
fpl = input("Your Favorite Programming language: \n" )


print("**" * 20)
print(f"      {name} PROFILE")
print("**" * 20)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Country: {country} ")
print(f"State: {state}")
print(f"Dream Company: {dream_company} ")
print(f"Role: {role} ")
print(f"Favorite Programming language: {fpl}")
print("**" * 20)
