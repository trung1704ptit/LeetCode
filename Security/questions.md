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
- Receiver generates 2 pairs key: public key (PK) and secret key (SK)
- Sender using public key to encrypt message m and send it to the receiver via a public channel.
- c = encrypt(message, PK)
- Now everyone in internet can see the encrypted message c, but cannot decrypt it.
- Receiver using Secret key to decrypt message c. m = decrypt(c, SK)

RSA for authentication: to confirm that a message has been sent by the right entity:
- Signer producers a digital signature by appling a hash function on a message m and sign it with SK. <br>
 signature = encrypt(hash(m), SK)
- Signer sends (m, signature, hash function) to verifier
- Verifier verifies by reproduce message hash using Public key and compare with actual hash value: <br>
check <b>decrypt(encrypt(hash(m), SK), PK) == hash(m)</b>

## 4. How HTTPS work?
- HTTPS uses an encryption protocol to encrypt communications. The protocol is called Transport layer security. This protocol secures communication by using what's known as an asymmetric public key infrastructure. This type of system using public key and private key: <br>
- private key: this key is controlled by owner of website and it's kept <br>
- public key: this key is available to everyone who wants to interact with the server in a way that's secure. The information encryptd by public key only be decrypted by private key.

Before the client and server can send and receive data securely using HTTPS, they need to do TLS handeshake to verify.


## 5. What happen during TLS Handshake?
1. Client sends Client Hello message to Server which include:
TLS version client supports (1.0 2.0 ..)
cipher suites client supports (algorithm)
a random bytes: client random


2. Server sends Server Hello message to Client which include:
Server's SSL certificate
server's chosen cipher suites
a random bytes: server random

3. Client confirms Server's identity (authentication) by checking the server's SSL certificate using RSA encryption:
SSL certificate contains:
domain name
person/ organization owns the certificate
which Certificate authority (CA) issued it
CA's digital signature
issue date
expiration date
server's PK (used later in key exchanges) …

The whole identity authentication is based on the idea "You trust the CA, and they trust me, therefore you can trust me.":
the browser has a build-in list of all CA's public key
it uses CA's PK to decrypt the CA's digital signature
it confirms that the decrypted data is matched.

4. Key Exchange, use RSA

Client generates a random pre-master secret, encrypts it with the Server's public key (found in Server SSL's certificate), sends the result to Server
Server decrypts the pre-master secret using its secret key.
At this point, both Client and Server share the same pre-master secret. 

5. Both Client and Server generate session key from pre-master secret, client random, and server random


session_key = hash(pre-master secret, ClientHello.random, ServerHello.random)

6. Client is ready: The client sends a "finished" message that is encrypted with a session key.

7. Server is ready: The server sends a "finished" message encrypted with a session key.

8. The handshake is completed, and communication continues using the symmetric encryption with key == session key.


## 6. Why use symmetric encryption for exchanging data instead of asymmetric encryption?
Bacause the symmetric is faster than asymmetric encryption.

## 7. What is the use of client random and server random in TLS handshake?
Avoid replay attack: if there is no client random and server random, hacker capture the package and resend.

## 8. What is CORS?
To understand about CORS we need to understand about Same origin policy (SOP) of browser. <br>
SOP that mean: A web application using APIs can only request HTTP resources from the same origin the application was loaded from.
- This policy is for security resone, not apply for debug tool (Postman,...), not apply for some HTMl tag: img, link, frame,...

### So what is CORS?
- CORS: cross-origin resource sharing.
- CORS is merchanism to bypass SOP
- Using CORS we can define which origin can request to the server's origin.


## 9. How to prevent SQL injection?
Use Prepared Statement: database to distinguish between code and data, regardless of what user input is supplied.

## 10. How do you implement authentication?
- Client login to system
- Server validate username/password. If success, server wil generate JWT using secret key and return it to client.
- Client using JWT attach in header, send request to server
- Server validates JWT using secret key. if Success, response to client.

### JWT = header + payload + signature
signature = hash(encode(header) + encode(payload), secret_key)
validate: signature == hash(encode(header) + encode(payload), public_key)

## 11. How JWT work? Pros & Cons? How to revoke JWT from server?
- Json web token is an open standard that defines a way for securely transmitting data between client-server.
- This information can be verified and trusted because it is digitally signed. JWTs can be signed using a secret or a public/private key pair using RSA.
- Client login to system
- Server validate username/password. If success, server wil generate JWT using secret key and return it to client.
- Client using JWT attach in header, send request to server
- Server validates JWT using secret key. if Success, response to client.

### So what are advantage of JWT:
- stateless: server does not need to maintain  a session storage because all authentication information is store in JWT, which is stored in client side.
- JWT is sent along with header, avoid Cross-site request Forgery attach.
### So what are disavantage of JWT?:
- JWT only become invalid when it expires. The user has no built-in feature to explicitly revoke the validity of token.
- The solution would be creating a database to maintain a revocation list. This would add complexity to the system and elimate the statless property of JWT authentication.
### Sturcture of JWT?
[Base64(HEADER)] . [Base64(PAYLOAD)] . [Base64(SIGNATURE)]
- Header: contains metadata. The hashing algorithm being used.
- Payload: contains veriable security statements, such as user info, permission, ...
- signature: used to validate that the token is truthworthy and has not been tampered with.


## 12. Two users in diff location login with same JWT, how to warn user?
When generate JWT we can store the IP address of client into the JWT.

## 13. Access token vs Refresh token
- Access token are credentials used to access protected resources. Access token are used as bearer tokens. A bearer token means that the bearer can access authorized resources without futher indentication.
- Refresh token: this is a long-lived token compared to the access  token and it used to request a new access token in cases where it is expired.

### So why we nee refresh token?
- As access token defined lifetimes, and there could be a possibility that current token becomes invalid or expires. This refresh token can be used to request new access token without user interaction.

## 14. What happen when enter Google.com
https://github.com/alex/what-happens-when


## 15. Hashing vs Encoding vs Encryption? When to use each of them?
- Encoding: Reversible transformation of data format, used to preserve usability of data.
- Hashing: Is a one-way summary of data, cannot be reversed, used to validate the integrity of data.
- Encryption: Secure encoding of data used to protect confidentiality of data.