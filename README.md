# captrac
 Legacy code for a high school government class. Interacts with a Google Sheets spreadsheet and implements some rules. OAuth credentials not included, for reasons. The code was poorly optimized, and makes far more API calls than necessary, but I thought I might finally publish it for the memories.
 
# what the?
My AP Government class, as an exercise, was required to propose, discuss, then define the class rules. One suggestion was to give people who came late to class dunce caps. The discussion devolved quite quickly, and soon a ridiculous ruleset surrounding this system emerged: In summary, students would acquire "stacks" every time they were late. These would decay over time, and determined the number of dunce caps to be worn.

Unfortunately, this was vetoed as "too difficult to keep track of" and "unenforceable" by our teacher. I, however, was not deterred from pursuing this silly idea; the spaghetti you see here was the result of the evening of wanton hackery that ensued.

After I introduced captrac, the rule was passed, and the student in charge of taking attendance would also note down who was late that day. This information was then entered into Google Sheets. Once a day, my laptop would run `captrac.py`, which would take this information and update the spreadsheet, which would in turn notify people who needed to be capped. Sadly, no one ever came late to class often enough to make use of the "stacks" from then on.
