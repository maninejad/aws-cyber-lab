# AWS Cyber Lab - Server Setup

## Overview

This project is a personal cybersecurity laboratory hosted on AWS.

The goal is to build practical skills in:

- Linux administration
- Web server security
- Network security
- Vulnerability testing
- Security monitoring
- Cloud infrastructure

## Infrastructure

### Server

- Platform: AWS EC2
- Operating System: Ubuntu Linux
- Web Server: Nginx
- Domain: lab.maninejad.com
- HTTPS: Let's Encrypt SSL

## Current Services

### Nginx

Used as the public web server and reverse proxy.

### FastAPI

Python backend used for AI experiments and API development.

## Security Configuration

Current AWS Security Group:

- SSH (22): Restricted to personal IP
- HTTP (80): Public
- HTTPS (443): Public

## Next Steps

- Configure firewall rules
- Install Fail2ban
- Perform security auditing
- Build security testing environments
