# Essay-Grader-Project
Reads and Writes Files to Grade a piece of Writing

**Written in Python**

Origonal Features
- Vocabulary Search
- Spell Check
- Grammar Checker

---

# Original Developer Notes

Grade My Essay includes a Python3 program that uses NLTK, a natural-language processing library, to extract statistics from the provided essay with the help of a dictionary and a vocabulary file.

### Dependencies
Grade My Essay uses the NLTK library with punkt and averaged perceptron tagger. This library can be installed from the following link: https://www.nltk.org/install.html

### Utility:
1. Clone this repository.
2. Modify run.sh to set the dictionary file, vocabulary file, remarks file and the essay file by the using the command:
	python3 grade.py -in=essay.txt -out=remarks.txt -dict=dictionary.txt [-voc=vocabs.txt]
3. Finally, execute run.sh.

### Issues
* Implement context-free grammars to determine various English sentences.
* Generate statistics to the remarks output file.

Note: Assumes the grammar rule that periods are never placed before ".

---

# To Include

Port to Pure Java or Processing-Java

Write the Teacher files for this Project

---
