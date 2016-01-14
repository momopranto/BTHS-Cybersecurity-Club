# Cryptography

This weeks presenation can be found [here](https://goo.gl/6ZY3v4)

This weeks brain blast is: [The Fuck](https://github.com/nvbn/thefuck)


## What is Cryptography?

Greek word for secret or hidden. 

The art of writing in secret code.

Cryptography is a method of storing and transmitting data in a particular form so that only those for whom it is intended can read and process it.

Encryption: converting a message into a form that cannot be interpreted and/or understood.

Decryption: converting an encrypted message into a form that can be easily interpreted and/or understood.

## Why and where do we use crypto?

Sensitive information such as personal info and bank information should always be encrypted. In general, anything you don’t want strangers to be able to see if intercepted over the internet.

* Passwords
* Financial transfers
* Online messages
* Files
* Web traffic
* Secret messages

## Cesar Cipher

The Caesar cipher is one of the earliest known and simplest ciphers. It is a substitution cipher where each letter in the plaintext is "shifted" a certain number of places down the alphabet. With a shift of 1, A would be replaced by B, B would become C, and so on. The method is named after Julius Caesar, who apparently used it to communicate with his generals.

**Example 1:**

Plaintext: A B C D

Ciphertext (shifted 1): B C D E

**Example 2:**

Plaintext: john cena

Ciphertext (shifted 4): nslr gire

Try this challenge: https://picoctf.com/crypto_mats/#classicalintro

## Substitution Cipher

Solve using frequency analysis (most frequently used letters are a,e,h,i,n,o,r,s,t,u)
Look for patterns and repeating words. The longer the sample the better.

Try this challenge: http://practicalcryptography.com/ciphers/simple-substitution-cipher

## Morse Code

## One Time Pad

One time pads are not meant to be decrypted.

The data is input to an algorithm that spits out the same output every time it gets that same input.

Try this challenge: https://picoctf.com/crypto_mats/#otp

**MD5:** Hashing algorithm

**Plaintext:** cybersecurity

**Hash Generated:** b03a894e101746d09277f1f255cc8a40

## Single Byte XOR

A ⊕ A = 0

A ⊕ ? = B

B ⊕ ? = A

Try this challenge: https://picoctf.com/crypto_mats/#modern_versions

**Plaintext:** hello 

**Hex:** 68 65 6c 6c 6f

**Key:** 1
  0x68⊕1    0x65⊕1     0x6c⊕1      0x6c⊕1       0x6f⊕1
  
  0x69      0x64       0x6d        0x6d         0x6e
  
  i         d          m           m            n

## Other Types of Crypto

* Base64 encoding
* Vigenere cipher
* RSA
* AES
* RC4
* Enigma

### Other Challenges to Try

http://practicalcryptography.com/ciphers

http://cryptopals.com





