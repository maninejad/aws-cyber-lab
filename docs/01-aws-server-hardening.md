# Project 01: AWS Ubuntu Server Hardening

## Overview

This project documents the setup and security hardening of a public-facing Ubuntu server hosted on AWS EC2.

The objective was to build a secure cloud environment while learning practical defensive security techniques.

---

## Environment

### Infrastructure

- Cloud Provider: AWS EC2
- Operating System: Ubuntu Linux
- Web Server: Nginx
- Domain: lab.maninejad.com
- SSL Certificate: Let's Encrypt

---

## Initial Configuration

The server was configured with:

- Public HTTPS website
- Nginx web server
- Restricted SSH access
- Python FastAPI application environment

---

# Security Controls Implemented

## UFW Firewall Configuration

The Ubuntu firewall was enabled using UFW (Uncomplicated Firewall).

Allowed services:

| Service | Port | Purpose |
|---|---|---|
| SSH | 22 | Remote administration |
| HTTP | 80 | Web traffic |
| HTTPS | 443 | Secure web traffic |

The firewall provides an additional security layer alongside AWS Security Groups.

## 1. AWS Security Group Configuration

Inbound traffic was restricted:

| Service | Port | Access |
|---|---|---|
| SSH | 22 | Restricted to personal IP |
| HTTP | 80 | Public |
| HTTPS | 443 | Public |

Restricting SSH access reduces exposure to automated internet scanning and brute-force attempts.

---

## 2. HTTPS Configuration

Let's Encrypt SSL was configured to provide encrypted communication.

Benefits:

- Protects user traffic
- Prevents interception
- Provides trusted HTTPS connection

---

## 3. Nginx Reverse Proxy

Nginx was configured as the public-facing web server.

Responsibilities:

- Serve website content
- Handle HTTPS requests
- Route application traffic

---

## 4. System Resources

The server was configured with:

- Ubuntu Linux
- Limited cloud resources
- Swap memory enabled for stability

---

# Future Security Improvements

Planned improvements:

- Configure UFW firewall
- Install Fail2ban
- Enable automatic security updates
- Perform vulnerability scanning
- Add monitoring
- Document security testing

---

# Skills Practised

- AWS cloud administration
- Linux server management
- Web server configuration
- HTTPS deployment
- Network security fundamentals
- Security hardening principles
---

# Security Controls Implemented

## UFW Firewall

Ubuntu UFW firewall was enabled to provide host-level traffic filtering.

Allowed services:

| Service | Port | Purpose |
|---|---|---|
| SSH | 22 | Remote administration |
| HTTP | 80 | Web traffic |
| HTTPS | 443 | Secure web traffic |

The UFW configuration works together with AWS Security Groups to provide layered network protection.

---

## Fail2ban Intrusion Prevention

Fail2ban was installed and configured to monitor SSH authentication attempts.

Configuration:

- Jail: sshd
- Maximum failed attempts: 5
- Detection window: 10 minutes
- Ban duration: 1 hour

Fail2ban helps protect the server against automated brute-force login attempts by temporarily blocking suspicious IP addresses.

---

## SSH Hardening

SSH configuration was reviewed and hardened.

Implemented controls:

- Disabled root login
- Disabled empty password authentication
- Created SSH configuration backup before changes
- Validated SSH configuration before restarting service

These changes reduce the risk of unauthorized administrative access.

---

# Security Testing

Completed checks:

- Verified UFW firewall rules
- Confirmed Fail2ban SSH monitoring
- Tested SSH service configuration
- Confirmed HTTPS availability
