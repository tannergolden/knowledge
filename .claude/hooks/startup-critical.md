# BRAIN critical rules: survive session-start truncation

(The full text lives in Instructions.md and Constitution.md. This digest is cat'd separately because the auto-injected startup bundle is truncated to a preview, so these must-not-miss rules are guaranteed to reach context.)

1. GROUND BEFORE MODEL MEMORY. For any factual question, follow the retrieval order (Instructions Section 4.5): vault (`search` / `load`) first, then the offline knowledge bases (`kb search`, the offline Wikipedia), then the live web. A who, what, define, or explain question goes to `kb search` first. Reserve the live-web `research` skill for current or contested facts. Never leave the vault for questions about the user.

2. ORIENT FIRST. Read every file the session-start manifest lists (the Section 9 startup set) before substantive work, then check the Inbox and the recent Memory/Context summaries. In a plain terminal, `python3 System/brain.command startup` inlines the full bundle instead.

3. THE CONSTITUTION GOVERNS. Constitution.md wins every conflict. Back up before editing any file; never delete or restructure Layer 0 or Layer 1 without explicit user confirmation; log core-file changes to the changelog.

4. FIRE MATCHING SKILLS without asking, and prefer the BRAIN's own (board, discover, editorial, identify, research, visualize) and the universal `develop` over any generic equivalent.

5. OUTPUT. No em dashes. 12-hour clock times. Answer directly, with no preamble or filler.
