
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.listings = []

    def add_listing(self):
        self.listings.append() 


class Listing(User):
    def __init__(self, address, bathrooms, bedrooms, longitude, latitude, zpid):
        self.address = address
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.longitude = longitude
        self.latitude = latitude
        self.zpid = zpid
