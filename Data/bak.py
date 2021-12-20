# # Bài 2: Replace First
# def replace_first(items: list):
# 	length = len(items)
# 	if length > 1:
# 		items.insert(length, items.pop(0))
# 	return items

# if __name__ == "__main__":
#	print("Example:")
#	print(list(replace_first([1, 2, 3, 4])))

#	# These "asserts" are used for self-checking and not for an auto-testing
#	assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
#	assert list(replace_first([1])) == [1]
#	assert list(replace_first([])) == []
#	print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 3: Split Pairs
# def split_pairs(a):
# 	lst = []
# 	if len(a) % 2 != 0:
# 		a += '_'
# 	for i in range(len(a)//2):
# 		lst.append(a[i*2:(i*2+2)])
	# return lst

# if __name__ == '__main__':
# 	print("Example:")
# 	print(list(split_pairs('abcd')))

# 	# These "asserts" are used for self-checking and not for an auto-testing
# 	assert list(split_pairs('abcd')) == ['ab', 'cd']
# 	assert list(split_pairs('abc')) == ['ab', 'c_']
# 	assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
# 	assert list(split_pairs('a')) == ['a_']
# 	assert list(split_pairs('')) == []
# 	print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 4: Nearest Values
# def nearest_value(values: set, num: int) -> int:
# 	lst = {}
# 	for i in values:
# 		if abs(i) > num:
# 			lst[i] = i - num
# 		else:
# 			lst[i] = num - i
# 	return min(lst, key = lst.get)

# if __name__ == '__main__':
# 	print("Example:")
# 	print(nearest_value([0,-2], -1))

# 	# These "asserts" are used for self-checking and not for an auto-testing
# 	assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
# 	assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
# 	assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
# 	assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
# 	assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
# 	assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
# 	assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
# 	assert nearest_value({-1, 2, 3}, 0) == -1
# 	print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 5: Between Makers
# def between_markers(text: str, begin: str, end: str) -> str:
# 	begin = text.find(begin)
# 	end = text.find(end)
# 	return text[begin+1:end]


# if __name__ == '__main__':
# 	print('Example:')
# 	print(between_markers('What is >apple<', '>', '<'))

# 	# These "asserts" are used for self-checking and not for testing
# 	assert between_markers('What is >apple<', '>', '<') == "apple"
# 	assert between_markers('What is [apple]', '[', ']') == "apple"
# 	assert between_markers('What is ><', '>', '<') == ""
# 	assert between_markers('>apple<', '>', '<') == "apple"
# 	print('Wow, you are doing pretty good. Time to check it!')

# Bài 6:
# def checkio(array: list) -> int:
# 	tmp = 0
# 	if not array:
# 		return 0
# 	for i in range(0, len(array), 2):
# 		tmp += array[i]
# 	return tmp*array[len(array)-1]

# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
# 	print('Example:')
# 	print(checkio([0, 1, 2, 3, 4, 5]))
	
# 	assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
# 	assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
# 	assert checkio([6]) == 36, "(6)*6=36"
# 	assert checkio([]) == 0, "An empty array = 0"
# 	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# Bài 7:
# def checkio(words: str) -> bool:
# 	lst = words.split(" ")
# 	count = 0

# 	for i in lst:
# 		if i.isnumeric():
# 			count = 0
# 		else:
# 			count += 1
# 		if count >= 3:
# 			return True
# 	return False

# #These "asserts" using only for self-checking and not necessary for auto-testing
# if __name__ == '__main__':
# 	print('Example:')
# 	print(checkio("one two 3 four five six 7 eight 9 ten eleven 12"))
	
# 	assert checkio("Hello World hello") == True, "Hello"
# 	assert checkio("He is 123 man") == False, "123 man"
# 	assert checkio("1 2 3 4") == False, "Digits"
# 	assert checkio("bla bla bla bla") == True, "Bla Bla"
# 	assert checkio("Hi") == False, "Hi"
# 	print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

# Bài 8:
# def first_word(text: str) -> str:
# 	word = ''
# 	for i in text:
# 		if i == "'" or i.isalpha() == True:
# 			word += i
# 		elif word != '' and i.isalpha() == False:
# 			break
# 		continue
# 	return word

# if __name__ == '__main__':
# 	print("Example:")
# 	print(first_word("Hello world"))
	
# 	# These "asserts" are used for self-checking and not for an auto-testing
# 	assert first_word("Hello world") == "Hello"
# 	assert first_word(" a word ") == "a"
# 	assert first_word("don't touch it") == "don't"
# 	assert first_word("greetings, friends") == "greetings"
# 	assert first_word("... and so on ...") == "and"
# 	assert first_word("hi") == "hi"
# 	assert first_word("Hello.World") == "Hello"
# 	print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 9:
# def days_diff(a, b):
# 	from datetime import date

# 	return abs(date(a[0], a[1], a[2]) - date(b[0], b[1], b[2])).days

# if __name__ == "__main__":
# 	print("Example:")
# 	print(days_diff((1982, 4, 19), (1982, 4, 22)))

# 	# These "asserts" are used for self-checking and not for an auto-testing
# 	assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
# 	assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
# 	assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
# 	print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 10:
# def bigger_price(limit: int, data: list) -> list:
# 	dct = {}
# 	for i in data:
# 		dct[i['price']] = i
# 	lst = sorted(dct, reverse = True)
# 	return [dct[lst[j]] for j in range(limit)]


# if __name__ == '__main__':
# 	from pprint import pprint
# 	print('Example:')
# 	pprint(bigger_price(2, [
# 		{"name": "bread", "price": 100},
# 		{"name": "wine", "price": 138},
# 		{"name": "meat", "price": 15},
# 		{"name": "water", "price": 1}
# 	]))

# 	# These "asserts" using for self-checking and not for auto-testing
# 	assert bigger_price(2, [
# 		{"name": "bread", "price": 100},
# 		{"name": "wine", "price": 138},
# 		{"name": "meat", "price": 15},
# 		{"name": "water", "price": 1}
# 	]) == [
# 		{"name": "wine", "price": 138},
# 		{"name": "bread", "price": 100}
# 	], "First"

# 	assert bigger_price(1, [
# 		{"name": "pen", "price": 5},
# 		{"name": "whiteboard", "price": 170}
# 	]) == [{"name": "whiteboard", "price": 170}], "Second"

# 	print('Done! Looks like it is fine. Go and check it')

# Bài 11:
# def between_markers(text: str, begin: str, end: str) -> str:
# 	s = text[text.find(begin)+len(begin):] if begin in text else text
# 	s = s[:s.find(end)] if end in text else s
# 	return s

# if __name__ == '__main__':
# 	print('Example:')
# 	print(between_markers('What is >apple<', '>', '<'))

# 	# These "asserts" are used for self-checking and not for testing
# 	assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
# 	assert between_markers("<head><title>My new site</title></head>",
# 						  "<title>", "</title>") == "My new site", "HTML"
# 	assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
# 	assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
# 	assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
# 	assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
# 	print('Wow, you are doing pretty good. Time to check it!')

# Bài 1:
# def remove_all_before(items: list, border: int):
# 	if border in items:
# 		for i in range(items.index(border)):
# 			items.remove(items[0])
# 	return items

# if __name__ == '__main__':
#     print("Example:")
#     print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
#     assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
#     assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
#     assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
#     assert list(remove_all_before([], 0)) == []
#     assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 12:
# def checkio(data: list) -> list:
# 	lst = []
# 	for i in range(len(data)):
# 		counter = 1
# 		for j in range(len(data)):
# 			if data[j] == data[i] and i != j:
# 				counter += 1
# 		if counter > 1:
# 			lst.append(data[i])
# 	return lst
# #Some hints
# #You can use list.count(element) method for counting.
# #Create new list with non-unique elements
# #Loop over original list


# if __name__ == "__main__":
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
#     assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
#     assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
#     assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
#     print("It is all good. Let's check it now")

# Bài 13:
# def popular_words(text: str, words: list) -> dict:
#     dicts = {}
#     count_custom = lambda s, kw: len([True for char in range(0, len(s) + 1 - len(kw)) if s[char:char+len(kw)] == kw ])
#     for word in words:
#     	dicts[word] = count_custom(text.lower(), word.lower())
#     return dicts

# if __name__ == '__main__':
#     print("Example:")
#     print(popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert popular_words('''
# When I was One
# I had just begun
# When I was Two
# I was nearly new
# ''', ['i', 'was', 'three', 'near']) == {
#         'i': 4,
#         'was': 3,
#         'three': 0,
#         'near': 0
#     }
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 14:
# def second_index(text: str, symbol: str) -> [int, None]:
#     from re import sub
#     if text.count(symbol) < 2:
#         return None
#     return sub(symbol, '', text, 1).find(symbol)+1

# if __name__ == '__main__':
#     print('Example:')
#     print(second_index("sims", "s"))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert second_index("find the river", "e") == 12, "Second"
#     assert second_index("sims", "s") == 3, "First"
#     assert second_index("hi", " ") is None, "Third"
#     assert second_index("hi mayor", " ") is None, "Fourth"
#     assert second_index("hi mr Mayor", " ") == 5, "Fifth"
#     print('You are awesome! All tests are done! Go Check it!')

# # Bài 15:
def frequency_sort(items):
    lst = []
    for i in range(len(items)):
        lst.append(items[i])
        for j in range(i, len(items)):
            if items[j] == items[i]:
                lst.append(items[j])
        items.remove(items[i])
    return lst

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    # assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    # assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    # assert list(frequency_sort([])) == []
    # assert list(frequency_sort([1])) == [1]
    # print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 16:
"""
Every true traveler must know how to do 3 things: fix the fire, find the water and extract useful information from the nature around him. Programming won't help you with the fire and water, but when it comes to the information extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".

Input: The time of the day.
Output: The angle of the sun, rounded to 2 decimal places.

Example:
sun_angle("07:00") == 15
sun_angle("12:15") == 93.75
sun_angle("01:23") == "I don't see the sun!"
How it is used: One day it can save your life, if you'll be lost far away from civilization.

Precondition :
00:00 <= time <= 23:59  
"""
# from typing import Union
# def sun_angle(time: str) -> Union[int, str]:
#     # replace this for solution
#     return
# if __name__ == '__main__':
#     print("Example:")
#     print(sun_angle("07:00"))

#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert sun_angle("07:00") == 15
#     assert sun_angle("01:23") == "I don't see the sun!"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 17:
# def split_list(items: list) -> list:
#     # your code here
#     return

# if __name__ == '__main__':
#     print("Example:")
#     print(split_list([1, 2, 3, 4, 5, 6]))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
#     assert split_list([1, 2, 3]) == [[1, 2], [3]]
#     assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
#     assert split_list([1]) == [[1], []]
#     assert split_list([]) == [[], []]
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 18:
# def date_time(time: str) -> str:
#     # replace this for solution
#     return

# if __name__ == "__main__":
#     print("Example:")
#     print(date_time("01.01.2000 00:00"))

#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert (
#         date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
#     ), "Millenium"
#     assert (
#         date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
#     ), "Victory"
#     assert (
#         date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
#     ), "Somebody was born"
#     print("Coding complete? Click 'Check' to earn cool rewards!")

# Bài 19:
# MORSE = {
#     ".-": "a",
#     "-...": "b",
#     "-.-.": "c",
#     "-..": "d",
#     ".": "e",
#     "..-.": "f",
#     "--.": "g",
#     "....": "h",
#     "..": "i",
#     ".---": "j",
#     "-.-": "k",
#     ".-..": "l",
#     "--": "m",
#     "-.": "n",
#     "---": "o",
#     ".--.": "p",
#     "--.-": "q",
#     ".-.": "r",
#     "...": "s",
#     "-": "t",
#     "..-": "u",
#     "...-": "v",
#     ".--": "w",
#     "-..-": "x",
#     "-.--": "y",
#     "--..": "z",
#     "-----": "0",
#     ".----": "1",
#     "..---": "2",
#     "...--": "3",
#     "....-": "4",
#     ".....": "5",
#     "-....": "6",
#     "--...": "7",
#     "---..": "8",
#     "----.": "9",
# }

# def morse_decoder(code):
#     # replace this for solution
#     return

# if __name__ == "__main__":
#     print("Example:")
#     print(morse_decoder("... --- ..."))

#     # These "asserts" using only for self-checking and not necessary for auto-testing
#     assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
#     assert morse_decoder("..--- ----- .---- ---..") == "2018"
#     assert (
#         morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--")
#         == "It was a good day"
#     )
#     print("Coding complete? Click 'Check' to earn cool rewards!")