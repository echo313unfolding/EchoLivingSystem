#!/usr/bin/env python3
import pexpect
import sys
import os

def run_gemini_reflex(prompt):
    try:
        gem = pexpect.spawn("bash", encoding='utf-8', timeout=20)
        gem.expect_exact("$")
        gem.sendline("gemini")
        gem.expect("╭────────────────────────╮")

        gem.sendline(prompt)
        gem.expect("╭─────────────────────────────────────────────────────╮", timeout=15)

        output = gem.before.strip()
        print(output)

        # Optional: log to Echo trace
        with open(os.path.expanduser("~/EchoLivingSystem/echo_reflect_trace.sym"), "a") as log:
            log.write(f"\n\n# GEMINI REFLEX\nPrompt: {prompt}\n\n{output}\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:]) or "Hello Gemini"
    run_gemini_reflex(prompt)
