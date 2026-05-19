# Substitution & Vigenère Cipher

A pair of classical encryption tools built in both Python and HTML/JavaScript — featuring interactive apps, character-by-character step traces, and full encrypt/decrypt support.

---

## How it works

### Vigenère Cipher
A repeating keyword is used — each letter of the key applies a different shift, making it far harder to crack than a simple Caesar cipher.

```
Encrypt: cipher_index = (plain_index + key_index) % 26
Decrypt: plain_index  = (cipher_index - key_index + 26) % 26
```

Example with key = SECRET:
```
Plaintext:  H  e  l  l  o
Key letter: S  E  C  R  E
Shift:      18 4  2  17 4
Ciphertext: Z  i  n  c  s
```

Non-alphabetic characters (spaces, punctuation, numbers) are passed through unchanged in both ciphers.

## Features

- Encrypt and decrypt with a keyword (Vigenère)
- Preserves case — lowercase stays lowercase, uppercase stays uppercase
- Non-alpha characters pass through unchanged
- Interactive HTML apps with live character trace and highlighted tableau

---

## Limitations

These are classical ciphers intended for learning purposes. They are **not secure** for real-world use:

- The Caesar cipher has only 25 possible keys and can be cracked instantly by brute force
- The Vigenère cipher can be broken with frequency analysis if the key is short or the message is long
- For real encryption, use modern standards like AES

---

## Requirements

- **HTML files** — any modern browser (Chrome, Edge, Firefox, Safari). No internet needed.
- **Python files** — Python 3.6 or higher. No third-party libraries needed.
