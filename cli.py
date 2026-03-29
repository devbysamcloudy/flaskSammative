import requests

BASE_URL = "http://127.0.0.1:5000"

def menu():
    while True:
        print("1. View Items")
        print("2. Add Item")
        print("3. Delete Item")
        print("4. Fetch from API")
        choice = input("Choose: ")

        if choice == "1":
            resp = requests.get(f"{BASE_URL}/items")
            print(resp.json())

        elif choice == "2":
            name = input("Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            barcode = input("Barcode: ")
            resp = requests.post(f"{BASE_URL}/items", json={
                "name": name, "quantity": quantity, "price": price, "barcode": barcode
            })
            print(resp.json())

        elif choice == "3":
            id = input("ID to delete: ")
            resp = requests.delete(f"{BASE_URL}/items/{id}")
            print(resp.json())

        elif choice == "4":
            barcode = input("Barcode: ")
            resp = requests.get(f"{BASE_URL}/fetch/{barcode}")
            print(resp.json())

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()