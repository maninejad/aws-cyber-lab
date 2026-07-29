# AI Assistant — FastAPI + Gemini Integration

## Objective
Build a minimal AI-powered chat backend, deployed on the existing AWS lab
infrastructure, as the foundation for later LLM security testing
(prompt injection playground, guardrails, OWASP LLM Top 10 mitigations).

## Architecture

Browser -> Nginx (HTTPS reverse proxy) -> FastAPI (127.0.0.1:8000) -> Gemini API

- Nginx: terminates TLS (Let's Encrypt), routes /api/chat to the local
  FastAPI process via proxy_pass.
- FastAPI: single /chat POST endpoint, wraps the LLM call behind a
  call_llm() function so the provider can be swapped later.
- Gemini API (gemini-3.5-flash-lite): free-tier model, chosen to keep
  this project cost-free while testing/breaking things repeatedly.

## Why Gemini over Claude/OpenAI

- Free tier is ongoing (rate-limited, not a time-limited trial), which
  matters since this app will be repeatedly tested and intentionally
  attacked as part of later prompt-injection work.
- Already paying for AWS compute, so avoided adding a second recurring
  paid API on top of that while still learning.
- Provider is abstracted behind call_llm(), so switching to
  Claude/OpenAI/local Llama later is a small, contained change.

## Setup steps

1. Created a free API key via Google AI Studio (aistudio.google.com)
2. Stored it as an environment variable (GEMINI_API_KEY) in ~/.bashrc,
   never hardcoded in source
3. Created an isolated Python environment with venv
4. Built main.py, a FastAPI app with a single /chat endpoint
5. Ran locally with uvicorn and tested via curl from the server itself
6. Confirmed Nginx's /api/chat proxy block routes correctly
7. Tested externally from a separate machine to confirm HTTPS works end-to-end

## Issues encountered

- Deprecated model ID: initial code used gemini-2.5-flash-lite, which
  returned a 404. Google retired it in favor of the gemini-3.x model
  family. Fixed by updating to gemini-3.5-flash-lite.
- PowerShell quoting: testing from a Windows client using curl
  (aliased to Invoke-WebRequest) mangled the JSON body due to
  PowerShell's quote-escaping rules. Resolved by using
  Invoke-RestMethod with single-quoted JSON instead.

## Persistent deployment (systemd)

Running uvicorn directly in a foreground PuTTY session meant the AI
Assistant went offline every time the SSH connection closed. Fixed by
converting it into a managed systemd service (ai-lab.service) so it
starts on boot, restarts automatically on crash, and runs independent
of any SSH session. Verified working via systemctl status and
journalctl logs showing live external requests being handled.

## Frontend redesign

Replaced the original plain chat page with a custom-styled interface
at /var/www/html/chat/index.html. Dark theme built around a "packet
log" concept, each message renders like a logged entry with a
timestamp and status tag (USER / MODEL), reinforcing the security-lab
framing rather than a generic chatbot look. JetBrains Mono for system
chrome, Inter for message content. Includes a typing indicator and
visible error states instead of failing silently.

Bug encountered: an earlier version of the frontend read
data.response, but the backend returns {"reply": "..."}. Field name
mismatch caused the UI to display "undefined" for every response.
Fixed by aligning the frontend JS to read data.reply.

Deployment note: large file pastes into nano/heredoc over PuTTY proved
unreliable for big blocks, silently truncating content. Worked around
by breaking deployments into smaller chunks and verifying line counts
after each write.

## Current status

Fully working end-to-end: persistent backend (systemd) + custom
frontend, both confirmed live and tested externally.

## Next steps

- [ ] Add a system prompt with a canary secret (for the injection playground)
- [ ] Add input length limits and basic rate limiting
- [ ] Add output filtering
- [ ] Build the prompt-injection playground UI + attempt logging
- [ ] Write OWASP LLM Top 10 mitigation mapping doc
