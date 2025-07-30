# 🔍 Romanian CNP Hash Table – Generator & Search Performance

This Python project simulates the generation and storage of 1 million Romanian CNPs (Personal Numeric Codes), and evaluates the performance of a custom-built hash table implementation.

---

## 📌 Description

The program:
- Randomly generates **valid-looking CNPs** along with first and last names
- Saves them to a CSV file (`cnp_data.csv`)
- Stores them in a **custom hash table** using a simple hash function
- Selects 1,000 random CNPs and searches them in the table
- Reports the **average number of iterations** per search (as a collision indicator)

---

## 🧠 Algorithm Overview

- **Hash function**: based on the sum of digits of the CNP, modulo a large prime (`TABLE_SIZE = 1000003`)
- **Collision handling**: chaining (linked list per index)
- **Search analysis**: calculates how many elements must be traversed on average

---

## 🧬 CNP Structure (simplified)

Each generated CNP follows this format:

```text
S A A L L Z Z J J N N N C

Where:

S: sex (1 = male, 2 = female)

AA: year of birth (last 2 digits)

LL: month

ZZ: day

JJ: county code (01–52)

NNN: unique serial number

C: control digit (random)


