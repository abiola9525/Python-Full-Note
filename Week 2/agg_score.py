'''
2.  A university gave a project to create a admission selection programme for them.
The programmer should prompt the user to input his/her name,
after that the program will welcome the user and then prompt the user to
input his/her JAMB score, after the post UTME score and
the program will calculate the aggregate score ((jamb score / 8) + (post-utme score / 2)).
Now the program should be able to tell the user the course he/she can apply for according to his/her aggregate score.

            Outline
0 - 49           Fail
50 - 60          Agric,Botany,Zoology,Biology,Economics
61 - 70          Computer Sci.,Statictics, Physchology,Theatre Art
71 - 80          Vetenary, CLA, Mathe, Biochemistry
81 - above       Medicine, Law, Nursing.
'''


name = str(input("Enter your name: "))
print(f'Welcome {name}')
jamb = int(input("Enter your JAMB Score: "))
p_utme = int(input("Enter your Post UTME Score: "))
agg_score = ((jamb / 8) + (p_utme / 2))
print(f'Your aggregate Score is {agg_score}')

if agg_score <= 49:
    print("Fail")
elif agg_score >= 50 and agg_score <= 60:
    print("Agric")
elif agg_score >= 61 and agg_score:
    pass
