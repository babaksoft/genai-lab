from pathlib import Path

DEF_GPT_MODEL = "gpt-4o-mini"
DELIMITER = "````"
MAX_WORDS = 100
MAX_INPUT_LEN = 20_000

PACKAGE_ROOT = Path(__file__).resolve().parent.parent
SAMPLES_DIR = PACKAGE_ROOT / "samples"

SAMPLE_REVIEW_1 = """
This is one of the oddest movies I have watched in a long while. Usually if they are this strange
I bail out early and rarely regret it. Luckily, I held on for this one. While I can't say that this
is a great movie (it isn't), I can say that watching it is rather like a good acid trip - only a few
really awful moments and the rest filled with "did I really just see that?" wonderment. Lots of laugh
out loud moments. A great cast of characters with Meredith Eaton outstanding as the dwarf daughter-in-law
with an attitude. Keep an open mind."""

SAMPLE_REVIEW_2 = """
This was a dreadful, boring movie, even for a documentary. At times, it did provided insight to life
and also had humorous moments, but overall it was not worth seeing. Every time I began to feel
sympathetic towards Mark and began to hope he would be successful, I would become disappointed by his
lack of responsibility and drug and alcohol abuse."""

SAMPLE_STATEMENT_1 = """
I am just fed up of everything. Everything and everyone pisses me off and I have tried
to be happy but that just does not work. I have made plans of suicide for sometime after
i pass my driving test and get a car. Its the only thing i can think of, I have tried self
harm but I am too scared of pain, thought about jumping off a building like my brother tried
but I am a coward and anything else is too painful or I am scared to do it. I know I have not
passed my gcses because i did not try so I probably will not be able to get into college,
I am so negative to everyone around me I am scared I am losing friends. Everything about me
is just a fucking waste, anyone else could have been born in my place and done better, children
are dying in impoverished countries who could have had great potential but people like me were
born who are selfish and useless. I do not know what to title this"""

SAMPLE_STATEMENT_2 = """
I cannot take it anymore. I tried all the advice. I tried reaching out.
It does not change the fact that I just do not belong. I am so sorry.
I think it is the end"""

SAMPLE_STATEMENT_3 = """
Public speaking tips? Hi, all. I have to give a presentation at work next week
(45 minutes long and the CEO will be in attendance). I’m already panicking,
as once the anxiety kicks in, I’m certain I’m going to forget everything I’m
supposed to say. (anxiety makes it very difficult for me to focus on anything)
Does anyone have any speaking tips that have worked for them in the past?
Thanks so much!"""

SAMPLE_TEXT_1 = """
My mind rebels at stagnation. Give me problems, give me work,
give me the most abstruse cryptogram, or the most intricate analysis,
and I am in my own proper atmosphere. But I abhor the dull routine
of existence. I crave for mental exaltation.

Arthur Conan Doyle"""

SAMPLE_TRANS_1 = """
Mon esprit se rebelle face à la stagnation. Donnez-moi des problèmes,
donnez-moi du travail, donnez-moi le cryptogramme le plus abscons,
ou l'analyse la plus complexe, et je suis dans ma propre atmosphère.
Mais je déteste la routine ennuyeuse d'exister. J'ai soif d'exaltation mentale. 

Arthur Conan Doyle"""

SAMPLE_TEXT_2 = """
Ci sono pittori che trasformano il sole in una macchia gialla,
ma ce ne sono altri che con l'aiuto della loro arte e della loro
intelligenza trasformano una macchia gialla in sole.

Pablo Picasso"""

SAMPLE_TRANS_2 = """
There are painters who transform the sun to a yellow spot, but there are
others who with the help of their art and their intelligence, transform
a yellow spot into sun.

Pablo Picasso"""

SAMPLE_MAIL_1 = """
Hello Mr. Colbert,

Thinking about your offer, I'm afraid it doesn't make my ends meet in
the long run : Payment is a little low and I'm sure I can find better
offers if I try. Thanks for the opportunity and best of luck.

Regards,
Barry Rosenfield"""

SAMPLE_MAIL_2 = """
To whom it may concern,

First, let me thank you for the time you allocated for my visa interview.
I think I had a perfectly valid and strong case, and I'd like to know why
my visa application was denied.

If it helps, I've aspired to be a Swedish citizen for quite some time and
will strive to serve my new country any other chance I may be approved.

God bless the king,
Marvin Hackley, Jr."""

SAMPLE_MAIL_3 = """
Hey Emma,

How's it going? You know what, I'm still having this buzz, you know,
from the last time we were together at the party. That was awesome,
baby. I think there may be something we can explore. How about we do
it again and find out?

Cheers,
Brian"""
