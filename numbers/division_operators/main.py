# Calculate the number of completed transactions antwoord is 6 
transactions = 10 
min_per_transactions = 7
available_min = 60
Totale_min_transactions = transactions * min_per_transactions

completed = available_min //min_per_transactions  
# Calculate the number of remaining minutes
minutes = available_min % min_per_transactions


# Print these values
print("The number of completed transactions is", completed)
print("The number of remaining minutes is", minutes)