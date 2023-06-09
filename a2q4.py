###############################################################################
# CMPT 145 Course material
# Original Author: Lauresa Stilling
# Date Created:   31 May 2023
# Last Edited:    15 June 2023
#
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Testing; relevant to Chapter 5, 6, 7
###############################################################################

# TODO: Fill in your information below
# Student Name: Hatem
# NSID: hma194
# Student Number: 11291988

# TODO: TEST DRIVEN DEVELOPMENT

def get_patient_people(community: list):
    """
    Purpose: Get a list of all dictionaries where value for "foes" is an empty list.
    Pre-condition:
        :param community: list of dictionaries to iterate through
            dictionaries must contain the keys "name", "friends", and "foes".
                "name" values should be unique otherwise unknown behaviour can occur.
                "friends" and "foes" values must be lists.
    Post Conditions:
        None
    Return:
        list of dictionaries of those with no foes.
    """
    # CHANGE:

    # A new list
    list_of_people_with_no_foes = []
    # A person represents a dictionary with a persons' information.
    for person in community:
        # Number of foes a person has
        foes_number = len(person["foes"])
        # If the number of foes is zero (the "foes" value is empty or is an empty list)
        if foes_number == 0:
            # append the person's information to this new list
            list_of_people_with_no_foes.append(person)

    return list_of_people_with_no_foes
    # return [] # commented out from original code because we want a list with specific content, and not just an empty
    # list.



def leave_community(community: list, name:str) -> None:
    """
    Purpose: Go through the list of dictionaries passed in removing name from lists for keys "friends"
        and "foes" and the dictionary associated with their name.
    Pre-condition:
        :param community: list of dictionaries to iterate through
            dictionaries must contain the keys "name", "friends", and "foes".
                "name" values should be unique otherwise unknown behaviour can occur.
                "friends" and "foes" values must be lists.
        :param name: str - name of person being removed from list passed in.
    Post Conditions:
        If the name passed in is a name of a person within the list community all traces of them are removed.
    Return:
        None
    """
    # CHANGE:
    # Into a new list a list of the community members is made excluding the person whose name is given

    # A new list
    updated_community = []
    # Searching the community of persons (dictionaries)
    for person in community:
        # If the person is not the one leaving the community we proceed.
        if person["name"] != name:
            # If the person being searched has the person leaving the community as a friend or foe, the person (whose
            # name is given) is removed from that list.
            if name in person["friends"]:
                person["friends"].remove(name)
            if name in person["foes"]:
                person["foes"].remove(name)
            # Then the new modified dictionary (the person ID) is appended into
            # the new list.
            updated_community.append(person)
    community.clear()  # Remove all elements from the original community list
    community.extend(updated_community)  # Add the updated elements to the community list
    # return # Not needed as there is no return for this function.

def are_community_besties(community: list, name1: str, name2: str) -> bool:
    """
    Purpose: Determine if the two names passed in are within the community and if they are on each
        others "friends" list.
    Pre-condition:
        :param community: list of dictionaries to iterate through
            dictionaries must contain the keys "name", "friends", and "foes".
                "name" values should be unique otherwise unknown behaviour can occur.
                "friends" and "foes" values must be lists.
        :param name1: str - name of the first person being examined within list passed in.
        :param name2: str - name of the first person being examined within list passed in.
    Post Conditions:
        None
    Return:
        bool -> returns True if they are both within the community and their names are in each others
        list associated with the key "friends".
        Returns True if on both "friends" and "foes" list simultaneously
    """
    # CHANGE: Entire function

    # To be considered besties, friendship has to go both ways. Those are the conditions
    conditions_met = 0
    # Looking through the list of persons (dictionaries) in the community.
    for person in community:
        # If the person has the name under the argument name1
        if person["name"] == name1:
            # and if name2 is in the persons friends list
            if name2 in person["friends"]:
                # The first condition is met
                conditions_met += 1
                # If the person is also a foe (in an addition to being a friend) return True
                if name2 in person["foes"]:
                    return True
        # If the person has the name under the argument name2
        if person["name"] == name2:
            # and if name1 is in the persons friends list
            if name1 in person["friends"]:
                # The second condition is met
                conditions_met += 1
                # If the person is also a foe (in an addition to being a friend) return True
                if name1 in person["foes"]:
                    return True
    # If both conditions are met return True. The conditions are that both persons are each other's friends. else return
    # False
    if conditions_met == 2:
        return True
    else:
        return False
    # return False # Commented original code.

def get_all_community_besties(community: list, name: str) -> list:
    """
    Purpose: Determine all friends of name passed in where they are on each others "friends list".
    Pre-condition:
        :param community: list of dictionaries to iterate through
            dictionaries must contain the keys "name", "friends", and "foes".
                "name" values should be unique otherwise unknown behaviour can occur.
                "friends" and "foes" values must be lists.
        :param name: str - name of the person being examined within list passed in.
    Post Conditions:
        None
    Return:
        list of dicts -> returns list of all people within the list passed in if their names are in each others
        list associated with the key "friends"
        Still added to list if names are simultaneously in lists associated with "friends" and "foes"
    """
    # CHANGE:

    all_community_besties = []
    persons_friends = []
    # This for-loop makes a list of the friends of the person of interest
    for person in community:
        if name == person["name"]:
            for friend in person['friends']:
                persons_friends.append(friend)
    # for persons in the community
    for person in community:
        # If a person has the person of interest in both the list of friends and foes, their dictionary is added to the
        # main list to be returned. else, is the person of interest just a friend (elif conditional)
        if name in person["friends"] and name in person["foes"]:
            all_community_besties.append(person)
        # If the person of interest is in a person's friends list.
        elif name in person["friends"]:
            # If the examined person has the person of interest as a friend, check if their name is on the
            # persons_friend list (the person examined is in the friend list of the person of interst)
            if person["name"] in persons_friends:
                # Looking at people in the examined person's friend list
                for examined_person_friends in person["friends"]:
                    # If the person looked at is the person of interest (the one inputted as an argument)
                    if examined_person_friends == name:
                        # The friendship goes both ways so,
                        # append the dictionary of the person examined to the list all_communit_besties.
                        all_community_besties.append(person)

    return all_community_besties


### TESTS
# TODO - Resolve 1 testcase at a time
def testing():
    # General Inputs
    def get_inputs():
        return [
            # Case 1: Empty List
            [],
            # Case 2: Single Element with friends, no foes
            [{"name": "Bugs",
              "friends": ["Tweety"],
              "foes":[]}],
            # Case 3: Single Element with no friends or foes
            [{"name": "Bugs",
              "friends": [],
              "foes": []
              }],
            # Case 4: Single element with no friends, has foes
            [{"name": "Bugs",
              "friends": [],
              "foes": ["Elmer"]
              }],
            # Case 5: Slightly complicated community
            [{"name": "Bugs",
              "friends": [],
              "foes": ["Elmer"]},
             {"name": "Tweety",
              "friends": ["Bugs","Granny","Lola"],
              "foes": []},
             {"name": "Taz",
              "friends": [],
              "foes": ["Bugs"]},
             {"name": "Granny",
              "friends": ["Bugs", "Tweety"],
              "foes": []}],
            # Case 6: Even more complex community
            [{"name": "Bugs",
              "friends": ["Tweety","Sylvester","Lola"],
              "foes": ["Elmer","Taz","WileE"]},
             {"name": "Tweety",
              "friends": ["Bugs","Granny"],
              "foes": ["Sylvester"]},
             {"name": "Taz",
              "friends": ["Daffy"],
              "foes": ["Bugs"]},
             {"name": "Granny",
              "friends": ["Bugs", "Tweety","Sylvester"],
              "foes": []},
             {"name": "Sylvester",
              "friends": ["Bugs", "Granny"],
              "foes": ["Tweety","Bugs"]}
             ]]
    def test_get_patient_people():
        test_count = 0
        case1,case2,case3,case4,case5,case6 = get_inputs()
        case5_expects = [{"name": "Tweety",
              "friends": ["Bugs","Granny","Lola"],
              "foes": []},
              {"name": "Granny",
              "friends": ["Bugs", "Tweety"],
              "foes": []}]
        case6_expects = [{"name": "Granny",
              "friends": ["Bugs", "Tweety","Sylvester"],
              "foes": []}]
        test_cases = [{"input": case1,
                        "expect": [],
                        "output":get_patient_people(case1),
                        "message" : "Empty list should get back empty list"},
                    {"input": case2,
                    "expect": case2,
                    "output": get_patient_people(case2),
                    "message": "Bugs has no foes and should be in the list returned"},
                    {"input": case3,
                     "expect": case3,
                     "output": get_patient_people(case3),
                     "message": "Bugs has no foes and should be in the list returned"},
                    {"input": case4,
                     "expect": [],
                     "output": get_patient_people(case4),
                     "message": "Bugs has foes and should have empty list returned"},
                    {"input": case5,
                     "expect": case5_expects,
                     "output": get_patient_people(case5),
                     "message": "Two dictionaries have empty lists associated with key 'foes' (Tweety, Granny)"},
                      {"input": case6,
                       "expect": case6_expects,
                       "output": get_patient_people(case6),
                       "message": "One dictionary has an empty lists associated with key 'foes' (Granny)"}
                      ]
        for test in test_cases:
            test_count += 1
            assert test["output"] == test["expect"], "Error Test Case "+str(test_count)+": " +test["message"]+"\n"+\
                                                     "Input: " + str(test["input"]) + "\n" +\
                                                     "Expected: " + str(test["expect"]) + "\n" +\
                                                     "Output: " + str(test["output"])

        return test_count

    def test_leave_community():
        test_count = 0
        case1,case2,case3,case4,case5,case6 = get_inputs()
        test_cases = [{"input": (case1,"Taz"),
                        "expect": None,
                        "output":leave_community(case1, "Taz"),
                        "message" : "Name not in community list should be unchanged."},
                    {"input": (case2,"Bugs"),
                    "expect": None,
                    "output": leave_community(case2,"Bugs"),
                    "message": "Bugs is in list and should be removed"},
                    {"input": (case3, "Lola"),
                     "expect": None,
                     "output": leave_community(case3,"Lola"),
                     "message": "Bugs has no foes and should not be impacted"},
                    {"input": (case4,"Elmer"),
                     "expect": None,
                     "output": leave_community(case4,"Elmer"),
                     "message": "Bugs has name in list associated with 'foes' and should no longer have name present in list"},
                    {"input": (case5,"Foghorn Leghorn"),
                     "expect": None,
                     "output": leave_community(case5,"Foghorn Leghorn"),
                     "message": "Expect no impact on the list passed in because name not present"},
                      {"input": (case5, "Lola"),
                       "expect": None,
                       "output": leave_community(case5, "Lola"),
                       "message": "Expect name to be removed from list associated with key 'friends' and key 'foes'."},
                      {"input": (case6,"Bugs"),
                       "expect": None,
                       "output": leave_community(case6,"Bugs"),
                       "message": "Name present within numerous lists and as as a dictionary, make sure it is removed from all occurrences"}
                      ]
        for test in test_cases:
            community = test["input"][0]
            name_removed = test["input"][1]
            test_count += 1
            for person in community:
                assert name_removed != person["name"], "Error Test Case "+str(test_count)+": " +test["message"]+"\n"+\
                                                     "Input: " + str(test["input"]) + "\n" +\
                                                     "Output: " + str(community)
                assert name_removed not in  person["friends"], "Error Test Case "+str(test_count)+": " +test["message"]+"\n"+\
                                                     "Input: " + str(test["input"]) + "\n" +\
                                                     "Output: " + str(community)
                assert name_removed not in person["foes"], "Error Test Case "+str(test_count)+": " +test["message"]+"\n"+\
                                                     "Input: " + str(test["input"]) + "\n" +\
                                                     "Output: " + str(community)
        return test_count


    def test_are_community_besties():
        test_count = 0
        case1,case2,case3,case4,case5,case6 = get_inputs()
        test_cases = [{"input": (case1, "Bugs", "Taz"),
                        "expect": False,
                        "output":are_community_besties(case1, "Bugs", "Taz"),
                        "message" : "Neither name is in the list."},
                    {"input": (case2,"Bugs","Foghorn Leghorn"),
                    "expect": False,
                    "output": are_community_besties(case2, "Bugs", "Foghorn Leghorn"),
                    "message": "Bugs is in list but is not friends with 'Foghorn Leghorn'"},
                    {"input": (case3, "Bugs", "Lola"),
                     "expect": False,
                     "output": are_community_besties(case3,"Bugs","Lola"),
                     "message": "Bugs is friends with 'Lola' but Lola not in community list"},
                    {"input": (case4, "Bugs", "Elmer"),
                     "expect": False,
                     "output": are_community_besties(case4,"Bugs","Elmer"),
                     "message": "Bugs has Elmer in list associated with 'foes' not 'friends'"},
                    {"input": (case5, "Elmer", "Foghorn Leghorn"),
                     "expect": False,
                     "output": are_community_besties(case5,"Elmer", "Daffy"),
                     "message": "Neither are within the community"},
                      {"input": (case5, "Tweety", "Granny"),
                       "expect": True,
                       "output": are_community_besties(case5, "Tweety", "Granny"),
                       "message": "Granny and Tweety are in each other's friends lists"},
                      {"input": (case6, "Bugs", ""),
                       "expect": True,
                       "output": are_community_besties(case6, "Bugs", "Sylvester"),
                       "message": "Bugs is in both Sylvester's list of 'foes' and 'friends', should still get True."},
                      # CHANGE: more test cases.
                      {"input": (case6, "Bugs", "Sylvester"),
                       "expect": True,
                       "output": are_community_besties(case6, "Bugs", "Sylvester"),
                       "message": "Bugs is in both Sylvester's list of 'foes' and 'friends', should still get True."},
                      # More tests
                      {"input": (case6, "Tweety", "Sylvester"),
                       "expect": False,
                       "output": are_community_besties(case6, "Tweety", "Sylvester"),
                       "message": "Tweety is in both Sylvester's list of 'foes' and 'friends', should still get True."},
                      # More tests
                      {"input": (case6, "Tweety", "Granny"),
                       "expect": True,
                       "output": are_community_besties(case6, "Tweety", "Granny"),
                       "message": "Bugs is in both Sylvester's list of 'foes' and 'friends', should still get True."}
                      ]
        for test in test_cases:
            test_count += 1
            assert test["output"] == test["expect"], "Error Test Case " + str(test_count) + ": " + test[
                "message"] + "\n" + \
                                                       "Input: " + str(test["input"]) + "\n" + \
                                                       "Expected: " + str(test["expect"]) + "\n" + \
                                                       "Output: " + str(test["output"])
        return test_count

    def test_get_all_community_besties():
        test_count = 0
        case1, case2, case3, case4, case5, case6 = get_inputs()
        # Case 5: Expected Output
        tweeties_besties = [{"name": "Granny",
              "friends": ["Bugs", "Tweety"],
              "foes": []}]
        # Case 6: Expected Output
        bugs_besties = [{"name": "Tweety",
              "friends": ["Bugs","Granny"],
              "foes": ["Sylvester"]},
             {"name": "Sylvester",
              "friends": ["Bugs", "Granny"],
              "foes": ["Tweety","Bugs"]}]
        test_cases = [{"input": (case1, "Elmer"),
                       "expect": [],
                       "output": get_all_community_besties(case1, "Elmer"),
                       "message": "Elmer is not in list and has no friends"},
                      {"input": (case2, "Bugs"),
                       "expect": [],
                       "output": get_all_community_besties(case2, "Bugs"),
                       "message": "Bugs has no local besties"},
                      {"input": (case3, "Bugs"),
                       "expect": [],
                       "output": get_all_community_besties(case3, "Bugs"),
                       "message": "Bugs has no local besties"},
                      {"input": (case4, "Elmer"),
                       "expect": [],
                       "output": get_all_community_besties(case4, "Elmer"),
                       "message": "Elmer is not associated with key 'name' within the list and should have no friends"},
                      {"input": (case5, "Tweety"),
                       "expect": tweeties_besties,
                       "output": get_all_community_besties(case5, "Tweety"),
                       "message": "Tweety should have granny as a community bestie"},
                      {"input": (case5, "Taz"),
                       "expect": [],
                       "output": get_all_community_besties(case5, "Taz"),
                       "message": "Taz is in list but has no local besties"},
                      {"input": (case6, "Bugs"),
                       "expect": bugs_besties,
                       "output": get_all_community_besties(case6, "Bugs"),
                       "message": "Bugs is in both Sylvester's list of 'foes' and 'friends',"
                                  " should still be part of list returned."}
                      ]
        for test in test_cases:
            test_count += 1
            assert test["output"] == test["expect"], "Error Test Case " + str(test_count) + ": " +\
                                                       test["message"] + "\n" + \
                                                       "Input: " + str(test["input"][0]) + "\n" + \
                                                       "\t"+ str(test["input"][1])+"\n"+\
                                                       "Expected: " + str(test["expect"]) + "\n" + \
                                                       "Output: " + str(test["output"])
        return test_count

    total_tests = 0
    print("STATING TESTING...")
    print("TESTING: get_patient_people")
    total_tests += test_get_patient_people()
    print("DONE TESTING: get_patient_people")
    print("TESTING: leave_community")
    total_tests += test_leave_community()
    print("DONE TESTING: leave_community")
    print("TESTING: are_community_besties")
    total_tests += test_are_community_besties()
    print("DONE TESTING: are_community_besties")
    print("TESTING: get_all_community_besties")
    total_tests += test_get_all_community_besties()
    print("DONE TESTING: get_all_community_besties")
    print("TESTING COMPLETE", total_tests, "PASSED!")


if __name__=="__main__":
    testing()
