import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd


class CSVCleanerApp:
    def __init__(self, root):
        self.root = root
        self.df = 'orders_raw.csv'
        self.build.ui()
        self.tree = ttk.Treeview(self.root, show="headings")
        # Create the table
        self.tree["columns"] = ("order_id", "customer_name", "product")
        # Set the header text for each column
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)
        # Add a row of data
        self.tree.insert("", "end", values=(1001, "Alice Johnson", "Wireless Mouse"))

        def show_dataframe(self, df):
            # 1. Clear any existing rows
            self.tree.delete(*self.tree.get_children())

            # 2. Set the columns to match the Dataframe
            self.tree["columns"] = list(df.columns)
            for col in df.columns:
                self.tree.heading(col, text=col)
                self.tree.column(col, width=110)
            # 3. Add every row from the Dataframe
            for _, row in df.iterrows():
                self.tree.insert("", "end", values=list(row))


from tkinter import filedialog


def load_csv(self):
    path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=["CSV files," "*.csv"]
    )
    if not path:
        return
    self.df = pd.read_csv(path)
    self.show_dataframe(self.df)
    self.log(f"Loaded{path}-{len(self.df)} rows, {len(self.df.columns)} columns")

    def clean_data(self):
        if self.df is None:
            self.log("Load a CSV first!")
            return
        df = self.df
        # ---Strip whitespace from text columns---
        text_cols = ["customer_name", "product", "category", "status"]
        for col in text_cols:
            df[col] = df[col].astype(str).str.strip()
        # --- Standardize capitalization ----
        df["category"] = df["category"].str.title()  # electronics-> Electronics
        df["status"] = df["status"].str.lower()  # COMPLETED -> completed

        # ---Fix the price column ----
        df["unit_price"] = df["unit_price"].astype(str).replace("$", "", regex=False)
        df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
        # ... (quantity,missing values, total_price)...
        self.df = df
        self.show_dataframe(self.df)

        # understanding missing value handling
        df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
        df["quantity"] = df["quantity"].fillna(1).astype(int)

        # missing unit price
        category_avg = df.groupby("category")["unit_price"].transform("mean")
        df["unit_price"] = df["unit_price"].fillna(category_avg).round(2)
        df["total_price"] = (df["quantity"] * df["unit_price"]).round(2)


from tkinter import scrolledtext

# In build_ui:
self.status_log = scrolledtext.ScrolledText(self.root, height=6)


def log(self, message):
    self.status_log.insert(tk.END, message + "\n")
    self.status_log.see(tk.END)
