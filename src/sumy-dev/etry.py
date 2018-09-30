#Import library essentials
from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer #We're choosing Lexrank, other algorithms are also built in

from sumy._compat import to_unicode


'''
parser1 = PlaintextParser.from_file(file1, Tokenizer("english"))
parser2 = PlaintextParser.from_file(file2, Tokenizer("english"))

#print parser.document
summarizer = LexRankSummarizer()

summary = summarizer(parser1.document,parser2.document,5) #Summarize the document with 5 sentences
'''

scores=[[1, '1 Introduction', 0],
[2, 'Chapter Introduction', 0.40778247406509277],
[2, '1.1 What Is an Algorithm?', 0.22770986234003876],
[2, '1.2 Fundamentals of Algorithmic Problem Solving', 0.19568943309295941],
[2, '1.3 Important Problem Types', 0.27338649181785341],
[2, '1.4 Fundamental Data Structures', 0.29860022363235822],
[1, '2 Fundamentals of the Analysis of Algorithm Efficiency', 0],
[2, 'Chapter Introduction', 0.17676399761141481],
[2, '2.1 The Analysis Framework', 0.24813058395274068],
[2, '2.3 Mathematical Analysis of Nonrecursive Algorithms', 0.17518263816400062],
[2, '2.4 Mathematical Analysis of Recursive Algorithms', 0.19436220617146954],
[2, '2.5 Example: Computing the nth Fibonacci Number', 0.27674088929221591],
[2, '2.6 Empirical Analysis of Algorithms', 0.30318075762917351],
[2, '2.7 Algorithm Visualization', 0.46951381257342062],
[1, '3 Brute Force and Exhaustive Search', 0],
[2, 'Chapter Introduction', 0.23594952646231054],
[2, '3.1 Selection Sort and Bubble Sort', 0.23105993812658263],
[2, '3.2 Sequential Search and Brute-Force String Matching', 0.31564020049854824],
[2, '3.3 Closest-Pair and Convex-Hull Problems by Brute Force', 0.32684260952624511],
[2, '3.4 Exhaustive Search', 0.30312782545387168],
[2, '3.5 Depth-First Search and Breadth-First Search', 0.34360367762892136],
[1, '4 Decrease-and-Conquer', 0],
[2, 'Chapter Introduction', 0.15527289987953263],
[2, '4.1 Insertion Sort', 0.24597926496976147],
[2, '4.2 Topological Sorting', 0.42701684813982554],
[2, '4.3 Algorithms for Generating Combinatorial Objects', 0.19207462148921706],
[2, '4.4 Decrease-by-a-Constant-Factor Algorithms', 0.37302462710531625],
[2, '4.5 Variable-Size-Decrease Algorithms', 0.2839223057349996],
[1, '5 Divide-and-Conquer', 0],
[2, 'Chapter Introduction', 0.23481534491669348],
[2, '5.1 Mergesort', 0.19316855383570236],
[2, '5.2 Quicksort', 0.15026005682883559],
[2, '5.3 Binary Tree Traversals and Related Properties', 0.25920638766207799],
[2, '5.4 Multiplication of Large Integers and Strassens Matrix Multiplication', 0.35454367826053323],
[2, '5.5 The Closest-Pair and Convex-Hull Problems by Divide-and-Conquer', 0.34408994686913014],
[1, '6 Transform-and-Conquer', 0],
[2, 'Chapter Introduction', 0.17999489103174129],
[2, '6.1 Presorting', 0.31604766091902803],
[2, '6.2 Gaussian Elimination', 0.19911582881658274],
[2, '6.3 Balanced Search Trees', 0.259311295059728],
[2, '6.4 Heaps and Heapsort', 0.21146703051979254],
[2, '6.5 Horners Rule and Binary Exponentiation', 0.21480585735904684],
[2, '6.6 Problem Reduction', 0.2354648110457952],
[1, '7 Space and Time Trade-Offs', 0],
[2, 'Chapter Introduction', 0.28611645581877004],
[2, '7.1 Sorting by Counting', 0.26401043681114533],
[2, '7.2 Input Enhancement in String Matching', 0.11732845919987737],
[2, '7.3 Hashing', 0.32877314644466105],
[2, '7.4 B-Trees', 0.2585358575596004],
[1, '8 Dynamic Programming', 0],
[2, 'Chapter Introduction', 0.22647208715238448],
[2, '8.1 Three Basic Examples', 0.28888622549412596],
[2, '8.2 The Knapsack Problem and Memory Functions', 0.36979284185227723],
[2, '8.3 Optimal Binary Search Trees', 0.23450780179274913],
[2, '8.4 Warshall\xe2\x80\x99s and Floyd\xe2\x80\x99s Algorithms', 0.224299591485949],
[1, '9 Greedy Technique', 0],
[2, 'Chapter Introduction', 0.23735563244208052],
[2, '9.1 Prims Algorithm', 0.30156309146803251],
[2, '9.3 Dijkstras Algorithm', 0.26699263039886323],
[2, '9.4 Huffman Trees and Codes', 0.23837925226330539],
[1, '10 Iterative Improvement', 0],
[2, 'Chapter Introduction', 0.15974762956915872],
[2, '10.1 The Simplex Method', 0.27382291729429309],
[2, '10.2 The Maximum-Flow Problem', 0.26554750260353982],
[2, '10.3 Maximum Matching in Bipartite Graphs', 0.30893065663750874],
[2, '10.4 The Stable Marriage Problem', 0.27993848744551192],
[1, '11 Limitations of Algorithm Power', 0],
[2, 'Chapter Introduction', 0.20554697037564365],
[2, '11.1 Lower-Bound Arguments', 0.33041509719006379],
[2, '11.2 Decision Trees', 0.30959725701066221],
[2, '11.3 P, NP, and NP-Complete Problems', 0.25390817780155239],
[2, '11.4 Challenges of Numerical Algorithms', 0.22043715463827562],
[1, '12 Coping with the Limitations of Algorithm Power', 0],
[2, 'Chapter Introduction', 0.10086239240479668],
[2, '12.1 Backtracking', 0.27000521144245326],
[2, '12.2 Branch-and-Bound', 0.36735396431096079],
[2, '12.3 Approximation Algorithms for NP-Hard Problems', 0.15041829284117414],
[2, '12.4 Algorithms for Solving Nonlinear Equations', 0.21972192781686881],
[2, 'Properties of Logarithms', 0.079772079772079771],
[2, 'Sum Manipulation Rules', 0.065359477124182996],
[2, 'Floor and Ceiling Formulas', 0.09004329004329005],
[2, 'Miscellaneous', 0.034053072389811298],
[2, 'Sequences and Recurrence Relations', 0.14646988458123242],
[2, 'Methods for Solving Recurrence Relations', 0.1286218009275728],
[2, 'Common Recurrence Types in Algorithm Analysis', 0.089974533390936196],
[1, 'Hints to Exercises', 0.057991031077334443]]


for i in range(0,len(scores)):
    scores[i][1]=to_unicode(scores[i][1]).strip()

print scores
    
    

