import re
from sumy._compat import to_unicode

title="Computer Architecture"
'''
scores=[[1, '1 Fundamentals of Computer Design', 0],
[2, 'Chapter Introduction', 0.53333333333333333],
[2, '1.1 Introduction', 0.47896317683708778],
[2, '1.2 Classes of Computers', 0.37955426761953076],
[2, '1.4 Trends in Technology', 0.39656376362071477],
[2, '1.5 Trends in Power in Integrated Circuits', 0.57390618841150964],
[2, '1.6 Trends in Cost', 0.39350078642887953],
[2, '1.7 Dependability', 0.39955348920638634],
[2, '1.8 Measuring, Reporting, and Summarizing Performance', 0.23523981584045822],
[2, '1.9 Quantitative Principles of Computer Design', 0.37707132718846736],
[2, '1.10 Putting It All Together: Performance and Price-Performance', 0.4199363491769284],
[2, '1.11 Fallacies and Pitfalls', 0.38797907483457655],
[2, '1.12 Concluding Remarks', 0.57166371233223601],
[2, '1.13 Historical Perspectives and References', 0.25885271980780561],
[1, '2 Instruction-Level Parallelism and Its Exploitation', 0],
[2, 'Chapter Introduction', 0.21818181818181817],
[2, '2.1 Instruction-Level Parallelism: Concepts and Challenges', 0.35529800011599799],
[2, '2.2 Basic Compiler Techniques for Exposing ILP', 0.31036390860333857],
[2, '2.3 Reducing Branch Costs with Prediction', 0.33481369701822045],
[2, '2.4 Overcoming Data Hazards with Dynamic Scheduling', 0.32010353174827882],
[2, '2.5 Dynamic Scheduling: Examples and the Algorithm', 0.30140595551011329],
[2, '2.6 Hardware-Based Speculation', 0.39719467595907521],
[2, '2.7 Exploiting ILP Using Multiple Issue and Static Scheduling', 0.40254168574623916],
[2, '2.8 Exploiting ILP Using Dynamic Scheduling, Multiple Issue, and Speculation', 0.37239372878616439],
[2, '2.9 Advanced Techniques for Instruction Delivery and Speculation', 0.30048694118116842],
[2, '2.10 Putting It All Together: The Intel Pentium 4', 0.31510049729228867],
[2, '2.11 Fallacies and Pitfalls', 0.58129370629370647],
[2, '2.12 Concluding Remarks', 1.1666666666666667],
[2, '2.13 Historical Perspective and References', 0.29384123715436294],
[1, '3 Limits on Instruction-Level Parallelism', 0],
[2, 'Chapter Introduction', 0.10833333333333332],
[2, '3.1 Introduction', 0.69565217391304346],
[2, '3.2 Studies of the Limitations of ILP', 0.36420473664610747],
[2, '3.3 Limitations on ILP for Realizable Processors', 0.35292324985017048],
[2, '3.4 Crosscutting Issues: Hardware versus Software Speculation', 0.55045871559633031],
[2, '3.5 Multithreading: Using ILP Support to Exploit Thread-Level Parallelism', 0.38717887640346194],
[2, '3.7 Fallacies and Pitfalls', 0.59462550028587768],
[2, '3.8 Concluding Remarks', 0.57142857142857151],
[2, '3.9 Historical Perspective and References', 0.29379612965549279],
[1, '4 Multiprocessors and Thread-Level Parallelism', 0],
[2, 'Chapter Introduction', 0.14218114597178894],
[2, '4.1 Introduction', 0.37819792370027511],
[2, '4.2 Symmetric Shared-Memory Architectures', 0.30651615801308446],
[2, '4.3 Performance of Symmetric Shared-Memory Multiprocessors', 0.36974941348023954],
[2, '4.4 Distributed Shared Memory and Directory-Based Coherence', 0.33892017497291738],
[2, '4.5 Synchronization: The Basics', 0.43573466196096206],
[2, '4.6 Models of Memory Consistency: An Introduction', 0.43394873297543696],
[2, '4.7 Crosscutting Issues', 0.47259811368181764],
[2, '4.8 Putting It All Together: The Sun T1 Multiprocessor', 0.29821271832125512],
[2, '4.9 Fallacies and Pitfalls', 0.33985543930385198],
[2, '4.10 Concluding Remarks', 0.44117006288942784],
[2, '4.11 Historical Perspective and References', 0.2545406959165003],
[1, '5 Memory Hierarchy Design', 0],
[2, 'Chapter Introduction', 0.14613500779201224],
[2, '5.1 Introduction', 0.42406852063601652],
[2, '5.2 Eleven Advanced Optimizations of Cache Performance', 0.25710341193347347],
[2, '5.3 Memory Technology and Optimizations', 0.36929663505128502],
[2, '5.4 Protection: Virtual Memory and Virtual Machines', 0.35581967968814404],
[2, '5.5 Crosscutting Issues: The Design of Memory Hierarchies', 0.56079545454545454],
[2, '5.6 Putting It All Together: AMD Opteron Memory Hierarchy', 0.1357563726619001],
[2, '5.7 Fallacies and Pitfalls', 0.33374927732344162],
[2, '5.8 Concluding Remarks', 0.70761207133777992],
[2, '5.9 Historical Perspective and References', 0.19103459195269432],
[1, '6 Storage Systems', 0],
[2, 'Chapter Introduction', 0.13736974091985446],
[2, '6.1 Introduction', 0.84615384615384615],
[2, '6.2 Advanced Topics in Disk Storage', 0.35235448005497888],
[2, '6.4 I/O Performance, Reliability Measures, and Benchmarks', 0.41347458154574096],
[2, '6.5 A Little Queuing Theory', 0.26321574165462724],
[2, '6.6 Crosscutting Issues', 0.42644299746164882],
[2, '6.8 Putting It All Together: NetApp FAS6000 Filer', 0.5074701290730903],
[2, '6.9 Fallacies and Pitfalls', 0.46991451919660571],
[2, '6.10 Concluding Remarks', 0.55834217110081119],
[2, '6.11 Historical Perspective and References', 0.5],
[2, 'Case Studies with Exercises by Andrea C. Arpaci-Dusseau and Remzi H. Arpaci-Dusseau', 0.063111755928624516],
[1, 'A Pipelining: Basic and Intermediate Concepts', 0],
[2, 'Chapter Introduction', 0.53333333333333333],
[2, 'A.1 Introduction', 0.062783366954164116],
[2, 'A.3 How Is Pipelining Implemented?', 0.051446151812044975],
[2, 'A.4 What Makes Pipelining Hard to Implement?', 0.079658703880554807],
[2, 'A.5 Extending the MIPS Pipeline to Handle Multicycle Operations', 0.068152070522769712],
[2, 'A.6 Putting It All Together: The MIPS R4000 Pipeline', 0.034113091816938119],
[2, 'A.7 Crosscutting Issues', 0.028279271464570668],
[2, 'A.8 Fallacies and Pitfalls', 0.040465147965800939],
[2, 'A.9 Concluding Remarks', 0.34782608695652178],
[2, 'A.10 Historical Perspective and References', 0.1361662235685013],
[1, 'B Instruction Set Principles and Examples', 0],
[2, 'Chapter Introduction', 0.26229508196721313],
[2, 'B.1 Introduction', 0.3290380719171358],
[2, 'B.2 Classifying Instruction Set Architectures', 0.14739120016052015],
[2, 'B.3 Memory Addressing', 0.14426521454674049],
[2, 'B.4 Type and Size of Operands', 0.12709140900485433],
[2, 'B.5 Operations in the Instruction Set', 0.3277543289477074],
[2, 'B.6 Instructions for Control Flow', 0.33017696575420252],
[2, 'B.7 Encoding an Instruction Set', 0.3160754892723458],
[2, 'B.8 Crosscutting Issues: The Role of Compilers', 0.13000281922388723],
[2, 'B.9 Putting It All Together: The MIPS Architecture', 0.19022215492569658],
[2, 'B.10 Fallacies and Pitfalls', 0.05628969209601728],
[2, 'B.11 Concluding Remarks', 0.18701717035044446],
[2, 'B.12 Historical Perspective and References', 0.17394404373449479],
[1, 'C Review of Memory Hierarchy', 0],
[2, 'Chapter Introduction', 0.81203809846038133],
[2, 'C.1 Introduction', 0.089782226318934649],
[2, 'C.2 Cache Performance', 0.12862486843574913],
[2, 'C.3 Six Basic Cache Optimizations', 0.077176715179021096],
[2, 'C.4 Virtual Memory', 0.16705682023613186],
[2, 'C.5 Protection and Examples of Virtual Memory', 0.14916635467843117],
[2, 'C.6 Fallacies and Pitfalls', 0.15790604581079479],
[2, 'C.7 Concluding Remarks', 0.090627772941508117],
[2, 'C.8 Historical Perspective and References', 0.20869565217391309]]
'''
scores=[[1, u'1 Fundamentals of Computer Design', 0],
[2, 'Chapter Introduction', 0.50062578222778475],
[2, u'1.1 Introduction', 0.72670807453416064],
[2, u'1.2 Classes of Computers', 0.45979084024522165],
[2, u'1.3 Defining Computer Architecture', 0.21018276762402086],
[2, u'1.4 Trends in Technology', 0.50826037572950511],
[2, u'1.5 Trends in Power in Integrated Circuits', 0.63841106579180695],
[2, u'1.6 Trends in Cost', 0.41358559379986326],
[2, u'1.7 Dependability', 0.57146345930764975],
[2, u'1.8 Measuring, Reporting, and Summarizing Performance', 0.19244875550715973],
[2, u'1.9 Quantitative Principles of Computer Design', 0.26558576263784295],
[2, u'1.10 Putting It All Together: Performance and Price-Performance', 0.40378476316470596],
[2, u'1.11 Fallacies and Pitfalls', 0.4023581429624169],
[2, u'1.12 Concluding Remarks', 0.5818881402839271],
[2, u'1.13 Historical Perspectives and References', 0.18089547173997689],
[1, u'2 Instruction-Level Parallelism and Its Exploitation', 0],
[2, 'Chapter Introduction', 0.20042949176807445],
[2, u'2.1 Instruction-Level Parallelism: Concepts and Challenges', 0.32166333248436851],
[2, u'2.2 Basic Compiler Techniques for Exposing ILP', 0.46411483253588487],
[2, u'2.3 Reducing Branch Costs with Prediction', 0.33628140502313625],
[2, u'2.4 Overcoming Data Hazards with Dynamic Scheduling', 0.28189402433880967],
[2, u'2.5 Dynamic Scheduling: Examples and the Algorithm', 0.29436351499404839],
[2, u'2.6 Hardware-Based Speculation', 0.29031589133890962],
[2, u'2.7 Exploiting ILP Using Multiple Issue and Static Scheduling', 0.41737476817327562],
[2, u'2.8 Exploiting ILP Using Dynamic Scheduling, Multiple Issue, and Speculation', 0.60504201680672276],
[2, u'2.9 Advanced Techniques for Instruction Delivery and Speculation', 0.30179032001875777],
[2, u'2.10 Putting It All Together: The Intel Pentium 4', 0.29218072447972743],
[2, u'2.11 Fallacies and Pitfalls', 0.67618332081141974],
[2, u'2.12 Concluding Remarks', 1.1666666666666667],
[2, u'2.13 Historical Perspective and References', 0.30705867859518371],
[1, u'3 Limits on Instruction-Level Parallelism', 0],
[2, 'Chapter Introduction', 0.10012755102040816],
[2, u'3.1 Introduction', 0.88888888888888884],
[2, u'3.2 Studies of the Limitations of ILP', 0.34636461451871908],
[2, u'3.3 Limitations on ILP for Realizable Processors', 0.41281103392001467],
[2, u'3.4 Crosscutting Issues: Hardware versus Software Speculation', 1.0],
[2, u'3.5 Multithreading: Using ILP Support to Exploit Thread-Level Parallelism', 0.37076369622067945],
[2, u'3.6 Putting It All Together: Performance and Efficiency in Advanced Multiple-Issue Processors', 0.54945188056447214],
[2, u'3.7 Fallacies and Pitfalls', 0.78260869565217428],
[2, u'3.8 Concluding Remarks', 0.83333333333333337],
[2, u'3.9 Historical Perspective and References', 0.30620741895081266],
[1, u'4 Multiprocessors and Thread-Level Parallelism', 0],
[2, 'Chapter Introduction', 0.12206082298735078],
[2, u'4.1 Introduction', 0.42870814395661627],
[2, u'4.2 Symmetric Shared-Memory Architectures', 0.25438718021071127],
[2, u'4.3 Performance of Symmetric Shared-Memory Multiprocessors', 0.31447164008267925],
[2, u'4.4 Distributed Shared Memory and Directory-Based Coherence', 0.35507955749316761],
[2, u'4.5 Synchronization: The Basics', 0.47001192977270084],
[2, u'4.6 Models of Memory Consistency: An Introduction', 0.59437148217636027],
[2, u'4.7 Crosscutting Issues', 0.62397203189190376],
[2, u'4.8 Putting It All Together: The Sun T1 Multiprocessor', 0.35201611569184593],
[2, u'4.9 Fallacies and Pitfalls', 0.43113922989902337],
[2, u'4.10 Concluding Remarks', 0.732117812061711],
[2, u'4.11 Historical Perspective and References', 0.24414874327083055],
[1, u'5 Memory Hierarchy Design', 0],
[2, 'Chapter Introduction', 0.11953223888575687],
[2, u'5.1 Introduction', 0.26626960036315711],
[2, u'5.2 Eleven Advanced Optimizations of Cache Performance', 0.23104814056204587],
[2, u'5.3 Memory Technology and Optimizations', 0.36987502546433665],
[2, u'5.4 Protection: Virtual Memory and Virtual Machines', 0.39752576037797444],
[2, u'5.5 Crosscutting Issues: The Design of Memory Hierarchies', 0.63650898147277335],
[2, u'5.6 Putting It All Together: AMD Opteron Memory Hierarchy', 0.095226120084507648],
[2, u'5.7 Fallacies and Pitfalls', 0.29493858992683253],
[2, u'5.8 Concluding Remarks', 0.82317073170731736],
[2, u'5.9 Historical Perspective and References', 0.15234437527571917],
[1, u'6 Storage Systems', 0],
[2, 'Chapter Introduction', 0.11892717176687682],
[2, u'6.1 Introduction', 0.84615384615384615],
[2, u'6.2 Advanced Topics in Disk Storage', 0.35951994434137285],
[2, u'6.3 Definition and Examples of Real Faults and Failures', 0.53556380194857955],
[2, u'6.4 I/O Performance, Reliability Measures, and Benchmarks', 0.37712686918846505],
[2, u'6.5 A Little Queuing Theory', 0.22630114159703291],
[2, u'6.6 Crosscutting Issues', 0.50704225352112686],
[2, u'6.7 Designing and Evaluating an I/O System - The Internet Archive Cluster', 0.32898538287619156],
[2, u'6.8 Putting It All Together: NetApp FAS6000 Filer', 0.63028663034856347],
[2, u'6.9 Fallacies and Pitfalls', 0.51112162801703775],
[2, u'6.10 Concluding Remarks', 0.65274405050995588],
[2, u'6.11 Historical Perspective and References', 0.5],
[2, u'Case Studies with Exercises by Andrea C. Arpaci-Dusseau and Remzi H. Arpaci-Dusseau', 0.05100045722968586],
[1, u'A Pipelining: Basic and Intermediate Concepts', 0],
[2, 'Chapter Introduction', 1.0],
[2, u'A.1 Introduction', 0.05456790704470011],
[2, u'A.3 How Is Pipelining Implemented?', 0.024006255146430421],
[2, u'A.4 What Makes Pipelining Hard to Implement?', 0.045395058330415572],
[2, u'A.5 Extending the MIPS Pipeline to Handle Multicycle Operations', 0.033527036311023543],
[2, u'A.6 Putting It All Together: The MIPS R4000 Pipeline', 0.019146492225103],
[2, u'A.7 Crosscutting Issues', 0.014954489910564814],
[2, u'A.8 Fallacies and Pitfalls', 0.022662769619263348],
[2, u'A.9 Concluding Remarks', 0.333889816360601],
[2, u'A.10 Historical Perspective and References', 0.14747116208776156],
[1, u'B Instruction Set Principles and Examples', 0],
[2, 'Chapter Introduction', 0.25046963055729493],
[2, u'B.1 Introduction', 0.25287374844439975],
[2, u'B.2 Classifying Instruction Set Architectures', 0.097490727701638927],
[2, u'B.3 Memory Addressing', 0.086639767038569848],
[2, u'B.4 Type and Size of Operands', 0.078915356432282868],
[2, u'B.5 Operations in the Instruction Set', 0.24205843115663134],
[2, u'B.6 Instructions for Control Flow', 0.22157677418506722],
[2, u'B.7 Encoding an Instruction Set', 0.21247070656950484],
[2, u'B.8 Crosscutting Issues: The Role of Compilers', 0.070239682382214896],
[2, u'B.9 Putting It All Together: The MIPS Architecture', 0.11586879046577025],
[2, u'B.10 Fallacies and Pitfalls', 0.044989127768375027],
[2, u'B.11 Concluding Remarks', 0.11440637322442858],
[2, u'B.12 Historical Perspective and References', 0.19835456944258267],
[1, u'C Review of Memory Hierarchy', 0],
[2, 'Chapter Introduction', 0.50062578222778475],
[2, u'C.1 Introduction', 0.054601128592117722],
[2, u'C.2 Cache Performance', 0.087772121427451472],
[2, u'C.3 Six Basic Cache Optimizations', 0.053497371022261611],
[2, u'C.4 Virtual Memory', 0.095056245060405081],
[2, u'C.5 Protection and Examples of Virtual Memory', 0.08886596503751619],
[2, u'C.6 Fallacies and Pitfalls', 0.10136741531271856],
[2, u'C.7 Concluding Remarks', 0.06823091054614068],
[2, u'C.8 Historical Perspective and References', 0.20033388981636061]]

for i in range(0,len(scores)):
    scores[i][1]=to_unicode(scores[i][1]).strip() 
    scores[i][1] = re.sub(u"(\u2018|\u2019)", "'", scores[i][1])

  
