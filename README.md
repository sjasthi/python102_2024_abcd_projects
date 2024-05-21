# python102_2024_abcd_projects
This repo contains all the projects done by Python 102 students (the class of 2023-2024) for Project ABCD.
## Convention to be used -  <first_name>_<simple_project_name>.py

============================================================================

Our Strategy:
First phase:
+ Project 10  (Frequency Table - Each student has done this as part of Assignment 18)
+ Project 15 (Frequency Table with out the stop words - Each student has done this as part of Assignment 18)

  Second Phase
+ Projects assigned to you

  Third Phase
+ Project 80 (PPT generation - Each student will do this)
+ Project 90 (Google translation - Each student will do this)

Rest of the projects will be distributed across the class. If you are interested in any specific project, please drop me a note.

==============================================================================


Background / Recap: You already did an assignment where you can call an API from http://abcd2.projectabcd.com and display a dress information as HTML.

For all the following projects, you will make use of the same mechanism (which is basically call the API for an ID and get the details about it).

+ https://abcd2.projectabcd.com/api/getinfo.php?id=50  (get the information about 50)
+ https://abcd2.projectabcd.com/api/getinfo.php?id=650  (get the information about 650).

### [Project 10] (All: Assignment 18) Frequency table of SHEROES book:

N = 10 or 20 or 30 (some number given by the user)
What are the top N words used in the SHEROES book? 
You will be given the ABCD IDs of 256 profiles

### [Project 15] (All: Assignment 19) This is an extension to the Project 10
We will maintain a list of stop words in a file (stop_words.txt). Stop words are such "the, a, an, in, he, she, her".
We will exclude those words in our top N frequency table.
So, we want to take this as an optional parameter.
convert_word_list_to_frequency_table(word_list, exclude_stop_words = True)

### [Project 20] (Ahala) Word Cloud based on the frequency
Can you create a Word Cloud based on the top N frequent words?

https://resilienteducator.com/wp-content/uploads/2015/09/Revising-With-Pictures-How-Word-Clouds-Help-Students-Become-Better-Writers.jpg

### [Project 30] (Rama noonela) Length Table

Reference: https://www.w3schools.com/

Can you produce a HTML table with the following fields?

Serial No (of SHEROES), ABCD ID, Name,  Length of the description, Length of Did you know, Total Length

And can you highlight all the ROWS where the "Total Length" > some threshold N words (For example, N can be 225)


### [Project 40] (Nidhi) Language Analysis - Noun and Adjective count

https://abcd2.projectabcd.com/  (click on any image to see the description and did_you_know?)

Given description and did_you_know, how many words are nouns and how many words are adjectives?

For the SHEROES book, can you produce this HTML table?

Serial No (of SHEROES), ABCD ID, Name, count_of_nouns, count_of_adjectives


### [Project 50] (Pavani)  Language Analysis - Ease of Reading, Lexile Score, Grade Level

For the SHEROES book profiles, how do I assess our current writing is suitable for middle and high school students?

What are the language factors we can determine based on python libraries (eg: textstats)?
Can we do comparative analysis?

Serial No (of SHEROES), ABCD ID, Name,  measure_1 (lexile score), measure_2 (grade level), measure_3 (ease of reading)

### [Project 60] (Jasthi to demo) Who is my pair?

It is interesting to note that some SHEROES are inspired by other SHEROES.
Some SHEROES may have friendships or some references.
For example, Pandita Ramabai attended the graduation of Anandi Joshi (first doctor from India).

How many such pairs exist in our SHEROS book?

Here is the algorithm / logic:
-- you are given the IDs of 256 sheroes.
-- for each ID, get the name, description and did you know
-- store the data into some suitable data structure
-- for each ID,
            --- get the name
            -- check whether the same name exists in the description and did you know fields of all other 255 IDs
            -- if there exists a name, we got a pair. Otherwise, move on to the next ID.


### [Project 70] (Mayukha) Create Alphabet book?

Problem Statement: I want to generate an alphabet book of SHEROES. 
It will have 26 pages. Each page will contain a character starting with a specific letter (For example, "I" may have "Indira Gandhi")

You can produce the book as follows.
(option 1) As a pure text file
(option 2) As a Power Point file including the Picture of the character.


### [Project 80] (All) (Jasthi to demo the example) Generate Power Point for SHEROES book

Assume that you are given the IDs of 256 sheroes.

Using the power point python library and using the APIs from the Project ABCD,
Det the name, description, did you know from the web site.
Download the image from the website.
Place those on the PPTX slide
And save the PPTX slide.

Implementation  / Testing Strategy: You always test your code with 5 or 6 IDs. Once it is proven, feed all 256 IDs.

### [Project 90] (All) (Jasthi to demo the example) Translation

Assume that you are given the IDs of 256 sheroes.
The user is also specifying the destination language for the translation (eg: Telugu, Hindi, Tamil, or other)
Using the "google translation APIs", we want to translate (name, description and did you know) into the destination language.

(option 1) As a pure text file
(option 2) As a Power Point file including the Picture of the character.


### [Project 100] (Anika) Generate a Text file for translators

Problem Statement: The machine translation done by google will be awful. We can not use it as-is. We must pass it through the professional / human translator.

How do I help the translator? I would like to send 
[1] English text (name, description, did you know)
[2] Machine translated text (from the google API)

And send 256 + 256 pages of text document to the translator.  (English 1, Telugu 1 --> English 2 Telugu 2)


### [Project 110] (Prabhav Sai) Generate Word Document for review

Here you are generating a WORD document through python program
Every profile will be on a separate page of the word document.


### [Project 120] (Krish) Compare Master version with the local version

Problem Statement: We (authors) are updating the write-ups on a google drive (which can be exported as EXCEL file). This is the "Work in Process" working document.

And periodically, this data will need to transferred to the website at www.projectabcd.com

How do I know which information/data got changed in my local version (i.e on google drive)?

So, we need a tool that can compare
-- the information on the google drive
with
-- the information on the website (which you can get from the APIs)

And produce a report of what IDs I need to consider for updating on the website.
(I want to update only those IDs who got some updates on the local version; I do not want to update all 256 each time)

Input: You are given google sheet hosted on a google drive. How can you connect to it from python? Then read the text from google sheet (you need to explore pandas to read the excel; and then compare it with projectabcd.com website to report out any discrepancies)

### [Project 130] (Sai Chennupati) Date of Birth Analyzer

Can you create a histogram of sheroes based on their birth year (century)

### [Project 140] (Samhita) Histogram of Indian States

How many are from Tamilnadu?
How many are from Bihar?
What is the frequency table based on the state?
In text format - OK
In visual format - matplotlib

### [Project 150]  (Ahala)  Padma Awards:

How many SHEROES got Padma Awards?
Who are they? What awards they got?

(Requirement) We need to display the output in two different ways.

Name-Driven output
------------------
Anita Pauldurai - Padma Shri
Mother Teresa - Padma Shri, Padma Bhushan, Bharat Ratna
..
..

Award-Driven output
-------------------
Padma Shri - Anita Pauldurai, Mother Teresa
Padma Bhushan - Mother Teresa
Bharata Ratna - Mother Teresa

(Design/Implementation)
-----------------------
Option 1: list of tuples
Option 2: dictionary of [name, award list]
Option 3: dictionary of [award, name_list]
option 4: option 2 and option 3 in one go

I can somehow acheive the final result (OK)
I am achieving the result in the most efficient way (python 102 level)


### [Project 160] (Sumedh Ghatti) Word Search Puzzle Generator

Identify 10 words for each ID.
Given an option to the user to edit / modify / add / delete the auto-selected word list
Generate word search puzzle for the final word list.
Generate it as Power Point
Also show the solutions.

### [Project 170] (Instructor Demo) How many books are shipped ?  (Demonstrated in the class)

I have a text file with addresses and the header of the address is in this format
If a book is shipped to a profiled SHERO, I am adding (SHERO) at the end of the line.

ID of the address   (number)  copy/copies/book/books  (SHERO)

This header is followed by the address.

So the final output should be:
--> Total number of books shipped: 600
--> Total number of books shipped to SHEROES: 69
--> Total number of SHEROES: 25


### [Project 180] (Instructor Demo / Exploration - Done)  TTS: Text to Speech

SHEROES writeup should be converted to audio file (mp4) using python libraries.

### [Project 190]  (Prabhav) Convert the text from third person to first person
using automation and AI
Many teachers and children are translating the SHEROES articles from third person to first person
for mono-acts and such.

We can rely on AI to do such translations (aka transformations / rewrites).

This project focusses on integrating with ChatGPT or other tools to convert the SHEROES text from third-person to first person.


### [Project 200] (Prashanthi / Sailakshmi) US spellings are used in the text.

Can you identify all the words that would be spelled differently in UK English.

(Option 1): id_driven display  (verbose)
abcd_id, name,  us_spelling, uk_spelling
1, abala bose, color, colour
1, abala bose, honor, honour
99, sridevi, color, colour

(Option 2): id_driven display   (one row per id)
abcd_id, name,  us_spelling, uk_spelling
1, abala bose, [color, honor], [colour, honour]
99, sridevi, [color], [colour]

(Option 3): word_driven display   
us_spelling, uk_spelling, [abcd_ids], [abcd_names]
color, colour, [1, 99], [abala bose, sridevi]
honor, honour, [1], [abala bose]


### [Project 210] (nakul) Generation of Bingo Tables

Assume 5 * 5  grid (table).
Assume 10 people are playing the bingo

Generate 10 random cards as follows
            From the 256 Sheroes, pick 25 names at random.
            Place those in 5 * 5 grid

(Option 1): Generate text based bingo cards
(Option 2): Generate image based bingo cards
(Option 3): Generate bingo cards containing both text + images

