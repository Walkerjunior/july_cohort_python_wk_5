# Activity 1: Design Your Own Class (Smartphone Example)

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Device Info: {self.brand} {self.model}"


class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)
        self.__storage = storage        # Encapsulation
        self.__battery = battery

    def make_call(self, number):
        print(f"{self.brand} {self.model} calling {number}...")

    def browse_internet(self):
        print(f"{self.brand} {self.model} is browsing the internet...")

    def phone_specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, "
              f"Storage: {self.__storage}GB, Battery: {self.__battery}mAh")


# Example usage
if __name__ == "__main__":
    phone1 = Smartphone("Samsung", "Galaxy S22", 256, 4500)
    phone2 = Smartphone("Apple", "iPhone 14", 128, 3900)

    print(phone1.device_info())
    phone1.make_call("0712345678")
    phone1.browse_internet()
    phone1.phone_specs()

    print("\n")
    print(phone2.device_info())
    phone2.make_call("0798765432")
    phone2.browse_internet()
    phone2.phone_specs()
