"""
Из предложенного текстового файла (text18-30.txt) вывести на экран его содержимое, количество знаков препинания. 
Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив после последней строки автора и название произведения.
"""

poem = """Да, в наше время были люди,
Могучее, лихое племя:
Богатыри - не бы.
Плохая им досталась доля:
Немногие вернулись с поля.
Когда б на то не божья воля,
Не отдали б Москвы!"""

with open('text18-30.txt', 'w', encoding='utf-8') as f:
    f.write(poem)

with open('text18-30.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("Содержимое файла text18-30.txt:")
    print(content)
    
    punctuation = ',.:;!?-'
    punct_count = sum(1 for char in content if char in punctuation)
    print(f"\nКоличество знаков препинания: {punct_count}")

author_and_title = "\n\nМ.Ю. Лермонтов \"Бородино\""
new_content = content + author_and_title

with open('poem_with_author.txt', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\nФайл poem_with_author.txt успешно создан.")
