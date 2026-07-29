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
