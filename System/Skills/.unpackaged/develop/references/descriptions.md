# Descriptions - writing the line that decides whether a skill fires

The `description` is a skill's single most important deliverable. A strong body behind a passive description never triggers. Same for an agent's `description`, which is its routing key.

## The rules (skill descriptions)

1. **Third person, written as when-to-use.** "Use this skill whenever the user ..." not "I build skills."
2. **Concrete quoted trigger phrases**, 4 to 6, drawn from how a user actually asks: "build a skill", "create an agent", "make a team", "turn this workflow into a skill".
3. **A pushy anti-undertrigger clause**: "even when they never say the word skill." Under-triggering is the common failure; lean against it.
4. **Front-load keywords.** The first words carry the most routing weight.
5. **Keep all when-to-use in the description.** Do not split it between the description and the body; the router sees only the description.
6. **Stay short.** One to three sentences of trigger surface. The often-cited "~100" figure is the always-loaded name-plus-description metadata block in tokens, not a word cap; still, brevity sharpens routing.
7. **No "do not use for" list.** Negative examples contaminate the keyword field and cause the misses they mean to prevent.
8. **No "claude" or "anthropic" in the name.**

## Agent descriptions

Same spirit, routing-first: "Dispatch this agent when ...", naming the capability and the situation. The orchestrator routes from this line alone, so make the trigger condition unmistakable.

## How it is tested

- **Light trigger check** (every build): read the description cold and confirm the obvious phrasings would route to it.
- **Full smoke test** (Publish or complex tier): about 20 queries, half should-trigger and half near-miss negatives, scored by model judges against realistic distractor descriptions; the true-negative rate is load-bearing. Caveat: a headless harness can fail to trigger skills at all, so verify the harness before blaming the description.
