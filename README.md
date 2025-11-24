# OVERVIEW
This project works as a basic command line tool for a small restaurant. It helps log daily sales transactions in a simple way. The tool asks for details on each one interactively. That includes the dish name, the amount, whether the order was online or offline, and the time it happened. Once everything is entered, it puts together a short daily report. The report covers total revenue, how many of each dish got sold, and a split by order types. It also shows the biggest transaction amount in different four hour blocks of the day with a basic bar chart.

# FEATURES
The features make it easy to use. It guides you through entering transaction details one at a time. Then it calculates the total revenue for the whole day and shows it clearly. It tracks which dishes were popular by counting orders for each. For order types, it adds up the online ones marked as ON and the offline as OFF. It gives insights into peak hours too. That comes from a bar chart highlighting the highest transaction in three four hour blocks, like from zero to four, four to eight, and eight to twelve hours. Overall, the thing is lightweight. It runs from just one Python script and does not need many extra things.

# TECHNOLOGIES/TOOLS USED
The technologies involved are pretty standard. Python three handles all the main logic in the script. Matplotlib is the library that makes the bar chart for visualizing the transaction data.

# STEPS TO INSTALL AND RUN PROJECT
To get it installed and running, start by making sure Python is on your system. You need version three for this. If Matplotlib is not there yet, open your terminal or command prompt. Run this command to install it. pip install matplotlib. Next, take the code provided and save it as a Python file. Something like restaurant tracker.py works fine. To run it, open your terminal again. Go to the folder where you saved the file. Then use this command. python restaurant tracker.py.

# INSTRUCTIONS FOR USE
When you start the script, it prompts for each transaction detail right away. First, type in the dish name and hit enter. Then put the transaction amount, which is the price, and hit enter again. For the order type, enter ON if it was online or OFF for in person, then enter. Now for the hour, use a number from zero to eleven in twelve hour format. Like eight for eight AM, and hit enter. After that, it asks if you want to add another transaction. Type y to keep going with more. Or type n to stop and get the report.

Once you enter n, the script prints the full daily report right in the console. It also opens a new window with the bar chart.
