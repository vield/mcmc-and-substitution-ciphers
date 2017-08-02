from collections import Counter
import random

import numpy as np

from probs import transitions
from faster_log_prob_sampling import sample_log_prob


alphabet = "abcdefghijklmnopqrstuvwxyz ?"

probabilities = dict((char, {}) for char in alphabet)

for char in alphabet:
    total = sum(transitions[char].values())
    for follower in transitions[char]:
        probabilities[char][follower] = transitions[char][follower] / total


ciphertext = """hrmdakhjxicx mpqidxvmkzxdipohxem kixdhobiqjxwpekuqhxobhxcikkivwpsx
dho iaikwjxbmjowpsjxmksi wobdxobwjxdhobiqxshph mohjxmx mpqidxvmkzxujwpsxmxa iaijmkxqhpjwotxmpqxmxdhobiqxci x hgheowpsxjidhxicxobhxa iaijhqxdinhjx
swffjxjmdakwpsxobwjxdhobiqx hyuw hjxmkkxobhxeipqwowipmkxqwjo wfuowipjxicxobhxom shoxqwjo wfuowipxoixfhxjmdakhqxhrmeoktx
vbhpxq mvwpsxc idxobhxcukkxeipqwowipmkxqwjo wfuowipjxwjxpioxjo mwsboci vm qxiobh xjmdakh jxvwobwpxswffjxm hxujhqx
swffjxjmdakwpsxwjxaiaukm xam oktxfhemujhxwoxqihjxpiox hyuw hxmptxoupwpsx
jkwehxjmdakwpsxobwjxdhobiqxqhahpqjxipxobhxa wpewakhxobmoxiphxempxjmdakhxc idxmxqwjo wfuowipxftxjmdakwpsxupwci dktxc idxobhx hswipxupqh xobhxakioxicxwojxqhpjwotxcupeowipx
woxmkoh pmohjxupwci dxjmdakwpsxwpxobhxnh owemkxqw heowipxvwobxupwci dxjmdakwpsxc idxobhxbi wlipomkxjkwehxqhcwphqxftxobhxeu  hpoxnh owemkxaijwowipx
dukowakhxo txdho iaikwjxobwjxdhobiqxwjxmxnm wmowipxicxobhxdho iaikwjxbmjowpsjxmksi wobdxobmoxmkkivjxdukowakhxo wmkjxmoxhmebxaiwpox
ftxdmzwpsxwoxaijjwfkhxoixomzhxkm sh xjohajxmoxhmebxwoh mowipxwoxbhkajxmqq hjjxobhxeu jhxicxqwdhpjwipmkwotx
 hnh jwfkhxgudaxobwjxdhobiqxwjxmxnm wmpoxicxobhxdho iaikwjxbmjowpsjxmksi wobdxobmoxmkkivjxa iaijmkjxobmoxebmpshxobhxqwdhpjwipmkwotxicxobhxjameh
dedexdhobiqjxobmoxebmpshxqwdhpjwipmkwotxbmnhxkipsxfhhpxujhqxwpxjomowjowemkxabtjwejxmaakwemowipjxvbh hxci xjidhxa ifkhdjxmxqwjo wfuowipxobmoxwjxmxs mpqxempipwemkxhpjhdfkhxwjxujhqxhxsxvbhpxobhxpudfh xicxdikheukhjxwpxmxfirxwjxnm wmfkhx
fuoxobhx hnh jwfkhxgudaxnm wmpoxwjxujhcukxvbhpxqiwpsxdedexi xswffjxjmdakwpsxinh xpipam mdho wexfmthjwmpxdiqhkjxjuebxmjxobijhxwpniknwpsxobhxqw webkhoxa iehjjxi xebwphjhx hjomu mpoxa iehjjxvbh hxobhxpudfh xicxdwrwpsxeidaiphpojxekujoh jxhoexwjxmuoidmowemkktxwpch  hqxc idxobhxqmomx
"""

real_mapping = {'o': 'i', 'y': 't', 'f': 'c', 'n': 'p', 'u': 'u', 'b': 'f', ' ': 'x', 's': 'j', 'j': 'g', 'd': 'q', 'i': 'w', '\n': '\n', 'r': ' ', 'm': 'd', 'g': 's', 'l': 'k', 't': 'o', 'q': 'y', 'v': 'n', 'c': 'e', 'p': 'a', 'x': 'r', 'a': 'm', 'k': 'z', 'w': 'v', 'z': 'l', 'e': 'h', 'h': 'b'}
real_mapping_reversed = {v: k for k, v in real_mapping.items()}
for key in real_mapping_reversed:
    if real_mapping_reversed[key] not in alphabet:
        real_mapping_reversed[key] = '?'

all_characters = [t[0] for t in Counter(list(ciphertext)).most_common()]


def get_next_mapped():
    for char in alphabet:
        yield char
    while True:
        yield '?'


mapping = get_next_mapped()
initial_mapping = dict(zip(all_characters, [next(mapping) for i in range(len(all_characters))]))


def translate(mapping):
    translated_text = ''.join(mapping[char] for char in ciphertext)
    return translated_text


def log_probability(translated_text):
    prob = 0
    for i in range(1, len(translated_text)):
        first = translated_text[i-1]
        second = translated_text[i]

        prob += np.log(probabilities[first][second])

    return prob


mapping = initial_mapping.copy()

translated = translate(mapping)
log_prob = log_probability(translated)

real_translated = translate(real_mapping_reversed)
real_prob = log_probability(real_translated)
print(real_translated)
print(real_prob)

actual_steps = 0
accepted = False

while actual_steps < 2000:

    if accepted and actual_steps % 10 == 0:
        print("steps:", actual_steps)
        print(translated.split('\n')[0])
        print(log_prob)

    next_mapping = mapping.copy()
    r1, r2 = random.sample(all_characters, 2)

    next_mapping[r1] = mapping[r2]
    next_mapping[r2] = mapping[r1]

    next_translated = translate(next_mapping)
    next_prob = log_probability(next_translated)

    if next_prob > log_prob:
        # Accept
        translated = next_translated
        log_prob = next_prob
        mapping = next_mapping

        actual_steps += 1
        accepted = True
    else:
        #if np.log(random.random()) < next_prob - log_prob:
        if sample_log_prob() < next_prob - log_prob:
            translated = next_translated
            log_prob = next_prob

            mapping = next_mapping

            actual_steps += 1
            accepted = True
        else:
            # Reject
            pass
            accepted = False