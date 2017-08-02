from collections import Counter
from copy import deepcopy
import random
import re


alphabet = "abcdefghijklmnopqrstuvwxyz \n"

# From Wikipedia's MCMC article with a little bit of editing
s = """examples of random walk monte carlo methods include the following:
metropolis–hastings algorithm: this method generates a random walk using a proposal density and a method for rejecting some of the proposed moves.
gibbs sampling: this method requires all the conditional distributions of the target distribution to be sampled exactly.
when drawing from the full-conditional distributions is not straightforward other samplers-within-gibbs are used.
gibbs sampling is popular partly because it does not require any 'tuning'.
slice sampling: this method depends on the principle that one can sample from a distribution by sampling uniformly from the region under the plot of its density function.
it alternates uniform sampling in the vertical direction with uniform sampling from the horizontal 'slice' defined by the current vertical position.
multiple-try metropolis: this method is a variation of the metropolis–hastings algorithm that allows multiple trials at each point.
by making it possible to take larger steps at each iteration, it helps address the curse of dimensionality.
reversible-jump: this method is a variant of the metropolis–hastings algorithm that allows proposals that change the dimensionality of the space
mcmc methods that change dimensionality have long been used in statistical physics applications, where for some problems a distribution that is a grand canonical ensemble is used (e.g., when the number of molecules in a box is variable).
but the reversible-jump variant is useful when doing mcmc or gibbs sampling over nonparametric bayesian models such as those involving the dirichlet process or chinese restaurant process, where the number of mixing components/clusters/etc. is automatically inferred from the data.
"""

s = re.sub('[^' + alphabet + ']', ' ', s)
while '  ' in s:
    s = s.replace('  ', ' ')

print(s)


all_characters = list(Counter(list(s)).keys())
all_characters.remove('\n')
shuffled_characters = deepcopy(all_characters)
random.shuffle(shuffled_characters)

tr = dict(zip(all_characters, shuffled_characters))
tr['\n'] = '\n'

untr = dict(zip(shuffled_characters, all_characters))
untr['\n'] = '\n'


translated_text = ''.join(tr[char] for char in s)

plain_text = ''.join(untr[char] for char in translated_text)

print(translated_text)
print()
print(plain_text)
print()
print("The text has", len(translated_text), "characters.")
print(tr)