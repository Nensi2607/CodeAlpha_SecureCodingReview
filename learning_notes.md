# Day 1 - Secure Coding Basics

## What is Secure Coding
Secure coding means writing software in a way that protects against security vulnerabilities and cyber attacks.

## Common Security Vulnerabilities
- Hardcoded credentials
- SQL Injection
- Weak input validation
- Plaintext password storage
- Information disclosure

## SQL Injection
SQL Injection happens when attackers manipulate database queries through user input.

## Secure Coding Importance
Secure coding helps protect:
- User data
- Authentication systems
- Databases
- Applications

## Key Learning
Even small coding mistakes can create major security risks.

# Day 2 - Vulnerable Login System

## Project Created
Created a basic Python login system intentionally containing security vulnerabilities for security review purposes.

## Vulnerabilities Identified
- Hardcoded username and password
- Plaintext password storage
- Weak authentication logic

## Security Risks
If attackers access source code, they can easily see credentials and compromise the system.

## Key Learning
Authentication systems should never store sensitive information directly in source code.


# Day 3 - Security Review and Vulnerability Analysis

## Work Completed
Performed a security review of the vulnerable login system.

## Vulnerabilities Identified
- Hardcoded credentials
- Plaintext password storage
- Weak authentication design

## Concepts Learned
- Security auditing
- Risk assessment
- Vulnerability documentation
- Remediation recommendations

## Key Learning
Proper documentation and remediation suggestions are important parts of secure coding reviews.


# Day 4 - Secure Version Development

## Work Completed
Created a more secure version of the vulnerable login system.

## Security Improvements
- Password hashing using SHA-256
- Better password verification
- Improved authentication process

## Concepts Learned
- Cryptographic hashing
- Secure password storage
- Authentication security

## Key Learning
Hashing helps protect passwords from direct exposure even if attackers access stored data.