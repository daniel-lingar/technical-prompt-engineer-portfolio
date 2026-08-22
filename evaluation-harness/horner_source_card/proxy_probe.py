#!/usr/bin/env python3
"""Probe the configured OpenAI-compatible proxy using the supported SDK."""

import json

from openai import OpenAI


client = OpenAI()

basic = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[{"role": "user", "content": "Reply with the word ready."}],
    max_completion_tokens=64,
)
print(json.dumps({"basic": basic.choices[0].message.content}, ensure_ascii=False))

structured = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[{"role": "user", "content": "Return {\"ok\": true}."}],
    max_completion_tokens=64,
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "probe",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {"ok": {"type": "boolean"}},
                "required": ["ok"],
                "additionalProperties": False,
            },
        },
    },
)
print(json.dumps({"structured": structured.choices[0].message.content}, ensure_ascii=False))
