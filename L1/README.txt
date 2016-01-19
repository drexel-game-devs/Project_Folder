------------README LAB01-----------------


Name								ID
-----------------------------------------
Matthew Freihofer              		mrf77
Joseph Lipinski 					jsl94


Design Description and Instructions:

i) if-else structure to determine if the program 
is being run on the command line or otherwise. If 
the command line is being used, then the first 
argument passed is giong to be the key used to connect
to the weather underground API. Otherwise you MUST supply
your own personal key in order for the program to run.

ii) The program then goes about setting up a connection
to the website. A string is built that represents the websites
URL, and we connect to the website using it. A JSON object is 
then created, and an array is created from that. The Programs
first line of output is the ZipCode of the user, which is obtained
through the original JSON object.

iii) The last part of the program loops over the array created,
starting at its first element, and prints data in the following
order: 1) Date and Time, 2) current condition outside, 3) current 
temperature, 4) Current humidity. Following the data are two newlines
for formatting.



