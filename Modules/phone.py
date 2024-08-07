import phonenumbers
from phonenumbers import geocoder, carrier, timezone

class Phone:
    def __init__(self):
        pass

    def phonelookup(self, phone):
        if phone:
            mobile = phonenumbers.parse(phone, None)

            car = carrier.name_for_number(mobile, "en")
            loc = geocoder.description_for_number(mobile, "en")
            tzn = list(timezone.time_zones_for_number(mobile))

            return (True, {
                "Carrier": car,
                "Location": loc,
                "Timezone": [i for i in tzn]
            })


        return (False, None)