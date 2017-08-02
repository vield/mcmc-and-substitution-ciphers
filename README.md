# Super short write-up

I had always been wondering about applications of MCMC methods after learning about them in uni (I'd only worked on artificial practice problems).

Recently, I found a [paper describing their use in solving substitution ciphers](http://statweb.stanford.edu/~cgates/PERSI/papers/MCMCRev.pdf) (as in, each character is mapped to exactly one other character).

This code (more or less) implements what is described in the paper.

## Preparations

To collect statistics about the English language, I used this copy of War and Peace from Project Gutenberg: http://www.gutenberg.org/files/2600/2600-0.txt

I ran it through `collect_transition_probabilities.py` to produce `probs.py`.

I then needed a plaintext to turn into a ciphertext. I used a 1700-ish-character snippet from the Wikipedia MCMC article. See `prepare_known_ciphertext.py`.

## Solving

Finally, I wrote `solve.py` to perform the sampling steps. The initial mappings are random-ish (currently sorted by commonness of occurrence).

Each step consists of randomly picking two characters, swapping their mapping and then, if the mapping is better (by log likelihood), accepting the mapping, or if it is worse, accepting it with a small probability.

On my chosen ciphertext, I got to a legible version in about 90 successful steps (there was one mistake where q and j were mapped wrong).

After 10 steps (still illegible nonsense):

	tdolustea?jaiohn?laposxal?hytafois?altyb?neachfsmntaybtaj?ss
	?pchqawltyi?u?sceaboeychqeaosq?icyblaybcealtyb?naqthtioyteao
	aiohn?laposxamechqaoaui?u?eosanthecyraohnaoaltyb?naj?iaitztf
	ychqae?lta?jaybtaui?u?etnal?vteawqckkeaeoluschqaybcealtyb?na
	it mciteaossaybtaf?hncyc?hosanceyickmyc?hea?jaybtayoiqtyance
	yickmyc?hay?aktaeolustnatdofysrawpbthaniopchqaji?laybtajmssa
	f?hncyc?hosanceyickmyc?heaceah?yaeyiocqbyj?ipoina?ybtiaeolus
	tieapcybchaqckkeaoitametnawqckkeaeoluschqaceau?umsoiauoiysra
	ktfometacyan?teah?yait mcitaohraymhchqawescftaeoluschqaybcea
	ltyb?nantuthnea?haybtauichfcustayboya?htafohaeolustaji?laoan
	ceyickmyc?hakraeoluschqamhcj?ilsraji?laybtaitqc?hamhntiaybta
	us?ya?jacyeanthecyrajmhfyc?hawcyaosytihoyteamhcj?ilaeoluschq
	achaybtavtiycfosancitfyc?hapcybamhcj?ilaeoluschqaji?laybtab?
	icg?hyosaescftantjchtnakraybtafmiithyavtiycfosau?ecyc?hawlms
	ycustayiraltyi?u?sceaybcealtyb?naceaoavoicoyc?ha?jaybtaltyi?
	u?sceaboeychqeaosq?icyblayboyaoss?pealmsycustayicoseaoyatofb
	au?chyawkraloxchqacyau?eeckstay?ayoxtasoiqtiaeytueaoyatofbac
	ytioyc?hacyabtsueaonniteeaybtafmieta?janclthec?hoscyrawitvti
	eckstazmluaybcealtyb?naceaoavoicohya?jaybtaltyi?u?sceaboeych
	qeaosq?icyblayboyaoss?peaui?u?eoseayboyafbohqtaybtanclthec?h
	oscyra?jaybtaeuoftwlflfaltyb?neayboyafbohqtanclthec?hoscyrab
	ovtas?hqaktthametnachaeyoyceycfosaubrecfeaouuscfoyc?heapbtit
	aj?iae?ltaui?kstleaoanceyickmyc?hayboyaceaoaqiohnafoh?hcfosa
	thetlkstaceametnataqapbthaybtahmlktia?jal?stfmsteachaoak?dac
	eavoicokstawkmyaybtaitvtieckstazmluavoicohyaceametjmsapbthan
	?chqalflfa?iaqckkeaeoluschqa?vtiah?huoioltyicfakortecohal?nt
	seaemfbaoeayb?etachv?svchqaybtancicfbstyaui?fteea?iafbchteta
	iteyomiohyaui?fteeapbtitaybtahmlktia?jalcdchqaf?lu?hthyeafsm
	eytieatyfaceaomy?loycfossrachjtiitnaji?laybtanoyoaw


After 90 steps:

	examples of random walk monte carlo methods include the foll
	owing ?metropolis hastings algorithm this method generates a
	 random walk using a proposal density and a method for reqec
	ting some of the proposed moves ?gibbs sampling this method 
	rejuires all the conditional distributions of the target dis
	tribution to be sampled exactly ?when drawing from the full 
	conditional distributions is not straightforward other sampl
	ers within gibbs are used ?gibbs sampling is popular partly 
	because it does not rejuire any tuning ?slice sampling this 
	method depends on the principle that one can sample from a d
	istribution by sampling uniformly from the region under the 
	plot of its density function ?it alternates uniform sampling
	 in the vertical direction with uniform sampling from the ho
	rizontal slice defined by the current vertical position ?mul
	tiple try metropolis this method is a variation of the metro
	polis hastings algorithm that allows multiple trials at each
	 point ?by making it possible to take larger steps at each i
	teration it helps address the curse of dimensionality ?rever
	sible qump this method is a variant of the metropolis hastin
	gs algorithm that allows proposals that change the dimension
	ality of the space?mcmc methods that change dimensionality h
	ave long been used in statistical physics applications where
	 for some problems a distribution that is a grand canonical 
	ensemble is used e g when the number of molecules in a box i
	s variable ?but the reversible qump variant is useful when d
	oing mcmc or gibbs sampling over nonparametric bayesian mode
	ls such as those involving the dirichlet process or chinese 
	restaurant process where the number of mixing components clu
	sters etc is automatically inferred from the data ?

## Future improvement ideas

- Incorporate a dictionary word check to get to the solution faster. After 80 steps, a human was already able to see which remaining characters should be swapped. This could be done with a standard dictionary
- Better initialization (e.g. doing it properly based on initial probabilities)
- Test with texts that contain more special characters (which were omitted in the initial test to keep it simple)
- Compute the likelihood differently, e.g. using "a -> bc" transitions instead of "a -> b" transitions and see if this makes any difference

