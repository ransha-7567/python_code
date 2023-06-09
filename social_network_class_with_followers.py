from social_network_class_based import SocialNetwork
from social_network_class_based import Person

import datetime

class SocialNetworkWithFollowers(SocialNetwork):
    """SocialNetwork class to represent a network of people, relationship info (incl followers), and posts"""
    def __init__(self,people_friendship_data,post_history):
        self.people_friendship_data = people_friendship_data #list of str
        self.posts = post_history #list of tuples
        self.people = {} #dictionary will store people instances

        # Split people depending on direction of follow
        for line in self.people_friendship_data: # Right now line = 'Fred,2022-02-01<->Jenny,2004-11-18'
            # split depending on follow type
            if '<->' in line:
                line = line.split('<->') # Then line = ['Fred,2022-02-01', 'Jenny,2004-11-18']
                split_type = 'mutual'
            elif '-->' in line:
                line = line.split('-->')
                split_type = 'x_follows_y'
            elif '<--' in line:
                line = line.split('<--')
                split_type = 'y_follows_x'
            else:
                line = [line]

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
                if split_type == 'mutual':
                    person_X.make_friendship(person_Y)
                    if person_X_name == self.get_person_by_id(id).get_name():
                        friend_list = person_Y
                    elif person_Y_name == self.get_person_by_id(id).get_name():
                        friend_list = person_X
                elif split_type == 'x_follows_y':
                    person_X.get_friends().append(person_Y.get_id())
                    follow_list = person_Y
                elif split_type == 'y_follows_x':
                    person_Y.get_friends().append(person_X.get_id())
                    follow_list = person_X
                else:
                    follow_list = 0
                    friend_list = 0
            
    def __str__(self):
        social_network_str = ''
        for id in self.people:
            person = self.get_person_by_id(id)
            social_network_str += f'{person.__str__()} --> Fr[{friend_list}] ==> Fo[{follow_list}]\n'
        return social_network_str
        
#collect user input and instantiate the people class to represent a particular social network
if __name__=="__main__":
    friendship_list = [] 
    user_input = input("Please enter a social network line by line in the form 'Fred, 2022-02-01<->Jenny, 2004-11-18'\n \
    OR type '.' now to use the template social network\n") #say to type '.' when done with option a?
    if user_input != '.':
        exit = False
        while exit == False:
            user_input = input()
            if user_input == '.':
                exit = True
            else:
                friendship_list.append(user_input)
    else:
        friendship_list = [
            'Fred,2022-02-01<--Jenny,2004-11-18',
            'Jiang,1942-09-16-->Sasha,1834-02-02',
            'Corey,2015-05-22',
            'Sasha,1834-02-02<->Amir,1981-08-11'
        ]
    network_x = SocialNetworkWithFollowers(friendship_list, [])
    print('Below are the people in your network')
    for id in network_x.get_people():
        print(network_x.get_person_by_id(id))

