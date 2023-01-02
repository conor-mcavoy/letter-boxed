from nltk.corpus import words

from box import Box

# some example Boxes
sep_16 = Box('dfk', 'onw', 'blr', 'eai')
sep_18 = Box('swl', 'yer', 'but', 'api')
sep_19 = Box('png', 'iro', 'dmh', 'tau')
sep_22 = Box('cvm', 'rin', 'suo', 'edl')
jan_2 = Box('ozu', 'nri', 'lfa', 'mbt')

all_words = words.words()


# the 'score' of a word is simply the number of unique letters it has
# this is the most valuable trait of a useful word in letter boxed
def word_score(*word_list):
    return len(set(''.join(word_list)))


# this map contains all known word scores, mapped to the words that have that score
def make_score_to_word_map(box):
    score_to_word_map = {}
    for word in all_words:
        if box.is_valid_word(word):
            score = word_score(word)
            if score in score_to_word_map:
                score_to_word_map[score].append(word)
            else:
                score_to_word_map[score] = [word]
    return score_to_word_map


def find_solution(dict_word_score, points_left, starting_word):
    solution_list = []
    first_letter = starting_word[0]
    last_letter = starting_word[-1]

    for score_to_search in range(points_left, 13):
        if score_to_search not in dict_word_score:
            continue
        current_words = dict_word_score[score_to_search]
        for candidate_word in current_words:
            # has to start with the last letter or end with first letter
            if candidate_word[0] == last_letter:
                if word_score(candidate_word, starting_word) == 12:
                    solution_list.append([starting_word, candidate_word])
            elif candidate_word[-1] == first_letter:
                if word_score(candidate_word, starting_word) == 12:
                    solution_list.append([candidate_word, starting_word])
    return solution_list


todays_map = make_score_to_word_map(jan_2)
if 12 in todays_map:
    print(todays_map[12])
    exit()


highest_score = max(todays_map.keys())
all_solutions = []
for first_word_score in range(highest_score, 5, -1):
    if first_word_score in todays_map:
        for first_word in todays_map[first_word_score]:
            all_solutions.extend(find_solution(todays_map, 12 - first_word_score, first_word))

all_solutions.sort(key=lambda x: x[1])
all_solutions.sort(key=lambda x: x[0])
for solution in all_solutions:
    print(solution)
