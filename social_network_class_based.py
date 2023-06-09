import datetime
#------------------------------------------------------------------------------------------------------------
# QUESTION 6 (completed) 
class Person: 
    """ Person class to represent a user with id, name, date_of_birth, friends, and history. """
    def __init__(self,this_id: int,name: str,date_of_birth: datetime.datetime):
        '''initialises an instance of the Person class'''
        self.this_id = this_id
        self.name = name 
        self.date_of_birth = date_of_birth
        self.friends = [] #this will store int ids
        self.history = [] #this will store tuple posts

    # getting details
    def get_id(self):
        return self.this_id
    def get_name(self):
        return self.name
    def get_date_of_birth(self):
        return self.date_of_birth
    def get_friends(self):
        return self.friends

    # Functions
    def birthday_within_X_days_of_Y(self,days,comparison_date: datetime.datetime)->bool:
        '''Return True if the person's birthday is within the given number of days of comparison date, else returns False'''
        # Turns date object into str, where the str represent nth day of the year(no. days in a year is 366 for a leap year)
        dob = self.date_of_birth.strftime('%j')
        date = comparison_date.strftime('%j')
        dob_int = int(dob)
        date_int = int(date)
        # checks if dob and comparison date is in a leap year 
        dob_leap = is_leap_year(int(self.date_of_birth.strftime('%Y'))) #strftime('%Y') returns the year from the date object
        date_leap = is_leap_year(int(comparison_date.strftime('%Y')))
        # leap year gets shifted 1 day earlier from day 61 (1/3 on the leap year) turning it into day 60 (1/3 on a non-leap year)
        if (dob_leap == True) and (date_leap == False) and (dob_leap >= 61): # thus, 29/2 would the same as 1/3
            dob_int -= 1 
        if (date_leap == True) and (dob_leap == False) and (date_leap >= 61):
            date_int -= 1
        # Finds the distance(in days) between bday and a given date (comparison_date)
        # distance between 2 days cannot exceed (365/2) # because going half way in both directions give you the full thing
        # if it does, the larger date gets brought back by 1 phase (365 days in a year) # Analogous to how sin(pi/2) = sin(5pi/2)
        if abs(date_int - dob_int) > 182.5 and dob_int > date_int:
            delta_date = abs(date_int - (dob_int - 365))
        elif abs(date_int - dob_int) > 182.5 and date_int > dob_int:
            delta_date = abs((date_int - 365) - dob_int)
        else:
            delta_date = abs(date_int - dob_int)
        if delta_date <= days:
            return True
        else:
            return False
    
    def make_friendship(self,other_person: "Person"):
        '''Add the IDs of self and other_person to each others' friends list'''
        if self.this_id == other_person.get_id(): # Doesn't let the person add themselves as a friend
            return None
        if self.this_id not in other_person.get_friends(): 
            other_person.get_friends().append(self.this_id) # add person_X[id] to other_person.get_friends()
        if other_person.get_id() not in self.friends:
            self.friends.append(other_person.get_id()) # add person_Y[id] to self.friends
    
    def end_friendship(self,other_person: "Person"):
        '''Goes through each person's friend list and removes the ID of each from the other'''
        if self.this_id in other_person.get_friends():
            other_person.get_friends().remove(self.this_id)
        if other_person.get_id() in self.friends:
            self.friends.remove(other_person.get_id())  
    
    def find_my_friend(self,other_person: "Person")->int:
        '''Looks for other_person's if in the friend list of self; passes back the position it is found at (or None if not found)'''
        for i in range(len(self.friends)):
            if other_person.get_friends() == self.friends[i]:
                return i
    
    def make_post(self,content: str,tagged: list)->tuple:
        '''gets social media post details, processes it (removing non-friend tags), and adds the post to the author's history'''
        successful_tags = []
        for tag_id in tagged:
            if tag_id in self.friends:
                successful_tags.append(tag_id)
        post = (content, self.this_id, successful_tags)
        self.history.append(post) #adds the post to the history key of the author
        return post
        
    def __str__(self):
        dob_str = self.date_of_birth.strftime("%Y-%m-%d")
        return f"{self.get_id()} ({self.get_name()}, {dob_str}) --> {str(self.get_friends())[1:-1]}" 


class SocialNetwork:
    """SocialNetwork class to represent a network of people, relationship info, and posts"""
    def __init__(self,people_friendship_data: list,post_history: list):
        '''initialises an instance of the SocialNetwork class'''
        self.people_friendship_data = people_friendship_data #list of str
        self.posts = post_history #list of tuples
        self.people = {} #dictionary will store people instances

        # split people_friendship data into information segments
        for line in self.people_friendship_data: # Right now line = 'Fred,2022-02-01<->Jenny,2004-11-18'
            line = line.split('<->') # Then line = ['Fred,2022-02-01', 'Jenny,2004-11-18']
            # add each new person to people dictionary
            for individual in line: # Right now individual = 'name,year-month-day'
                individual = individual.split(',') #  individual = ['Jenny', '2004-11-18']
                new_name = individual[0]
                new_dob_list = individual[1].split('-')
                new_dob = datetime.date(int(new_dob_list[0]),int(new_dob_list[1]),int(new_dob_list[2]))
                # check if the person is already in data_set
                person_already_in_network = False
                for id in self.people:
                    if new_name == self.get_person_by_id(id).get_name():
                        person_already_in_network = True
                if person_already_in_network == False: #or len(data_set) == 0:
                    self.add_person(new_name, new_dob) 
                    
            #add relationships
            if len(line) == 2: 
                # Right now line = ['Fred,2022-02-01', 'Jenny,2004-11-18']
                person_X_name = line[0].split(',')[0] # It would be Fred in this example
                person_Y_name = line[1].split(',')[0] # and Jenny in this example
                
                # find the id for person_X and person_Y
                for id in self.people:
                    if person_X_name == self.get_person_by_id(id).get_name():
                        person_X = self.get_person_by_id(id)
                    if person_Y_name == self.get_person_by_id(id).get_name():
                        person_Y = self.get_person_by_id(id)
                # Now using the their ids, add X and Y to each other as friends
                person_X.make_friendship(person_Y)

    def make_person(self, this_id: int, name: str, date_of_birth: datetime.datetime)->Person:
        return Person(this_id, name, date_of_birth)

    def add_person(self,name: str,date_of_birth: datetime.datetime)->int:
        '''Adds a new person to a dictionary containing a set of Person instances, and returns new person's id'''
        if len(self.people) == 0:
            # if the dictionary of people is empty
            this_id = 1
        else:
            # run thru the dict and find highest index
            highest_id = 0
            for id in self.people:
                if id > highest_id:
                    highest_id = id
            this_id = highest_id + 1
        # Now that we have the highest index, we can add the person to 1 plus that
        new_person = self.make_person(this_id, name, date_of_birth)
        self.people[this_id] = new_person
        return this_id
           
    # Gather required details (functions for getting attributes)
    def get_people(self):
        return self.people
    def get_history(self):
        return self.post_history     
    def get_person_by_id(self,find_id: int):
        '''Accesses a dictionary of people to find a dictionary with a given id'''
        return self.people.get(find_id) # using .get(key) instead because ['key'] returns an error when the item is absent

    def make_birthday_posts(self,from_person_id: int,comparison_date: datetime.datetime):
        '''A customised post is made for each friend with birthdays within 7 days of comparison date (either side)'''
        #adds a list of friends who the message will be sent to
        birthday_post = ()
        sender = self.get_person_by_id(from_person_id)
        for friend_id in sender.get_friends():
            friend = self.get_person_by_id(friend_id)
            if friend.birthday_within_X_days_of_Y(7,comparison_date):
                birthday_post = sender.make_post(f"Happy birthday {friend.get_name()}! Hope you have a good one!",[friend.get_id()])
                self.posts.append(birthday_post)

    def __str__(self):
        social_network_str = ''
        for id in self.people:
            person = self.get_person_by_id(id)
            social_network_str += f'{person.__str__()}\n'
        return social_network_str

def is_leap_year(year: int)->bool: 
    '''NOT IN OFFICIAL FUNCTIONS LIST: determines if a given year is a leap year, returns True if yes. If no, returns False'''
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

#------------------------------------------------------------------------------------------------------------
# QUESTION 7
def year_of_birthdays(people_friendship_data: str):
    '''receives social network structure, makes all birthday posts for this year, prints posts in chronological order'''
    social_group = SocialNetwork(people_friendship_data, []) # creates a social network called social group
    this_year = datetime.datetime.now().year
    # Goes through every day in the year and makes birthday posts for each of their friends with a birthday falling on that exact day.
    start_date = datetime.date(this_year,1 , 1)
    stop_date = datetime.date(this_year,12 , 31)
    while stop_date >= start_date:
        for id in social_group.people:  
            person = social_group.get_person_by_id(id)
            for friend_id in person.get_friends():
                birthday_post = ()
                friend = social_group.get_person_by_id(friend_id)
                if friend.birthday_within_X_days_of_Y(0,start_date):
                    birthday_post = person.make_post(f"Happy birthday {friend.get_name()}! Hope you have a good one!",[friend.get_id()])
                    print(birthday_post)
        start_date += datetime.timedelta(days = 1)

#--------------------------------------------------------------------------------------------

#collect user input and instantiate the people class to represent a particular social network
if __name__=="__main__":
    friendship_list = [] 
    user_input = input("Please enter a social network line by line in the form 'Fred, 2022-02-01<->Jenny, 2004-11-18'\n \
    OR type '.' now to use the template social network")
    if user_input != '.':
        exit = False
        while exit == False:
            user_input = input()
            if user_input == '.':
                exit = True
            else:
                friendship_list.append(user_input)
    else:
        friendship_list = ['Fred, 2022-02-01<->Jenny, 2004-11-18','Jiang, 1942-09-16<->Sasha, 1234-02-02','Corey, 2015-05-22','Sasha, 1234-02-02<->Amir, 1981-08-11']
    network_x = SocialNetwork(friendship_list, [])
    print('Below are the people in your network')
    for id in network_x.get_people():
        print(network_x.get_person_by_id(id))

    print("Do you want to see all birthday posts in 1 year for all members of this network?")
    user_input = input('if you do, type "Y"\n')
    if user_input == 'Y':
        year_of_birthdays(friendship_list)

    

