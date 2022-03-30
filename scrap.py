Step - 1
Introduction:
The
Given
data
set is Aspiring
Minds
from the Aspiring

Mind
Employment
Outcome
2015(AMEO) and it
contains
approximately
4000
rows and 40
columns
The
dataset
contains
the
employment
outcomes
of
all
engineering
graduates
these
employees
having
different
types
of
deppendent
variables
like
Designation, JobCity, 10
percentage, Salary
etc and the
data
set
contains
the
both
numerical and categorical
data
Step - 2
Import
the
data and display
the
head, shape and description
of
the
data.
import numpy as np
import pandas as pd

df = pd.read_excel("C:\\Users\\hp123\\Downloads\\Data analysis.xlsx")
df
Unnamed: 0
ID
Salary
DOJ
DOL
Designation
JobCity
Gender
DOB
10
percentage...ComputerScience
MechanicalEngg
ElectricalEngg
TelecomEngg
CivilEngg
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
train
203097
420000
2012 - 06 - 01
present
senior
quality
engineer
Bangalore
f
1990 - 02 - 19
84.30... - 1 - 1 - 1 - 1 - 1
0.9737
0.8128
0.5269
1.35490 - 0.4455
1
train
579905
500000
2013 - 0
9 - 01
present
assistant
manager
Indore
m
1989 - 10 - 04
85.40... - 1 - 1 - 1 - 1 - 1 - 0.7335
0.3789
1.2396 - 0.10760
0.8637
2
train
810601
325000
2014 - 06 - 01
present
systems
engineer
Chennai
f
1992 - 0
8 - 03
85.00... - 1 - 1 - 1 - 1 - 1
0.2718
1.7109
0.1637 - 0.86820
0.6721
3
train
267447
1100000
2011 - 07 - 01
present
senior
software
engineer
Gurgaon
m
1989 - 12 - 05
85.60... - 1 - 1 - 1 - 1 - 1
0.0464
0.3448 - 0.3440 - 0.40780 - 0.9194
4
train
343523
200000
2014 - 03 - 01
2015 - 03 - 01
00: 00:00
get
Manesar
m
1991 - 02 - 27
78.00... - 1 - 1 - 1 - 1 - 1 - 0.8810 - 0.2793 - 1.0697
0.09163 - 0.1295
..................................................................
3993
train
47916
280000
2011 - 10 - 01
2012 - 10 - 01
00: 00:00
software
engineer
New
Delhi
m
1987 - 04 - 15
52.09... - 1 - 1 - 1 - 1 - 1 - 0.1082
0.3448
0.2366
0.64980 - 0.9194
3994
train
752781
100000
2013 - 07 - 01
2013 - 07 - 01
00: 00:00
technical
writer
Hyderabad
f
1992 - 0
8 - 27
90.00... - 1 - 1 - 1 - 1 - 1 - 0.3027
0.8784
0.9322
0.77980 - 0.0943
3995
train
355888
320000
2013 - 07 - 01
present
associate
software
engineer
Bangalore
m
1991 - 07 - 03
81.86... - 1 - 1 - 1 - 1 - 1 - 1.5765 - 1.5273 - 1.5051 - 1.31840 - 0.7615
3996
train
947111
200000
2014 - 07 - 01
2015 - 01 - 01
00: 00:00
software
developer
Asifabadbanglore
f
1992 - 03 - 20
78.72...
438 - 1 - 1 - 1 - 1 - 0.1590
0.0459 - 0.4511 - 0.36120 - 0.0943
3997
train
324966
400000
2013 - 02 - 01
present
senior
systems
engineer
Chennai
f
1991 - 02 - 26
70.60... - 1 - 1 - 1 - 1 - 1 - 1.1128 - 0.2793 - 0.6343
1.32553 - 0.6035
3998
rows × 39
columns

df.head()
Unnamed: 0
ID
Salary
DOJ
DOL
Designation
JobCity
Gender
DOB
10
percentage...ComputerScience
MechanicalEngg
ElectricalEngg
TelecomEngg
CivilEngg
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
train
203097
420000
2012 - 06 - 01
present
senior
quality
engineer
Bangalore
f
1990 - 02 - 19
84.3... - 1 - 1 - 1 - 1 - 1
0.9737
0.8128
0.5269
1.35490 - 0.4455
1
train
579905
500000
2013 - 0
9 - 01
present
assistant
manager
Indore
m
1989 - 10 - 04
85.4... - 1 - 1 - 1 - 1 - 1 - 0.7335
0.3789
1.2396 - 0.10760
0.8637
2
train
810601
325000
2014 - 06 - 01
present
systems
engineer
Chennai
f
1992 - 0
8 - 03
85.0... - 1 - 1 - 1 - 1 - 1
0.2718
1.7109
0.1637 - 0.86820
0.6721
3
train
267447
1100000
2011 - 07 - 01
present
senior
software
engineer
Gurgaon
m
1989 - 12 - 05
85.6... - 1 - 1 - 1 - 1 - 1
0.0464
0.3448 - 0.3440 - 0.40780 - 0.9194
4
train
343523
200000
2014 - 03 - 01
2015 - 03 - 01
00: 00:00
get
Manesar
m
1991 - 02 - 27
78.0... - 1 - 1 - 1 - 1 - 1 - 0.8810 - 0.2793 - 1.0697
0.09163 - 0.1295
5
rows × 39
columns

df.shape
df.describe()
ID
Salary
10
percentage
12
graduation
12
percentage
CollegeID
CollegeTier
collegeGPA
CollegeCityID
CollegeCityTier...ComputerScience
MechanicalEngg
ElectricalEngg
TelecomEngg
CivilEngg
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
count
3.998000e+03
3.998000e+03
3998.000000
3998.000000
3998.000000
3998.000000
3998.000000
3998.000000
3998.000000
3998.000000...
3998.000000
3998.000000
3998.000000
3998.000000
3998.000000
3998.000000
3998.000000
3998.000000
3998.000000
3998.000000
mean
6.637945e+05
3.076998e+05
77.925443
2008.087544
74.466366
5156.851426
1.925713
71.486171
5156.851426
0.300400...
90.742371
22.974737
16.478739
31.851176
2.683842 - 0.037831
0.146496
0.002763 - 0.169033 - 0.138110
std
3.632182e+05
2.127375e+05
9.850162
1.653599
10.999933
4802.261482
0.262270
8.167338
4802.261482
0.458489...
175.273083
98.123311
87.585634
104.852845
36.658505
1.028666
0.941782
0.951471
1.007580
1.008075
min
1.124400e+04
3.500000e+04
43.000000
1995.000000
40.000000
2.000000
1.000000
6.450000
2.000000
0.000000... - 1.000000 - 1.000000 - 1.000000 - 1.000000 - 1.000000 - 4.126700 - 5.781600 - 4.600900 - 2.643000 - 7.375700
25 % 3.342842e+05
1.800000e+05
71.680000
2007.000000
66.000000
494.000000
2.000000
66.407500
494.000000
0.000000... - 1.000000 - 1.000000 - 1.000000 - 1.000000 - 1.000000 - 0.713525 - 0.287100 - 0.604800 - 0.868200 - 0.669200
50 % 6.396000e+05
3.000000e+05
79.150000
2008.000000
74.400000
3879.000000
2.000000
71.720000
3879.000000
0.000000... - 1.000000 - 1.000000 - 1.000000 - 1.000000 - 1.000000
0.046400
0.212400
0.091400 - 0.234400 - 0.094300
75 % 9.904800e+05
3.700000e+05
85.670000
2009.000000
82.600000
8818.000000
2.000000
76.327500
8818.000000
1.000000... - 1.000000 - 1.000000 - 1.000000 - 1.000000 - 1.000000
0.702700
0.812800
0.672000
0.526200
0.502400
max
1.298275e+06
4.000000e+06
97.760000
2013.000000
98.700000
18409.000000
2.000000
99.930000
18409.000000
1.000000...
715.000000
623.000000
676.000000
548.000000
516.000000
1.995300
1.904800
2.535400
3.352500
1.822400
8
rows × 27
columns

Data
Manipulation
we
have
to
remove
the
unwanted
coloumns
df.drop("Unnamed: 0", axis=1, inplace=True)
df
ID
Salary
DOJ
DOL
Designation
JobCity
Gender
DOB
10
percentage
10
board...ComputerScience
MechanicalEngg
ElectricalEngg
TelecomEngg
CivilEngg
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
203097
420000
2012 - 06 - 01
present
senior
quality
engineer
Bangalore
f
1990 - 02 - 19
84.30
board
ofsecondary
education, ap... - 1 - 1 - 1 - 1 - 1
0.9737
0.8128
0.5269
1.35490 - 0.4455
1
579905
500000
2013 - 0
9 - 01
present
assistant
manager
Indore
m
1989 - 10 - 04
85.40
cbse... - 1 - 1 - 1 - 1 - 1 - 0.7335
0.3789
1.2396 - 0.10760
0.8637
2
810601
325000
2014 - 06 - 01
present
systems
engineer
Chennai
f
1992 - 0
8 - 03
85.00
cbse... - 1 - 1 - 1 - 1 - 1
0.2718
1.7109
0.1637 - 0.86820
0.6721
3
267447
1100000
2011 - 07 - 01
present
senior
software
engineer
Gurgaon
m
1989 - 12 - 05
85.60
cbse... - 1 - 1 - 1 - 1 - 1
0.0464
0.3448 - 0.3440 - 0.40780 - 0.9194
4
343523
200000
2014 - 03 - 01
2015 - 03 - 01
00: 00:00
get
Manesar
m
1991 - 02 - 27
78.00
cbse... - 1 - 1 - 1 - 1 - 1 - 0.8810 - 0.2793 - 1.0697
0.09163 - 0.1295
..................................................................
3993
47916
280000
2011 - 10 - 01
2012 - 10 - 01
00: 00:00
software
engineer
New
Delhi
m
1987 - 04 - 15
52.09
cbse... - 1 - 1 - 1 - 1 - 1 - 0.1082
0.3448
0.2366
0.64980 - 0.9194
3994
752781
100000
2013 - 07 - 01
2013 - 07 - 01
00: 00:00
technical
writer
Hyderabad
f
1992 - 0
8 - 27
90.00
state
board... - 1 - 1 - 1 - 1 - 1 - 0.3027
0.8784
0.9322
0.77980 - 0.0943
3995
355888
320000
2013 - 07 - 01
present
associate
software
engineer
Bangalore
m
1991 - 07 - 03
81.86
bse, odisha... - 1 - 1 - 1 - 1 - 1 - 1.5765 - 1.5273 - 1.5051 - 1.31840 - 0.7615
3996
947111
200000
2014 - 07 - 01
2015 - 01 - 01
00: 00:00
software
developer
Asifabadbanglore
f
1992 - 03 - 20
78.72
state
board...
438 - 1 - 1 - 1 - 1 - 0.1590
0.0459 - 0.4511 - 0.36120 - 0.0943
3997
324966
400000
2013 - 02 - 01
present
senior
systems
engineer
Chennai
f
1991 - 02 - 26
70.60
cbse... - 1 - 1 - 1 - 1 - 1 - 1.1128 - 0.2793 - 0.6343
1.32553 - 0.6035
3998
rows × 38
columns

df.drop(["DOJ", "DOL", "CollegeCityID", "CollegeCityTier", "Domain", "ComputerProgramming", "ElectronicsAndSemicon",
         "ComputerScience", "MechanicalEngg"
            , "ElectricalEngg", "TelecomEngg", "CivilEngg"], axis=1, inplace=True)
df
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
203097
420000
senior
quality
engineer
Bangalore
f
1990 - 02 - 19
84.30
board
ofsecondary
education, ap
2007
95.80...Andhra
Pradesh
2011
515
585
525
0.9737
0.8128
0.5269
1.35490 - 0.4455
1
579905
500000
assistant
manager
Indore
m
1989 - 10 - 04
85.40
cbse
2007
85.00...Madhya
Pradesh
2012
695
610
780 - 0.7335
0.3789
1.2396 - 0.10760
0.8637
2
810601
325000
systems
engineer
Chennai
f
1992 - 0
8 - 03
85.00
cbse
2010
68.20...Uttar
Pradesh
2014
615
545
370
0.2718
1.7109
0.1637 - 0.86820
0.6721
3
267447
1100000
senior
software
engineer
Gurgaon
m
1989 - 12 - 05
85.60
cbse
2007
83.60...Delhi
2011
635
585
625
0.0464
0.3448 - 0.3440 - 0.40780 - 0.9194
4
343523
200000
get
Manesar
m
1991 - 02 - 27
78.00
cbse
2008
76.80...Uttar
Pradesh
2012
545
625
465 - 0.8810 - 0.2793 - 1.0697
0.09163 - 0.1295
..................................................................
3993
47916
280000
software
engineer
New
Delhi
m
1987 - 04 - 15
52.09
cbse
2006
55.50...Haryana
2010
365
334
475 - 0.1082
0.3448
0.2366
0.64980 - 0.9194
3994
752781
100000
technical
writer
Hyderabad
f
1992 - 0
8 - 27
90.00
state
board
2009
93.00...Telangana
2013
415
410
535 - 0.3027
0.8784
0.9322
0.77980 - 0.0943
3995
355888
320000
associate
software
engineer
Bangalore
m
1991 - 07 - 03
81.86
bse, odisha
2008
65.50...Orissa
2012
475
475
465 - 1.5765 - 1.5273 - 1.5051 - 1.31840 - 0.7615
3996
947111
200000
software
developer
Asifabadbanglore
f
1992 - 03 - 20
78.72
state
board
2010
69.88...Karnataka
2014
450
410
320 - 0.1590
0.0459 - 0.4511 - 0.36120 - 0.0943
3997
324966
400000
senior
systems
engineer
Chennai
f
1991 - 02 - 26
70.60
cbse
2008
68.00...Tamil
Nadu
2012
565
515
464 - 1.1128 - 0.2793 - 0.6343
1.32553 - 0.6035
3998
rows × 26
columns

df.info()
df["JobCity"].value_counts()
df[df.Designation == "get"]
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
4
343523
200000
get
Manesar
m
1991 - 02 - 27
78.00
cbse
2008
76.80...Uttar
Pradesh
2012
545
625
465 - 0.8810 - 0.2793 - 1.0697
0.09163 - 0.1295
332
597966
180000
get - 1
m
1990 - 0
8 - 02
91.80
cbse
2008
82.70...Delhi
2013
580
640
720 - 0.1590
0.8784
0.3174
0.27270
0.4805
350
38162
340000
get
Faridabad
m
1988 - 0
8 - 13
67.67
up
board
2004
73.80...Jharkhand
2010
455
615
725 - 1.9629 - 1.0593 - 0.7794 - 0.17270 - 0.1295
1717
330551
145000
get
Hyderabad
m
1991 - 07 - 29
80.00
ssc
2008
90.60...Telangana
2012
345
495
575
1.5533
1.7488
1.6880 - 1.14220
0.1864
1897
1064862
175000
get
Hyderabad
m
1991 - 02 - 04
87.00
state
board
2009
79.90...Andhra
Pradesh
2013
350
445
295
1.5644 - 1.1196
0.4711
1.16010
0.4805
2140
796296
600000
get
Indore
m
1992 - 01 - 05
91.20
cbse
2010
90.00...Jharkhand
2014
720
655
680 - 1.4517
0.0459 - 1.6807
0.90660
0.0973
2318
1094242
220000
get
Lucknow
m
1992 - 02 - 06
80.20
cbse
2009
64.20...Uttar
Pradesh
2014
500
505
645
1.4208
1.0449 - 0.4511
0.01920
0.6721
2443
1259589
110000
get
kharagpur
m
1993 - 03 - 18
80.00
icse
2010
76.00...Chhattisgarh
2014
735
555
535 - 0.4463 - 0.9531
0.1637
0.01920 - 2.0105
2666
110817
200000
get
Hyderabad
m
1989 - 05 - 15
80.00
ssc
2007
74.53...Telangana
2010
385
345
425 - 0.4173
0.3448
0.3817 - 0.64280
0.9763
2757
1083682
350000
get
Nashik
m
1994 - 01 - 17
90.60
cbse
2011
74.40...Punjab
2015
640
565
715
0.1282
0.2124 - 1.2196 - 0.99500 - 0.2859
3045
35694
180000
get
Sahibabad
m
1989 - 06 - 18
84.80
cbse
2006
85.80...Delhi
2012
475
605
605
0.0464 - 0.1232 - 1.0697
1.00240 - 0.2875
3126
87319
1210000
get
Bhopal
m
1986 - 10 - 27
56.40
0
2006
72.00...Madhya
Pradesh
2010
305
395
455
0.2009 - 0.9033
0.3817
0.29730
0.3444
3594
967009
280000
get
MEERUT
m
1991 - 10 - 15
84.16
cbse
2010
73.40...Uttar
Pradesh
2014
510
475
545 - 0.0154 - 0.6201
0.3174
1.92070 - 0.0943
3980
197796
150000
get
haryana
m
1986 - 0
8 - 05
84.00
cbse
2004
67.00...Haryana
2011
515
575
595 - 1.4992
0.5008 - 0.9245 - 0.64280 - 0.6035
14
rows × 26
columns

df
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
203097
420000
senior
quality
engineer
Bangalore
f
1990 - 02 - 19
84.30
board
ofsecondary
education, ap
2007
95.80...Andhra
Pradesh
2011
515
585
525
0.9737
0.8128
0.5269
1.35490 - 0.4455
1
579905
500000
assistant
manager
Indore
m
1989 - 10 - 04
85.40
cbse
2007
85.00...Madhya
Pradesh
2012
695
610
780 - 0.7335
0.3789
1.2396 - 0.10760
0.8637
2
810601
325000
systems
engineer
Chennai
f
1992 - 0
8 - 03
85.00
cbse
2010
68.20...Uttar
Pradesh
2014
615
545
370
0.2718
1.7109
0.1637 - 0.86820
0.6721
3
267447
1100000
senior
software
engineer
Gurgaon
m
1989 - 12 - 05
85.60
cbse
2007
83.60...Delhi
2011
635
585
625
0.0464
0.3448 - 0.3440 - 0.40780 - 0.9194
4
343523
200000
get
Manesar
m
1991 - 02 - 27
78.00
cbse
2008
76.80...Uttar
Pradesh
2012
545
625
465 - 0.8810 - 0.2793 - 1.0697
0.09163 - 0.1295
..................................................................
3993
47916
280000
software
engineer
New
Delhi
m
1987 - 04 - 15
52.09
cbse
2006
55.50...Haryana
2010
365
334
475 - 0.1082
0.3448
0.2366
0.64980 - 0.9194
3994
752781
100000
technical
writer
Hyderabad
f
1992 - 0
8 - 27
90.00
state
board
2009
93.00...Telangana
2013
415
410
535 - 0.3027
0.8784
0.9322
0.77980 - 0.0943
3995
355888
320000
associate
software
engineer
Bangalore
m
1991 - 07 - 03
81.86
bse, odisha
2008
65.50...Orissa
2012
475
475
465 - 1.5765 - 1.5273 - 1.5051 - 1.31840 - 0.7615
3996
947111
200000
software
developer
Asifabadbanglore
f
1992 - 03 - 20
78.72
state
board
2010
69.88...Karnataka
2014
450
410
320 - 0.1590
0.0459 - 0.4511 - 0.36120 - 0.0943
3997
324966
400000
senior
systems
engineer
Chennai
f
1991 - 02 - 26
70.60
cbse
2008
68.00...Tamil
Nadu
2012
565
515
464 - 1.1128 - 0.2793 - 0.6343
1.32553 - 0.6035
3998
rows × 26
columns

df.drop(df[df["Designation"] == "get"].index, inplace=True)
df
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
203097
420000
senior
quality
engineer
Bangalore
f
1990 - 02 - 19
84.30
board
ofsecondary
education, ap
2007
95.80...Andhra
Pradesh
2011
515
585
525
0.9737
0.8128
0.5269
1.35490 - 0.4455
1
579905
500000
assistant
manager
Indore
m
1989 - 10 - 04
85.40
cbse
2007
85.00...Madhya
Pradesh
2012
695
610
780 - 0.7335
0.3789
1.2396 - 0.10760
0.8637
2
810601
325000
systems
engineer
Chennai
f
1992 - 0
8 - 03
85.00
cbse
2010
68.20...Uttar
Pradesh
2014
615
545
370
0.2718
1.7109
0.1637 - 0.86820
0.6721
3
267447
1100000
senior
software
engineer
Gurgaon
m
1989 - 12 - 05
85.60
cbse
2007
83.60...Delhi
2011
635
585
625
0.0464
0.3448 - 0.3440 - 0.40780 - 0.9194
5
1027655
300000
system
engineer
Hyderabad
m
1992 - 07 - 02
89.92
state
board
2010
87.00...Karnataka
2014
560
555
620 - 0.3027 - 0.6201 - 2.2954 - 0.74150 - 0.8608
..................................................................
3993
47916
280000
software
engineer
New
Delhi
m
1987 - 04 - 15
52.09
cbse
2006
55.50...Haryana
2010
365
334
475 - 0.1082
0.3448
0.2366
0.64980 - 0.9194
3994
752781
100000
technical
writer
Hyderabad
f
1992 - 0
8 - 27
90.00
state
board
2009
93.00...Telangana
2013
415
410
535 - 0.3027
0.8784
0.9322
0.77980 - 0.0943
3995
355888
320000
associate
software
engineer
Bangalore
m
1991 - 07 - 03
81.86
bse, odisha
2008
65.50...Orissa
2012
475
475
465 - 1.5765 - 1.5273 - 1.5051 - 1.31840 - 0.7615
3996
947111
200000
software
developer
Asifabadbanglore
f
1992 - 03 - 20
78.72
state
board
2010
69.88...Karnataka
2014
450
410
320 - 0.1590
0.0459 - 0.4511 - 0.36120 - 0.0943
3997
324966
400000
senior
systems
engineer
Chennai
f
1991 - 02 - 26
70.60
cbse
2008
68.00...Tamil
Nadu
2012
565
515
464 - 1.1128 - 0.2793 - 0.6343
1.32553 - 0.6035
3984
rows × 26
columns

df.drop(df[df["GraduationYear"] == 0].index, inplace=True)
df
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
203097
420000
senior
quality
engineer
Bangalore
f
1990 - 02 - 19
84.30
board
ofsecondary
education, ap
2007
95.80...Andhra
Pradesh
2011
515
585
525
0.9737
0.8128
0.5269
1.35490 - 0.4455
1
579905
500000
assistant
manager
Indore
m
1989 - 10 - 04
85.40
cbse
2007
85.00...Madhya
Pradesh
2012
695
610
780 - 0.7335
0.3789
1.2396 - 0.10760
0.8637
2
810601
325000
systems
engineer
Chennai
f
1992 - 0
8 - 03
85.00
cbse
2010
68.20...Uttar
Pradesh
2014
615
545
370
0.2718
1.7109
0.1637 - 0.86820
0.6721
3
267447
1100000
senior
software
engineer
Gurgaon
m
1989 - 12 - 05
85.60
cbse
2007
83.60...Delhi
2011
635
585
625
0.0464
0.3448 - 0.3440 - 0.40780 - 0.9194
5
1027655
300000
system
engineer
Hyderabad
m
1992 - 07 - 02
89.92
state
board
2010
87.00...Karnataka
2014
560
555
620 - 0.3027 - 0.6201 - 2.2954 - 0.74150 - 0.8608
..................................................................
3993
47916
280000
software
engineer
New
Delhi
m
1987 - 04 - 15
52.09
cbse
2006
55.50...Haryana
2010
365
334
475 - 0.1082
0.3448
0.2366
0.64980 - 0.9194
3994
752781
100000
technical
writer
Hyderabad
f
1992 - 0
8 - 27
90.00
state
board
2009
93.00...Telangana
2013
415
410
535 - 0.3027
0.8784
0.9322
0.77980 - 0.0943
3995
355888
320000
associate
software
engineer
Bangalore
m
1991 - 07 - 03
81.86
bse, odisha
2008
65.50...Orissa
2012
475
475
465 - 1.5765 - 1.5273 - 1.5051 - 1.31840 - 0.7615
3996
947111
200000
software
developer
Asifabadbanglore
f
1992 - 03 - 20
78.72
state
board
2010
69.88...Karnataka
2014
450
410
320 - 0.1590
0.0459 - 0.4511 - 0.36120 - 0.0943
3997
324966
400000
senior
systems
engineer
Chennai
f
1991 - 02 - 26
70.60
cbse
2008
68.00...Tamil
Nadu
2012
565
515
464 - 1.1128 - 0.2793 - 0.6343
1.32553 - 0.6035
3983
rows × 26
columns

df['GraduationYear'].value_counts()
df
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
203097
420000
senior
quality
engineer
Bangalore
f
1990 - 02 - 19
84.30
board
ofsecondary
education, ap
2007
95.80...Andhra
Pradesh
2011
515
585
525
0.9737
0.8128
0.5269
1.35490 - 0.4455
1
579905
500000
assistant
manager
Indore
m
1989 - 10 - 04
85.40
cbse
2007
85.00...Madhya
Pradesh
2012
695
610
780 - 0.7335
0.3789
1.2396 - 0.10760
0.8637
2
810601
325000
systems
engineer
Chennai
f
1992 - 0
8 - 03
85.00
cbse
2010
68.20...Uttar
Pradesh
2014
615
545
370
0.2718
1.7109
0.1637 - 0.86820
0.6721
3
267447
1100000
senior
software
engineer
Gurgaon
m
1989 - 12 - 05
85.60
cbse
2007
83.60...Delhi
2011
635
585
625
0.0464
0.3448 - 0.3440 - 0.40780 - 0.9194
5
1027655
300000
system
engineer
Hyderabad
m
1992 - 07 - 02
89.92
state
board
2010
87.00...Karnataka
2014
560
555
620 - 0.3027 - 0.6201 - 2.2954 - 0.74150 - 0.8608
..................................................................
3993
47916
280000
software
engineer
New
Delhi
m
1987 - 04 - 15
52.09
cbse
2006
55.50...Haryana
2010
365
334
475 - 0.1082
0.3448
0.2366
0.64980 - 0.9194
3994
752781
100000
technical
writer
Hyderabad
f
1992 - 0
8 - 27
90.00
state
board
2009
93.00...Telangana
2013
415
410
535 - 0.3027
0.8784
0.9322
0.77980 - 0.0943
3995
355888
320000
associate
software
engineer
Bangalore
m
1991 - 07 - 03
81.86
bse, odisha
2008
65.50...Orissa
2012
475
475
465 - 1.5765 - 1.5273 - 1.5051 - 1.31840 - 0.7615
3996
947111
200000
software
developer
Asifabadbanglore
f
1992 - 03 - 20
78.72
state
board
2010
69.88...Karnataka
2014
450
410
320 - 0.1590
0.0459 - 0.4511 - 0.36120 - 0.0943
3997
324966
400000
senior
systems
engineer
Chennai
f
1991 - 02 - 26
70.60
cbse
2008
68.00...Tamil
Nadu
2012
565
515
464 - 1.1128 - 0.2793 - 0.6343
1.32553 - 0.6035
3983
rows × 26
columns

df[df.Designation == "associate software engineer"]
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
38
550371
330000
associate
software
engineer
Bangalore
m
1991 - 10 - 02
52.33
state
board
2007
67.00...Uttar
Pradesh
2013
450
525
545 - 0.0154
1.2114
0.6248
0.77980
0.8637
42
895673
350000
associate
software
engineer
Bangalore
m
1991 - 12 - 11
91.40
icse
2010
73.00...Uttar
Pradesh
2014
555
560
825 - 0.0154
0.2578 - 0.5349 - 1.12180 - 1.3590
190
864904
215000
associate
software
engineer
Chennai
m
1991 - 04 - 11
81.20
state
board
2008
80.70...Tamil
Nadu
2012
500
460
235
1.8517
1.2114 - 0.4511 - 1.88240 - 0.4776
249
746050
300000
associate
software
engineer
Bangalore
m
1991 - 03 - 16
78.83
icse
2008
80.50...Uttarakhand
2013
595
520
605 - 0.4463
0.5454
1.3933 - 0.74150
0.8637
343
929120
300000
associate
software
engineer
Bangalore
m
1992 - 0
9 - 28
66.33
state
board
2008
61.00...Uttar
Pradesh
2013
535
510
680
0.2718
0.5454 - 1.5270
0.27270
0.6721
385
984121
300000
associate
software
engineer
Bangalore
f
1992 - 03 - 20
91.60
state
board
2010
86.50...Karnataka
2014
465
510
570 - 0.1590
1.2114
0.4711 - 1.62890
0.0973
439
1264748
205000
associate
software
engineer - 1
m
1992 - 07 - 0
9
74.00
cbse
2010
69.00...Haryana
2014
545
565
415 - 0.1590
0.3789
0.7785 - 1.50210 - 0.2859
632
1077591
240000
associate
software
engineer
Bangalore
m
1989 - 0
8 - 15
87.00
cbse
2008
75.00...Uttar
Pradesh
2013
560
555
535 - 0.5899 - 0.9531
0.0100
0.01920 - 1.0524
831
1094255
320000
associate
software
engineer
pune
m
1991 - 11 - 17
83.30
icse
2009
81.00...Uttar
Pradesh
2014
755
555
605 - 0.1590
0.3789
0.0100 - 0.74150 - 0.8608
885
1152411
315000
associate
software
engineer
Pune
m
1992 - 0
8 - 12
74.00
state
board
2008
71.00...Maharashtra
2014
465
650
655 - 1.7389
0.0459
0.7785 - 1.75560
1.0554
1199
963241
380000
associate
software
engineer
Hyderabad
m
1993 - 0
8 - 22
94.80
state
board
2010
97.40...Telangana
2014
510
450
545
1.1336
0.3789
0.9322 - 2.13600 - 0.6692
1324
624224
300000
associate
software
engineer
Mumbai
m
1991 - 05 - 10
82.60
cbse
2009
76.00...Madhya
Pradesh
2013
370
385
385
1.2772 - 0.2871 - 0.6048 - 1.75560 - 0.0943
1466
1247289
275000
associate
software
engineer
BANGALORE
f
1992 - 02 - 01
68.00
state
board
2008
60.20...West
Bengal
2013
580
540
525
1.2772
0.8784
0.1637
1.41360
1.2470
1608
1035879
385000
associate
software
engineer
Pune
m
1992 - 06 - 24
76.00
state
board
2009
78.00...Maharashtra
2013
360
590
535 - 2.7443 - 1.9521 - 1.9881 - 0.10760 - 1.4356
1778
34472
375000
associate
software
engineer
Noida
m
1988 - 04 - 30
90.20
cbse
2006
82.40...Punjab
2010
645
615
695 - 0.4173
0.1888
0.3817
0.06230
0.0284
1807
1043852
300000
associate
software
engineer - 1
m
1993 - 01 - 26
81.00
cbse
2009
67.70...Punjab
2013
510
480
705
1.2772
0.2124 - 1.2196 - 0.23440
1.2470
1891
965196
305000
associate
software
engineer
Bhubaneswar
f
1993 - 05 - 31
90.00
state
board
2010
74.00...Andhra
Pradesh
2014
520
545
450
0.4155
1.0449 - 0.1437 - 1.24860 - 0.4776
2064
64400
500000
associate
software
engineer
Bangalore
m
1989 - 01 - 22
86.80
central
board
of
secondary
education
2006
78.20...Karnataka
2010
635
535
495 - 0.7264
0.5008
0.2366
0.76730 - 0.2875
2072
963956
390000
associate
software
engineer
Hyderabad
m
1992 - 11 - 0
9
84.83
state
board
2010
93.30...Telangana
2014
675
545
545
1.2772
0.0459
1.5470
0.01920
0.8637
2248
1064536
330000
associate
software
engineer
Hyderabad
m
1992 - 07 - 0
8
68.30
state
board
2009
86.00...Telangana
2013
500
505
585
0.8463
0.0459
0.7785
0.65300
1.4386
2378
846398
300000
associate
software
engineer
Mumbai
f
1993 - 01 - 23
77.80
cbse
2010
79.20...Punjab
2014
405
525
415
0.2718
0.0459 - 0.6048 - 0.10760
0.0973
2387
553852
330000
associate
software
engineer - 1
m
1992 - 12 - 05
79.20
cbse
2009
76.60...Delhi
2013
545
560
665
0.9900
1.0449
0.1637 - 0.86820
0.2889
2444
1092991
315000
associate
software
engineer
Bangalore
m
1993 - 02 - 12
75.40
state
board
2009
68.80...Madhya
Pradesh
2014
440
565
430
1.7081
0.7119
1.2396 - 1.88240 - 0.2859
2479
823293
450000
associate
software
engineer
Pune
m
1991 - 10 - 11
75.40
cbse
2009
65.20...Punjab
2014
590
555
560 - 1.3080 - 0.6201
0.1637
0.39950 - 1.0524
2516
1093551
305000
associate
software
engineer
Pune
m
1991 - 11 - 29
76.40
cbse
2010
73.80...Madhya
Pradesh
2014
560
435
440 - 2.0262
0.5454 - 0.4511
0.65300 - 0.2859
2556
304341
315000
associate
software
engineer
Pune
m
1989 - 07 - 04
70.00
nashik
board
2007
72.00...Maharashtra
2011
435
485
565 - 1.1901 - 0.2793
0.2366 - 0.17270 - 0.2875
2596
1088319
610000
associate
software
engineer
Hyderabad
m
1990 - 10 - 04
86.00
cbse
2009
81.60...Rajasthan
2014
805
580
620
0.2718
0.8784
0.1637 - 1.24860
1.0554
2601
1194943
200000
associate
software
engineer
Noida
m
1992 - 07 - 07
71.04
icse
2010
81.33...Uttar
Pradesh
2014
335
540
415
1.2772
0.2124
0.3174
2.17430
1.0554
2781
1029602
345000
associate
software
engineer
Hyderabad
m
1992 - 11 - 0
8
88.10
state
board
2009
88.10...Telangana
2013
560
510
520
1.1336
1.3779
0.0100 - 2.26270 - 0.0943
2921
322718
110000
associate
software
engineer - 1
m
1990 - 01 - 26
72.00
bihar
school
examination
board
2006
64.00...Orissa
2012
405
485
495 - 1.6538 - 1.8393 - 0.9245
1.35490 - 0.5245
2939
954255
330000
associate
software
engineer
Hyderabad
m
1992 - 10 - 31
88.00
state
board
2010
90.00...Telangana
2014
580
470
555
0.2718
0.0459
0.6248 - 1.88240
1.0554
2944
781935
70000
associate
software
engineer
Bhubaneswar
f
1991 - 10 - 0
9
81.00
cbse
2008
53.00...Orissa
2013
615
645
470 - 0.3027
0.5454
1.2396
0.77980 - 0.2859
3012
901224
315000
associate
software
engineer
Bengaluru
f
1993 - 07 - 05
85.76
state
board
2010
83.83...Karnataka
2014
520
630
560 - 1.5953 - 1.4859 - 1.7086 - 0.48790 - 1.9234
3107
1166135
305000
associate
software
engineer
Bangalore
f
1992 - 11 - 06
90.00
state
board
2010
90.00...Andhra
Pradesh
2014
595
495
510
1.2772
1.5444
2.1617 - 0.10760
0.8637
3225
1230200
300000
associate
software
engineer
Bangalore
m
1990 - 07 - 12
65.00
state
board
2008
65.40...Uttar
Pradesh
2014
490
615
725 - 0.3027 - 0.7866 - 1.5270
1.92070 - 1.6273
3403
664758
300000
associate
software
engineer
Bangalore
f
1989 - 02 - 11
73.00
cbse
2006
74.00...Haryana
2013
285
560
545
0.5591 - 0.1206 - 0.7585 - 0.74150
0.0973
3426
460251
310000
associate
software
engineer - 1
m
1986 - 05 - 27
67.00
j & k
state
board
of
school
education
2004
53.16...Punjab
2012
565
475
475
0.5100
0.8128 - 0.3440 - 1.11280
1.0158
3478
796891
300000
associate
software
engineer
Bangalore
f
1992 - 07 - 0
8
93.00
cbse
2010
89.40...Rajasthan
2014
545
585
575 - 0.0154
1.2114
0.9322
1.54040
0.8637
3519
346596
220000
associate
software
engineer
Bangalore
m
1989 - 11 - 14
69.40
icse
2008
65.12...Karnataka
2012
585
645
475 - 0.5332
0.5008 - 0.9245 - 0.26090 - 0.9194
3561
338449
180000
associate
software
engineer - 1
m
1990 - 11 - 26
69.00
state
board
2009
81.40...Madhya
Pradesh
2013
425
515
565 - 1.2287
0.3448
0.3817
0.53233 - 0.6035
3583
986780
210000
associate
software
engineer
Delhi
m
1992 - 05 - 15
71.00
cbse
2009
60.00...Uttar
Pradesh
2014
315
505
510 - 1.3080 - 0.7866 - 0.9122 - 0.23440 - 0.8608
3775
1066890
180000
associate
software
engineer - 1
m
1992 - 0
8 - 03
84.00
state
board
2009
84.00...Tamil
Nadu
2013
475
375
390
1.2772
1.7109
1.7007 - 2.13600
0.4805
3827
711329
375000
associate
software
engineer
Noida
f
1992 - 07 - 31
80.20
cbse
2009
74.80...Uttar
Pradesh
2013
555
535
430
0.2718
0.8784 - 1.3733 - 0.86820
1.0554
3856
379339
400000
associate
software
engineer
Noida
m
1988 - 11 - 23
63.20
cbse
2007
63.20...Uttar
Pradesh
2012
495
395
585 - 0.7335 - 1.6191 - 1.3733
0.39950 - 1.4356
3930
1087768
315000
associate
software
engineer
New
Delhi
m
1992 - 0
9 - 24
83.60
cbse
2010
73.40...Haryana
2014
525
420
500
1.4208
1.7109
1.7007 - 2.26270 - 1.4356
3995
355888
320000
associate
software
engineer
Bangalore
m
1991 - 07 - 03
81.86
bse, odisha
2008
65.50...Orissa
2012
475
475
465 - 1.5765 - 1.5273 - 1.5051 - 1.31840 - 0.7615
46
rows × 26
columns

df["Designation"].value_counts()
df.Designation = df.Designation.apply(lambda x: x.replace('ase', 'application support engineer'))
df.Designation
df[df.Designation == "ase"]
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
rows × 26
columns

df['JobCity'] = df['JobCity'].apply(lambda x: str(x))
df['JobCity'].dtype
df['Salary'].dtype
df.JobCity = df["JobCity"].apply(lambda x: x.replace('-1', 'India') if '-1' in x else x)

df.JobCity = df['JobCity']
df['JobCity']
df['JobCity'].head(50)
df['JobCity'].value_counts()
df['JobCity'] = df['JobCity'].apply(lambda x: x.upper())
df['JobCity'] = df['JobCity'].apply(lambda x: x.lstrip())
df['JobCity'] = df['JobCity'].apply(lambda x: x.rstrip())
y = df["JobCity"].unique()
y.sort()
df['JobCity'] = df['JobCity'].replace(to_replace='A-64,SEC-64,NOIDA', value='NOIDA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='AL JUBAIL,SAUDI ARABIA', value='INDIA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='AM', value='AMBALA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='AMBALA CITY', value='AMBALA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='AUSTRALIA', value='INDIA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='BANAGALORE', value='BANGALORE', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='BANAGLORE', value='BANGALORE', regex=False)

df['JobCity'] = df['JobCity'].replace(to_replace='ASIFABADBANGLORE', value='BANGALORE', regex=False)

df['JobCity'] = df['JobCity'].replace(to_replace='BENGALURU', value='BANGALORE', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='BANGLORE', value='BANGALORE', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='BHUBANESHWAR', value='BHUBANESWAR', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='BHUBNESHWAR', value='BHUBANESWAR', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='CHENNAI & MUMBAI', value='CHENNAI', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='CHENNAI, BANGALORE', value='CHENNAI', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='DELHI/NCR', value='DELHI', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='DUBAI', value='INDIA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='GAZIABAAD', value='GHAZIABAD', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='GAZIBAAD', value='GHAZIABAD', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='INDIRAPURAM, GHAZIABAD', value='GHAZIABAD', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='GANDHINAGAR', value='GANDHI NAGAR', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='GREATER NOIDA', value='NOIDA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='GURAGAON', value='GURGAON', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='GURGA', value='GURGAON', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='GURGOAN', value='GURGAON', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='HDERABAD', value='HYDERABAD', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='HYDERABAD(BHADURPALLY)', value='HYDERABAD', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='JEDDAH SAUDI ARABIA', value='INDIA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='KOCHI/COCHIN', value='KOCHI', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='KOCHI/COCHIN, CHENNAI AND COIMBATORE', value='KOCHI', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='KOLKATA`', value='KOLKATA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='KUDANKULAM ,TARAPUR', value='KUDANKULAM', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='LATUR (MAHARASHTRA )', value='LATUR', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='LONDON', value='INDIA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='METTUR, TAMIL NADU', value='METTUR', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='MUZAFFARNAGAR', value='MUZAFFARPUR', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='MUZZAFARPUR', value='MUZAFFARPUR', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='NAVI MUMBAI', value='MUMBAI', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='NAVI MUMBAI , HYDERABAD', value='MUMBAI', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='NEW DEHLI', value='DELHI', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='NEW DELHI', value='DELHI', regex=False)

df['JobCity'] = df['JobCity'].replace(to_replace='DEHLI', value='DELHI', regex=False)

df['JobCity'] = df['JobCity'].replace(to_replace='NEW DELHI - JAISALMER', value='DEHLI', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='NOUDA', value='NOIDA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='PONDI', value='PONDICHERRY', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='PONDY', value='PONDICHERRY', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='PUNR', value='PUNE', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='RAYAGADA, ODISHA', value='ODISHA', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='ORISSA', value='ODISHA', regex=False)

df['JobCity'] = df['JobCity'].replace(to_replace='SADULPUR,RAJGARH,DISTT-CHURU,RAJASTHAN', value='RAJASTHAN',
                                      regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='SONIPAT', value='SONEPAT', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='TIRUPATI', value='TIRUPATHI', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='TECHNOPARK, TRIVANDRUM', value='TRIVANDRUM', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='UNA', value='UNNAO', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='VIZAG', value='VISAKHAPATNAM', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='VSAKHAPTTNAM', value='VISAKHAPATNAM', regex=False)
df['JobCity'] = df['JobCity'].replace(to_replace='KALMAR, SWEDEN', value='INDIA', regex=False)
len(df["JobCity"].unique())
df["Designation"].value_counts()
x = df["Designation"].unique()
x.sort()
df['Designation'] = df['Designation'].replace(to_replace='dotnet developer', value='.net developer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='.net web developer', value='.net developer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='assistant system engineer - trainee',
                                              value='assistant system engineer trainee', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='assistant systems engineer',
                                              value='assistant system engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='associate software engg', value='associate software engineer',
                                              regex=False)
df['Designation'] = df['Designation'].replace(to_replace='business development managerde',
                                              value='business development manager', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='business systems analyst', value='business system analyst',
                                              regex=False)
df['Designation'] = df['Designation'].replace(to_replace='co faculty', value='computer faculty', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='db2 dba',
                                              value='databapplication support engineer administrator', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='dba', value='databapplication support engineer administrator',
                                              regex=False)
df['Designation'] = df['Designation'].replace(to_replace='executive engg', value='executive engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='front end web developer', value='front end developer',
                                              regex=False)
df['Designation'] = df['Designation'].replace(to_replace='graduate trainee engineer', value='graduate engineer trainee',
                                              regex=False)

df['Designation'] = df['Designation'].replace(to_replace='hr executive', value='executive hr', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='jr. software engineer', value='junior software engineer',
                                              regex=False)
df['Designation'] = df['Designation'].replace(to_replace='operations engineer and jetty handling',
                                              value='operations engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='qa analyst', value='quality analyst', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='qa engineer', value='quality engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='qa trainee', value='quality trainee', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='r & d', value='r&d engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='rf/dt engineer', value='rf engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='sales and service engineer', value='sales & service engineer',
                                              regex=False)
df['Designation'] = df['Designation'].replace(to_replace='seo', value='seo analyst', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='software devloper', value='software developer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='software eng', value='software engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='software engg', value='software engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='software engineere', value='software engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='software enginner', value='software engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='software test engineer (etl)', value='software test engineer',
                                              regex=False)
df['Designation'] = df['Designation'].replace(to_replace='software test engineerte', value='software test engineer',
                                              regex=False)
df['Designation'] = df['Designation'].replace(to_replace='sr. engineer', value='senior engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='team leader', value='team lead', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='systems analyst', value='system analyst', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='systems administrator', value='system administrator',
                                              regex=False)
df['Designation'] = df['Designation'].replace(to_replace='testing engineer', value='test engineer', regex=False)
df['Designation'] = df['Designation'].replace(to_replace='web designer and joomla administrator', value='web designer',
                                              regex=False)
df['Designation'] = df['Designation'].replace(to_replace='web designer and seo', value='web designer', regex=False)
df['Specialization'] = df['Specialization'].replace(to_replace='electronics & instrumentation eng',
                                                    value='electronics and instrumentation engineering', regex=False)
len(df["Designation"].unique())

df["Specialization"].value_counts()

df["10board"].value_counts()
df["10board"] = df["10board"].apply(lambda x: str(x))
df["10board"] = df["10board"].apply(lambda x: x.replace("0", "Indian Board of Secondary Education") if "0" in x else x)
df["10board"].value_counts()
df["12board"].value_counts()
df["12board"] = df["12board"].apply(lambda x: str(x))
df["12board"] = df["12board"].apply(lambda x: x.replace("0", "Indian Board of Secondary Education") if "0" in x else x)
df["12board"].value_counts()
df.head()
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
203097
420000
senior
quality
engineer
BANGALORE
f
1990 - 02 - 19
84.30
board
ofsecondary
education, ap
2007
95.8...Andhra
Pradesh
2011
515
585
525
0.9737
0.8128
0.5269
1.3549 - 0.4455
1
579905
500000
assistant
manager
INDORE
m
1989 - 10 - 04
85.40
cbse
2007
85.0...Madhya
Pradesh
2012
695
610
780 - 0.7335
0.3789
1.2396 - 0.1076
0.8637
2
810601
325000
systems
engineer
CHENNAI
f
1992 - 0
8 - 03
85.00
cbse
2010
68.2...Uttar
Pradesh
2014
615
545
370
0.2718
1.7109
0.1637 - 0.8682
0.6721
3
267447
1100000
senior
software
engineer
GURGAON
m
1989 - 12 - 05
85.60
cbse
2007
83.6...Delhi
2011
635
585
625
0.0464
0.3448 - 0.3440 - 0.4078 - 0.9194
5
1027655
300000
system
engineer
HYDERABAD
m
1992 - 07 - 02
89.92
state
board
2010
87.0...Karnataka
2014
560
555
620 - 0.3027 - 0.6201 - 2.2954 - 0.7415 - 0.8608
5
rows × 26
columns

The
cleaned
Data
set
removed
unwanted
rows and columns
df.head()
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
203097
420000
senior
quality
engineer
BANGALORE
f
1990 - 02 - 19
84.30
board
ofsecondary
education, ap
2007
95.8...Andhra
Pradesh
2011
515
585
525
0.9737
0.8128
0.5269
1.3549 - 0.4455
1
579905
500000
assistant
manager
INDORE
m
1989 - 10 - 04
85.40
cbse
2007
85.0...Madhya
Pradesh
2012
695
610
780 - 0.7335
0.3789
1.2396 - 0.1076
0.8637
2
810601
325000
systems
engineer
CHENNAI
f
1992 - 0
8 - 03
85.00
cbse
2010
68.2...Uttar
Pradesh
2014
615
545
370
0.2718
1.7109
0.1637 - 0.8682
0.6721
3
267447
1100000
senior
software
engineer
GURGAON
m
1989 - 12 - 05
85.60
cbse
2007
83.6...Delhi
2011
635
585
625
0.0464
0.3448 - 0.3440 - 0.4078 - 0.9194
5
1027655
300000
system
engineer
HYDERABAD
m
1992 - 07 - 02
89.92
state
board
2010
87.0...Karnataka
2014
560
555
620 - 0.3027 - 0.6201 - 2.2954 - 0.7415 - 0.8608
5
rows × 26
columns

Data
Visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')
df
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
203097
420000
senior
quality
engineer
BANGALORE
f
1990 - 02 - 19
84.30
board
ofsecondary
education, ap
2007
95.80...Andhra
Pradesh
2011
515
585
525
0.9737
0.8128
0.5269
1.35490 - 0.4455
1
579905
500000
assistant
manager
INDORE
m
1989 - 10 - 04
85.40
cbse
2007
85.00...Madhya
Pradesh
2012
695
610
780 - 0.7335
0.3789
1.2396 - 0.10760
0.8637
2
810601
325000
systems
engineer
CHENNAI
f
1992 - 0
8 - 03
85.00
cbse
2010
68.20...Uttar
Pradesh
2014
615
545
370
0.2718
1.7109
0.1637 - 0.86820
0.6721
3
267447
1100000
senior
software
engineer
GURGAON
m
1989 - 12 - 05
85.60
cbse
2007
83.60...Delhi
2011
635
585
625
0.0464
0.3448 - 0.3440 - 0.40780 - 0.9194
5
1027655
300000
system
engineer
HYDERABAD
m
1992 - 07 - 02
89.92
state
board
2010
87.00...Karnataka
2014
560
555
620 - 0.3027 - 0.6201 - 2.2954 - 0.74150 - 0.8608
..................................................................
3993
47916
280000
software
engineer
DELHI
m
1987 - 04 - 15
52.09
cbse
2006
55.50...Haryana
2010
365
334
475 - 0.1082
0.3448
0.2366
0.64980 - 0.9194
3994
752781
100000
technical
writer
HYDERABAD
f
1992 - 0
8 - 27
90.00
state
board
2009
93.00...Telangana
2013
415
410
535 - 0.3027
0.8784
0.9322
0.77980 - 0.0943
3995
355888
320000
associate
software
engineer
BANGALORE
m
1991 - 07 - 03
81.86
bse, odisha
2008
65.50...Orissa
2012
475
475
465 - 1.5765 - 1.5273 - 1.5051 - 1.31840 - 0.7615
3996
947111
200000
software
developer
BANGALORE
f
1992 - 03 - 20
78.72
state
board
2010
69.88...Karnataka
2014
450
410
320 - 0.1590
0.0459 - 0.4511 - 0.36120 - 0.0943
3997
324966
400000
senior
systems
engineer
CHENNAI
f
1991 - 02 - 26
70.60
cbse
2008
68.00...Tamil
Nadu
2012
565
515
464 - 1.1128 - 0.2793 - 0.6343
1.32553 - 0.6035
3983
rows × 26
columns

df.describe()
ID
Salary
10
percentage
12
graduation
12
percentage
CollegeID
CollegeTier
collegeGPA
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
count
3.983000e+03
3.983000e+03
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
3983.000000
mean
6.640845e+05
3.076874e+05
77.911396
2008.087873
74.453979
5152.548079
1.925935
71.485900
2012.609842
501.591263
501.441627
513.137334 - 0.037777
0.147023
0.003720 - 0.170104 - 0.138242
std
3.629123e+05
2.125035e+05
9.850298
1.651540
11.009006
4800.865391
0.261909
8.172179
1.314228
104.814965
86.719266
122.242349
1.028459
0.942175
0.951684
1.008065
1.008970
min
1.124400e+04
3.500000e+04
43.000000
1995.000000
40.000000
2.000000
1.000000
6.450000
2007.000000
180.000000
195.000000
120.000000 - 4.126700 - 5.781600 - 4.600900 - 2.643000 - 7.375700
25 % 3.343240e+05
1.800000e+05
71.665000
2007.000000
66.000000
494.000000
2.000000
66.400000
2012.000000
425.000000
445.000000
430.000000 - 0.700650 - 0.287100 - 0.604800 - 0.868200 - 0.669200
50 % 6.396640e+05
3.000000e+05
79.000000
2008.000000
74.400000
3879.000000
2.000000
71.720000
2013.000000
500.000000
505.000000
515.000000
0.046400
0.212400
0.091400 - 0.234400 - 0.094300
75 % 9.904660e+05
3.700000e+05
85.665000
2009.000000
82.600000
8811.000000
2.000000
76.345000
2014.000000
570.000000
565.000000
595.000000
0.702700
0.812800
0.672000
0.526200
0.502400
max
1.298275e+06
4.000000e+06
97.760000
2013.000000
98.700000
18409.000000
2.000000
99.930000
2017.000000
875.000000
795.000000
900.000000
1.995300
1.904800
2.535400
3.352500
1.822400
df["Gender"].value_counts()
Step - 3 - Univariate
Analysis
Numerical
columns
PDF
Histograms
Boxplots
Countplots
etc..
kdeplot in all
educational
percentages
fig = plt.subplots(figsize=(7, 4))
sns.kdeplot(data=df, x="10percentage", color="k")

this
kdeplot
shows
the
dencity
of
the
10
percentage
of
each
employee
its
shows
like
a
left
skewed and the
most
of
the
employee
's are 10percentage is approximatly 80 percentage
fig = plt.subplots(figsize=(7, 4))
sns.kdeplot(data=df, x="12percentage", color="k")

this
kdeplot
shows
the
dencity
of
the
12
percentage
of
each
employee
its
shows
like
a
normal
distribution and the
most
of
the
employee
's are 12percentage is approximatly 70-80 percentage
fig = plt.subplots(figsize=(7, 4))
sns.kdeplot(data=df, x="collegeGPA", color="k")

this
kdeplot
shows
the
dencity
of
the
collegeGPA
of
each
employee
it is a
normal
distribution and the
most
of
the
employee
's are collegeGPA is approximatly 65-75
Histogram in Passed
out
years
fig = plt.subplots(figsize=(10, 5))
plt.xticks(rotation=90)
sns.histplot(data=df, x="12graduation", color="r")

This
hisogram
tells
about
the
most
of
the
employee
's are passed out in year 2009 in 12graduation
fig = plt.subplots(figsize=(10, 5))
plt.xticks(rotation=90)
sns.histplot(data=df, x="GraduationYear", color="r")

This
hisogram
tells
about
the
most
of
the
employee
's are passed out in year 2013 in Graduation year
Boxplot in General
intelligence
fig = plt.subplots(figsize=(7, 4))
plt.boxplot(df['English'])
plt.show()

This
Box
plot
tells
abouts
the
English
coloumn
it
shows
the
marks
of
each
employee and this
coloumn
have
the
many
outliers
like
high
extream
outliers and low
extream
outliers
fig = plt.subplots(figsize=(7, 4))
plt.boxplot(df['Logical'])
plt.show()

This
Box
plot
tells
abouts
the
Logical
coloumn
it
shows
the
marks
of
each
employee and this
coloumn
have
the
many
outliers
like
high
extream
outliers and low
extream
outliers
fig = plt.subplots(figsize=(7, 4))
plt.boxplot(df['Quant'])
plt.show()

This
Box
plot
tells
abouts
the
Quant
coloumn
it
shows
the
marks
of
each
employee and this
coloumn
have
the
many
outliers
like
high
extream
outliers and low
extream
outliers
countplot in categorical
coloumns
fig = plt.subplots(figsize=(50, 20))
plt.xticks(rotation=90)
sns.countplot(df['JobCity'])

This
countplot
tells
the
most
of
the
employees
are
working in Bangalore and Less
employees
are
working in Rajpura
fig = plt.subplots(figsize=(10, 7))

sns.countplot(df['Degree'])

This
countplot
tells
about
the
all
the
employee
's are which stream in the Degree coloumn
fig = plt.subplots(figsize=(20, 10))
plt.xticks(rotation=90)
sns.countplot(x=df['CollegeState'])

This
countplot
tells
about
the
college
state
employee
's are from they are studied which state and the most of the employee'
s
are
from Uttar pradesh

Step - 4 - Bivariate
analysis
on
Numeric
columns
Scatter
plots,
hexbin
plots,
pair
plots, etc..
Scatterplot
on
Specialization, Salary
comparing
the
Gender
fig = plt.subplots(figsize=(15, 7))
plt.xticks(rotation=90)
sns.scatterplot(x="Specialization", y="Salary", data=df, hue="Gender", hue_order=['m', 'f'])

This
scatter
plot
tells
about
the
specialization and salary
of
the
employee
's and Gender how many employee'
s
are
from male and the
how
many
employee
's are from female
Hexbinplot
on
Salary, collegeGPA
fig = plt.subplots(figsize=(10, 7))
plt.hexbin(x='Salary', y='collegeGPA', data=df, cmap='icefire_r')

sns.pairplot(df, x_vars=["10percentage", "12percentage", "collegeGPA"],
             y_vars=["10percentage", "12percentage", "collegeGPA"],
             hue="Gender")

This
pair
plot
tells
about
the
all
the
employee
's percentages and it shows the difference of male and female
Categorical and numerical
coloumns
fig = plt.subplots(figsize=(10, 7))
sns.swarmplot(data=df, x='Degree', y='collegeGPA')

This
swarmplot
tells
about
the
Degree and collegeGPA and most
of
the
employee
's are from B.E/B.Tech
fig = plt.subplots(figsize=(10, 6))
sns.barplot(x="Degree", y="Salary", data=df)

This
barplot
tells
about
the
salary and Degree
most
of
the
salary
got
M.Tech / M.E
employee
's
fig = plt.subplots(figsize=(12, 6))
sns.boxplot(x="Degree", y="collegeGPA", data=df)

This
Boxplot
tells
about
the
Degree and collegeGPA
M.sc(Tech)
employee
's having there is no outliers all the remaining streams are having extream outliers

Step - 5 - Research
Questions
Times
of
India
article
dated
Jan
18, 2019
states
that “After
doing
your
Computer
Science
Engineering if you
take
up
jobs as a
Programming
Analyst, Software
Engineer, Hardware
Engineer and Associate
Engineer
you
can
earn
up
to
2.5 - 3
lakhs as a
fresh
graduate.” Test
this
claim
with the data given to you.

df_R = df[(df["Designation"] == "programmer analyst") | (df["Designation"] == "software engineer") | (
            df["Designation"] == "hardware engineer")
          | (df["Designation"] == "associate engineer")]
df_R
ID
Salary
Designation
JobCity
Gender
DOB
10
percentage
10
board
12
graduation
12
percentage...CollegeState
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
19
466888
325000
software
engineer
PUNE
f
1990 - 11 - 30
79.00
cbse
2008
62.20...Uttar
Pradesh
2012
485
445
435
0.8192
0.2668 - 0.2714 - 0.40780 - 0.1295
20
140069
320000
software
engineer
BANGALORE
f
1988 - 07 - 25
91.20
karnataka
secondary
school
of
examination
2006
84.63...Karnataka
2010
455
535
445 - 0.1082
0.9688
0.5269 - 0.29020
0.3444
21
339689
200000
software
engineer
INDIA
f
1991 - 0
8 - 20
75.67
up
2007
74.40...Uttar
Pradesh
2012
385
555
445 - 1.0355 - 0.5913 - 1.3599
0.06223 - 1.3539
24
963123
335000
programmer
analyst
HYDERABAD
m
1993 - 06 - 28
88.00
state
board
2010
90.00...Telangana
2014
625
555
630
0.4155
0.8027
0.1357 - 0.99500 - 0.6692
31
1094324
340000
software
engineer
BANGALORE
m
1992 - 10 - 23
77.20
state
board
2010
86.10...Tamil
Nadu
2014
560
485
450 - 0.0154
1.2114
1.0859 - 1.50210
0.2889
..................................................................
3979
212055
550000
software
engineer
BANGALORE
m
1989 - 07 - 22
69.16
up
board
2006
65.66...Uttar
Pradesh
2013
395
435
645 - 0.5719
0.5008 - 0.4891
0.41480 - 1.2354
3981
1077872
220000
software
engineer
GURGAON
m
1991 - 12 - 17
53.40
cbse
2009
65.40...Madhya
Pradesh
2013
560
420
645
0.1282 - 0.2871 - 0.1437 - 1.12180
1.4386
3984
305041
480000
software
engineer
GURGAON
f
1990 - 01 - 18
89.80
cbse
2007
83.80...Haryana
2011
535
455
525 - 0.2628
0.1888
0.3817 - 0.29020
1.6082
3989
1204604
300000
software
engineer
BANGALORE
m
1991 - 11 - 23
74.88
state
board
2010
82.55...Karnataka
2014
500
480
500
0.1282
0.0459
1.2396
1.03330
0.6721
3993
47916
280000
software
engineer
DELHI
m
1987 - 04 - 15
52.09
cbse
2006
55.50...Haryana
2010
365
334
475 - 0.1082
0.3448
0.2366
0.64980 - 0.9194
697
rows × 26
columns

df_R["Salary"]

ab = df_R["Salary"]
bc = []
for i in ab:
    bc.append(i)
print(bc)

import random

n = 40
cd = random.sample(bc, n)
print(cd)


def t_score(sample_size, sample_mean, pop_mean, sample_std):
    numerator = sample_mean - pop_mean
    denomenator = sample_std / sample_size ** 0.5
    return numerator / denomenator


import numpy as np
import statistics
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import t, norm

sum(cd) / len(cd)
statistics.stdev(cd)
sample_size = 100
sample_mean = 332250.0
pop_mean = 300000
sample_std = 89621.3
t_value = t_score(sample_size, sample_mean, pop_mean, sample_std)

print(t_value)
confidence_level = 0.95

alpha = 1 - confidence_level

t_critical = t.ppf(1 - alpha / 2, df=99)

print(t_critical)
x_min = -200000
x_max = 800000

mean = pop_mean
std = sample_std

x = np.linspace(x_min, x_max, 100)
y = norm.pdf(x, mean, std)
plt.xlim(x_min, x_max)
plt.plot(x, y)

t_critical_left = pop_mean + (-t_critical * std)
t_critical_right = pop_mean + (t_critical * std)

x1 = np.linspace(x_min, t_critical_left, 100)
y1 = norm.pdf(x1, mean, std)
plt.fill_between(x1, y1, color='red')

x2 = np.linspace(t_critical_right, x_max, 100)
y2 = norm.pdf(x2, mean, std)
plt.fill_between(x2, y2, color='red')

plt.scatter(sample_mean, 0)
plt.annotate("x_bar", (sample_mean, 0.7))

if (t_value < t_critical):
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")
p_value = 2 * (1.0 - norm.cdf(np.abs(t_value)))

print("p_value = ", p_value)

if (p_value > alpha):
    print("Reject Null Hypothesis")
else:
    print("Fail to reject Null Hypothesis")

Step - 6 - Conclusion
Data
understanding:
The
dataset
contains
the
employment
outcomes
of
engineering
graduates as dependent
variables(Salary, Job
Titles, and Job
Locations) along
with the standardized scores from three different areas – cognitive skills, technical skills and personality skills.
Data
manipulation:
Here
i
am
obeserving
the
Data
set
contains
the
4000
rows and 40
columns and the
this
data
set
having
so
many
duplicate
values and frist
we
to
manipulate
the
data
set and remove
unwanted
rows and columns
after
that
check
the
any
nan
values
are
there or not and after
to
take
the
cleaned
data
set
do
visualization
Data
Visualization:
Univariate
Analysis -> PDF, Histograms, Boxplots, Countplots
univariate
analysis
having
many
plots and it
shows
the
probability and frequency
distribution
Bivariate
Analysis -> Scatterplot, hexbinplot, pairplot, swarmplot, barplot, boxplot
Here
the
conclusion is the
total
project
oberverving
the
we
are
showing
the
employee
's data set is to comparing the all percentages and in this data set having outliers using boxplot find out the outliers using countplot to find out the for ex: jobcity having which city have more employee'
s
so
we
can
find
the
place...
Research
questions
There
are
two
friends in a
city
first
friend is one
of
the
managers
of
TATA
company and second
one is one
of
managers in AMEO
company
the
second
person
started
conversation
by
saying
that, we, the
AMEO
company
hires or recruits
the
students or freshres
who
are
having
percentage
of
above
70 and he
also
mentioned
that
the
avarege
percentage
who
are
recruited is 80.
Then
the
frist
person
replied
that
am
i
joke
to
you ? and he
said
that is that
even
possible
to
maintain
the
average
percentage
of
80.can
you
prove
it
Step - 7 - Perform
feature
transformation:
Numerical
columns - Standardization
Mean - 0, std - 1
df_num = df.select_dtypes(include=['int64', 'float64'])
df_num
ID
Salary
10
percentage
12
graduation
12
percentage
CollegeID
CollegeTier
collegeGPA
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
openess_to_experience
0
203097
420000
84.30
2007
95.80
1141
2
78.00
2011
515
585
525
0.9737
0.8128
0.5269
1.35490 - 0.4455
1
579905
500000
85.40
2007
85.00
5807
2
70.06
2012
695
610
780 - 0.7335
0.3789
1.2396 - 0.10760
0.8637
2
810601
325000
85.00
2010
68.20
64
2
70.00
2014
615
545
370
0.2718
1.7109
0.1637 - 0.86820
0.6721
3
267447
1100000
85.60
2007
83.60
6920
1
74.64
2011
635
585
625
0.0464
0.3448 - 0.3440 - 0.40780 - 0.9194
5
1027655
300000
89.92
2010
87.00
5086
2
76.32
2014
560
555
620 - 0.3027 - 0.6201 - 2.2954 - 0.74150 - 0.8608
......................................................
3993
47916
280000
52.09
2006
55.50
6268
2
61.50
2010
365
334
475 - 0.1082
0.3448
0.2366
0.64980 - 0.9194
3994
752781
100000
90.00
2009
93.00
4883
2
77.30
2013
415
410
535 - 0.3027
0.8784
0.9322
0.77980 - 0.0943
3995
355888
320000
81.86
2008
65.50
9786
2
70.00
2012
475
475
465 - 1.5765 - 1.5273 - 1.5051 - 1.31840 - 0.7615
3996
947111
200000
78.72
2010
69.88
979
2
70.42
2014
450
410
320 - 0.1590
0.0459 - 0.4511 - 0.36120 - 0.0943
3997
324966
400000
70.60
2008
68.00
6609
2
68.00
2012
565
515
464 - 1.1128 - 0.2793 - 0.6343
1.32553 - 0.6035
3983
rows × 17
columns

from sklearn.preprocessing import StandardScaler

features = ["Salary", "10percentage", "12graduation", "12percentage", "CollegeID", "CollegeTier", "collegeGPA",
            "GraduationYear", "English",
            "Logical", "Quant", "conscientiousness", "agreeableness", "extraversion", "nueroticism", "nueroticism"]
autoscaler = StandardScaler()
df[features] = autoscaler.fit_transform(df[features])
df[features].describe()
Salary
10
percentage
12
graduation
12
percentage
CollegeID
CollegeTier
collegeGPA
GraduationYear
English
Logical
Quant
conscientiousness
agreeableness
extraversion
nueroticism
nueroticism
count
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
3.983000e+03
mean
4.622910e-17
5.287984e-16 - 3.861168e-14
7.199865e-16
2.020868e-18 - 2.765941e-16 - 8.345766e-16
6.946469e-14 - 5.758777e-17
2.940014e-16
2.202746e-16
1.167922e-16
7.509266e-17 - 4.002155e-16
2.280096e-17
2.280096e-17
std
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
1.000126e+00
min - 1.283375e+00 - 3.544642e+00 - 7.925642e+00 - 3.130010e+00 - 1.072972e+00 - 3.535774e+00 - 7.959207e+00 - 4.269080e+00 - 3.068566e+00 - 3.534164e+00 - 3.216452e+00 - 3.976277e+00 - 6.293274e+00 - 4.839001e+00 - 2.453420e+00 - 2.453420e+00
25 % -6.009474e-01 - 6.342123e-01 - 6.587851e-01 - 7.680113e-01 - 9.704777e-01
2.828235e-01 - 6.224214e-01 - 4.640886e-01 - 7.308201e-01 - 6.509362e-01 - 6.801879e-01 - 6.446118e-01 - 4.608247e-01 - 6.394946e-01 - 6.925977e-01 - 6.925977e-01
50 % -3.618004e-02
1.105287e-01 - 5.321366e-02 - 4.903820e-03 - 2.653080e-01
2.828235e-01
2.864956e-02
2.969097e-01 - 1.518354e-02
4.103840e-02
1.523940e-02
8.185764e-02
6.939795e-02
9.214282e-02 - 6.378934e-02 - 6.378934e-02
75 % 2.932676e-01
7.872430e-01
5.523578e-01
7.400344e-01
7.621358e-01
2.828235e-01
5.946652e-01
1.057908e+00
6.527439e-01
7.330130e-01
6.697593e-01
7.200772e-01
7.067266e-01
7.022960e-01
6.908204e-01
6.908204e-01
max
1.737748e+01
2.015279e+00
2.974643e+00
2.202657e+00
2.761610e+00
2.828235e-01
3.481039e+00
3.340903e+00
3.562999e+00
3.385583e+00
3.165116e+00
1.977067e+00
1.865892e+00
2.660545e+00
3.494861e+00
3.494861e+00
Categorical
columns
convert
the
feature
to
Binary.
df_cat = df.select_dtypes(include=['object'])

df_cat.head()
Designation
JobCity
Gender
10
board
12
board
Degree
Specialization
CollegeState
0
senior
quality
engineer
BANGALORE
f
board
ofsecondary
education, ap
board
of
intermediate
education, ap
B.Tech / B.E.computer
engineering
Andhra
Pradesh
1
assistant
manager
INDORE
m
cbse
cbse
B.Tech / B.E.electronics and communication
engineering
Madhya
Pradesh
2
systems
engineer
CHENNAI
f
cbse
cbse
B.Tech / B.E.information
technology
Uttar
Pradesh
3
senior
software
engineer
GURGAON
m
cbse
cbse
B.Tech / B.E.computer
engineering
Delhi
5
system
engineer
HYDERABAD
m
state
board
state
board
B.Tech / B.E.electronics and communication
engineering
Karnataka
# OneHotEncoding the categorical features

from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(drop='first', sparse=False)

# column names are (annoyingly) lost after OneHotEncoding
# (i.e. the dataframe is converted to a numpy ndarray)

categorical = pd.DataFrame(encoder.fit_transform(df_cat),
                           columns=encoder.get_feature_names(df_cat.columns))

categorical.head()
Designation_account
executive
Designation_account
manager
Designation_admin
assistant
Designation_administrative
coordinator
Designation_administrative
support
Designation_aircraft
technician
Designation_android
developer
Designation_application
developer
Designation_application
engineer
Designation_application
support
engineer...CollegeState_Orissa
CollegeState_Punjab
CollegeState_Rajasthan
CollegeState_Sikkim
CollegeState_Tamil
Nadu
CollegeState_Telangana
CollegeState_Union
Territory
CollegeState_Uttar
Pradesh
CollegeState_Uttarakhand
CollegeState_West
Bengal
0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0...
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
1
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0...
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
2
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0...
0.0
0.0
0.0
0.0
0.0
0.0
0.0
1.0
0.0
0.0
3
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0...
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
4
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0...
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
5
rows × 1244
columns

The
Standardization is done
using
onehot - encoding and it
will
be
coverted
into
the
feature
to
Binary
only
object
columns








