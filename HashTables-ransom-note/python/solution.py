def ransom_note(magazine, ransom):
  result = True
  magazine_look_up = {}
  for mag_word in magazine:
    word_found = magazine_look_up.get(mag_word, False)
    if word_found:
      magazine_look_up[mag_word] += 1
    else:
      magazine_look_up[mag_word] = 1

  for word in ransom:
    word_found = magazine_look_up.get(word, False)
    if word_found > 0:
      magazine_look_up[word] -= 1
    else:
      result = False
      break
  return result


m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"

