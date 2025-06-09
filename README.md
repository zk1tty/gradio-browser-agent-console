---
tags: [gradio-custom-component, SimpleTextbox, browser, Chrome, extension, polling, queuing, daemon, logging]
title: gradio_gradio_browser_agent_console
short_description: the starter package for 99% browser-agent demos
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# gradio_gradio_browser_agent_console

## Why package a Browser Agent Console component?

99 % of browser-agent demos need the same trio:

1. Controls – Start / Stop / Replay

2. Live log viewer – scroll-locked, ∞-length

3. Event feed – emit {status, progress, error} to Python

Instead of copy-pasting that block every time, ship a reusable
gradio-browser-agent-console component that:

- plugs into any backend queue (asyncio.Queue, socket, MCP stream…)

- gives you the polling / diffing logic you already wrote in webui.py
