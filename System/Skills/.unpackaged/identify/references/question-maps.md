# Question maps - the per-facet item banks

The instrument library, one entry per Profile facet. Read this after `interviewing.md` and before filling `templates/interview-plan.md`: `interviewing.md` sets the rules every item obeys; this file supplies the items, the framework each rests on, and the order in which a facet's sections earn a question. The plan draws from here; it never invents an item off-book.

## How to read an entry

Each facet gives four things:

- **Sensitivity.** Non-sensitive, or **sensitive** (Health, Finances, Values, Relationships). Sensitive facets open only through the consent gate (`interviewing.md`), run 6 to 8 questions, and carry the explicit "Prefer not to say" option on every item. A section marked *sensitive-adjacent* inside a non-sensitive facet (Substance Use in Lifestyle, Weaknesses in Personality) carries the explicit skip even though its facet does not gate.
- **Frameworks.** The validated basis the items are drawn from. The framework name lives here and in the ledger, never in the question the user hears (`interviewing.md`, plain language).
- **Highest-signal sections, in fill order.** The sections that most change how the BRAIN helps come first; completionism comes last. Snapshot is never asked: Calvin composes it last from the run's material and proposes it like any other diff.
- **Item bank.** Representative items, one construct each, tagged by delivery: **(tool)** scaled or pick via the question tool, 3-point self-anchored scale plus a skip option, max 4 options, batched up to 4 within one framework block; **(prose)** one narrative prompt at a time in chat; **(cluster)** one compact chat question covering a set of simple registry facts. The bank is a source, not a script: the plan pulls the highest-signal items for the gaps found, about 10 per run.

Scale convention: options read as the user describing themselves to themselves ("Usually true of me"), not ranked against other people. A genuine scale is 3 points plus a skip; a categorical pick may carry up to 4 substantive options, skip added wherever the ground is sensitive or sensitive-adjacent.

---

## Working Style (non-sensitive)

**Frameworks:** the mainstream assistant custom-instruction schema ("what to know about me / how to respond to me") and the personal user-manual genre.
**Highest-signal sections, in fill order:** How to Respond to Me (the directly-executable rules), How I Like to Be Addressed, then Feedback, Decision-Making Style, Pet Peeves, How I Communicate, Terminology. This is the facet the AI acts on most directly, so it usually leads coverage; give it depth first.

- **Default length** (tool): "When I ask you something, the answer I want by default is..." Just the answer, terse / The answer plus brief reasoning / A thorough deep dive / Skip.
- **Format default** (tool): "For most answers I would rather read..." Tight bullets / Flowing prose / Depends on the topic / Skip.
- **Push-back** (tool): "When you think I am wrong, I want you to..." Challenge me directly / Raise it gently / Defer unless it matters / Skip.
- **Uncertainty handling** (tool): "When you are not sure of an answer, I would rather you..." Say so plainly / Give your best guess, flagged / Hold it until sure / Skip.
- **Do's and don'ts** (prose): "Name one thing an assistant does that reliably earns your trust, and one that reliably annoys you." (feeds Do's, Don'ts, Pet Peeves at once.)
- **Address** (cluster): "What should I call you, how formal do you want me, and are nicknames welcome?"

## Biography (non-sensitive)

**Frameworks:** McAdams' narrative identity (agency, communion, redemption, contamination, coherence) for the life story; Erikson life stage for the era anchor; standard biographical registry for facts.
**Highest-signal sections, in fill order:** Life Story (Narrative Themes) and Life Stage carry information traits and facts do not, so they lead once the registry basics exist; then Personal, Occupation, Career, Formative Environment, Key Life Events. Open with a warm-up scaled block before the first narrative prompt.

- **Life stage** (tool, warm-up): "The era you are in right now feels most like..." Building and establishing / Steady and sustaining / Transition or reinvention / Skip.
- **Agency** (prose): "Tell me about a time you feel you authored your own path, a decision or turn that was clearly yours." (McAdams agency.)
- **Communion** (prose): "Who or what has most defined your sense of belonging over the years?" (McAdams communion.)
- **Redemption or contamination** (prose): "Is there a hard chapter that turned into something good, or a good one that turned painful? Tell me whichever comes to mind." (one prompt, either sequence.)
- **Coherence** (prose): "If you drew a single thread from your past to where you are today, what would it be?"
- **Registry** (cluster): "The basics when you feel like it: where you are based, what you do, and where you grew up."

## Personality (non-sensitive; Weaknesses is sensitive-adjacent)

**Frameworks:** Big Five with the 15 BFI-2 facets (Soto & John, 2017), three per domain; HEXACO Honesty-Humility as the sixth factor; Regulatory Focus for self-regulation; VIA for character strengths. Items are behavior-anchored, not self-theory.
**Highest-signal sections, in fill order:** Under Pressure (the most operationally important), then the Big Five domains that are thin, Temperament & Energy, Regulatory Focus, Thinking Style, Character Strengths, and Weaknesses & Blind Spots last and gently. Batch BFI-2 items with BFI-2 items only, never with a Schwartz ordering.

- **Organization / Conscientiousness** (tool): "My space and my systems tend to be..." Kept in order / A mix / Left to pile up / Skip.
- **Sociability / Extraversion** (tool): "A day around a lot of people usually leaves me..." Energized / Neutral / Drained / Skip.
- **Intellectual curiosity / Openness** (tool): "Abstract ideas and theories tend to..." Pull me in / Depend on the topic / Leave me cold / Skip.
- **Anxiety / Negative emotionality** (tool): "Once a worry starts, it usually..." Sticks with me / Comes and goes / Rarely takes hold / Skip.
- **Honesty-Humility** (tool): "Getting ahead by bending the rules is..." Something I will not do / Situational / Sometimes worth it / Skip.
- **Regulatory Focus** (tool): "When I take on something, I am mostly moved by..." Chasing the gain / Depends / Avoiding the loss / Skip.
- **Under Pressure** (prose): "Think of the last time you were genuinely under pressure. What changed in how you worked, and what was the first thing to drop?"
- **Blind spots** (prose, sensitive-adjacent, explicit skip): "Is there a weakness you would actually want me to help you notice? Say skip and we move on."

## Values (sensitive - consent gate)

**Frameworks:** Schwartz's theory of basic human values (ten values in four higher-order families); Moral Foundations (care, fairness, loyalty, authority, sanctity, liberty); Self-Determination Theory (autonomy, competence, relatedness) for motivation.
**Highest-signal sections, in fill order:** Core Values (the ranking is the point), Orientations, Ethical Orientation, Motivation, then Purpose & Meaning and Definition of Success. Held beliefs are their own sensitive entries and are only ever offered, never pressed. Gentlest register; every item carries the explicit skip.

- **Value family ranking** (prose, or tool as an ordering): "Of these four pulls, which comes first for you and which comes last: freedom to chart your own course, achievement and getting ahead, security and stability, or caring for others and the wider world? Prefer not to say is always fine."
- **Money orientation** (tool): "Money is mostly, for me..." A tool for other things / A goal in itself / A source of stress / Prefer not to say.
- **Self vs. others** (tool): "When they pull apart, I lean toward..." Individual achievement / It depends / The collective good / Prefer not to say.
- **Ethical frame** (tool): "When I judge right from wrong, I weigh most..." The rule or duty / The outcome / The kind of person it makes me / Prefer not to say.
- **Motivation** (prose): "What kind of work makes you lose track of time, and what drains you fastest? Skip if you would rather not."
- **Purpose** (prose): "What, if anything, do you feel called to do or leave behind? Say skip and we move on."

## Goals (non-sensitive)

**Frameworks:** possible-selves theory (hoped-for, feared, ought self), which drives motivated behavior more than stated goals; goal-direction framing.
**Highest-signal sections, in fill order:** Direction (the arc the individual goals serve), Possible Selves, then Active Goals as their own entries. Status and next actions belong in Focus, not here; keep Goals to the durable "what I am working toward".

- **Hoped-for self** (prose): "Picture yourself a few years out, going well. Who are you becoming, and what are you doing?"
- **Feared self** (prose): "And the version you are working to avoid becoming, what does that look like?"
- **Ought self** (prose): "Is there a self you feel you *should* be, that is different from the one you want? What is the gap?"
- **Direction** (prose): "What is the one arc your smaller goals are all serving right now?"
- **Active goal** (cluster): "Name a goal or two that are genuinely live for you at the moment, one line each."

## Skills (non-sensitive)

**Frameworks:** self-assessed expertise calibration (the map the AI uses to set explanation depth) and standard competency self-report.
**Highest-signal sections, in fill order:** Expertise Map (this is what calibrates how much the AI explains, the highest leverage), Languages, then Skill Entries per domain. Self-rated depth is a stated fact, not an inference.

- **Expertise level** (tool, one per named domain): "In [domain], take me as..." A working expert / Competent / A beginner / Skip.
- **Explanation preference** (tool): "When I explain something in an area you know well, I would rather you..." Skip the basics / Give a quick recap / Explain in full / Skip.
- **Domains and languages** (cluster): "Which few areas should I treat you as expert in, and which spoken or programming languages do you use?"
- **Growing edge** (prose): "Is there a skill you are actively building right now that I should calibrate to as improving, not fixed?"

## Preferences (non-sensitive)

**Frameworks:** interest and taste self-report; the tools-and-environment inventory the AI uses to personalize suggestions.
**Highest-signal sections, in fill order:** Interests & Passions and Tools & Tech (the two that most change suggestions), then Media & Content, Food & Drink, Likes, Dislikes & Avoidances. Aesthetic Preferences last.

- **Interests** (cluster): "What genuinely holds your interest outside of work, a few things?"
- **Tools** (cluster): "Which tools and tech are you loyal to, and any you avoid?"
- **Media** (cluster): "What do you read, watch, or listen to that says something about your taste?"
- **Dislikes** (prose): "Anything I should steer clear of suggesting, a hard no in food, tools, or content?"

## Focus (non-sensitive; dynamic layer)

**Frameworks:** current-priority and near-horizon self-report. This is the deliberate dynamic facet: only what is true right now. A durable aspiration routes to Goals; a life-history arc routes to Biography. Route accordingly rather than writing a standing fact into Focus.
**Highest-signal sections, in fill order:** Current Priorities and How to Help Right Now (what the AI should do differently this week), then Current Life Chapter, Routines & Cadence, Active Contexts.

- **Current priorities** (prose): "What is genuinely at the top of your plate right now, the two or three things?"
- **How to help now** (prose): "Given that, what should I do differently for you this week specifically?"
- **Current chapter** (tool): "The chapter you are in feels like..." Heads-down execution / Exploring options / Recovering or resetting / Skip.
- **Cadence** (cluster): "Any routines or standing rhythms I should know about to time things well?"

## Lifestyle (non-sensitive; Substance Use is sensitive-adjacent)

**Frameworks:** chronotype and daily-rhythm self-report; standard health-behavior inventory for sleep, diet, and exercise.
**Highest-signal sections, in fill order:** Daily Rhythm & Chronotype (this times everything the AI proposes), Sleep, then Exercise & Fitness, Diet & Nutrition, Living Environment, Recreation & Leisure. Substance Use is sensitive-adjacent: offered plainly with an explicit skip, never pressed.

- **Chronotype** (tool): "My sharpest hours are..." Early morning / Midday / Late night / Skip.
- **Energy pattern** (tool): "Across a normal day my energy..." Starts high and fades / Builds later / Stays fairly even / Skip.
- **Rhythm** (cluster): "Roughly how do your sleep, meals, and movement land in a normal day?"
- **Substance use** (prose, sensitive-adjacent, explicit skip): "Anything about caffeine, alcohol, or other substances worth noting for how I help? Say skip and we move on."

## Relationships (sensitive - consent gate)

**Frameworks:** adult attachment (secure, anxious, avoidant), framed non-clinically; household and social-network structure. The people themselves are Memory entities; this facet holds the relational self only.
**Highest-signal sections, in fill order:** Family & Household and Roles & Inner Circle (structure the AI must not get wrong), then Relational Style & Attachment, Social Network. 6 to 8 questions, gentle, explicit skip on every item. Named people route to Memory promotions, not into this facet.

- **Household** (cluster): "Who is in your household or immediate family, in the plainest terms? Prefer not to say is always fine."
- **Inner circle** (prose): "Who are the few people you lean on most? Names are not needed; skip freely."
- **Closeness style** (tool): "In close relationships I tend to..." Trust and lean in easily / Take a while to open up / Keep some distance / Prefer not to say.
- **Conflict style** (tool): "When something is wrong with someone close, I usually..." Raise it directly / Wait and watch / Pull back / Prefer not to say.

## Health (sensitive - consent gate)

**Frameworks:** accessibility and support-needs self-report; the minimum stable-attribute record the AI needs to be considerate. Keep it terse and factual: record only what changes how to help, never a full medical history.
**Highest-signal sections, in fill order:** Implications for How to Help (by far the highest signal, the accessibility and support needs), then Conditions & Needs only as they affect assistance. Medical History and Insurance are offered last and only if the user opens them. 6 to 8 questions, gentlest register, explicit skip everywhere.

- **How to help** (prose): "Is there anything about how you are doing that should change how I work with you, pace, format, timing, anything? Prefer not to say is completely fine."
- **Accessibility** (tool): "Do you have an access or format need I should build in by default?" Yes, and I will name it / Not really / Prefer not to say.
- **Stable conditions** (prose, explicit skip): "Only if you want it on file: any ongoing condition I should be considerate of. Say skip and we move on."

## Finances (sensitive - consent gate)

**Frameworks:** money-management-style self-report and financial-orientation framing. Money style and orientation are the high-signal, low-exposure items; balances and totals are only ever recorded if the user volunteers them.
**Highest-signal sections, in fill order:** Money Management Style and Financial Situation orientation (how the AI should frame money advice), then Financial Goals & Constraints. Assets, Liabilities, Net Worth, and Legal & Estate are never asked for figures; they are only noted if offered. 6 to 8 questions, explicit skip everywhere.

- **Money style** (tool): "With money I run mostly..." Careful and planned / A mix / Loose and by feel / Prefer not to say.
- **Risk posture** (tool): "On financial risk I tend to..." Seek it / Tolerate it / Avoid it / Prefer not to say.
- **Money's role** (tool): "Money is mostly, for me..." A tool / A goal / A source of stress / Prefer not to say.
- **Constraints** (prose, explicit skip): "Any money constraint or goal I should keep in mind when I suggest things? No figures needed. Say skip and we move on."

---

## Confirm-pass items (all facets)

In confirm mode and at the head of any run with existing `unconfirmed` markers, up to two confirmation asks come first (`interviewing.md`, question order). Each is a short check, not a fresh construct:

- **Confirmation** (tool): "I have you down as [the marked line]. Does that hold?" Yes, that holds / Not quite, here is the correction / Prefer not to say.

A **Yes** shortens the marker to `confirmed`; a correction becomes a new stated fact (unmarked); a shrug or skip leaves the marker untouched, never re-probed (`provenance.md`, `interviewing.md`).
