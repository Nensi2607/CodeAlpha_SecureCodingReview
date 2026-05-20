# 🔐 Secure Coding Review Report

## 📌 Project Reviewed
Vulnerable Python Login System

---

# 🚨 Vulnerability 1: Hardcoded Credentials

## Description
The application stores username and password directly inside the source code.

```python
stored_username = "admin"
stored_password = "admin123"
```

## Risk
If attackers gain access to the source code, they can easily obtain credentials and compromise the system.

## Recommendation
- Store credentials securely
- Use databases or environment variables
- Avoid hardcoding sensitive information

---

# 🚨 Vulnerability 2: Plaintext Password Storage

## Description
Passwords are stored in readable plaintext format.

## Risk
Anyone accessing the code can directly view passwords.

## Recommendation
- Use password hashing
- Use secure hashing algorithms like bcrypt or SHA-256

---

# 🚨 Vulnerability 3: Weak Authentication Design

## Description
The login system uses simple direct string comparison without additional security checks.

## Risk
The application lacks:
- Account lockout
- Rate limiting
- Multi-factor authentication

This increases the risk of brute-force attacks.

## Recommendation
- Add login attempt limits
- Use MFA
- Implement secure authentication mechanisms

---

# ✅ Overall Security Assessment

The application contains multiple critical security weaknesses and should not be used in production environments without remediation.

---

# 🎯 Key Learning

Small insecure coding practices can lead to major cybersecurity risks.


# 🔒 Secure Remediation Implemented

## Improvements Added
- Password hashing using SHA-256
- Improved password verification
- Better authentication handling

## Security Benefits
- Passwords are no longer stored directly in plaintext
- Reduced risk of credential exposure
- Improved secure coding practices

## Secure Coding Practices Used
- Hashing sensitive data
- Avoiding plaintext password comparison
- Safer authentication workflow