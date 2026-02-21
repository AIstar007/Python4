import pandas as pd

def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return None

def show_preview(df):
    print("\n📄 First 5 rows:\n")
    print(df.head())

def show_stats(df):
    print("\n📊 Statistical Summary:\n")
    print(df.describe())

def check_missing(df):
    print("\n⚠️ Missing Values Per Column:\n")
    print(df.isnull().sum())

def clean_missing(df):
    print("\n1. Drop rows with missing values")
    print("2. Fill missing values with column mean")

    choice = input("Choose option (1/2): ")

    if choice == "1":
        return df.dropna()
    elif choice == "2":
        return df.fillna(df.mean(numeric_only=True))
    else:
        print("Invalid choice.")
        return df

def export_csv(df):
    name = input("\nEnter output file name (example: cleaned.csv): ")
    df.to_csv(name, index=False)
    print(f"✅ File saved as {name}")

def main():
    print("\n📈 CSV Data Analyzer Tool")

    path = input("Enter CSV file path: ")
    df = load_csv(path)

    if df is None:
        return

    while True:
        print("\nChoose an option:")
        print("1. Preview Data")
        print("2. Show Statistics")
        print("3. Check Missing Values")
        print("4. Clean Missing Values")
        print("5. Export CSV")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_preview(df)
        elif choice == "2":
            show_stats(df)
        elif choice == "3":
            check_missing(df)
        elif choice == "4":
            df = clean_missing(df)
        elif choice == "5":
            export_csv(df)
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
