class Smartphone:
    def __init__(self, vendor, model, phone):
        self.vendor = vendor
        self.model = model
        self.phone = phone

    def get_vendor(self):
        return self.vendor

    def get_model(self):
        return self.model

    def get_phone(self):
        return self.phone
