# Python String Methods Task

## 🎯 Task Description
Your task is to practice **Python string methods** by analyzing and modifying a given text.  
You will need to use most of the functions listed in the summary section.

---

## 📝 Instructions
1. Start with the following string:
   ```python
   text = "   welcome to PYTHON programming 101!   "
   ```

2. Perform the following operations step by step (print the result after each step):

- **strip()** → Remove spaces at the beginning and end.  
- **capitalize()** → Capitalize the first letter of the whole sentence.  
- **upper()** → Convert the text into uppercase.  
- **lower()** → Convert the text into lowercase.  
- **title()** → Make the first letter of each word uppercase.  
- **swapcase()** → Swap the case of all letters.  
- **center(50, '-')** → Center the text inside 50 characters wide, filled with `-`.  
- **count("o")** → Count how many times the letter `o` appears in the string.  
- **replace("PYTHON", "Java")** → Replace `PYTHON` with `Java`.  
- **split()** → Split the text into a list of words.  
- **join()** → Join the list back into a string, separated by `|`.  

3. Test the string with Boolean methods:  
- **startswith("welcome")**  
- **endswith("101!")**  
- **isalnum()**  
- **isalpha()**  
- **islower()**  
- **isupper()**  
- **isspace()**  

---

## String Comparisons, Sorting, and Conversions

### 🔍 Comparing Strings
- Compare `"cat" == "cat"` → are they equal?  
- Compare `"cat" != "Cat"` → are they different?  
- Compare `"cat" < "caterpillar"` → which one is smaller?  
- Compare `"dog" > "Dog"` → what happens with uppercase vs lowercase?  
- Compare `"10" == 10`, `"10" != 10`, and `"10" > 10` → what happens when you compare a string with a number?  

---

### 📑 Sorting Strings
- Make a list of words (like `"dog"`, `"cat"`, `"zebra"`, `"ant"`).  
- Use `sorted(list)` → does it make a new sorted list?  
- Use `list.sort()` → what happens to the original list?  
- Which one keeps the original list unchanged?  

---

### 🔄 Converting Between Strings and Numbers
- Change a number into a string using `str()`.  
- Change a string with digits into a number using `int()`.  
- Change a string with a decimal into a float using `float()`.  
- Try `int("hello")` → what happens?  

---
