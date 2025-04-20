import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})

class Hotel:

    def __init__(self,customer_name, hotel_id):
        self.hotel_id = hotel_id
        self.customer_name = customer_name
    def view_hotel(self):
        pass

    def book(self):
        """Books a hotel by changing its availability from yes to no """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotel.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationConfirmation:
    def generate(self):
        pass

print(df)
hotel_ID = input("Enter the id of the hotel: ")
name = input("Enter you name: ")
hotel = Hotel(hotel_id=hotel_ID, customer_name=name)

if hotel.available():
    hotel.book()
    reservation = ReservationConfirmation(name, hotel_ID)
    print(reservation.generate())
else:
    print("Hotel is not free")