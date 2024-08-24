
class Reservation:
    def __init__(self, reservation_code: str, date: str, hour: int) -> None:
        self.reservation_code = reservation_code
        self.date = date
        self.hour = hour
        
    def details_exibition(self) -> None:
        print(f"Código da Reserva: {self.reservation_code}\nData: {self.date}\nHora: {self.hour}\n")
        
        
class ReservationHotel(Reservation):
    def __init__(self, reservation_code: str, date: str, hour: int, hotel_name: str, nights: int) -> None:
        super().__init__(reservation_code, date, hour)
        self.hotel_name = hotel_name
        self.nights = nights
    
    
    def details_exibition(self) -> None:
        super().details_exibition()
        print(f"Nome do Hotel: {self.hotel_name}\nNúmero de Noites: {self.nights}\n")
        
    
    def calculate_total_price_per_night(self) -> None:
        # 100 reais por noite
        print(f"Total: R${self.nights * 100}")


class ReservationFlight(Reservation):
    def __init__(self, reservation_code: str, date: str, hour: int, flight_number: int, class_type: str) -> None:
        super().__init__(reservation_code, date, hour)
        self.flight_number = flight_number
        self.class_type = class_type
        

    def details_exibition(self) -> None:
        super().details_exibition()
        print(f"Número do Voo: {self.flight_number}\nTipo de Classe: {self.class_type}\n")
        
    
    def class_type_price(self) -> None:
        if self.class_type == "ECONOMY":
            price: float = 100
            print("Preço: R$", price)
            
        if self.class_type == "BUSINESS":
            price: float = 200
            print("Preço: R$", price)
        
        if self.class_type == "DELUXE":
            price: float = 300
            print("Preço: R$", price)
        

if __name__ == "__main__":
    reservationHotel: ReservationHotel = ReservationHotel("123456", "10/10/2020", 14, "Hilton", 2)
    reservationHotel.details_exibition()
    reservationHotel.calculate_total_price_per_night()
    
    reservationFlight: ReservationFlight = ReservationFlight("123456", "10/10/2020", 14, 123, "ECONOMY")
    reservationFlight.details_exibition()
    reservationFlight.class_type_price()
    