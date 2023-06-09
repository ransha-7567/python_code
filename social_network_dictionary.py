# ------------------------------------------------------------------------------------------------------------
# QUESTION 1
import datetime

def make_person(this_id: int, name: str, date_of_birth: datetime.datetime) -> dict:
    '''Creates a dictionary with a person's properties, including empty lists for friends and history'''
    return dict(friends=[], history=[], id=this_id, name=name, date_of_birth=date_of_birth)


def find_friendX_inY(person_X: dict, person_Y: dict) -> int:
    '''Looks for person_X's ID in the friend list of person_Y; returns the position it is found at (or None if not found)'''
    for i in range(len(person_Y['friends'])):
        if person_X['id'] == person_Y['friends'][i]:
            return i


def make_friendship(person_X: dict, person_Y: dict):
    '''Add the IDs of person_X and person_Y to each others' friends list'''
    if person_X['id'] == person_Y['id']:  # Doesn't let the person add themselves as a friend
        return None
    if person_X['id'] not in person_Y['friends']:
        person_Y['friends'].append(person_X['id'])  # add person_X[id] to person_Y['friends']
    if person_Y['id'] not in person_X['friends']:
        person_X['friends'].append(person_Y['id'])  # add person_Y[id] to person_X['friends']


def end_friendship(person_X: dict, person_Y: dict):
    '''Goes through each person's friend list and removes the ID of each from the other'''
    if person_X['id'] in person_Y['friends']:
        person_Y['friends'].remove(person_X['id'])  # remove person_X[id] from person_Y['friends']
    if person_Y['id'] in person_X['friends']:
        person_X['friends'].remove(person_Y['id'])  # remove person_Y[id] from person_X['friends']


def birthday_within_X_days_of_Y(person: dict, days: int, comparison_date: datetime.datetime) -> bool:
    '''Return True if the person's birthday is within the given number of days of comparison date (either side), \
    else returns False. Uses the 29/2 = 1/3 convention for leap year bdays.'''
    # Turns date object into str, where the str represent nth day of the year(no. days in a year is 366 for a leap year)
    dob = person['date_of_birth'].strftime('%j')  # %j day of the year : 001 - 366
    date = comparison_date.strftime('%j')
    dob_int = int(dob)
    date_int = int(date)
    # Checks if dob and comparison date is in a leap year
    dob_leap = is_leap_year(
        int(person['date_of_birth'].strftime('%Y')))  # strftime('%Y') returns the year from the date object
    date_leap = is_leap_year(int(comparison_date.strftime('%Y')))
    # leap year gets shifted 1 day earlier from day 61 (1/3 on the leap year) turning it into day 60 (1/3 on a non-leap year)
    if (dob_leap == True) and (date_leap == False) and (date_int >= 61):  # thus, 29/2 would the same as 1/3
        dob_int -= 1
    if (date_leap == True) and (dob_leap == False) and (dob_int >= 61):
        date_int -= 1

    # Finds the distance(in days) between bday and a given date (comparison_date) by subtracting dob from comparison date
    # We know that the distance between 2 dates in a year can't exceed 365/2
    # So if our deltadate ends up being bigger then 365/2, we take the larger date back by 1 year
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


def is_leap_year(year: int) -> bool:
    '''NOT IN OFFICIAL FUNCTIONS LIST: determines if a given year is a leap year, returns True if yes. if no, returns False'''
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

# ------------------------------------------------------------------------------------------------------------
# QUESTION 2

def add_person(dict_of_people: dict, name: str, date_of_birth: datetime.datetime) -> int:
    '''Adds a new person to a dictionary containing a set of person dictionaries, and returns new person's id'''
    if bool(dict_of_people) == False:
        # if the dictionary of people is empty
        this_id = 1
    else:
        # run thru the dict and find highest index
        highest_id = 0
        for id in dict_of_people:
            if id > highest_id:
                highest_id = id
        this_id = highest_id + 1
    # Now that we have the highest index, we can add the person to 1 plus that
    new_person = make_person(this_id, name, date_of_birth)
    dict_of_people[this_id] = new_person
    return this_id


def get_person_by_id(dict_of_people: dict, find_id: int) -> dict:
    '''Accesses a dictionary of people to find a dictionary for one person with a given id'''
    return dict_of_people.get(
        find_id)  # using .get(key) instead because ['key'] returns an error when the item is absent


# ------------------------------------------------------------------------------------------------------------
# QUESTION 3

def convert_lines_to_friendships(lines: list) -> dict:
    '''Reads a list of str containing relationship status, converts it into a dictionary of people and their friends'''
    data_set = {}
    for line in lines:  # Right now line = 'Fred,2022-02-01<->Jenny,2004-11-18'
        line = line.split('<->')  # Then line = ['Fred,2022-02-01', 'Jenny,2004-11-18']
        # add person to dict
        for individual in line:  # Right now individual = 'name,year-month-day'
            individual = individual.split(',')  # Then individual = ['Jenny', '2004-11-18']
            new_name = individual[0]
            new_dob_list = individual[1].split('-')
            new_dob = datetime.date(int(new_dob_list[0]), int(new_dob_list[1]), int(new_dob_list[2]))
            # check if the person is already in data_set
            person_already_in_network = False
            for id in data_set:
                if new_name == get_person_by_id(data_set, id)['name']:
                    person_already_in_network = True
            if person_already_in_network == False:  # or len(data_set) == 0:
                add_person(data_set, new_name, new_dob)
        # add relationships
        if len(line) == 2:
            # Right now line = ['Fred,2022-02-01', 'Jenny,2004-11-18']
            person_X_name = line[0].split(',')[0]  # It would be Fred in this example
            person_Y_name = line[1].split(',')[0]  # and Jenny in this example
            # find the id for person_X and person_Y
            for id in data_set:
                if person_X_name == get_person_by_id(data_set, id)['name']:
                    person_X_id = id
                if person_Y_name == get_person_by_id(data_set, id)['name']:
                    person_Y_id = id
            # Now using the their ids, add X and Y to each other as friends
            make_friendship(get_person_by_id(data_set, person_X_id), get_person_by_id(data_set, person_Y_id))
    return data_set

# ------------------------------------------------------------------------------------------------------------
# QUESTION 4

def new_post(content: str, author: dict, tagged: list) -> tuple:
    '''gets social media post details, processes it (removing non-friend tags), and adds the post to the author's post history'''
    successful_tags = []
    for tag_id in tagged:
        if tag_id in author['friends']:
            successful_tags.append(tag_id)
    post = (content, author['id'], successful_tags)
    author['history'].append(post)  # adds the post to the history key of the author
    return post


# ------------------------------------------------------------------------------------------------------------
# QUESTION 5

def birthdays_within_a_week_of(person_id: int, people_dict: dict, comparison: datetime.datetime) -> list:
    '''creates a list of int IDs for those friends of person_id who have a birthday within 7 days (either side) of the comparison date'''
    id_list = []
    for friend_id in people_dict[person_id]['friends']:
        if birthday_within_X_days_of_Y(people_dict[friend_id], 7, comparison):
            id_list.append(friend_id)
    return id_list

def make_birthday_posts(people_dict: dict, from_person_id: int, for_people_ids: list) -> list:
    '''Given a list of people to send a bday message to, a customised post is made'''
    birthday_post = ()
    destination_ids = []
    list_birthday_posts = []
    for friend_id in for_people_ids:
        birthday_post = new_post(
            f"Happy birthday {get_person_by_id(people_dict, friend_id).get('name')}! Hope you have a good one!",
            get_person_by_id(people_dict, friend_id), [friend_id])
        list_birthday_posts.append(birthday_post)
    return list_birthday_posts


