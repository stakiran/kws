# The Big Picture of Soft Skills
In this chapter, we will outline the overall picture of soft skills.

## The Soft Skill Tree
In SSE, we believe there is **no single correct way to systematize soft skills**. Here, "systematization" means a hierarchical classification—for example, large/medium/small categories. We will call this a **soft skill tree**, or simply a tree. In other words, SSE does not assume an absolute tree exists; instead, we create a tree as needed.

### Example Trees
For instance, consider a tree like the following:

- Soft Skills/
    - Communication/
        - Meetings/
            - 1on1/

Here, the large category is "Communication"; within it, the medium category is "Meetings"; and within that, the small category is "1on1". This is not claimed to be "correct"—it's simply one possible definition.

Let's create another tree. I gave GPT-5.2 the following prompt:

> Organize soft skills into five major categories. Also list five components for each. That means it should become a 5x5 list of 25 lines. Use Markdown list syntax, and make the indentation 4 spaces.

As a result, it returned the following tree (slightly edited):

- Communication/
    - Active listening
    - Clear explanations
    - Asking good questions
    - Feedback
    - Writing
- Collaboration & Interpersonal Relationships/
    - Building trust
    - Relationship alignment
    - Teamwork
    - Conflict handling
    - Consideration for diversity
- Thinking & Problem Solving/
    - Logical thinking
    - Critical thinking
    - Problem discovery
    - Decision-making
    - Creativity
- Self-Management & Execution/
    - Time management
    - Stress management
    - Autonomy
    - Perseverance
    - Adaptability
- Leadership & Influence/
    - Presenting a vision
    - Motivation
    - Delegation
    - Coaching
    - Stakeholder management

If I presented this as-is, all one could say is "So what?" And it would be absurd for SSE to submit this 그대로 to a team or a customer. Still, it provides hints for engineering soft skills. For example, it should be useful as a reference when creating a tree for yourself or your team.

Finally, I'll introduce just one more: [a tree I created myself](https://dev.to/stakiran/categorizing-soft-skills-into-5cs-387n). It's unified by five "C"s. Note that it includes only the major categories, and in the sublists I attach descriptions rather than medium categories.

- Communicaiton/
    - Interaction between A and B
    - `A <-> B`. Two-party interaction. Direct
- Collaboration/
    - Interaction through output
    - `A <-> Output <-> B`. Indirect
- Consolidation/
    - Creating high-density experiences
    - Examples: pair programming, mob programming, communication time, retreats, and other events
- Culture/
    - Matters related to the national culture of individuals, teams, or organizations
    - Examples: vision, ways of working, roles and hierarchy, organizational paradigms, tools in use, etc.
- Care/
    - How to care for, regulate, and maintain yourself as a human being
    - Examples: personal task management, well-being, and other things grouped under self-management

This 5C is a tree based on bold inclusion/exclusion choices, and I think it's relatively easy for developers to understand. At the very least, it's far better than the second 5x5.

### Create a Tree That Fits You
What we want is not to "know" soft skills—we want to use tools that are useful. That is why this book teaches SSE, an "engineering discipline for handling conceptual tools," and why this chapter discusses the big-picture concept of a tree.

A tree is like a system architecture diagram. Just as an architecture diagram shows the elements a system needs and its overall structure, a soft skill tree shows how soft skills are categorized for a given purpose. In other words, **you can create a tree whenever you need one**.

Typically, you define a tree at the individual, team, or organizational level. You can organize the soft skills you personally want to acquire; or create a tree of the skills everyone on a team should learn. Or you can build a company-wide tree as a catalog, so any employee can use and maintain it.

Either way, you should create some kind of tree **yourself**. Soft skills are extremely broad and ambiguous, and without a tree you cannot focus.

## The Components of Soft Skills
What you may be wondering about next is the set of concepts beneath a skill.

For example, in the following tree, what belongs inside the small category "1on1"?

- Soft Skills/Communication/Meetings/
    - 1on1/
        - *What goes here?*

Or, what belongs under the following small category and beyond?

- Communication/
    - Active listening/
        - *What goes here?*
            - *And could there be more levels below?*

In other words: what are the sub-concepts of a skill?

### Skills Are Emergent
First, as a major premise: **skills are emergent**. "Emergence" refers to the property that "the whole is more than the sum of its parts." What we call a skill is exactly that: you cannot call something a skill just because you assembled its components. Even with a simple view, skills involve factors like "the person's inherent capability and current condition," "the situation and context at the time," and "experience," so they cannot be explained in a fully systematic way.

### The 6T: The Components of Soft Skills
With that in mind, SSE expresses the components of soft skills concisely. We call this the **6T**.

- Things that represent concepts
    - 1: Tool
        - ~~Hard tools: things you can physically use, such as hardware and software~~ Not included
        - Soft tools: things humans operate, such as templates, checklists, and procedures
    - 2: Technique
    - 3: Thought
    - 4: Tenet
- Things that represent actions
    - 5: Training
    - 6: Test

Concepts were discussed in Chapter 1. SSE fundamentally deals with soft skills, or concepts (including creating them). That is, it indicates there are four types of concepts. As for actions, they succinctly indicate how to use concepts.

Let's look at them in order.

### 1: Tool
As the name suggests, this is something you use directly—but note that **hard tools are not included**. In other words, when SSE says "tool," it often means a soft tool: templates, checklists, procedures, classification items, question prompts, and the like.

I organized the main soft tools into seven viewpoints. I call it the [Seven Lists Principle](https://dev.to/stakiran/the-seven-lists-principle-for-creating-tools-for-soft-skills-26f8), shown below.

```
               Task    Span
     Trigger                  Question
            Check        Label
                   Fill
```

Skipping the details, in short these are seven items: "instructions," "time span," "hints," "open questions," "Yes-or-No closed questions," "classification," and "fields to be filled in."

### 2: Technique
Words that fit here include "how-to," "approach," "method," "tactic," and so on. It's not as concrete as a Tool, but it is organized enough to be used directly.

For example, "brainstorming" is a Technique. It was originally devised by Osborn and has certain premises and steps. Meanwhile, today individuals and organizations often treat it casually, and it is frequently refined into their own Technique.

### 3: Thought
Words that fit here include "philosophy," "strategy," "principles," "guidelines," and "standards." Rather than something you use directly like a Tool or Technique, it's something you first understand and then keep in mind when needed.

This "keep in mind" part is tricky. To keep something in mind means you actually understand it, remember it, and recall it when necessary—then reflect it in your behavior. In SSE, we call this **application**. Just as understanding the basics doesn't mean you can solve applied problems, with Thought, understanding doesn't necessarily mean you can use it (i.e., translate it into action).

For example, consider the overly familiar phrase "Always question common sense." This can be a Thought, but using it in practice is extremely difficult. When you're busy at work or fighting with your family—when you're not calm—you can't question anything at all, and you may even knowingly cancel the questioning and force your own way through.

### 4: Tenet
Words that fit here include "religion," "beliefs," "philosophy," "values," "culture," "tradition," and "precedent."

In SSE, rather than creating new Tenets, we aim to **capture existing Tenets by putting them into words**.

For example, Erin Meyer's "The Culture Map" clarifies Tenets in the form of each country's culture. It frames countries across eight scales and shows that there is no single "right" way for a country to be. In Japan, the "evaluating" scale leans strongly toward "indirect negative feedback"; in fact, negative feedback must be delivered one-on-one and in a roundabout manner. Breaking this norm can be considered harassment in Japan.

Soft skills often actually depend on Tenets. In SSE, we often verbalize Tenets to make them explicit, and then consider how to push against them. For instance, if you want to introduce direct negative feedback in Japan to increase business speed, simply preparing the Tools or Techniques for that purpose won't make them used. You must first clarify Japan's Tenets, and then think concretely about how to proceed.

Assume that **soft skill engineering often starts with understanding Tenets**. In software development terms, it's like understanding domain knowledge.

### 5: Training
From here on, these are elements representing actions rather than concepts.

Training refers to preparation and practice to make concepts usable. It includes preparation such as creating Tools and keeping them close at hand so you can use them immediately, as well as practice such as doing mental rehearsal, trying them alone, or even asking someone to practice with you.

Software runs on its own once executed, but soft skills must be operated by humans themselves. Because it's a skill, the user's proficiency matters. Even if you can use it, if it takes too long, it won't be acceptable. You want to be able to use it as quickly as possible, and reliably.

### 6: Test
Test refers to using the concept. Whether it's just personal or in-group Training, or a real high-stakes situation where failure is absolutely not allowed, SSE considers both to be Test.

This naming reflects SSE's philosophy: **exercising soft skills is always experimental**. There is no absolute correct answer, and completion is impossible. All you have are the best decisions and actions you can take at that moment, the results they produce, and the learning you gain from them. SSE is an endless journey.

## Summary
Soft skills are emergent:

- Soft skills are implemented using components called concepts, but they are not complete simply by collecting concepts
- Just as the whole exceeds the sum of its parts, soft skills are more than a set of concepts

6T:

- To handle soft skills, SSE simplifies them as 6T
    - Concepts can be broadly divided into Tool, Technique, Thought, and Tenet
    - As actions, SSE defines Training and Test
- About each of the 6T:
    - Tool: refers to soft tools such as templates and checklists
    - Technique: less concrete than a Tool, but a structured method that can be used
    - Thought: not something you can directly use; something you must keep in mind. You must use it appropriately as needed (application)
    - Tenet: existing assumptions such as values and culture. SSE aims to capture them by putting them into words
    - Training: preparation and practice to make concepts usable
    - Test: in SSE, exercising soft skills is always treated as "experimentation"