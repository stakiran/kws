# Naming
**Naming** means giving something a name. What we create in SSE are concepts, and concepts have both content and a name (caption). By naming the content, the concept becomes easier to handle.

Because naming is an important activity in SSE, this chapter explains it in detail.

## Overview and necessity of names
What is a name in the first place? Why do we give names? Let's look at how SSE treats them.

### Why name things?
Do names really matter?

In this book, I introduced QWINCS, but even without making up such a term, you could still get the point across by saying "There are five communication tools besides chat." So why bother naming it QWINCS?

There is one reason: **reusability**. A named thing is easier to refer to, and the easier it is to refer to, the easier it is to use in practice. You can't keep writing "There are five communication tools besides chat" every single time. Writing QWINCS gets it done in 6 characters. If you're a developer, naming should feel familiar through variable names, function names, or file names. You generally don't attach descriptive phrases that are dozens of characters long. I can't fully explain why names are easier to refer to, but I think it's a limitation of human cognition.

Also, a name is a concise summary of the content. You can't avoid understanding the content itself, but names help you understand it, and help you recall it after you've understood it. QWINCS is simply the initials of six words, but it makes it easier to remember components like Q&A, Wiki, and Issues. That said, the S stands for Sticky boards, meaning digital whiteboards like Miro, and that part is forced and therefore harder to remember. I prioritized the readability of the name QWINCS, but I still have a lot to learn.

### Names are nouns or noun phrases
What is a name? QWINCS is a name, but "There are five communication tools besides chat" is not. What's the difference?

**In SSE, a name refers to a noun (a word) or a noun phrase (a phrase).**

- "Communication" is a noun
- "QWINCS" is a noun (a coined word)
- "Five categories of communication" is a noun phrase

A name has the nuance of firmly representing its target, and it can draw a relatively clear outline of what it points to. SSE deals with abstractions called concepts, so it's important to use names to express things clearly. Otherwise interpretations drift too much, and you can't build up thinking or discussion.

### There is no single correct name
There is no absolute correct answer for naming. Later, names may become standardized due to differences in adoption or by gaining authority, but SSE does not deal with that stage. Also, when you develop, submit, and operate something, you ultimately must unify which name you use, but in SSE, **it's common for multiple names to coexist**.

For example, for QWINCS, you could imagine the following names:

- QWINCS
- QWINC (reduced to five by dropping the hard-to-understand element Sticky boards)
- Five categories of communication tools (five because chat isn't included)
- Six categories of communication tools (six including chat)
- Five Alternatives (emphasizing that there are five "alternatives" to chat tools)

Any of these is fine. At some point you must choose one and unify, but until then, you can list multiple names and be unsure which to use. In fact, shaking things up that way makes it easier to arrive at a good name.

By the way, I think name proliferation happens more often with multiple people than alone. In particular, if B doesn't like concept name N1 created by A, B often creates their own name N2 and uses N2 in daily work.

```
 N1 ---> (A's content) <--- N2
```

In the end, whether you settle on N1, N2, or a different name N3 is unknown, but you must unify somehow. In the early stage, though, everyone can use whatever name is easiest for them, and propose whatever names they feel are good.

This may sound complicated, but developers will understand it with one word: "alias." A name is nothing more than an alias for a concept (the concept's content).

## Coined words
This section explains "coined words," which you can't avoid when practicing SSE.

### Overview and necessity
Coined words tend to be disliked, but in SSE they are an important activity.

A coined word refers to **a new noun that doesn't already exist**. It's a noun, not a noun phrase. So QWINCS is a coined word, but Five Alternatives is not. However, if you make it Five Alternatives To Chat and abbreviate it as FAC, or 5 Alternatives To Chat and abbreviate it as 5AC, then FAC and 5AC are words, so they are coined words.

As already stated, in SSE it is important to give names (noun-like words or phrases), but you cannot always find an existing name that can point to a developed concept, nor a new phrase composed of existing names. SSE beginners tend to forcibly apply existing names "because they're similar," but that kills the differences and details expressed by the concept's content. If you kill those, SSE can't hold. We don't want a "clean ideal theory" that can be expressed with existing names; we want something dirtier, more realistic, and closer to us.

To handle something, you need a name, especially a word, but no existing one fits. That's why **coined words occur naturally**. It's almost more unnatural if no coined words appear. So while this section says "necessity," "inevitability" would be more accurate.

You don't need to brace yourself for coined words. If you can clearly express what a coined word indicates, there's no real problem even if it is coined. Of course, as the person creating the concept, you must also create a clear definition and explanation for each coined word, which is a heavy burden, but you can't avoid it. If you try to save that effort, the coined word becomes garbage that no one understands.

### The coined-word matrix
A point often discussed together with coined words is "how new the content is." Typically people say "coined words should be used for new content." And "modifications that merely rephrase or rearrange existing content" are said not to be "new," and to be less valuable than truly new things. Especially well-read people can connect it to various knowledge, so their bar for calling something new is extremely high. Against generative AI, it's even higher.

Because many people care about this discussion, I'll整理 it here. I call it the coined-word matrix. I'll first show the whole picture, then explain how someone engaged in SSE needs to change their thinking.

In the coined-word matrix, there are 2 possibilities for whether the content is old or new, and 4 possibilities for how naming is done, for a total of 8 patterns.

|                                      | Existing content | New content |
| ------------------------------------ | --- | --- | 
| Existing word                         | 1 (existing) | 2 (misuse) |
| Combination of existing words         | 3 (reconstruction) | 4 (avoiding coined words) |
| New word (coined word)                | 5 (weak coined word) | 6 (strong coined word) |
| Combination including new words (coined phrase) | 7 (hard coined phrase) | 8 (acceptable coined phrase) |

Let's go through them.

1 simply shows the obvious: expressing existing content with an existing word. For example, suppose there is content like "For developers, what's important isn't only productivity; the quality of experience and subjective satisfaction each developer feels also matters." This has the name DevEx, and both are existing.

2 applies an existing word to new content, so it uses the existing word incorrectly. For example, naming the content from 1 as "QoL." QoL already has another meaning, and this misinterprets what the word QoL means.

3 gives a phrase made from existing words to existing content. For example, the content in 1 is also called "developer experience," using two existing words: "developer" and "experience." A single word can't express it, so you use multiple words as a phrase. But because it doesn't use a new word, it is still easy to understand.

4 gives a phrase made from existing words to new content. The name is a phrase, but because it's composed of existing words, it should feel relatively familiar. It avoids the aversion people feel toward coined words, and **it is excellent in that it avoids coining**. For example, suppose you take the content in 1 as a base, add concreteness, and build a theory at a level that ensures reproducibility. Then you name it Engineering Effectiveness. This is [a real concept created by Thoughtworks](https://github.com/OkayHQ/ee-handbook). Whether Engineering Effectiveness is truly new is debatable, but here I treat it as "new" because it is formalized into a theory.

5 assigns a coined word (a new word) to existing content. Two common patterns are: (1) you're simply too unaware, and coin a word even though a name already exists, and (2) you create an application by combining existing content and coin a word for it. For example, I've created coined words like "Speeriece," "Management 3.0," and "Experiencity" to express concepts around developer experience. Speeriece comes from Speed + Experience, claiming the essence of experience is speed. Management 3.0 frames 3.0 as the next paradigm after 1.0 (managing process) and 2.0 (managing results), where 3.0 monitors an ideal state. Experiencity was created simply because I wanted a word to replace Productivity. In all cases, they are nothing more than reprints of the concepts indicated by developer experience or Engineering Effectiveness, with a coined word attached, so I'd classify them as 5. Either way, **it's immature to coin a word for content that isn't new; it's a weak coined word**.

6 assigns a coined word to new content. New content is difficult to express precisely because it is new. It's best if you can express it using only existing words like 4, but you can't always. Coining is possible, and in this case it is relatively legitimate. As a coined word, it's strong.

7 assigns a phrase that includes coined words to existing content. A weak coined word was already bad enough per 5, and now you're using that coined word inside a phrase. It's the worst. I call this a coined phrase (Coined Phase).

8 assigns a coined phrase to new content. When you create a large concept, such as a system or a theory, this is often unavoidable. In that sense, I call it an acceptable coined phrase.

Next, let's compare the general interpretation of this matrix with the interpretation in SSE.

First, the general interpretation. I'll mark the avoided parts with ❌. For "debatable," I'll mark 🔺.

|                                      | Existing content | New content |
| ------------------------------------ | --- | --- | 
| Existing word                         | 1 (existing) | ❌2 (misuse) |
| Combination of existing words         | 🔺3 (reconstruction) | 4 (avoiding coined words) |
| New word (coined word)                | ❌5 (weak coined word) | ❌6 (strong coined word) |
| Combination including new words (coined phrase) | ❌7 (hard coined phrase) | ❌8 (acceptable coined phrase) |

As you can see, coined words themselves are rejected, regardless of whether the content is new. People either lack the knowledge to judge whether the content is truly new, or they don't have the time or cognitive room to verify and discuss it. So they avoid it half instinctively.

For 3, I used 🔺 because especially when the "existing content" is some kind of reconstruction, some people accept it and others don't. For example, suppose you extract and reconstruct part of what "developer experience" covers and name it "Quality of Work (QoW)." Some people will nod and say "I see," while others will say, "You just renamed a reconstruction of something existing..."

Now let's look at the SSE interpretation. Where the general interpretation is ❌ or 🔺 but SSE differs, I'll mark ⭕.

|                                      | Existing content | New content |
| ------------------------------------ | --- | --- | 
| Existing word                         | 1 (existing) | ❌2 (misuse) |
| Combination of existing words         | ⭕3 (reconstruction) | 4 (avoiding coined words) |
| New word (coined word)                | ⭕5 (weak coined word) | ⭕6 (strong coined word) |
| Combination including new words (coined phrase) | ❌7 (hard coined phrase) | ⭕8 (acceptable coined phrase) |

How does it look? Even in SSE, only 2 and 7 are not acceptable. Everything else is acceptable, and used proactively.

In other words, **SSE is tolerant of coined words**. More specifically, it takes the following stance.

- ❌
    - Emphasize whether the content is truly new (concept laggard)
    - Emphasize "Can it really not be expressed with existing words?" (coined-word allergy)
- ⭕
    - Proactively present reconstructions of existing content and content that "might" be new
    - To present quickly, proactively use new names as well

Now we can finally state the conclusion.

**Those engaged in SSE must break free from being concept laggards and having a coined-word allergy.**

### Connecting to the "lower world"
As described, SSE practitioners (soft-skill engineers) gain a perspective from which they can freely create concepts. However, if the novelty of those concepts is doubtful, or if their names are coined words, they will be poorly received. In the worst case, you won't be taken seriously at all. I liken this structure as follows:

**SSE creates concepts in the "higher world." But as-is, they won't work in the "lower world," so they must be translated for the lower world.**

So at some point, you need translation for the lower world. I call this **De-Translation**. SSE is done in the higher world, using coined words as well, which you can think of as translating lower-world phenomena into a higher-world form so you can work with them. When development is done and you return to the lower world, you must undo that higher-world translation. That's why I named it de + translation.

Think of it like serialization and deserialization. You serialize complex real-world data so that computers can handle it. After processing it on a computer, you must return it to complex real-world data, so you deserialize it. Or think of encoding and decoding: you encode to handle real-world data, and after processing, you decode to restore it.

Similarly in SSE, if you follow the lower world's messy reality as-is (especially the logic of concept laggardness and coined-word allergy), you can't get much done. So you make it easier to operate in the higher world. I compare that to translation. Then you do SSE, create concepts, and when you pass them down to the lower world, you restore them. You undo the translation.

So when do you do de-translation? Soft-skill development consists of development → submission → operation. Typically, you do it near the end of development. De-translation is **equivalent to deployment or release in software development**.

Of course, if you're talking to someone for whom SSE already works, you don't need de-translation. Developers sometimes directly fetch and use source code from GitHub; similarly, a soft-skill engineer can handle concepts that haven't been de-translated.

## Naming techniques
From here, I'll introduce various techniques (overall more Thought-oriented) that are useful in SSE.

### Five Category
Naming directions can be divided into the following five.

- Authoritative
    - Bring in highly authoritative proper nouns or widely used words
    - Example 1: Conway's Law (Conway), serendipity (The Three Princes of Serendip)
    - Example 2: laggard, Git
- Attractive
    - Create appeal through visuals, sound, etc.
    - Example: Golden Circle (Golden Circle theory), Teal (Teal organizations), Deno (an anagram of Node)
- Collective
    - Collect components, connect them, and/or abbreviate them
    - Example: SMART goals, Five Forces analysis
- Descriptive
    - Use descriptive names; often turn them into abbreviations
    - Example: paradigm shift, psychological safety, mansplaining
- Figurative
    - Rely on metaphor
    - Example: bottleneck, red ocean, bridging, sandbox

Each direction has pros and cons. There are also individual fit differences. As already stated, there is no single correct name, so by relying on the direction that suits you, you can balance "not spending too much time on naming" while still "creating a usable name."

Roughly speaking, people split into an artistic type and an academic type. Artistic types prefer naming where taste is tested, such as Authoritative and Attractive. Academic types prefer Collective and Descriptive. Figurative is something some people can do, and others can't do even if they try their hardest. So aptitude splits more than you might think.

### Balancing clarity and fun
**Names should be easy to understand.**

Ease of understanding means "how low the cognitive cost is" and "how reliably anyone involved (including your future self) can interpret it in one unique way." For developers, that's readability and idempotence. It's easy to say, but creating truly clear names is extremely difficult, and often impossible. Given that no two people fully share the same prior knowledge, thinking systems, and culture, assume that clarity for everyone is basically impossible.

If you're developing alone, you should prioritize clarity for yourself. A good guideline is whether your future self (e.g., one week later, one month later, one year later) can understand it immediately. Aptitude differs a lot here too; some people can't do this at all. There's no need to lament if you can't.

If you're developing with multiple people, prioritize clarity for the concept's proposer or primary owner. The ideal is a "miraculous name" that's clear to everyone, but it's usually unrealistic. If naming itself isn't the goal (as in copywriting), stop chasing miracles.

Now, is clarity enough? Not necessarily. We're human, lazy, and self-centered, so "only clear" sometimes fails to spark interest or attachment. Without those, you'll stop touching the concept that name refers to, and it becomes nothing.

So in fact, **a name should also be interesting enough to draw interest and attachment**.

For "interestingness," getting agreement from everyone involved is not as unrealistic. It may be hard, but it's not as reckless as chasing universal clarity. At the same time, if backgrounds differ too much, they'll never intersect. Someone who watches 100+ films a year, someone who plays music rhythm games at the arcade almost daily, and someone whose hobby is reading philosophy at the library will have different metrics for what's interesting. I think it's impossible to produce a name everyone agrees is interesting.

Up to this point, we've talked about aligning as a group, but for interestingness too, it's best to secure it first from your own solo perspective. SSE is a creative and solitary endeavor, and how far you can verbalize and maintain the abstract thing called a concept depends on your persistence. **Unlike entertainers or engineers, there are no visible reactions or behaviors, so it's hard to stay motivated. That's why naming that you personally find even a little interesting is extremely, extremely important**.

Of course, a name you find interesting may not be interesting to others. Somewhere along the way, you'll reconsider the name to move it toward "interestingness that works for everyone" or toward "clarity." Even so, before you reach that stage, as a companion to the solitary work, "a name that you personally find interesting" is optimal.

Thus, names have axes of clarity and interestingness, and you must search for the best balance.

### Name-driven development
**Name-driven development** refers to a way of developing where you decide the name first, and then think through the content and organize the components.

As an example, let's look at the soft-skill tree I developed: "5C." Reposting it, 5C is as follows:

- Communicaiton/
    - Interaction between A and B. `A <-> B`
- Collaboration/
    - Interaction through output. `A <-> Output <-> B`
- Consolidation/
    - Creating high-density experiences. Pair programming, mob programming, retreats, etc.
- Culture/
    - Things related to the culture of an individual, team, or organization. Vision, ways of working, organizational paradigms, tools used, etc.
- Care/
    - How you take care of yourself as a human. Personal task management, well-being, and other things grouped under self-management, etc.

This concept was also created through name-driven development.

First, I created 3C: Communication, Collaboration, and Consolidation. I thought there were limits to "communication" as "direct 1-to-1 interaction," and believed a paradigm shift was needed. For clarity, I decided to use words starting with C- and build up to the third generation. That gave me Communication → Collaboration → Consolidation as 3C.

Now, when creating a soft-skill tree, I decided to base it on this 3C. It's obviously hard to cover a broad range of soft skills with only 3C, so I wanted to add more, but I also wanted consistency. So **I added two more slots and made it 5C. Once you do that, all you have to do is think of two more elements that start with C-**.

How is it? There's no real basis for starting with C-, and there's no absolute logic that it must be five elements. It's just a light reason like "it's easy to understand and seems to fit nicely." **And that's fine.**

SSE has no correct answers. It's enough if you can create a decent concept with best effort. If you suffer from perfectionism about evidence and logic, you won't be able to do anything, and in fact, that's why humanity still hasn't gained the perspective to create concepts. You can validate the developed concept later through submission and operation. Just like software and business: rather than trying to create something perfect from the start, you should build it quickly and ship it. Of course, science and philosophy require strict logic, but SSE is neither.

If you want to become familiar with SSE, trying name-driven development is the best approach.

Create the name first. Then mobilize your creativity to fill in its content. Share the concept you created. Try using it. Discuss it. By doing so, you can get used to the new world of SSE.

### Collecting definitions
To think about naming, you need to know the precise meaning and nuance of words. I call this **collecting definitions**.

Examples:

- Cases with no correct answer:
    - If you're doing soft-skill development related to developer experience, you need to know what "developer experience" even means. It likely differs by individual and organization, so you'll collect definitions from multiple sources. By collecting and lining them up, you can then think about how you want to interpret it.
- Cases with a correct answer:
    - For common words that appear in dictionaries, you can treat the dictionary definition as the correct answer. For words you're unsure about, it's important to consciously look them up. We often recognize word meanings **more loosely than we think**, and while that usually doesn't cause problems, it becomes a source of hesitation when naming. By properly knowing definitions, you can reduce these hesitations one by one.

Use the trigger list below as well.

```markdown
- Write down your definition of that word.
- Have you looked up the dictionary definition of that word?
- Have you looked up the original definition or origin of that word?
- Have you looked up how major people or organizations define that word?
- After collecting definitions, what decision do you want to make?
    - Do you want to follow one of the existing definitions?
    - Do you want to combine the best parts of existing definitions?
    - Do you want to create your own definition? Why do you think that's necessary?
```

### Comparing differences
Hesitation like "Which word should I use, W1 or W2?" happens often. In such cases, comparing differences in nuance is helpful.

**You can just ask generative AI.** Soft-skill development isn't about establishing absolute correct answers or airtight logic; it's about gathering hints and then creating something that seems useful. You only need the hints, so you don't need to worry too much about whether the answer is correct, and in terms of correctness, it may already be more correct than most humans.

Examples:

- Differences between tool, technique, and method
- Differences between principle, law, and theorem
- Differences between remove, delete, erase, and purge

By asking about differences, you can compare fine nuances. You'll get a sense of direction for how to create your naming. If you need strict nuance or definitions, you can research or ask later.

### Describing concrete examples
What SSE deals with are concepts, and concepts are abstract. But development doesn't go well with abstraction alone. By moving back and forth between abstract and concrete, you refine concepts into something easier to understand and more precise.

The problem is that gathering concrete examples is hard. Ideally, you'd catch customers and validate, but that's business and engineering thinking, and concepts can't always be validated. In fact, "concepts that can be validated" are only a tiny subset of all concepts, and this is the limitation of business and engineering as they stand. SSE is a new weapon for breaking through that limitation and thinking and examining within the world of concepts. **Don't get trapped by the curse of validation.** Even so, you still need concrete examples.

There are three approaches.

- 1: Apply your own experience
- 2: Create concrete examples through your own or others' imagination
- 3: Have generative AI create concrete examples

That's still hard to grasp, so let's practice by giving one concrete example.

For instance, in addition to DevEx (developer experience) and DevRel (building good relationships with developers), I also created a concept called DevDEI (DEI for developers). So what is DevDEI like? How should you build out this concept? Of course, you go back and forth with the concrete, and there are three ways to do it.

> 1: Apply your own experience

Concrete: I am neurodivergent, and I often feel that workplaces and teams don't provide enough consideration. In particular, teams request long core hours and frequent meetings, but I am optimized for a morning-person lifestyle of 6:00 to 15:00, and I don't want to break that. This isn't selfishness; without this optimization I can't function at work. But it didn't get through.

By the way, if you return from this concrete example to abstraction, you can derive things like "building teams that consider morning-type members as well," "maybe multiple working-hour patterns could coexist," and "there is a 'single way of being' that relies on long core hours and frequent meetings."

> 2: Create concrete examples through your own or others' imagination

For example, you could brainstorm around the theme "a day in the life of a team where DevDEI is well-established," or do light SF prototyping. DevDEI itself will likely be interpreted differently by different people, and that's exactly why diverse opinions should come out.

> 3: Have generative AI create concrete examples

I asked GPT-5.2, "Create concrete examples of DevDEI." Let's quickly look at the results.

- As a DevDEI concrete example for recruiting/selection (the entry point), it suggested switching to a take-home assignment (no time limit) + a review session (Q&A). In interviews, only people who can do fast verbal back-and-forth tend to win, and people with other strengths fall through; this approach recovers them.
- As a DevDEI concrete example for onboarding (the first 30 days), it suggested maintaining an acronym dictionary, decision logs, and Architecture Decision Records (ADRs), and also starting meetings with the first 5 minutes to support first-time attendees. This shifts the environment from one where only new hires who are good at speaking up and asking questions grow, to one where others can grow as well.
- For promotion depending on "relationships built at drinking parties," it suggested ideas like: always sharing important information with everyone in text, making the sponsor system (recommendation mechanism) transparent, documenting promotion criteria, and training evaluators.

At first glance, it may look like nothing more than obvious content, but that's exactly why it's easy to understand, and you'll likely come up with many additional ideas. Also, unknown terms may appear, and by researching them, your knowledge expands. For example, if you don't know what an Architecture Decision Record is, look it up.

My own reaction to the above was: "It seems good to additionally install a reading-and-writing-based way of working."

If you want to go further, you could define DevDEI as something like "the idea and methodology of completing work and evaluation using only reading and writing." Then, next, you can produce concrete examples like "techniques and methods for doing reading and writing well."