def main():
  with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_count = count_words(file_contents)
    alpha_count = count_alpha_characters(file_contents)
    sorted_list = sort_alpha_count(alpha_count)
    print(format_report(sorted_list, word_count, f.name))

def sort_alpha_count(list):
  list.sort(reverse=True, key=sort_on)
  return list

def format_report(list, word_count, report_name):
  formatted_report = f"--- Begin report of {report_name} ---\n"
  formatted_report += f"{word_count} words found in the document\n\n"

  for letter in list:
    formatted_report += f"The '{letter["letter"]}' character was found {letter["count"]} times\n"

  formatted_report += "--- End Report ---"
  
  return formatted_report

def sort_on(dict):
  return dict["count"]

def count_alpha_characters(book):
  character_count = {}
  character_count_list = list()
  lowered_book = book.lower()
  
  for character in lowered_book:
    if character.isalpha() == False:
      continue

    if character in character_count:
     character_count[character] += 1
    else:
     character_count[character] = 1

  for character in character_count:
    character_count_list.append({
      "letter": character,
      "count": character_count[character]
    })

  return character_count_list

def count_words(book):
    return len(book.split())

main()