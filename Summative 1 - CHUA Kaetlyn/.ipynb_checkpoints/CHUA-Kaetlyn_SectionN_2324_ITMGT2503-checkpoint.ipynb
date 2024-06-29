{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a45da6f3",
   "metadata": {},
   "source": [
    "# General Instructions\n",
    "Change the filenames to LastName-FirstName_Section_M-N_2324_ITMGT2503 <br>\n",
    "__Ex. GAW-Adriel_SectionM_2324_ITMGT2503__"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d6da16c7",
   "metadata": {},
   "source": [
    "# Question 1: Watch Your Words\n",
    "Your task is to count the number of times that each word was used in a movie script! Please be guided by the instructions below!"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2ac08c4d",
   "metadata": {},
   "source": [
    "#### 1a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "733f65e0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('A', 59), ('B', 100), ('C', 20), ('D', 88), ('E', 25), ('F', 38)]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# First, to help guide you, here is a list containing tuples. Run this block of code to initialize the list\n",
    "list_of_tuples = [('A',59),('B',100),('C',20),('D',88),('E',25),('F',38)]\n",
    "\n",
    "list_of_tuples"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "be1700c1",
   "metadata": {},
   "source": [
    "If we want to __sort this tuple according to the numerical value__, using the sort() without any other arguments will not suffice. But, diving a bit deeper into the sort() function, we can see that it can accept two parameters: \n",
    "\n",
    "- `key` which is what will be used as the basis for sorting\n",
    "- `reverse` which accepts a Boolean value to determine if the sorting will be ascending or descending\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "cde85a14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('B', 100), ('D', 88), ('A', 59), ('F', 38), ('E', 25), ('C', 20)]\n"
     ]
    }
   ],
   "source": [
    "# execute this cell to see how the two arguments help us achieve the desired result\n",
    "\n",
    "list_of_tuples.sort(key=lambda x: x[1], reverse=True)\n",
    "\n",
    "print(list_of_tuples)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d9503f7e",
   "metadata": {},
   "source": [
    "#### 1b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57374ae4",
   "metadata": {},
   "outputs": [],
   "source": [
    "# To formally start this problem:\n",
    "# Load the \"script.json\" file and store it in the `jsondata` variable. \n",
    "# The dictionary will contain the \"line number\" (starting from 0) as the key, \n",
    "# and the lines itself as the value\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 281,
   "id": "f19eaf5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "with open(\"script.json\",\"r\") as file:\n",
    "    jsondata = json.load(file)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7ff1d466",
   "metadata": {},
   "source": [
    "#### 1c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 284,
   "id": "bfd0f682",
   "metadata": {},
   "outputs": [],
   "source": [
    "# To process the lines in the script, you need to do the following in chronological order:\n",
    "#### Convert all characters to uppercase characters\n",
    "#### Remove the following pieces of text: <P>, </P>, <B>, </B>, <I>, </I>\n",
    "#### Remove all the unnecessary punctuation symbols denoted in the string below\n",
    "unnecessary_punctuation = r\"&$@[].,'#()-\\\"!?’_;:/\"\n",
    "#for i in range(0, len(jsondata)):\n",
    " #   jsondata[str(i)]=str(jsondata[str(i)])\n",
    "for i in range(0, len(jsondata)):\n",
    "    while \"<p>\" in jsondata[str(i)]:\n",
    "        jsondata[str(i)]=jsondata[str(i)].replace(\"<p>\",\"\")\n",
    "    while \"</p>\" in jsondata[str(i)]:\n",
    "        jsondata[str(i)]=jsondata[str(i)].replace(\"</p>\",\"\")\n",
    "    while \"<b>\" in jsondata[str(i)]:\n",
    "        jsondata[str(i)]=jsondata[str(i)].replace(\"<b>\",\"\")\n",
    "    while \"</b>\" in jsondata[str(i)]:\n",
    "        jsondata[str(i)]=jsondata[str(i)].replace(\"</b>\",\"\")\n",
    "    while \"<i>\" in jsondata[str(i)]:\n",
    "        jsondata[str(i)]=jsondata[str(i)].replace(\"<i>\",\"\")\n",
    "    while \"</i>\" in jsondata[str(i)]:\n",
    "        jsondata[str(i)]=jsondata[str(i)].replace(\"</i>\",\"\")\n",
    "for i in range(0, len(jsondata)):\n",
    "    for j in unnecessary_punctuation:\n",
    "        while j in jsondata[str(i)]:\n",
    "            jsondata[str(i)]=jsondata[str(i)].replace(j,\" \")\n",
    "for i in range(0, len(jsondata)):\n",
    "    jsondata[str(i)]=jsondata[str(i)].upper()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eb694aa4",
   "metadata": {},
   "source": [
    "#### 1d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 287,
   "id": "0fb22eb9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# From here, create a dictionary called `wordcount_dictionary` that will have the key:value pair of word:count\n",
    "# But, only include words that are three (3) letters or more\n",
    "wordcount_dictionary={}\n",
    "words=[]\n",
    "for i in range(0, len(jsondata)):\n",
    "    jsondata[str(i)]=jsondata[str(i)].split()\n",
    "    for j in jsondata[str(i)]:\n",
    "        if len(j)>=3:\n",
    "            words.append(j)\n",
    "for i in words:\n",
    "    wordcount_dictionary.update({i:words.count(i)})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 288,
   "id": "b6cab676",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Looks Good!\n"
     ]
    }
   ],
   "source": [
    "# If there were no errors in the way you processed your data, \n",
    "# this should output \"Looks Good!\"  \n",
    "\n",
    "import numpy as np\n",
    "import pandas as pd \n",
    "\n",
    "df1 = pd.read_json(\"output_dictionary_Q1.json\",typ=\"dictionary\").sort_values()\n",
    "df2 = pd.Series(wordcount_dictionary).sort_values()\n",
    "\n",
    "assert df1.equals(df2), \"The dictionaries are not equal. Please check your code again.\"\n",
    "\n",
    "print(\"Looks Good!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3d81395c",
   "metadata": {},
   "source": [
    "#### 1e"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 297,
   "id": "9891020e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Afterwards, we want to convert that dictionary to a list containing tuples\n",
    "# Create a list called \"final_wordlist_of_tuples\" containing tuples \n",
    "# Each tuple should be as follows: (word,count)\n",
    "# Sort the list by `count` (the second element of the tuple) in descending order\n",
    "# A correct sample is shown in the markdown cell below\n",
    "# Hint: this can be done using lambda but you can use a regular function definition. \n",
    "# Make sure you go through the mini-tutorial at the start of this problem.\n",
    "\n",
    "final_wordlist_of_tuples = [(k, v) for k, v in wordcount_dictionary.items()]\n",
    "final_wordlist_of_tuples.sort(key=lambda tup: tup[1], reverse=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 677,
   "id": "d741980a-a62c-45a0-86e2-001b723f8675",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"sorted_wordcount_Q1\",\"w\") as file:\n",
    "    json.dump(final_wordlist_of_tuples,file)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7d38d8e3",
   "metadata": {},
   "source": [
    "___<div align=\"center\">Once sorted, this should be the output of the first five items.</div>___\n",
    "\n",
    "|         |             |\n",
    "|:--------|------------:|\n",
    "| THE     |         830 |\n",
    "| JOY     |         585 |\n",
    "| AND     |         351 |\n",
    "| RILEY   |         326 |\n",
    "| SADNESS |         274 |"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "358fdc4f",
   "metadata": {},
   "source": [
    "# Question 2: Wait... What is LP Doing Here?\n",
    "I swear you don't need to do LP here. In fact, the LP formulation is already shown below! "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4df54d5e",
   "metadata": {},
   "source": [
    "#### LP Problem\n",
    "In the realm of Sanctoria, nestled deep within the misty forests and craggy mountains, lies the legendary dungeon of The Lost King. It is said to be filled with untold riches, ancient relics, and formidable monsters guarding its treasures. As the wise and benevolent ruler of Sanctoria, King Hexter has decided to assemble a daring raiding party to plunder the depths of the dungeon and reclaim its treasures for the kingdom.\n",
    "\n",
    "As the illustrious ruler of Sanctoria, King Hexter is faced with the daunting task of assembling a formidable dungeon raiding party. The success of the raid hinges upon the careful selection and allocation of resources to hire Fighters, Rangers, and Clerics for the expedition into the depths of the Lost King’s home.\n",
    "\n",
    "In the planning of this dungeon raid, the King’s advisors have provided him with the following: Gold: The kingdom's treasury can afford to spend no more than 18000 gold coins on hiring adventurers. Each Fighter costs 1000 gold coins, each Ranger costs 600 gold coins, and each Cleric costs 750 gold coins. Lumber: The construction of necessary equipment for each troop requires ample quality lumber. The kingdom has 12000 units of lumber available for the raid. Each Fighter requires 500 units, each Ranger requires 750 units, and each Cleric requires 300 units. Food: The raid will last several weeks so food must be kept and stored during the raid. The raid will be able to carry 1500 units of food available for the raid. Each Fighter requires 50 units, each Ranger requires 45 units, and each Cleric requires 75 units. Power: The power of the raiding party will dictate the level of the raid’s success. Each Fighter gives 10 points, each Ranger gives 12 points, each Cleric gives 16 points.\n",
    "\n",
    "The King’s military advisors have also discussed strategies that will be employed in the raid: Having more Fighters than Rangers will bolster the raiding party's frontline defense To avoid casualties, each Cleric must have at most 3 Fighters that they are supporting"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e7083e5f",
   "metadata": {},
   "source": [
    "# LP Formulation\n",
    "\n",
    "**Decision Variables:**\n",
    "- (F): Number of Fighters\n",
    "- (R): Number of Rangers\n",
    "- (C): Number of Clerics\n",
    "\n",
    "**Objective:** Maximize the power of the raiding party.\n",
    "\n",
    "$$ \\text{Maximize Z:  } 10F + 12R + 16C $$\n",
    "\n",
    "\n",
    "**Subject to:**\n",
    "\n",
    "\\begin{aligned}\n",
    "1000F + 600R + 750C &\\leq 18000 && \\text{(Gold constraint)} \\\\\n",
    "500F + 750R + 300C &\\leq 12000 && \\text{(Lumber constraint)} \\\\\n",
    "50F + 45R + 75C &\\leq 1500 && \\text{(Food constraint)} \\\\\n",
    "F, R, C &\\geq 0 && \\text{(Non-negativity constraints)}\n",
    "\\end{aligned}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 343,
   "id": "3edb6f22",
   "metadata": {},
   "outputs": [],
   "source": [
    "# With the LP Formulation as a basis, find the optimal solution to the problem using Python\n",
    "# Use the variable `optimal_Z` to store the value of the Maximum Z\n",
    "# Use the variables `optimal_F`, `optimal_R`, and `optimal_C` to store \n",
    "# the optimal solution of Fighters, Rangers, and Clerics respectively\n",
    "# Note: There may be multiple configurations of F, R, C to attain the Maximum Z. \n",
    "# Hint: Don't use your DecSci brain, use your Python programming brain\n",
    "f=[18000/1000, 12000//500, 1500//50,0]\n",
    "maxf=max(f)\n",
    "r=[18000//600, 12000//750, 1500//45,0]\n",
    "maxr=max(r)\n",
    "c=[18000//750, 12000//300, 1500//75,0]\n",
    "maxc=max(c)\n",
    "posvalues=[]\n",
    "for f in range(0,int(maxf)):\n",
    "    for r in range(0,int(maxr)):\n",
    "        for c in range(0,int(maxr)):\n",
    "            if 1000*f+600*r+750*c<=18000:\n",
    "                if 500*f + 750*r + 300*c <= 12000:\n",
    "                    if 50*f +45*r + 75*c <=1500:\n",
    "                        posvalues.append(10*f+12*r+16*c)\n",
    "optimal_Z=max(posvalues)\n",
    "for f in range(0,int(maxf)):\n",
    "    for r in range(0,int(maxr)):\n",
    "        for c in range(0,int(maxr)):\n",
    "            if 10*f+12*r+16*c==optimal_Z:\n",
    "                if 1000*f+600*r+750*c<=18000:\n",
    "                    if 500*f + 750*r + 300*c <= 12000:\n",
    "                        if 50*f +45*r + 75*c <=1500:\n",
    "                            optimal_F=f\n",
    "                            optimal_R=r\n",
    "                            optimal_C=c\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 345,
   "id": "739011e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Looks Good!\n"
     ]
    }
   ],
   "source": [
    "# If there were no errors in the way you processed your data, \n",
    "# this should output \"Looks Good!\"  \n",
    "\n",
    "assert optimal_Z == 344\n",
    "assert (1000*optimal_F + 600*optimal_R + 750*optimal_C) <= 18000\n",
    "assert (500*optimal_F + 750*optimal_R + 300*optimal_C) <= 12000\n",
    "assert (50*optimal_F + 45*optimal_R + 75*optimal_C) <= 1500\n",
    "print(\"Looks Good!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e4d68adb",
   "metadata": {},
   "source": [
    "# Question 3: Collatz"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "77584d2c",
   "metadata": {},
   "source": [
    "#### 3a"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "49defdc9",
   "metadata": {},
   "source": [
    "The __Collatz Conjecture__ is a mathematical sequence defined as follows:\n",
    "\n",
    "1. Start with any positive integer n.\n",
    "2. If n is even, divide it by 2 to get n / 2.\n",
    "3. If n is odd, multiply it by 3 and add 1 to get 3n + 1.\n",
    "4. Repeat the process with the resulting number.\n",
    "5. The conjecture states that no matter which positive integer you start with, you will always eventually reach 1."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7067fcd8",
   "metadata": {},
   "source": [
    "As an example, the number 5 will follow this sequence:\n",
    "- Start at __`5`__\n",
    "- 5 is odd, so we multiply by 3 and adds 1 to get __`16`__\n",
    "- 16 is even, so we divide by 2 to get __`8`__\n",
    "- 8 is even, so we divide by 2 to get __`4`__\n",
    "- 4 is even, so we divide by 2 to get __`2`__\n",
    "- 2 is even, so we divide by 2 to get __`1`__\n",
    "- Since the number is 1, we stop the sequence. \n",
    "\n",
    "For the purposes of this problem, let's call the list containing the numbers __[5, 16, 8, 4, 2, 1]__ the __`Collatz Sequence`__. \n",
    "\n",
    "This sequence also has a __`Collatz Length`__ of 6, since the sequence cycled through 6 numbers.\n",
    "\n",
    "The sequence also had a __`Max Collatz`__ of 16, since that was the highest number in the sequence. \n",
    "\n",
    "Lastly, the sequence had a __`Sequence Sum`__ of 36, since that is the sum of all the numbers in the sequence."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 675,
   "id": "3af64fdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Collatz(start_number):\n",
    "    collatz_sequence=[start_number]\n",
    "    ans={}\n",
    "    sum=0\n",
    "    while start_number!=1:\n",
    "        if start_number%2==0:\n",
    "            start_number=start_number/2\n",
    "            collatz_sequence.append(start_number)\n",
    "        else:\n",
    "            start_number=3*start_number+1\n",
    "            collatz_sequence.append(start_number)\n",
    "    for i in collatz_sequence:\n",
    "        sum+=i\n",
    "    ans[\"collatz_sequence\"]=[collatz_sequence]\n",
    "    ans[\"collatz_length\"]=[len(collatz_sequence)]\n",
    "    ans[\"max_collatz\"]=[max(collatz_sequence)]\n",
    "    ans[\"sequence_sum\"]=[sum]\n",
    "    return(ans)\n",
    "\n",
    "    '''\n",
    "    Create a SINGLE FUNCTION that will return the\n",
    "    `Collatz Sequence`, the `Collatz Length`,\n",
    "    and the `Max Collatz` in a dictionary.\n",
    "\n",
    "    The key-value pairs will be the following:\n",
    "    \"collatz_sequence\": the list containing the numbers of the sequence\n",
    "    \"collatz_length\": the length of the sequence\n",
    "    \"max_collatz\": the maximum number achieved in the sequence\n",
    "    \"sequence_sum\": the sum of all the numbers in the sequence \n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    start_number: int\n",
    "        the number used to start the sequence\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    dictionary\n",
    "        the dictionary containing the key-value pairs of the\n",
    "        collatz_sequence, collatz_length, max_collatz, and sequence_sum\n",
    "    '''"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d77c02b7",
   "metadata": {},
   "source": [
    "#### 3b"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 671,
   "id": "7d736c4b-b391-455a-a43f-ed78fb5d10bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Collatz_winner(number_list):\n",
    "    entries={}\n",
    "    lengthlist=[]\n",
    "    maxlist=[]\n",
    "    for i in number_list:\n",
    "        entries[i]=[Collatz(i)]\n",
    "    for i in entries:\n",
    "        lengthlist.append(entries[i][0][\"collatz_length\"])\n",
    "        maxlist.append(entries[i][0][\"max_collatz\"])\n",
    "        keylist=list(entries.keys())\n",
    "    for j in range(0,len(entries)):\n",
    "        if lengthlist[j]==max(lengthlist) and maxlist[j]==max(maxlist):\n",
    "            print(keylist[j])\n",
    "            return(keylist[j])\n",
    "\n",
    "\n",
    "    '''\n",
    "    Given a list of positive integers, return the `winner`\n",
    "    among them. The `winner` is categorized as such:\n",
    "        \n",
    "        1. The number has the largest `collatz_length`; and\n",
    "        2. The number has the largest `max_collatz`\n",
    "\n",
    "    If there is no winner, then the function must return None\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    number_list: list\n",
    "        a list of positive integers\n",
    "\n",
    "    Returns\n",
    "    -------\n",
    "    integer (or NoneType)\n",
    "        the \"winner\" that follows the specific criteria above\n",
    "        returns a None if it does not meet all the criteria above\n",
    "    '''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 673,
   "id": "77f8e082",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "27\n",
      "9\n",
      "97\n",
      "54\n",
      "110\n",
      "129\n"
     ]
    }
   ],
   "source": [
    "assert Collatz_winner(range(1,51)) == 27\n",
    "assert Collatz_winner(range(1,10)) == 9\n",
    "assert Collatz_winner(range(50,100)) == 97\n",
    "assert Collatz_winner(range(50,100,4)) == 54\n",
    "assert Collatz_winner(range(20,131,5)) == 110\n",
    "assert Collatz_winner(range(75,180,9)) == 129"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
