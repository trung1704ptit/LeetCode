# Security questions

## 1. How to store password in Database securely?
To store password securely, we avoid store password in plain text.
### Using Hash function:
Using Hash function to has password before storing.
- With hash function is irreverable.
- We can choose secure hash function: SHA256, SHA512, avoid MD5, SHA1.
- However, with this way still have save risks: Hacker can calculate the hash, predict password that victim choosen or using strong machine to brute force.

### Hash + salt:
- A salt is unique, randomly generated string that is added to each password as part of the hashing process.
Salt is stored in database.
- Hacker has to crack hashes one at time => slow hacking process
- hashed_password = hash(unique_salt + password)

### Hash + salt + pepper:
- Pepper is randomly generated string that is added to password as part of th hashing process.
- Similar to salt, but pepper is not stored in database, it just store in env,...
- hashed_password = hash(common_pepper + unique_salt + password)


## 2. Symmetric vs Asymmetric encryption?
- Symmetric both side (sender and receiver) share the same key to encrypt and decrypt => the Speed is fast.
- Asymmetric: Using Public key and private key to encrypt/decrypt. The plain text is encrypted using a public key, it is only decrypted using a private key. The speed slow. example: RSA

## 3. How RSA work?

## 4. How HTTPS work?
## 5. What happen during TLS Handshake?
## 6. Why use symmetric encryption for exchanging data instead of asymmetric encryption?
## 7. What is the use of client random and server random in TLS handshake?
What is CORS?
How to prevent SQL injection?
How do you implement authentication?
How JWT work? Pros & Cons? How to revoke JWT from server?
2 users in diff location login with same JWT, how to warn user?
Access token vs Refresh token
https://github.com/alex/what-happens-when
Hashing vs Encoding vs Encryption? When to use each of them?