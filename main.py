import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
class Hotel:

    def __init__(self,customer_name, hotel_id, name):
        self.hotel_id = hotel_id
        self.customer_name = customer_name
        self.name = name

    def view_hotel(self):
        pass

    def book(self):
        """Books a hotel by changing its availability from yes to no """
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationConfirmation:
    def __init__(self, customer_name, hotel_id, hotel_name):
        self.customer_name = customer_name
        self.hotel = hotel_id
        self.hotel_name = df.loc[df["id"] == self.hotel, "name"].squeeze()
    def generate(self, customer_name, hotel_name):
        content = f""" Thank you for your reservation
                        Here are your booking data:
                        Name: {self.customer_name}
                        Hotel: {self.hotel_name}
                        """
        return content


class CreditCard:

    def __init__(self,card_number):
        self.card_number = card_number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.card_number, "expiration": expiration,
                      "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            print("The payment was successfully proceeded!")
        else:
            return False


print(df)
hotel_ID = input("Enter the id of the hotel: ")
user_name = input("Enter you name: ")
hotel = Hotel(hotel_id=hotel_ID, customer_name=user_name, name=df.loc[df["id"] == hotel_ID, "name"].squeeze())

if hotel.available():
    credit_card = CreditCard(card_number="11111111111111111")
    if credit_card.validate(expiration="12/26", holder="John John", cvc="123"):
        hotel.book()
        reservation = ReservationConfirmation(customer_name=user_name, hotel_id=hotel_ID, hotel_name=hotel)
        print(reservation.generate(customer_name=user_name,hotel_name=hotel))
    else:
        print( "There was a problem with your payment")
else:
    print("Hotel is not free")