import tkinter as tk
from tkinter import font

# Example stock data
stock_data = [
    {
        "code": "LSE",
        "stockExchange": "London Stock Exchange",
        "topStocks": [
            {"code": "CRDA", "stockName": "CRODA INTERNATIONAL PLC", "price": 4807.00},
            {"code": "GSK", "stockName": "GSK PLC", "price": 1574.80},
            {"code": "ANTO", "stockName": "ANTOFAGASTA PLC", "price": 1746.00},
            {"code": "FLTR", "stockName": "FLUTTER ENTERTAINMENT PLC", "price": 16340.00},
            {"code": "BDEV", "stockName": "BARRATT DEVELOPMENTS PLC", "price": 542.60},
        ],
    },
    {
        "code": "NYSE",
        "stockExchange": "New York Stock Exchange",
        "topStocks": [
            {"code": "AHT", "stockName": "Ashford Hospitality Trust", "price": 1.72},
            {"code": "KUKE", "stockName": "Kuke Music Holding Ltd", "price": 1.20},
            {"code": "ASH", "stockName": "Ashland Inc.", "price": 93.42},
            {"code": "NMR", "stockName": "Nomura Holdings Inc.", "price": 5.84},
            {"code": "LC", "stockName": "LendingClub Corp", "price": 9.71},
        ],
    },
    {
        "code": "NASDAQ",
        "stockExchange": "Nasdaq",
        "topStocks": [
            {"code": "AMD", "stockName": "Advanced Micro Devices, Inc.", "price": 164.21},
            {"code": "TSLA", "stockName": "Tesla, Inc.", "price": 190.35},
            {"code": "SOFI", "stockName": "SoFi Technologies, Inc.", "price": 8.24},
            {"code": "PARA", "stockName": "Paramount Global", "price": 14.92},
            {"code": "GOOGL", "stockName": "Alphabet Inc.", "price": 141.91},
        ],
    }
]

# Function to show selected button text on the right
def show_selected_text(selected_text):
    # chat_log.insert(tk.END, f"{selected_text}\n\n")
    chat_log.insert(tk.END, f"{selected_text}\n\n", "response")    
# Function to display and append the selected stock in the chat_log
def append_selected_text(selected_text):
    chat_log.insert(tk.END, f"{selected_text}\n\n")  # Append the selected stock right below the question
# Function to get stock price based on code
def get_stock_price(stock_code):
    for exchange in stock_data:
        for stock in exchange["topStocks"]:
            if stock_code.lower() == stock["code"].lower():
                return f"{stock['stockName']} - Price: ${stock['price']:.2f}"
    return "Sorry, I couldn't find that stock."

# Function to show available stocks for selected exchange
def show_stocks_for_exchange(exchange):
    clear_button_frame()  # Only clear buttons, retain chat history
    show_selected_text(f"{exchange['stockExchange']}\n\n")
    chat_log.insert(tk.END, f"Please select a stock from {exchange['stockExchange']}:\n\n", "prompt")
    for stock in exchange["topStocks"]:
        # Insert a button for each stock into the chat_log
        btn = tk.Button(chat_log, text=stock["stockName"], font=btn_font, width=40, height=2, 
                        bg="#e0e0e0", fg="#333", bd=1, relief="solid", 
                        command=lambda s=stock: [show_stock_price(s)])
        
        # Add a button to the chat_log using window_create
        chat_log.window_create(tk.END, window=btn)
        chat_log.insert(tk.END, "\n")  # Add a newline after each button for spacing

# Function to display stock price
def show_stock_price(stock):
    show_selected_text(f"{stock['stockName']}")
    chat_log.insert(tk.END, f"Stock Price of {stock['stockName']} ({stock['code']}) is ${stock['price']:.2f}.\n\n", "prompt")
    # Options to go back or to main menu
    clear_button_frame()
    btn_back = tk.Button(chat_log, text="Go Back", font=btn_font, width=40, height=2,
                         bg="#e0e0e0", fg="#333", bd=1, relief="solid", command=display_exchange_buttons)
    # btn_back.pack(pady=5)
    chat_log.window_create(tk.END, window=btn_back)
    chat_log.insert(tk.END, "\n")  # Add a newline after each button for spacing   
    btn_main_menu = tk.Button(chat_log, text="Main Menu", font=btn_font, width=40, height=2,
                              bg="#e0e0e0", fg="#333", bd=1, relief="solid", command=display_welcome_message)
    # btn_main_menu.pack(pady=5)
    chat_log.window_create(tk.END, window=btn_main_menu)
    chat_log.insert(tk.END, "\n")  # Add a newline after each button for spacing

# Function to clear only the button frame, retaining chat history
def clear_button_frame():
    for widget in button_frame.winfo_children():
        widget.destroy()

# Function to display exchange options
def display_exchange_buttons():
    clear_button_frame()
    chat_log.insert(tk.END, "Please select a Stock Exchange:\n\n", "prompt")
    for exchange in stock_data:
      
        btn = tk.Button(chat_log, text=exchange["stockExchange"], font=btn_font, width=40, height=2,
                        bg="#e0e0e0", fg="#333", bd=1, relief="solid",
                        command=lambda e=exchange: [show_stocks_for_exchange(e)])
        # btn.pack(pady=5)
        chat_log.window_create(tk.END, window=btn)
        chat_log.insert(tk.END, "\n")  # Add a newline after each button for spacing
# Function to display welcome message
def display_welcome_message():
    chat_log.insert(tk.END, "Hello! Welcome to LSEG. I'm here to help you.\n\n", "greeting")
    root.after(500, display_exchange_buttons)

# Set up main application window
root = tk.Tk()
root.title("LSEG Chatbot")
root.geometry("800x500")
root.configure(bg="#f4f4f4")

# Custom font for buttons
btn_font = font.Font(family="Arial", size=12)

# Chat log to display messages
chat_log = tk.Text(root, height=15, width=60, wrap="word", bg="#f1f1f1", font=("Arial", 10), relief="flat", padx=10, pady=10)
chat_log.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

# Label to show selected button text on the right side
selected_label = tk.Label(root, text="", font=("Arial", 12), bg="#f4f4f4", fg="#333")
selected_label.grid(row=0, column=1, padx=10, pady=10, sticky="n")

# Frame for buttons below the chat log
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.grid(row=1, column=0, columnspan=2, pady=10)

# Initialize with the welcome message
root.after(100, display_welcome_message)

# Make the layout expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Run the application
root.mainloop()