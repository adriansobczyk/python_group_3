# ------------------------ KODOWANIE ZNAKÓW ------------------------ #

sample_txt = "Cześć"


utf8_emoji_string = "Jest to ciąg znaków zakodowany w formacie UTF-8 zawierający emoji: \U0001F602 \U0001F604 \u4500"
utf8_emoji_string_two = "Jest to ciąg znaków zakodowany w formacie UTF-8 zawierający emoji:😂 😄 䔀"
russian_hi = "Привет"
polska_litera = "ą".encode('utf-8')
zdekodowana_litera = polska_litera.decode('utf-8')


def sample_if_ascii():
   if sample_txt.isascii():
      print("Tekst jest w ASCII")
   else:
      print("Tekst nie jest w ASCII")

if __name__ == '__main__':
   # print(sample_txt.encode('utf-8'))
   # print(sample_txt.encode('utf-16'))
   # print(sample_txt.encode('utf-32'))
   # print(sample_txt.encode('ascii', errors='backslashreplace'))
   # print(sample_txt.encode('ascii', errors='replace'))
   # print(sample_txt.encode('ascii')) # UnicodeEncodeError: 'ascii' codec can't encode character '\u0119' in position 3: ordinal not in range(128)
   # print(utf8_emoji_string)
   # print(utf8_emoji_string_two)
   # print(utf8_emoji_string.encode('ascii', errors='replace'))
   # print(russian_hi.encode('utf-8'))
   # print(polska_litera.encode('utf-8'))
   print("Zakodowana litera: ", polska_litera) # b = bytes czyli zakodowana litera a nie zwykła litera
   print("Odkodowana litera: ", zdekodowana_litera)
   # sample_if_ascii()
   


# Więcej informacji na temat kodowania znaków:
# https://docs.python.org/3/howto/unicode.html
# https://www.flynerd.pl/2019/09/kodowanie-znakow-ascii-unicode-utf-co-to-znaczy.html