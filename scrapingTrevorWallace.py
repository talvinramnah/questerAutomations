import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup
import csv
# HTML content
mathsInSociety = """
<body lang="EN-US" link="blue" vlink="purple" style="tab-interval:.5in">

<div class="WordSection1">

<h1>MATH 107 – Math in Society</h1>

<p class="MsoNormal">This link will be updated when I make the videos, hopefully
in the near future! (this is the next course I plan to update – this summer!)</p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Course Description: </b>This
course will introduce the non-math/science major to mathematical applications
in a variety of disciplines.<b style="mso-bidi-font-weight:normal"><o:p></o:p></b></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><o:p>&nbsp;</o:p></b></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Textbook: </b>Lippman,
D. (2017). <i style="mso-bidi-font-style:normal"><a href="http://www.lulu.com/shop/http:/www.lulu.com/shop/david-lippman/math-in-society-edition-25/paperback/product-23872322.html">Math
in Society</a>:</i> Ed. 2.5</p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><o:p>&nbsp;</o:p></b></p>

<p class="MsoNormal"><a href="http://www.wallace.ccfaculty.org/MathinSociety.pdf">Textbook
download</a></p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Chapter 2: Voting
Theory<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l5 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/8IKvSthJCRQ">Plurality</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l5 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/PwUNpK_NLtM">Instant
Runoff Voting</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l5 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/XG1NfUjALZc"><span class="SpellE">Borda</span> Count</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l5 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/At5-tg1Va1c">Copeland’s
Method</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l5 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/UMIcay8OMQI">Approval
Voting</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Chapter 3: Weighted Voting<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/6bbPsWQ2y7o">Introduction</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/hSiv3i73wQw">Banzhaf
Power Index</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/Z1ZOy8rtEWA">Shapely-<span class="SpellE">Shubik</span> Power Index</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Chapter 5: Fair
Division<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l7 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/cX7IVunZAsM">Divider-Chooser</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l7 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/Y9vf2ShDipw">Lone
Divider</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l7 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/_RHtBiLa1o8">Last <span class="SpellE">Diminisher</span></a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l7 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/8pW6BTLg5o4">Sealed
Bids Method</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Chapter 6: Graph
Theory<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l2 level1 lfo8"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/yvNpYKavZQ0">Graphs
and Shortest Path</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo8"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/gG2Vr87FTOA">Euler
Circuits</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo8"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/y8WPpFtcl24">Hamiltonian
Circuits</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l2 level1 lfo8"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/T08yxvv-ER0">Spanning
Trees</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Chapter 8: Growth
Models<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo10"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/R9J6xCLm6V0">Linear
Growth Models</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo10"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/Z36OKKBEAHE">Exponential
Growth Models</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo10"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/URHUhpEKyeg">Solving
Exponentials for Time</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo10"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/jH6mOon0x1k">Logistic
Growth</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Chapter 9: Finance<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l6 level1 lfo12"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/j_91inEkmHE">Simple
&amp; Compound Interest</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l6 level1 lfo12"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/easvDsxAC8s">Annuities
&amp; Payout Annuities</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l6 level1 lfo12"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/zNPzbySdGQY">Loans
&amp; Loan Balance</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Chapter 11:
Describing Data<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l3 level1 lfo14"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/QZSwmb-rBXQ">Presenting
Data Visually</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo14"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/aW1Ojemi4Hs">Measures
of Central Tendency</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l3 level1 lfo14"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/D2bxWqGZkm8">Measures
of Variance</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Chapter 12:
Probability<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l4 level1 lfo16"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/n-hoJNuPBvw">Introduction
and Basic Concepts</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l4 level1 lfo16"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/zURgWr1fFA8">Bayes
Theorem</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l4 level1 lfo16"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/1REcU22ubyg">Counting</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l4 level1 lfo16"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/uljuXFRcDdA">Expected
Value</a></p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

</div>




</body>
"""

Precalculus = """
<body lang="EN-US" link="blue" vlink="purple" style="tab-interval:.5in">

<div class="WordSection1">

<h1>MATH 141 – <span class="SpellE">PreCalculus</span></h1>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Course Description: </b><span style="mso-spacerun:yes">&nbsp;</span>This course will present the following
concepts: non-linear inequalities, matrices and determinants, polynomial and
rational functions, conic sections, theory of equations, sequences and series,
mathematical induction.</p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Textbook: </b>Abed,
S., Farag, S., Lane, S., Wallace, T., Whitney, B. (2013). <i style="mso-bidi-font-style:
normal"><a href="http://www.lulu.com/shop/salah-abed-and-sonia-farag-and-stephen-lane-and-tyler-wallace/pre-calculus-141-142/paperback/product-23297850.html">Pre-Calculus
141 &amp; 142</a></i>: 4<sup>th</sup> Ed. </p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><a href="Book-141-and-142-4th-Edit.pdf">Textbook Download</a></p>

<p class="MsoNormal"><a href="Book-141-142-Selected-Answers-4th-Edition.pdf">Select
Answers Download</a></p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 1: College
Algebra<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/ZoNchDyX0_w">1.1
Simplifying with Exponents</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/VJYT01NdJns">1.2
Radical Expressions and Equations</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/N9y1_hdGTvU">1.3
Quadratic Expressions and Equations</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/In0_92TiTAI">1.4
Simplifying Rational Expressions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/LIuinnbUXwA">1.5
Complex Numbers</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/d1eYSHFwnnY">1.6
Complete the Square</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/PyLEhTiw1s0">1.7
Solving Linear Formulas</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=W5w2_Hutg9g">1.8 Solving Absolute Value
Equations and Inequalities</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 2: Functions and
Graphs<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/uTx38xjyw_E">2.1
Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/A5BQz_M0INE">2.2
Algebra of Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/iUiP9zTsYSM">2.3
Inverse Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/rCj59UJUCqo">2.4
Applications of Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/6a4YAumsC70">2.5
Reading Graphs of Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/vcTZoBl2ePE">2.6
Transformations of Graphs</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="http://youtu.be/i5Ul_uAXcpQ">2.7
Transformations of Basic Functions</a> </p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 3: Graphs of Key
Functions<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=c6XRRYJuMq0">3.1 Graphs of Polynomial
Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=vDTb24hwYu4">3.2 Synthetic Division</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=XM0QtEJ707M">3.3 Rational Root Theorem</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=KH0as0pvwwo">3.4 Graphs of Reciprocal
Functions</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=4pP1D0ghH1E">3.5 Graphs of Rational
Functions</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 4: Exponents and
Logarithms<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=cvsmKYaIDsc">4.1 Exponential Equations with
a Common Base</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=GMJMl9SxXY4">4.2 Properties of Logarithms</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=meJAMa50i6w">4.3 Exponential Equations
with Different Bases</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=pyJUTkb1gEQ">4.4 Solving Equations with
Logarithms</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://www.youtube.com/watch?v=J4Zvq5R8NZ0">4.5 Applications of Logarithms
and Exponents</a></p>

</div>




</body>
"""

Trigonometry = """
<body lang="EN-US" link="blue" vlink="purple" style="tab-interval:.5in">

<div class="WordSection1">

<h1>MATH 142</h1>

<p class="MsoNormal"><b>Course Description:&nbsp;</b>&nbsp;In preparation for
calculus this is a comprehensive study of trigonometry, circular functions,
right triangle trigonometry, <span class="GramE">analytical</span> trigonometry.
Sequences, series and induction are also covered.</p>

<p class="MsoNormal">&nbsp;</p>

<p class="MsoNormal"><b>Textbook:&nbsp;</b>Abed, S., <span class="SpellE">Farag</span>,
S., Lane, S., Wallace, T., Whitney, B. (2013).&nbsp;<i><a href="http://www.lulu.com/shop/salah-abed-and-sonia-farag-and-stephen-lane-and-tyler-wallace/pre-calculus-141-142/paperback/product-23297850.html">Pre-Calculus
141 &amp; 142</a></i>: 4<sup>th</sup>&nbsp;Ed.</p>

<p class="MsoNormal">&nbsp;</p>

<p class="MsoNormal"><a href="http://www.wallace.ccfaculty.org/Book-141-and-142-4th-Edit.pdf">Textbook
Download</a></p>

<p class="MsoNormal"><a href="http://www.wallace.ccfaculty.org/Book-141-142-Selected-Answers-4th-Edition.pdf">Select
Answers Download</a></p>

<p class="MsoNormal">&nbsp;</p>

<p class="MsoNormal"><b>Unit 1: Triangles and Circles<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/AVAQsA9BBOM">5.1
Angles</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/XFXgl6eTS_w">5.2 Right
Triangle Trigonometry</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/6_nHoAp3XWA">5.3a Law
of Sines</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/3X6TD8iqtS4">5.3b Law
of Cosines</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/C6PqRK44ryI">5.4
Points on a Circle</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/u3VUwPlQD_A">5.5a
Other Trig Functions</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 2: Foundational
Trig Identities<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/GdToVVaPWMA">5.5b
Introduction to Identities</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/B0VD9RFlN0Y">5.6a
Graph of Sine and Cosine</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/fN3QqowOWFw">5.6b
Graph of tan, cot, sec, <span class="SpellE">csc</span></a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/j4ERDQY49i4">5.7
Inverse Trig Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/OupoIfHBYDY">6.1 Solve
Trig Equations</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/qaoRubTEBUI">6.2
Modeling with Trig Functions</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 3: More Trig
Identities<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/eMVpJDGMCps">6.3
Solving Trig Equations with Identities</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/3iywef0B71k">6.4a.i
Deriving Addition, Subtraction, Product to Sum, and Sum to Product Identities</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/4T8gVzAUPh0">6.4a.ii
Addition, Subtraction, Product to Sum, and Sum to Product Identities</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/UVIqCekmZi0">6.4b
Using Identities</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/p6TEenyDGu8">6.5.i
Deriving Double and Half Angle Identities</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/dUMRpjxKnYo">6.5.ii
Double and Half Angle Identities</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/DNWvJU8EcxY">6.6a
Review Trig Equations</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/AMcryBjBAz8">6.6b
Review Trig Proofs</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 4: Other <span class="SpellE">PreCalc</span> Topics<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/fHfxw12BTOg">7.1 Polar
Coordinates</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/62PWwaRL7s4">7.2 Polar
Form of Complex Numbers</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/lzsZKcQb5vw">7.3 <span class="SpellE">DeMoivre’s</span> Theorem</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/R2t3t5e7Ar4">8.1
Sequences</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/n2BxvZRaEDQ">8.2
Series</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/aHkUxD_k9jI">8.3
Arithmetic Series</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/-hOC4FPydxM">8.4
Geometric Series</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/uKv35tsX5es">8.5
Induction</a></p>

</div>




</body>
"""

Statistics = """
<body lang="EN-US" link="blue" vlink="purple" style="tab-interval:.5in">

<div class="WordSection1">

<h1>MATH 146 – Introduction to Statistics</h1>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Course Description: </b>This
course is an introduction to descriptive statistics, probability and its
applications, statistical inference and hypothesis testing, predictive
statistics and linear regression.</p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><o:p>&nbsp;</o:p></b></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Textbook: </b>Wallace,
T. L. (2018), <i style="mso-bidi-font-style:normal"><a href="http://www.lulu.com/shop/tyler-l-wallace-edd/exploring-introductory-statistics/paperback/product-23752100.html">Exploring
Introductory Statistics: <span style="font-style:normal">2<sup>nd</sup> Ed</span></a></i>.
Lulu.com</p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><a href="Exploring%20Introductory%20Statistics%20Updated.docx">Textbook
Download</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><o:p>&nbsp;</o:p></b></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 1: Descriptive
Statistics<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l3 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/KBhD6WBjp2I" target="_blank">1.1 Vocabulary and Frequency Tables</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/rbXNJ3_oDss" target="_blank">1.2 Data and Sampling Techniques</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/x1goKJaPuR8" target="_blank">1.3 Histograms and Box Plots</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l3 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/xtUmDrzALx4" target="_blank">1.4 Measures of Center and Spread</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 2: Probability<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/7Yb8VFfiVnY" target="_blank">2.1 Probability Formulas</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/iEIsXQ2aPvE">2.2 Contingency
Tables</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/3wHqkYtTyXY">2.3 Tree
Diagrams and Bayes Theorem</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/d0ckAe3L9no">2.4
Discrete Probability Distributions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/enuExD02FuU">2.5
Binomial Distribution</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/I9LIvbXSsQc">2.6
Poisson Distribution</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/qQQjACfJDSs">2.7
Continuous Probability Distributions and the Uniform Distribution</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/uhTe1rBa96Q">2.8
Normal Distribution</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 3: Introduction
to Hypothesis Testing<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l1 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/ECuQt_nc1SI">3.1
Central Limit Theorem</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/Knv5hgouYVs">3.2
Confidence Interval for Proportions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/pNSCwoMpKgw">3.3 Hypothesis
Testing for a Single Proportion</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/JYvzm5QReIk">3.4
Hypothesis Testing for Two Proportions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/Qw2nInOp3rE">3.5
Confidence Interval for Means</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/hl7THaTlxEY">3.6
Hypothesis Testing for a Single Mean</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/VbcbnUOUfiU">3.7
Hypothesis Testing for Two Means</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l1 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/Bsefcd-ci_Q">3.8
Hypothesis Testing for Matched Pairs</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 4: More Hypothesis
Testing<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/MSl3NwNR6PI">4.1
Hypothesis Testing for Goodness-of-Fit</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/65UYU6vBqhI">4.2 Hypothesis
Testing for Independence</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/mcQ70_Lqdl8">4.3 Hypothesis
Testing for a Single Variance</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/yCwWhSGahdQ">4.4 Hypothesis
Testing for Two Variances</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/zZAIhmH8rBs">4.5 Hypothesis
Testing for Several Means</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/l0aYPFOnzOI">4.6 Hypothesis
Testing for Correlation and Regression</a></p>

<h1><o:p>&nbsp;</o:p></h1>

</div>




</body>
"""
BusinessCalculus = """
<body lang="EN-US" link="blue" vlink="purple" style="tab-interval:.5in">

<div class="WordSection1">

<h1>MATH 148 – Business Calculus</h1>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Course Description: </b>This
is an introductory calculus course for business and economics students.<span style="mso-spacerun:yes">&nbsp; </span>It includes an introduction to rates of
change, differentiation, integration, areas, and appropriate calculus
techniques.<span style="mso-spacerun:yes">&nbsp; </span>There are also applications
to marginal analysis in economics, optimization and other relevant
applications.</p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Textbook: </b><span class="SpellE">Burzynski</span>, D. (2018), <i style="mso-bidi-font-style:normal"><a href="https://www.xyztextbooks.com/catalog/product/applied_calculus?uxf=student">Applied
Calculus for Business, Life and Social Sciences</a></i>. XYZ Textbooks</p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 1: Functions and
Limits<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l3 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/CY6zso4z4ZY">1.1
Introduction to Functions and Relations</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/cERqY0vuFQU">1.2
Algebra and Composition of Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/cmXnLxGXeeA">1.3
Slope, Rates of Change, and Linear Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/zmZdPr5uCfI">4.1, 4.2
The Exponential and Logarithmic Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/M3rKySOXwX4">1.4
Introduction to Limits</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/R8c60b00zZo">1.5
Functions and Continuity</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/dM1CPkZiPSs">1.6
Average and Instantaneous Rates of Change</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l3 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/d0ZlVMMRF9o">7.1
Functions of Several Variables</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 2: Derivatives<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/4YRZHnEaejE">2.1 The
Derivative of a Function and Two Interpretations</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/PF3gYpwRo-Y">2.2
Differentiating Products and Quotients</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/lOi9AMEByXs">2.3
Higher-Ordered Derivatives</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/eBmmYxWMVM4">2.4 The
Chain Rule and General Power Rule</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/40TufUFBOyw">4.3, 4.4
Differentiating the Natural Logarithm &amp; Exponential Function</a> </p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/kIhVtN3Bof0">2.5
Implicit Differentiation</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/iqzPxRFqqYY">7.2
Partial Derivatives</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 3: Integrals<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l1 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/5SX_vxT-KG4">5.1
Antidifferentiation and the Indefinite Integral</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/bbFPG89LZdQ">5.2
Integration by Substitution</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/q40z5MgQN8E">5.3 The
Definite Integral</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/pEKYkogGoLY">5.4, 6.1
Area of Regions in the Plane</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/2CRLatt1AW4">5.6
Integration by Parts</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l1 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/w_nqzK137Cs">7.6
Double Integrals as Volume</a> </p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 4: Applications
of Calculus<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l2 level1 lfo8"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/aY3--VXNOAo">3.3
Applications of the Derivative: Optimization</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo8"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/YKJoCuazAr8">3.4
Applications of the Derivative in Business and Economics</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo8"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/GqQEW3V8iSw">6.2
Consumer’s and Producer’s Surplus</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo8"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/M--faVnar-M">6.3
Annuities and Money Streams</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l2 level1 lfo8"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/VAIOf84OrKM">7.8 The
Average Value of a Function</a></p>

</div>




</body>
"""
CalculusI = """
<body lang="EN-US" link="blue" vlink="purple" style="tab-interval:.5in">

<div class="WordSection1">

<h1>MATH 151 – Calculus I</h1>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Course Description: </b>This
course will introduce the student to the basic concepts of the calculus.<span style="mso-spacerun:yes">&nbsp; </span>It will give the student an appreciation of
the calculus and its applications in the real world and will prepare the
student for future work in mathematics and the sciences.<span style="mso-spacerun:yes">&nbsp; </span>Course includes functions, limits,
continuity, derivatives and their applications, and integration and its
applications.<b style="mso-bidi-font-weight:normal"><o:p></o:p></b></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><o:p>&nbsp;</o:p></b></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Textbook: </b>Herman,
E. J. &amp; Strang, G. (2018). <i style="mso-bidi-font-style:normal"><a href="http://www.lulu.com/shop/tyler-wallace/bbcc-calculus-i/paperback/product-23807909.html">BBCC
Calculus I</a></i>, published by OpenStax, remixed by Lulu.</p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><o:p>&nbsp;</o:p></b></p>

<p class="MsoNormal"><a href="Calculus%20I%20book.pdf">Textbook Download</a></p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 1: Limits<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/nKQ3LFlNGS8">2.1 A Preview
of Calculus</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/EVach-BUSbY">2.2 The
Limit of a Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/Ou7xbovOCtI">2.3 Limit
Laws</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/0p8wnF_gyTE">2.4
Continuity</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/bDmYq2nF90A">2.5 The
Precise Definition of a Limit</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 2: Derivatives<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/XJkGjdUf1Xg">3.1
Defining the Derivative</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/4G5J-kCQhGY">3.2 The
Derivative as a Function</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/9DtWqmmBfjA">3.3
Differentiation Rules</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/ezPaoc8uYVI">3.4
Derivatives as Rates of Change</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/-kOBQwSTUiI">3.5
Derivatives of Trigonometric Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/8YI06f9IPJI">3.6 The
Chain Rule</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/nguKNgaorAI">3.7
Derivatives of Inverse Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/xFotaPSIp7o">3.8
Implicit Differentiation</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/WfhCLKKvRPg">3.9 Derivatives
of Exponentials and Logarithms</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/uUN2emmcRDI">3.10
Partial Derivatives</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 3: Applications
of Derivatives<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/D1xnGlco8z0">4.1
Related Rates</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/KkMBDrYZkt4">4.2
Linear Approximations and Differentials</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/D6aPd3qDv-E">4.3
Maxima and Minima</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/9QtLPEW8K_g">4.4 The Mean
Value Theorem</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/a1KjKz5jw8w">4.5
Derivatives and the Shape of a Graph</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/ugrbi9AE8ns">4.6
Limits and Infinity and Asymptotes</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/x-cMfl_GznQ">4.7
Applied Optimization Problems</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/--BZl69t4do">4.8 <span class="SpellE">L’Hopital’s</span> Rule</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/iG_bpYVXqWo">4.9
Newton’s Method</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo1"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/2HDmicd_rzU">4.10 Antiderivatives</a></p>

<h1><o:p>&nbsp;</o:p></h1>

</div>




</body>
"""

CalculusII = """
<body lang="EN-US" link="blue" vlink="purple" style="tab-interval:.5in">

<div class="WordSection1">

<h1>MATH 152 – Calculus II</h1>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Course Description:</b>
This course will expand on the applications and techniques of differentiation
learned in the first quarter and give a depth study of integration including the
fundamental methods of integrating elementary algebraic and transcendental
functions. It will include the applications of the calculus to transcendental
functions, analytical geometry and other relevant topics.</p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Textbook: </b>Herman,
E. J. &amp; Strang, G. (2018). <i style="mso-bidi-font-style:normal"><a href="http://www.lulu.com/shop/tyler-wallace/bbcc-calculus-ii/paperback/product-23810978.html">BBCC
Calculus I</a></i>, published by OpenStax, remixed by Lulu.</p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><o:p>&nbsp;</o:p></b></p>

<p class="MsoNormal"><a href="Calc%20II%20Book.pdf">Textbook Download</a></p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 1:
Antiderivatives and Integration<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/WIVCB4zFyd0">5.0
Review Derivatives and Formulas</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/LgfTqathXuc">5.1
Approximating Areas</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/JFjwJ9NgI_c">5.2 The
Definite Integral</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/tPfZ2PM9vVM">5.3 The
Fundamental Theorem of Calculus</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/2HDmicd_rzU">4.10
Antiderivatives</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/RzNeIp7MaZs">5.4
Integration Formulas and the Net Change Theorem</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/Uk1j0-mRsdc">5.5
Substitution</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/fr1M_vpw-bA">5.6
Integrals Involving Exponential and Logarithmic Functions</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l2 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/kozRQrtv61o">5.7
Integrals Resulting in Inverse Trigonometric Functions</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 2: Applications
of Integration<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/N8kuGp7UE4U">6.1 Areas
Between Curves</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/0wK4B1jtgQU">6.2
Determining Volumes by Slicing</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/9p2RhS4soHY">6.3
Volumes of Revolution: Cylindrical Shells</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/7YxKDizqtO4">6.4 Arc
Length of a Curve and Surface Area</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/5NXDcBzT8dc">6.5
Physical Applications</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/ACjEQXLMDNo">6.6
Moments and Centers of Mass</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/lDhR5X1t3TI">6.7
Integrals, Exponential Functions, and Logarithms</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/TjSZf3qSYvA">6.8
Exponential Growth and Decay</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l1 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]-->6.9 Calculus of the Hyperbolic Functions (video
will be made soon!)</p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 3: Advanced
Integration Techniques<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/I25Q5J-Vl80">3.1
Integration by Parts</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/Fb1rd-cVJXY">3.2
Trigonometric Integrals</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/PBPc-2jC0GE">3.3
Trigonometric Substitutions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/thSU0cUs4s0">3.4
Partial Fractions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/bAR6zy5KgHQ">3.5 Other
Strategies for Integration</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/oFCSyJSKyzc">3.7
Improper Integrals</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo6"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/te8MlfASy7E">3.8
Double Integrals</a></p>

<h1><o:p>&nbsp;</o:p></h1>

</div>




</body>
"""

CalculusIII = """
<body lang="EN-US" link="blue" vlink="purple" style="tab-interval:.5in">

<div class="WordSection1">

<h1>MATH 163 – Calculus III</h1>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Course Description: </b>This
course will expand on the applications and techniques of differentiation learned
in the first and second quarters. It will introduce the student to the calculus
of sequences and series and the use of the <span class="SpellE">MacLaurin</span>
and Taylor series to approximate functions. It will introduce the student to
the calculus of curvilinear functions and the concept of the vector and vector
functions.<span style="mso-spacerun:yes">&nbsp; </span>It will also introduce the
concept of a partial derivative and the maximization of functions given in more
than one independent variable.</p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><o:p>&nbsp;</o:p></b></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Textbook: </b>Herman,
E. J. &amp; Strang, G. (2018). <i style="mso-bidi-font-style:normal"><a href="http://www.lulu.com/shop/tyler-wallace/bbcc-calculus-iii/paperback/product-23807858.html">BBCC
Calculus III</a></i>, published by OpenStax, remixed by Lulu.</p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><a href="Calc%203%20Book.pdf">Textbook Download</a></p>

<p class="MsoNormal"><o:p>&nbsp;</o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 1: Sequences and
Series<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/F7CpLDmYh68">5.1 Sequences</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/0jtPG4CTj18">5.2
Infinite Series</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/eIkc1QAbw2o">5.3 The Divergence
and Integral Tests</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/lSL4-MG6o_E">5.4
Comparison Tests</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/l1weAgpVeqY">5.5
Alternating Series</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/ozjwigUOZu4">5.6 Ratio
and Root Tests</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/xPrcXarM7go">6.1 Power
Series and Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/EoOwt8am0PM">6.2
Properties of Power Series</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l0 level1 lfo2"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/uxLnERjGfP8">6.3
Taylor and Maclaurin Series</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 2: Parametric
and Polar Coordinates<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l4 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/LU50pDc9DtM">7.5 Conic
Sections</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l4 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/fSQ4cqAPTgQ">7.1
Parametric Equations</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l4 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/UTLgwAFNQCo">7.2
Calculus of Parametric Curves</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l4 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/Ka__vteYxAs">7.3 Polar
Coordinates</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l4 level1 lfo3"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/GRDDt0KKaKg">7.4 Area
and Arc Length in Polar Coordinates</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 3: Vectors<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l2 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/C9n0UvGQp8k">2.1
Vectors in the Plane</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/MKkjMfTkD4U">2.2
Vectors in Three Dimensions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/2__W2ERTrjQ">2.3 The
Dot Product</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/rS7bSq60cCM">2.4 The
Cross Product</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/gLsUJ9jTCTY">2.5
Equations of Lines and Planes in Space</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l2 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/oelQsMbRwRI">2.6 Quadric
Surfaces</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l2 level1 lfo4"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/zbL1Kkod26w">2.7
Cylindrical and Spherical Coordinates</a></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal">Unit 4: Vector-Valued
Functions<o:p></o:p></b></p>

<p class="MsoListParagraphCxSpFirst" style="text-indent:-.25in;mso-list:l3 level1 lfo5"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/zbL1Kkod26w">3.1
Vector-Valued Functions and Space Curves</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo5"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/cUSyR_x5ZKw">3.2
Calculus of Vector-Valued Functions</a></p>

<p class="MsoListParagraphCxSpMiddle" style="text-indent:-.25in;mso-list:l3 level1 lfo5"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/v879VRPJeyk">3.3 Arc
Length and Curvature</a></p>

<p class="MsoListParagraphCxSpLast" style="text-indent:-.25in;mso-list:l3 level1 lfo5"><!--[if !supportLists]--><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">·<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</span></span></span><!--[endif]--><a href="https://youtu.be/V1DS4EIoygc">3.4
Motion in Space</a><o:p></o:p></p>

<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><o:p>&nbsp;</o:p></b></p>

<h1><o:p>&nbsp;</o:p></h1>

</div>




</body>
"""


import csv
from bs4 import BeautifulSoup

# Function to scrape links and save to a CSV file
def scrape_links_and_save_to_csv(html, csv_filename):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all the anchor tags (<a>) in the HTML
    links = soup.find_all('a')

    # Prepare data for the CSV file
    data = []
    for link in links:
        href = link.get('href')
        text = link.text.strip()
        data.append([href, text])

    # Write data to the CSV file
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Link', 'Text'])  # Header row
        writer.writerows(data)

# Names for the HTML content - update these as necessary
html_names = ['MathsInSociety', 'Precalculus', 'Trigonometry', 'Statistics', 'BusinessCalculus', 'CalculusI', 'CalculusII', 'CalculusIII']

# Assuming htmls is a list of HTML contents
htmls = [mathsInSociety, Precalculus, Trigonometry, Statistics, BusinessCalculus, CalculusI, CalculusII, CalculusIII]

for html, name in zip(htmls, html_names):
    csv_filename = f"{name}.csv"
    scrape_links_and_save_to_csv(html, csv_filename)

