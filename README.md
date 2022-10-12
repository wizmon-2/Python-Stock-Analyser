








# Python Stock Analyser













#### Video Demo: https://youtu.be/TyfA6FL5B8Y













#### Description:













Hello, world










This is my CS50x 2022 Final Project.



This is a python application which shows infomartion about the stock and stock company of the stock specified by user.











This can very useful to get outline of the company of the stock you are interested in by showing historical stock price graphs and financial informations in stylish table using rich library.












It includes `npyscreen` library which creates the form for user input.







It includes `yfinance` library which uses yahoo finance api to get information about the comapany.







It includes `rich` library which formats the information obtained into stylized tables and layouts.







It includes `mplfinance` library which is used to display OHLS graphs with data from yfinance.







It includes `pandas` library to modify pandas dataframe returned from yfinance.






#### Options:





- Info - Information about the company



- Financials - Latest and quarterly financials



- Balance Sheet - Latest and quarterly balance sheet



- Cash Flow - Latest and quarterly cash flow



- Earnings - Latest and quarterly earnings



- Analysis - Analysis of stock by various firms



- Graph: MAX - All time stock price graph



- Graph: 5Y - Stock price graph of last five years



- Graph: YTD - Stock price graph of current year



- Graph: 1MO - Stock price graph of last month



- Graph: 1D - Today's stock price graph





#### Instructions:

Install requirements.txt with `pip install or requirements.txt`

Before starting, first clear the screen and scrollback to easily view the output of the application.
In macOS, it would `ctrl+l` to clear screen and `cmd+alt+k` to clear scrollback.

To start application  run `python3 main.py` from your terminal.

A form will appear asking for user input, enter the stock name and select the desired options.

Finally press the ok button to submit it.

It will take a few seconds to process the input and then print out the apt output in your terminal screen in stylized tables.

Graphs will all be GUI, so please have x-server or similar for it to appear.


#### Files:











`main.py`: Front-end of the application which takes in information from user in form using the npyscreen library and passes it `helper.py`.













`helper.py`: Back-end of the application which takes information from user and executes methods which uses yfinance library for information, rich library for text formating and mplfinance for graphs, to display apt information to user.













`totable.py`: Module which converts pandas dataframe to rich table format. Referred code is mentioned in the file.













`requirements.txt`: Python module requirements to be installed.










#### Requirements:









mplfinance==0.12.9b1







npyscreen==4.10.5







pandas==1.5.0







rich==10.16.2







yfinance==0.1.74





#### Source:





All information is obtained from yfinance library which uses yahoo finance api.