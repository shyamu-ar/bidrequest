import random

punjab = "Chris Gayle, Ravichandran Ashwin (c), Mayank Agarwal, Mandeep Singh, David Miller, Mohammed Shami, Lokesh Rahul (wk), Murugan Ashwin, Sarfaraz Khan, Hardus Viljoen, Andrew Tye"
delhi = "Shikhar Dhawan, Amit Mishra, Colin Ingram, Harshal Patel, Chris Morris, Hanuma Vihari, Shreyas Iyer (c), Kagiso Rabada, Rishabh Pant (wk), Sandeep Lamichhane, Prithvi Shaw"
# mumbai vs punjab
# wicket_keeper = ["dekock", "lokesh_rahul"]
# batsman = ["rohit","gayle","miller","yadav","agarwal","mandeep","yuvraj","pollard","sarfaraz"]
# all_rounder = ["hardik","ashwin","krunal"]
# bowlers = ["bumrah","tye","shami","malinga","mcclenagan","viljoen","varun","markande"]

# kolkata vs delhi
wicket_keeper = ["Parthiv Patel" , "Dinesh Karthik (c & wk)"]
batsman = ["AB de Villiers" , "Virat Kohli (c)" ,  "Nitish Rana", "Chris Lynn" , "Robin Uthappa" ,  "Shimron Hetmyer", "Shubman Gill"]
second_batsman = []
all_rounder = ["Moeen Ali" , "Marcus Stoinis", "Sunil Narine"]
second_all_rounder = ["Andre Russell"]
bowlers = ["Umesh Yadav"  , "Mohammed Siraj" , "Piyush Chawla" , "Kuldeep Yadav" , "Lockie Ferguson" , "Prasidh Krishna"]
second_bowler = ["Yuzvendra Chahal"]


# prasidh krishna , keemo paul , "gill"

def batsman1(no_players):
    global batsman_options
    batsman_options = []
    # batsman_options.append(random.choice(second_batsman))
    for i in range(20):
        batting_player = random.choice(batsman)
        if len(batsman_options) < no_players:
            if batting_player in batsman_options:
                continue
            else:
                batsman_options.append(batting_player)
        else:
            break


def bowlers1(no_players):
    global bowlers_options
    bowlers_options = []
    bowlers_options.append(random.choice(second_bowler))
    for i in range(20):
        bowling_player = random.choice(bowlers)
        if len(bowlers_options) < no_players:
            if bowling_player in bowlers_options:
                continue
            else:
                bowlers_options.append(bowling_player)
        else:
            break



# def bowlers1(first,second):
#     global bowlers_options
#     bowlers_options = []
#     for i in range(10):
#         bowling_player = random.choice(second_bowler)
#         if len(bowlers_options) < second:
#             if bowling_player in bowlers_options:
#                 continue
#             else:
#                 bowlers_options.append(bowling_player)
#         else:
#             break
#     bowlers_options.append(random.choice(second_bowler))
#     for i in range(10):
#         bowling_player = random.choice(bowlers)
#         if len(bowlers_options) < first+second:
#             if bowling_player in bowlers_options:
#                 continue
#             else:
#                 bowlers_options.append(bowling_player)
#         else:
#             break


def all_rounders1(no_players):
    global all_rounder_options
    all_rounder_options = []
    all_rounder_options.append(random.choice(second_all_rounder))
    for i in range(20):
        all_rounder_player = random.choice(all_rounder)
        if len(all_rounder_options) < no_players:
            if all_rounder_player in all_rounder_options:
                continue
            else:
                all_rounder_options.append(all_rounder_player)
        else:
            break



def combinations(no_of_teams):
    complete_set = []
    count = 0
    for i in range(no_of_teams):
        batsman1(4)
        bowlers1(3)
        all_rounders1(3)
        players_list = batsman_options + bowlers_options + all_rounder_options
        complete_set.append(random.choice(wicket_keeper))
        players_list1 = players_list.sort()
        if players_list1 in complete_set:
            continue
        else:
            complete_set.append(players_list)
        count += 1
    for j in complete_set:
        print(j)
    print(len(complete_set))


combinations(20)

# count = 1
# for i in range(100):
#     batsman1(4)
#     bowlers1(4)
#     all_rounders1(2)
#     players_list = batsman_options + bowlers_options + all_rounder_options
#     complete_set = []
#     if players_list in complete_set:
#         continue
#     else:
#         complete_set.append(players_list)
#     # print(complete_set)
#     count +=1
#     print(count)
# print(complete_set)
#
#


# print(test)

# sarfaraz
# miller
# rohit
# yuvraj --
# agarwal --
# gayle --
#
#
# bumrah
# mclegan
# rahman


# rajpoot
# sam curran
#
