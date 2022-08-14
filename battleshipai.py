import random

def index_to_coord(list_number, list_index):
    letters = "abcde"
    first_coord = letters[list_number]
    second_coord = list_index
    coord = first_coord + str(second_coord)
    return coord


def coord_to_index(coord):
    letters = "abcde"
    listnum = letters.find(coord[0])
    listindex = int(coord[1])-1
    index = (listnum, listindex)
    return index


def all_ai_possible_hits():
    ai_possible_hits = []
    for letter in "abcde":
        for i in range(1,6):
            ai_possible_hits.append(letter+str(i))
    return ai_possible_hits


def ai_hits(ai_possible_hits):
    ai_coord = ai_possible_hits[random.randint(0, len(ai_possible_hits)-1)] 
    return ai_coord


def recording_ai_hits(all_ai_hits, ai_coord, player_battlefield):
    ai_coord_index = coord_to_index(ai_coord)
    list_num = ai_coord_index[0]
    list_index = ai_coord_index[1]
    if player_battlefield[list_num][list_index] == "#":
        all_ai_hits.append(ai_coord)


def possible_ai_hits_list(all_ai_hits, ai_possible_hits):
    if len(all_ai_hits) == 0:
        possiblehits = [ai_hits(ai_possible_hits)]
        return possiblehits 
    if len(all_ai_hits) == 1 or not check_double_pattern(all_ai_hits): 
        last_hit = all_ai_hits[-1]
        if last_hit[0].upper() == "A":
            listnum = 0
            listindex = int(last_hit[1])
            possiblehits = [index_to_coord(listnum, listindex+1), index_to_coord(listnum, listindex-1), index_to_coord(listnum+1, listindex)]
            for hit in possiblehits[:]:
                if hit not in ai_possible_hits:
                    possiblehits.remove(hit)
            return possiblehits
        elif last_hit[0].upper() == "E":
            listnum = 4
            listindex = int(last_hit[1])
            possiblehits = [index_to_coord(listnum, listindex+1), index_to_coord(listnum, listindex-1), index_to_coord(listnum-1, listindex)]
            for hit in possiblehits[:]:
                if hit not in ai_possible_hits:
                    possiblehits.remove(hit)
            return possiblehits     
        elif last_hit[1] == "1":
            listnum = coord_to_index(last_hit)[0] 
            listindex = int(last_hit[1])
            possiblehits = [index_to_coord(listnum, listindex+1), index_to_coord(listnum-1, listindex), index_to_coord(listnum+1, listindex)]
            for hit in ai_possible_hits[:]:
                if hit not in ai_possible_hits:
                    possiblehits.remove(hit)
            return possiblehits       
        elif last_hit[1] == "5":
            listnum = coord_to_index(last_hit)[0] 
            listindex = int(last_hit[1])
            possiblehits = [index_to_coord(listnum-1, listindex), index_to_coord(listnum, listindex-1), index_to_coord(listnum+1, listindex)]
            for hit in possiblehits[:]:
                if hit not in ai_possible_hits:
                    possiblehits.remove(hit)
            return possiblehits  
        else:
            listnum = coord_to_index(last_hit)[0] 
            listindex = int(last_hit[1]) 
            possiblehits = [index_to_coord(listnum, listindex+1), index_to_coord(listnum, listindex-1), index_to_coord(listnum+1, listindex), index_to_coord(listnum-1, listindex)]
            for hit in possiblehits[:]:
                if hit not in ai_possible_hits:
                    possiblehits.remove(hit)
            return possiblehits
    elif check_double_pattern(all_ai_hits) and (len(all_ai_hits) == 2 or not check_triple_pattern(all_ai_hits)):
        possiblehits = double_pattern_true(all_ai_hits)
        for hit in possiblehits[:]:
            if hit not in ai_possible_hits:
                possiblehits.remove(hit)
        return possiblehits
    elif check_triple_pattern(all_ai_hits):
        possiblehits = [ai_hits(ai_possible_hits)]
        for hit in possiblehits[:]:
            if hit not in ai_possible_hits:
                possiblehits.remove(hit)
        return possiblehits


def check_double_pattern(all_ai_hits): #returns true or false, checks if the number or letter follows each other #number stays same, letter increases, or letter increases and number stays the same
    last_hit = all_ai_hits[-1]
    second_last_hit = all_ai_hits[-2]
    last_hit_letter_num = coord_to_index(last_hit)[0]
    second_last_hit_num = coord_to_index(second_last_hit)[0]
    if (int(last_hit[1])+1 == int(second_last_hit[1]) or int(last_hit[1])-1 == int(second_last_hit[1])) and (last_hit_letter_num == second_last_hit_num):
        return True
    elif ((last_hit_letter_num+1 == second_last_hit_num) or (last_hit_letter_num-1 == second_last_hit_num)) and int(last_hit[1]) == int(second_last_hit[1]):
        return True
    else:
        return False
    
    
def double_pattern_true(all_ai_hits):
    last_hit = all_ai_hits[-1]
    second_last_hit = all_ai_hits[-2]
    last_hit_letter_num = coord_to_index(last_hit)[0]
    second_last_hit_num = coord_to_index(second_last_hit)[0]
    if (int(last_hit[1]) in [1,2] and int(second_last_hit[1]) in [1,2]) or (int(last_hit[1]) in [4,5] and int(second_last_hit[1]) in [4,5]) and last_hit_letter_num == second_last_hit_num:
        possiblehits = [last_hit[0] + "3"]
        return possiblehits
        #only one option and that is to go into 3
    elif last_hit_letter_num == second_last_hit_num: #horizontal pattern
        possiblehits = []
        if int(last_hit[1]) < int(second_last_hit[1]):
            possiblehits.append(last_hit[0] + str(int(last_hit[1])-1))
            possiblehits.append(last_hit[0] + str(int(second_last_hit[1])+1))
            return possiblehits
        else:
            possiblehits.append(last_hit[0] + str(int(last_hit[1])+1))
            possiblehits.append(last_hit[0] + str(int(second_last_hit[1])-1))
            return possiblehits
        #two options are the ones on either side of the double pattern
    elif (last_hit_letter_num in [0,1] and second_last_hit_num in [0,1]) or (last_hit_letter_num in [3,4] and second_last_hit_num in [3,4]) and last_hit[1] == second_last_hit[1]:
        possiblehits = ["c" + str(last_hit[1])]
        return possiblehits
        #only one option that is to go into c
    else:
        possiblehits = []
        if last_hit_letter_num < second_last_hit_num:
            possiblehits.append(index_to_coord(last_hit_letter_num-1, int(last_hit[1])))
            possiblehits.append(index_to_coord(second_last_hit_num+1, int(last_hit[1])))
            return possiblehits
        else: #last_hit_letter_num > second_last_hit_num
            possiblehits.append(index_to_coord(last_hit_letter_num+1, int(last_hit[1])))
            possiblehits.append(index_to_coord(second_last_hit_num-1, int(last_hit[1])))
            return possiblehits


def check_triple_pattern(all_ai_hits):
    last_hit = all_ai_hits[-1]
    second_last_hit = all_ai_hits[-2]
    third_last_hit = all_ai_hits[-3]
    last_hit_letter_num = coord_to_index(last_hit)[0]
    second_last_hit_num = coord_to_index(second_last_hit)[0]
    third_last_hit_num = coord_to_index(third_last_hit)[0]
    if int(last_hit[1])-1 == int(second_last_hit[1]) and int(second_last_hit[1])-1 == int(third_last_hit[1]) and (last_hit_letter_num == second_last_hit_num == third_last_hit_num):
        return True
    elif int(last_hit[1])+1 == int(second_last_hit[1]) and int(second_last_hit[1])+1 == int(third_last_hit[1]) and (last_hit_letter_num == second_last_hit_num == third_last_hit_num):
        return True
    elif int(third_last_hit[1])-1 == int(last_hit[1]) and int(third_last_hit[1])+1 == int(second_last_hit[1]) and (last_hit_letter_num == second_last_hit_num == third_last_hit_num):
        return True
    elif int(last_hit[1])-1 == int(third_last_hit[1]) and int(last_hit[1])+1 == int(second_last_hit[1]) and (last_hit_letter_num == second_last_hit_num == third_last_hit_num):
        return True
    elif last_hit_letter_num-1 == second_last_hit_num and second_last_hit_num-1 == third_last_hit_num and (int(last_hit[1]) == int(second_last_hit[1]) == int(third_last_hit[1])):
        return True
    elif last_hit_letter_num+1 == second_last_hit_num and second_last_hit_num+1 == third_last_hit_num and (int(last_hit[1]) == int(second_last_hit[1]) == int(third_last_hit[1])):
        return True
    elif last_hit_letter_num-1 == third_last_hit_num and last_hit_letter_num+1 == second_last_hit_num and (int(last_hit[1]) == int(second_last_hit[1]) == int(third_last_hit[1])):
        return True
    elif third_last_hit_num+1 == second_last_hit_num and third_last_hit_num-1 == last_hit_letter_num and (int(last_hit[1]) == int(second_last_hit[1]) == int(third_last_hit[1])):
        return True
    else:
        return False

def ai_play(possiblehits, ai_possible_hits):
    if len(possiblehits) == 0:
        possiblehits = ai_hits(ai_possible_hits)
    playcoord = possiblehits[random.randint(0, len(possiblehits)-1)]
    return playcoord
    

def ai_main(player_battlefield, all_ai_hits, ai_possible_hits):
    possiblehits = possible_ai_hits_list(all_ai_hits, ai_possible_hits)
    for hit in possiblehits[:]:
        if hit not in ai_possible_hits:
            possiblehits.remove(hit)
    if len(possiblehits)==0:
        possiblehits = [ai_hits(ai_possible_hits)]
    ai_coord = possiblehits[random.randint(0, len(possiblehits)-1)]
    all_ai_hits = recording_ai_hits(all_ai_hits, ai_coord, player_battlefield)
    return ai_coord

    

        