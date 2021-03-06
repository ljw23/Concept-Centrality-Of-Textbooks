import re
from sumy._compat import to_unicode

title="Rasberry PI Cookbook"

scores=[[1, u'Copyright', 0],
[1, u'Chapter 1. Setup and Management', 0],
[2, u'1.0. Introduction', 0.80000000000000004],
[2, u'1.1. Selecting a Model of Raspberry Pi', 0.67080745341614911],
[2, u'1.2. Enclosing a Raspberry Pi', 0.85375494071146241],
[2, u'1.3. Selecting a Power Supply', 0.2949731656356262],
[2, u'1.4. Selecting an Operating System Distribution', 0.65217391304347827],
[2, u'1.5. Writing an SD Card with NOOBS', 0.4310344827586205],
[2, u'1.6. Writing an SD Card Manually (Mac)', 0.43892243381328389],
[2, u'1.7. Writing an SD Card Manually (Windows)', 0.5230637464823199],
[2, u'1.8. Writing an SD Card Manually (Linux)', 0.61944808895962833],
[2, u'1.9. Connecting the System', 0.78260869565217406],
[2, u'1.10. Connecting a DVI or VGA Monitor', 0.71146245059288526],
[2, u'1.11. Using a Composite Video Monitor/TV', 0.47123495293901552],
[2, u'1.12. Using All the Storage on the SD Card', 0.81818181818181823],
[2, u'1.13. Adjusting the Picture Size on your Monitor', 0.69644381223328589],
[2, u'1.14. Maximizing Performance', 0.70164917541229366],
[2, u'1.15. Changing Your Password', 0.6164489117964348],
[2, u'1.16. Setting the Pi to Boot Straight into a Windowing System', 0.81818181818181823],
[2, u'1.17. Shutting Down Your Raspberry Pi', 0.65217391304347827],
[2, u'1.18. Installing the Raspberry Pi Camera Module', 0.49263257671981009],
[1, u'Chapter 2. Networking', 0],
[2, u'2.0. Introduction', 0.8571428571428571],
[2, u'2.1. Connecting to a Wired Network', 0.55714285714285705],
[2, u'2.2. Finding Out Your IP Address', 0.29032364488139623],
[2, u'2.3. Setting a Static IP Address', 0.25820122046846194],
[2, u'2.4. Setting the Network Name of a Raspberry Pi', 0.48896434634974528],
[2, u'2.5. Setting Up a Wireless Connection', 0.52227979274611402],
[2, u'2.6. Connecting with a Console Lead', 0.53443894049088114],
[2, u'2.7. Controlling the Pi Remotely with SSH', 0.54976820289064643],
[2, u'2.8. Controlling the Pi Remotely with VNC', 0.9375],
[2, u'2.9. File Sharing on a Mac Network', 0.66032608695652151],
[2, u'2.10. Sharing the Pi Screen on a Mac', 0.60631578947368425],
[2, u'2.11. Using a Raspberry Pi for Network Attached Storage', 0.68478260869565177],
[2, u'2.12. Network Printing', 0.54794520547945214],
[1, u'Chapter 3. Operating System', 0],
[2, u'3.0. Introduction', 0.66666666666666663],
[2, u'3.1. Moving Files Around Graphically', 0.64031620553359681],
[2, u'3.2. Starting a Terminal Session', 0.72727272727272729],
[2, u'3.3. Navigating the Filesystem Using a Terminal', 0.48333249026253255],
[2, u'3.4. Copying a File or Folder', 0.46889653016567678],
[2, u'3.5. Renaming a File or Folder', 0.52111982860947859],
[2, u'3.6. Editing a File', 0.49828979138065843],
[2, u'3.7. Viewing the Contents of a File', 0.64031620553359681],
[2, u'3.8. Creating a File Without Using an Editor', 0.56916996047430823],
[2, u'3.9. Creating a Directory', 0.7142857142857143],
[2, u'3.10. Deleting a File or Directory', 0.49612403100775204],
[2, u'3.11. Performing Tasks with Superuser Privileges', 0.62937062937062938],
[2, u'3.12. Understanding File Permissions', 0.55419661187346658],
[2, u'3.13. Changing File Permissions', 0.68899521531100494],
[2, u'3.14. Changing File Ownership', 0.6028194367405888],
[2, u'3.15. Making a Screen Capture', 0.65217391304347827],
[2, u'3.16. Installing Software with apt-get', 0.9285714285714286],
[2, u'3.17. Removing Software Installed with apt-get', 0.8571428571428571],
[2, u'3.18. Fetching Files from the Command Line', 0.40274599542334089],
[2, u'3.19. Fetching Source Code with git', 0.75],
[2, u'3.20. Running a Program or Script Automatically on Startup', 0.50050646487517136],
[2, u'3.21. Running a Program or Script Automatically at Regular Intervals', 0.62608695652173929],
[2, u'3.22. Finding Things', 0.72727272727272707],
[2, u'3.23. Using the Command-Line History', 0.49689726764014053],
[2, u'3.24. Monitoring Processor Activity', 0.58508044856167751],
[2, u'3.25. Working with File Archives', 0.63842135809634348],
[2, u'3.26. Listing Connected USB Devices', 0.58695652173913049],
[2, u'3.27. Redirecting Output from the Command Line to a File', 0.64031620553359681],
[2, u'3.28. Concatenating Files', 0.68246445497630326],
[2, u'3.29. Using Pipes', 0.66220735785953189],
[2, u'3.30. Hiding Output to the Terminal', 0.56916996047430835],
[2, u'3.31. Running Programs in the Background', 0.76923076923076927],
[2, u'3.32. Creating Command Aliases', 0.88888888888888884],
[2, u'3.33. Setting the Date and Time', 0.7142857142857143],
[2, u'3.34. Finding Out How Much Room You Have on the SD Card', 0.45652173913043481],
[1, u'Chapter 4. Software', 0],
[2, u'4.0. Introduction', 0.66666666666666663],
[2, u'4.1. Making a Media Center', 0.52342699283922778],
[2, u'4.2. Installing Office Software', 0.82639885222381648],
[2, u'4.3. Installing other Browsers', 0.8125],
[2, u'4.4. Using the Pi Store', 0.72670807453416142],
[2, u'4.5. Making a Webcam Server', 0.41648762106237397],
[2, u'4.6. Running a Vintage Game Console Emulator', 0.63085714285714256],
[2, u'4.7. Running Minecraft', 0.48659608019824274],
[2, u'4.8. Running Open Arena', 0.58947368421052626],
[2, u'4.9. Raspberry Pi Radio Transmitter', 0.51428571428571446],
[2, u'4.10. Running GIMP', 0.81818181818181823],
[2, u'4.11. Internet Radio', 0.5464444811087279],
[1, u'Chapter 5. Python Basics', 0],
[2, u'5.0. Introduction', 0.75],
[2, u'5.1. Deciding Between Python 2 and Python 3', 0.72240802675585292],
[2, u'5.2. Editing Python Programs with IDLE', 0.59259259259259256],
[2, u'5.3. Using the Python Console', 0.70588235294117652],
[2, u'5.4. Running Python Programs from the Terminal', 0.64129554655870435],
[2, u'5.5. Variables', 0.58623242042931167],
[2, u'5.6. Displaying Output', 0.58695652173913038],
[2, u'5.7. Reading User Input', 0.8571428571428571],
[2, u'5.8. Arithmetic', 0.70434782608695656],
[2, u'5.9. Creating Strings', 1.1111111111111112],
[2, u'5.10. Concatenating (Joining) Strings', 0.83333333333333337],
[2, u'5.11. Converting Numbers to Strings', 0.5714285714285714],
[2, u'5.12. Converting Strings to Numbers', 0.69999999999999996],
[2, u'5.13. Find the Length of a String', 0.59999999999999998],
[2, u'5.14. Find the Position of One String Inside Another', 0.625],
[2, u'5.15. Extracting Part of a String', 0.91666666666666663],
[2, u'5.16. Replacing One String of Characters with Another Inside a String', 0.7804878048780487],
[2, u'5.17. Converting a String to Upper- or Lowercase', 0.54262835609985871],
[2, u'5.18. Running Commands Conditionally', 0.43741588156123828],
[2, u'5.19. Comparing Values', 0.6149068322981367],
[2, u'5.20. Logical Operators', 0.5],
[2, u'5.21. Repeating Instructions an Exact Number of Times', 0.23999999999999996],
[2, u'5.22. Repeating Instructions Until Some Condition Changes', 0.41432225063938621],
[2, u'5.23. Breaking Out of a Loop', 0.33391304347826095],
[2, u'5.24. Defining a Function in Python', 0.50223214285714279],
[1, u'Chapter 6. Python Lists and Dictionaries', 0],
[2, u'6.0. Introduction', 0.66666666666666663],
[2, u'6.1. Creating a List', 0.81818181818181823],
[2, u'6.2. Accessing Elements of a List', 0.90909090909090906],
[2, u'6.3. Find the Length of a List', 0.66666666666666663],
[2, u'6.4. Adding Elements to a List', 0.43702579666160857],
[2, u'6.5. Removing Elements from a List', 0.57960644007155626],
[2, u'6.6. Creating a List by Parsing a String', 0.50471063257065951],
[2, u'6.7. Iterating over a List', 0.43043478260869572],
[2, u'6.8. Enumerating a List', 0.52682926829268306],
[2, u'6.9. Sorting a List', 0.55555555555555558],
[2, u'6.10. Cutting Up a List', 0.84615384615384615],
[2, u'6.11. Applying a Function to a List', 0.7142857142857143],
[2, u'6.12. Creating a Dictionary', 0.69565217391304346],
[2, u'6.13. Accessing a Dictionary', 0.76923076923076927],
[2, u'6.14. Removing Things from a Dictionary', 0.670807453416149],
[2, u'6.15. Iterating over Dictionaries', 0.31080031080031084],
[1, u'Chapter 7. Advanced Python', 0],
[2, u'7.0. Introduction', 0.5],
[2, u'7.1. Formatting Numbers', 0.47959870312595582],
[2, u'7.2. Formatting Dates', 0.81818181818181823],
[2, u'7.3. Returning More Than One Value', 0.45415634151836004],
[2, u'7.4. Defining a Class', 0.46344827586206899],
[2, u'7.5. Defining a Method', 0.7142857142857143],
[2, u'7.6. Inheritance', 0.66898954703832791],
[2, u'7.7. Writing to a File', 0.56916996047430835],
[2, u'7.8. Reading from a File', 0.39792746113989635],
[2, u'7.9. Pickling', 0.43590923401060711],
[2, u'7.10. Handling Exceptions', 0.45923858879808643],
[2, u'7.11. Using Modules', 0.68292682926829273],
[2, u'7.12. Random Numbers', 0.79314565483476129],
[2, u'7.13. Making Web Requests from Python', 0.48160535117056857],
[2, u'7.14. Command-Line Arguments in Python', 0.49680090327436965],
[2, u'7.15. Sending Email from Python', 0.72411428571428571],
[2, u'7.16. Writing a Simple Web Server in Python', 0.51191573403554969],
[1, u'Chapter 8. GPIO Basics', 0],
[2, u'8.0. Introduction', 0.5],
[2, u'8.1. Finding Your Way Around the GPIO Connector', 0.65150207422668927],
[2, u'8.2. Keeping Your Raspberry Pi Safe when Using the GPIO Connector', 0.64380149453918378],
[2, u'8.3. Installing RPi.GPIO', 0.56105610561056107],
[2, u'8.4. Setting Up I2C', 0.55072463768115942],
[2, u'8.5. Using I2C Tools', 0.5625],
[2, u'8.6. Setting Up SPI', 0.56559308719560097],
[2, u'8.7. Freeing the Serial Port', 0.83333333333333337],
[2, u'8.8. Installing PySerial for Access to the Serial Port from Python', 0.75],
[2, u'8.9. Installing Minicom to Test the Serial Port', 0.60869565217391319],
[2, u'8.10. Using a Breadboard with Jumper Leads', 0.70840787119856885],
[2, u'8.11. Using a Breadboard with a Pi Cobbler', 0.80000000000000004],
[2, u'8.12. Converting 5V Signals to 3.3V with Two Resistors', 0.54269621346051045],
[2, u'8.13. Converting 5V Signals to 3.3V with a Level Converter Module', 0.72277992277992276],
[2, u'8.14. Powering a Raspberry Pi with Batteries', 0.56962025316455678],
[2, u'8.15. Powering a Raspberry Pi with a LiPo Battery', 0.69282013323464109],
[2, u'8.16. Getting Started with a PiFace Digital Interface Board', 0.4428765264586158],
[2, u'8.17. Getting Started with a Gertboard', 0.49728369529145966],
[2, u'8.18. Getting Started with a RaspiRobot Board', 0.58775510204081649],
[2, u'8.19. Using a Humble Pi Prototyping Board', 0.64437117286858214],
[2, u'8.20. Using a Pi Plate Prototyping Board', 0.48489261012013118],
[2, u'8.21. Using a Paddle Terminal Breakout Board', 0.50537818435796511],
[1, u'Chapter 9. Controlling Hardware', 0],
[2, u'9.0. Introduction', 0.5],
[2, u'9.1. Connecting an LED', 0.50315078858220641],
[2, u'9.2. Controlling the Brightness of an LED', 0.44432995002318509],
[2, u'9.3. Make a Buzzing Sound', 0.52233496836035509],
[2, u'9.4. Switching a High-Power DC Device Using a Transistor', 0.39990031639343548],
[2, u'9.5. Switching a High-Power Device Using a Relay', 0.64325917984454573],
[2, u'9.6. Controlling High-Voltage AC Devices', 0.8666666666666667],
[2, u'9.7. Making a User Interface to Turn Things On and Off', 0.62989445011916934],
[2, u'9.8. Making a User Interface to Control PWM Power for LEDs and Motors', 0.51158108915527767],
[2, u'9.9. Changing the Color of an RGB LED', 0.52700894150394939],
[2, u'9.10. Using Lots of LEDs (Charlieplexing)', 0.48528323724116756],
[2, u'9.11. Using an Analog Meter as a Display', 0.55242966751918166],
[2, u'9.12. Programming with Interrupts', 0.47026693187557267],
[2, u'9.13. Controlling GPIO Outputs Using a Web Interface', 0.33806467365020637],
[1, u'Chapter 10. Motors', 0],
[2, u'10.0. Introduction', 0.5],
[2, u'10.1. Controlling Servo Motors', 0.59122527988331419],
[2, u'10.2. Controlling a Large Number of Servo Motors', 0.40914367471145469],
[2, u'10.3. Controlling the Speed of a DC Motor', 0.58661767734459991],
[2, u'10.4. Controlling the Direction of a DC Motor', 0.36231282110216301],
[2, u'10.5. Using a Unipolar Stepper Motor', 0.50057727135810126],
[2, u'10.6. Using a Bipolar Stepper Motor', 0.34635349556381839],
[2, u'10.7. Using a RaspiRobot Board to Drive a Bipolar Stepper Motor', 0.44114827483682012],
[2, u'10.8. Building a Simple Robot Rover', 0.46997632192300037],
[1, u'Chapter 11. Digital Inputs', 0],
[2, u'11.0. Introduction', 0.59999999999999998],
[2, u'11.1. Connecting a Push Switch', 0.3190281664469225],
[2, u'11.2. Toggling with a Push Switch', 0.56358073009321852],
[2, u'11.3. Using a Two-Position Toggle or Slide Switch', 0.71146245059288526],
[2, u'11.4. Using a Center-Off Toggle or Slide Switch', 0.5450581395348838],
[2, u'11.5. Debouncing a Button Press', 0.41284918514114072],
[2, u'11.6. Using an External Pull-up Resistor', 0.74634146341463448],
[2, u'11.7. Using a Rotary (Quadrature) Encoder', 0.46743967928418995],
[2, u'11.8. Using a Keypad', 0.55166589478845984],
[2, u'11.9. Detecting Movement', 0.5924950625411457],
[2, u'11.10. Adding GPS to the Raspberry Pi', 0.37784256559766771],
[2, u'11.11. Intercepting Keypresses', 0.58321480032530426],
[2, u'11.12. Intercepting Mouse Movements', 0.47035855391293063],
[2, u'11.13. Using a Real-Time Clock Module', 0.52142939010382616],
[1, u'Chapter 12. Sensors', 0],
[2, u'12.0. Introduction', 0.75],
[2, u'12.1. Using Resistive Sensors', 0.5020847815242695],
[2, u'12.2. Measuring Light', 0.8571428571428571],
[2, u'12.3. Detecting Methane', 0.51527081293172006],
[2, u'12.4. Measuring a Voltage', 0.39722572509457771],
[2, u'12.5. Reducing Voltages for Measurement', 0.62990455991516403],
[2, u'12.6. Using Resistive Sensors with an ADC', 0.57558139534883723],
[2, u'12.7. Measuring Temperature with an ADC', 0.5857627118644072],
[2, u'12.8. Measuring Acceleration', 0.56316619718893202],
[2, u'12.9. Measuring Temperature Using a Digital Sensor', 0.64962406015037621],
[2, u'12.10. Measuring Distance', 0.40833234702331656],
[2, u'12.11. Displaying Sensor Values', 0.56445047489823597],
[2, u'12.12. Logging to a USB Flash Drive', 0.50727120755526656],
[1, u'Chapter 13. Displays', 0],
[2, u'13.0. Introduction', 0.59999999999999998],
[2, u'13.1. Using a Four-Digit LED Display', 0.50823529411764712],
[2, u'13.2. Displaying Messages on an I2C LED matrix', 0.62512253185828281],
[2, u'13.3. Using Pi-Lite', 0.59422794212467434],
[2, u'13.4. Displaying Messages on an Alphanumeric LCD', 0.56640628071670851],
[1, u'Chapter 14. Arduino and Raspberry Pi', 0],
[2, u'14.0. Introduction', 0.90000000000000002],
[2, u'14.1. Programming an Arduino from Raspberry Pi', 0.56492239039355319],
[2, u'14.2. Communicating with the Arduino by Using the Serial Monitor', 0.75000000000000011],
[2, u'14.3. Setting Up PyFirmata to Control an Arduino from a Raspberry Pi', 0.448536117874131],
[2, u'14.4. Writing Digital Outputs on an Arduino from a Raspberry Pi', 0.67119246334214322],
[2, u'14.5. Using PyFirmata with TTL Serial', 0.60793695468618048],
[2, u'14.6. Reading Arduino Digital Inputs Using PyFirmata', 0.63402892869884042],
[2, u'14.7. Reading Arduino Analog Inputs Using PyFirmata', 0.38483603665514166],
[2, u'14.8. Analog Outputs (PWM) with PyFirmata', 0.60550458715596356],
[2, u'14.9. Controlling a Servo Using PyFirmata', 0.56593886462882093],
[2, u'14.10. Custom Communication with an Arduino over TTL Serial', 0.35179692350141406],
[2, u'14.11. Custom Communication with an Arduino over I2C', 0.44613051238549084],
[2, u'14.12. Using Small Arduinos with a Raspberry Pi', 0.77837837837837853],
[2, u'14.13. Getting Started with an aLaMode Board and a Raspberry Pi', 0.48648648648648651],
[2, u'14.14. Using an Arduino Shield with an aLaMode Board and a Raspberry Pi', 0.66898954703832758],
[2, u'14.15. Using Gertboard as an Arduino Interface', 0.32491375745943973],
[1, u'Appendix A. Parts and Suppliers', 0],
[2, u'Parts', 0.024076855858305587],
[2, u'Prototyping Equipment', 0.273603417152471],
[2, u'Resistors and Capacitors', 0.33768863050843173],
[2, u'Transistors and Diodes', 0.66722268557130937],
[2, u'Integrated Circuits', 0.43189410801490613],
[2, u'Opto-Electronics', 1.0],
[2, u'Modules', 0.25644983654501463],
[2, u'Miscellaneous', 0.25049966688874081]]



for i in range(0,len(scores)):  
    scores[i][1]=to_unicode(scores[i][1]).strip() 
    scores[i][1] = re.sub(u"(\u2018|\u2019)", "'", scores[i][1])
