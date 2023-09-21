class NationalPark:
    
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if type(value) is str and 3<=len(value) and not hasattr(self,"name"):
                self._name = value
        else: 
            raise Exception("Not valid name")
        
    name = property(get_name, set_name)

    def trips(self):
        r_list = []
        for trip in Trip.all:
            if type(trip) is Trip and trip.national_park is self:
                r_list.append(trip)
        return r_list
    
    def visitors(self):
        r_list = []
        for trip in Trip.all:
            if type(trip) is Trip and trip.national_park is self and trip.visitor not in r_list:
                r_list.append(trip.visitor)
        return r_list
    
    def total_visits(self):
        visits = 0
        for trip in Trip.all:
            if type(trip) is Trip and trip.national_park is self:
                visits += 1
        return visits
    
    def best_visitor(self):
        current_best = None
        current_best_count = 0
        all_visitors = self.visitors()
        for visitor in all_visitors:
            count = visitor.total_visits_at_park(self)
            if count > current_best_count:
                current_best = visitor
                current_best_count = count
        return current_best

class Trip:
    valid_month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    def get_start_date(self):
        return self._start_date
    
    def set_start_date(self,value):
        if type(value) is str and 7<=len(value):
            split_str = value.split()
            if split_str[0] in Trip.valid_month and 3<=len(split_str[1])<=4: 
                self._start_date = value
            else: 
                raise Exception("Not valid start date format")
        else: 
            raise Exception("Not valid start date")

    start_date = property(get_start_date,set_start_date)

    def get_end_date(self):
        return self._end_date
    
    def set_end_date(self,value):
        if type(value) is str and 7<=len(value):
            split_str = value.split()
            if split_str[0] in Trip.valid_month and 3<=len(split_str[1])<=4: 
                self._end_date = value
            else: 
                raise Exception("Not valid end date format!")
        else: 
            raise Exception("Not valid end date")

    end_date = property(get_end_date,set_end_date)

    def get_visitor(self):
        return self._visitor
    
    def set_visitor(self,value):
        if type(value) is Visitor:
            self._visitor = value
        else:
            raise ValueError ("Not valid visitor")
            
    visitor = property(get_visitor,set_visitor)

    def get_national_park(self):
        return self._national_park
    
    def set_national_park(self,value):
        if type(value) is NationalPark:
            self._national_park = value
        else:
            raise ValueError ("Not valid national park")
            
    national_park = property(get_national_park,set_national_park)

class Visitor:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if type(value) is str and 1<=len(value)<=15:
            self._name = value
        else: 
            raise Exception("Not valid name")
        
    name = property(get_name, set_name)


    def trips(self):
        r_list = []
        for trip in Trip.all:
            if type(trip) is Trip and trip.visitor is self:
                r_list.append(trip)
        return r_list
    
    def national_parks(self):
        r_list = []
        for trip in Trip.all:
            if type(trip) is Trip and trip.visitor is self and trip.national_park not in r_list:
                r_list.append(trip.national_park)
        return r_list
    
    def total_visits_at_park(self, park):
        our_trips = self.trips()
        count = 0
        for trip in our_trips:
            if trip.national_park is park:
                count += 1
        return count

bob = Visitor("Bob")
bill = Visitor("Bill")
tom = Visitor("Tom")
yosemite = NationalPark("Yosemite")
rocky_mts = NationalPark("Rocky Mountains")
Trip(bob,yosemite,"September 20th", "September 22nd")
Trip(bob,rocky_mts,"September 22nd", "September 24th")
Trip(bob, yosemite,"September 24th", "September 26th")
Trip(bill,yosemite,"September 26th", "September 27th")
Trip(tom,rocky_mts,"September 27th", "September 29th")
Trip(tom, rocky_mts, "September 29th", "October 30th")

# print(tom.trips())
# print(bill.national_parks()[0] is yosemite)
# print(yosemite.visitors()[0] is bob)
# print(yosemite.total_visits())
# print(bob.total_visits_at_park(rocky_mts))
# print(yosemite.best_visitor().name)
