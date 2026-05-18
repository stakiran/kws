# Case Studies
In this chapter, I present several case studies to demonstrate the power of SSE.

Each case study consists of:

- 1: A concrete, typical challenge, plus the underlying context and assumptions
- 2: An approach to the challenge, especially the concepts used
- 3: How to operationalize those concepts and what issues arise

For 2: in particular, I will use concepts I developed myself—developed through SSE. You will see how powerful a concept SSE can create. Of course, I do not intend to leave this at the level of ideals or armchair theory; in 3: I will connect it to practice.

## Case1: Enabling Instant Q&A in a Large Enterprise with Over 10,000 Employees

### Background
- A large enterprise with more than 10,000 employees
- Company-specific knowledge (the internal domain), such as internal rules and various procedures, has ballooned
- It's hard to look up the internal domain on your own; the people who know are usually busy, and you often don't even have much acquaintance or relationship with them in the first place

### Challenges
- New hires cannot autonomously catch up on the internal domain, so both work and learning stay slow
- Understanding the internal domain requires OJT, which costs labor on the trainer side
- Support for the internal domain is closed within each team and becomes person-dependent, so organization-wide improvement points and bottlenecks are not visible

### Approach
Use **Rapid Q&A**.

Rapid Q&A invites all employees into a single chat channel, enabling anyone to ask and answer freely.

There are two caveats. The first is to **not think about reusability at all**. You don't need to search for past answers; you simply ask. It's fine to treat it like you're talking to Google or ChatGPT. The other is to **strictly limit it to questions purely about the internal domain**. You must not ask things you could find via Google or ChatGPT. Small talk, debates, promotions, and top-down announcements are also not allowed. Limit it strictly to internal-domain Q&A. Think of this as a principle so strict that anyone who can't follow it should be expelled for a certain period.

### Mechanism
QWINCS is the main set of communication modes. Besides Chat, there are five others; the Q stands for Q&A. Q&A is the only area where no dedicated B2B tool has been established, but on the consumer side, Stack Overflow and Quora are well known. Its essence is this: **questions that are only answerable by "people who happen to know" can be resolved quickly and succinctly through the "power of numbers."**

If you run this in a company of 10,000 employees, it can be Slack, Teams, Discord—anything is fine. You create a single channel and gather 10,000 people there. Then everyone asks and answers as they like. You can rely on the power of 10,000 people. As it heats up, the message velocity becomes incredible, which triggers random rewards. It will almost certainly become the most-viewed channel. Like an SNS, people will start accessing it frequently and scrolling. And when they see a question they can answer, they post immediately.

### Operations and Challenges
Rapid Q&A is the simplest approach to realizing "Q&A with participation from all employees." In theory, you just create one channel and invite everyone.

Of course, there are many operational challenges. Major ones include:

- Who serves as the channel admin, who serves as moderators, and where the budget comes from
- How to reduce effort for inviting and maintaining all employees
- How to enforce operations that prevent it from becoming noisy
    - For example: "Do not use mentions at all," "Everyone turns off notifications," "Only handle questions about the internal domain"
- How to help online-shy people (those who can't react to or comment on posts by strangers) get over the hump
- How to design incentives for answering

You have to solve all of these. It's less about whether there's a single correct answer and more about decision-making. Because it's a company-wide initiative, it requires investment at the executive level, or at the level of a CTO or CDO. A common objection is "Let's try it bottom-up with a small team first," but as already stated, **Rapid Q&A depends on the power of numbers, so it must start large-scale from the beginning**.

## Case2: Coexisting with Neurodivergent People in Teams and Groups

### Background
Terminology:

- Neurodivergent refers to people who, when developmental disorders such as ASD, ADHD, and LD are understood as a form of diversity, are the individuals concerned
    - It's simply differences in brain traits, and there's growing momentum to treat it as diversity (neurodiversity)
- A team refers to your work assignment; a group refers to your organizational affiliation
    - Depending on the company, there may be only teams, or both teams and groups
    - The number of affiliations also varies by company: only one team, only n teams, one group and n teams, n groups and m teams, and so on

Context:

- 1: Due to advances in medicine and the casualization of diagnosis, more people fall under neurodivergence
- 2: Organizations and work are supported by high discipline and cooperativeness, which either exhausts neurodivergent people excessively or makes execution impossible
- 3: There's a reasonable chance that neurodivergent people will be present within teams and groups
- 4: When they are, neurotypicals (typically developing, non-neuro) try to impose their own standards, but as in 2:, that won't happen
- 5: "Reasonable accommodation" is often cited as an approach for neurodivergent people, but it's not enough

### Challenge
The challenge is that **reasonable accommodation cannot address neurodivergent people**.

In practice, reasonable accommodation is a neurotypical best effort. But neurotypicals are accustomed to high discipline and cooperativeness; they believe they can naturally do it, or at least that they should. So they won't abandon that premise. In other words, they won't come close to the level of accommodation neurodivergent people need; they simply try to impose their own standards. They try to cover it up with skillful acting.

For example, if there's someone with ASD who is good at remote work and text communication, you could allow that person alone to be fully remote and fully text-based. But there are virtually no managers who can introduce that kind of special treatment. They can't do it without the mindset of reasonable accommodation—and they also can't do it just by knowing the term.

### Approach
Use **Individualized Accommodation**.

Individualized Accommodation is a concept I created as an alternative to reasonable accommodation. As the name implies, it provides individualized accommodations for each neurodivergent person. Rather than forcing them to follow the norms the team or group must follow, you consider special handling so they can avoid following those norms as much as possible. **In short: you give special treatment.**

### Mechanism
Neurotypicals tend to avoid special treatment, but you can't avoid it. They fundamentally do not have the trait-level ability to sustainably follow norms, so forcing them to do so is out of the question. Once you acknowledge "we will give special treatment," you can stand at the starting line. Then you can think about balance.

- In other words:
    - ❌ Assume you'll make them follow norms, then think about balance
    - ⭕ Assume you'll give special treatment, then think about balance

To get people to understand this premise, the term reasonable accommodation is insufficient. You need new language to get people to understand that you will treat individuals specially.

### Operations and Challenges
I will discuss about five issues and how to break through them.

1: The highest priority is educating people about neurodiversity. Neuro-related literacy is overwhelmingly insufficient today, so you first have to get people to learn. Sexual minorities such as LGBTQ have seen significant progress in education, but I believe a similar scale and momentum is needed here. Of course, you must also derive business benefits or opportunities from doing this. It's difficult.

2: Next, you must define who is eligible for individualized accommodation. If you don't clearly define this, lazy employees will exploit it. The simple guideline I propose is: "They have a medical certificate related to neuro." Neurodivergence is congenital, and once diagnosed, it's considered unlikely to be reversed later (ADHD can be suppressed with medication, so it might change if you retest after suppression). Also, tests are carefully conducted by specialists, so it's hard for a lazy neurotypical to intentionally obtain such a diagnosis. Therefore, anyone with a medical certificate can be unconditionally eligible for individualized accommodation.

3: Neurodivergent people also face a dilemma: whether to come out to obtain individualized accommodation, or to continue enduring as before while fearing negative impact. To promote individualized accommodation, you need them to come out. How?

4: The capability question: what, specifically, do you do as individualized accommodation? This can be solved with SSE. You just create the necessary concepts, then perform Training and Test.

5: Finally, because individualized accommodation is nothing more than "extra work," you must develop benefits that outweigh it. Specifically, matching neurodivergent people with work. Ideally, you want to find roles or working styles where they can outperform neurotypicals. This isn't limited to finding above-average talent. Rather, it's about enabling them to work steadily as full-time employees at a comparable level to neurotypicals and secure substantial compensation. On this point as well, as with 4:, SSE-driven articulation of the current state and creation of concepts is required.

## Case3: Reducing Lifestyle Overtime and Quiet Quitting

### Background
- Lifestyle overtime has become the norm
    - The main purpose is known to be "living expenses," but there are also "killing time" and "addiction-like fulfillment of personal desires through work"
- Quiet quitting is widespread
    - Because people respond safely and do only the minimum necessary work, deep trust relationships and serendipity do not occur

### Challenge
Being unable to escape the spiral of low profit and labor shortages.

Structurally, in many cases the cause is the lack of diversity in the workplace. A lack of diversity can be rephrased as being monolithic—for example, explicitly or implicitly allowing only a single norm. In terms of working style, this could be "all employees come to the office every day." Then, for anyone who doesn't fit that monolith, it's a workplace that "doesn't fit."

People who don't fit, and can't make themselves fit, are treated as non-contributors, so the organization is always short on talent. Also, even those who do fit must spend significant energy to keep fitting, so they have no slack. They try to survive with minimal work, leading to quiet quitting. Of course, because it's a monolithic workplace, you can't improve that monolith (the people in power are monolithic). In addition, chronic fatigue and vigilance from adapting to the monolith prevent creative thinking, so people can't even gain the perspective needed for fundamental improvement or resolution. The status quo continues.

In other words, the challenge is a negative spiral, and its cause is monolithicity.

### Approach
Use **Chrono Diversity**.

Chrono Diversity treats two axes as traits and as diversity: "morning type vs. night type" and "speed of becoming fully awake." Morning types can't perform well at night, and night types can't perform well in the morning. Some people perform well immediately after waking up, while others ramp up over several hours.

What this idea wants to emphasize is avoiding mismatch. It's not so much that you can achieve high performance by working during hours that match your body clock; it's that **you can't perform when working at hours that don't match, so you want to avoid it**.

Under this approach, each person aims for a working style that avoids mismatch. Inevitably, core time shrinks or disappears, so you must increase asynchronous communication. More precisely, you need enough soft skills to make work function even asynchronously. SSE also helps.

### Mechanism
The primary cause of our fatigue and vigilance is body-clock mismatch.

In Japan, standard working hours are probably 9:00 to 17:00, but this mismatches both morning types and night types. For morning types, working after 15:00 is itself painful, and for night types, starting at 9:00 is painful too. But because you must adhere to these hours, you grit your teeth and hold back. Naturally, under such conditions it's hard to perform well, and engagement is unlikely to rise.

### Operations and Challenges
I'll highlight several major issues.

1: How to determine a person's body clock. Are you a morning type or a night type? And how quickly do you become fully awake? For morning vs. night, there are some diagnostic methods such as chronotype assessments, but there isn't one for awakeness. Because it's about constitution, you can roughly understand it yourself, but if you operate this at an organizational level, it's better to establish a diagnostic method. For the record, I propose these as ways to measure awakeness type: "Can you eat a meal at the level of lunch or dinner immediately after waking?" and "Can you go out to start high-intensity exercise within 10 minutes after waking?" If you can, your awakeness is likely fast.

2: Legal hurdles when respecting night types. For example, in Japan, 22:00 to 5:00 is considered late-night work, which imposes additional obligations such as premium wages and health considerations. So even when implementing full flex, organizations often limit workable hours to 5:00 to 22:00. However, for night types, 22:00 to 5:00 is often their golden time.

3: Operating asynchronous work. As you can see from how modern desk workers are still reverting to office attendance, humanity is still bad at asynchronous work. Also, from a capitalist viewpoint and in terms of organizational dynamics, gathering people physically is easier for management and exploitation, so incentives for async are weak to begin with. But if you respect chrono diversity, you must build things to run even asynchronously. This requires many soft skills and concepts. That's exactly why I launched SSE. You must implement asynchronous work suited to that team and organization using SSE.

## Case4: Improving Employee Engagement by Unlocking 1on1 Between Employees

### Background
- The pandemic accelerated remote work
- To increase employee engagement even under remote conditions, 1on1 where two people can talk privately rose to prominence
- The quality of 1on1 depends on facilitation, but the manager leading 1on1 is not necessarily good at it

### Challenge
The harms and limits of 1on1 are becoming more visible.

First, as a harm, **information disparity occurs**. 1on1 is conducted by senior people toward junior people, creating a hierarchical structure where one senior meets N juniors. Each session is closed and private, and keeping records makes candid conversation harder, so no records remain. In other words, the senior side monopolizes information.

Second, it tends to become a bottleneck for information transmission. For example, if you do 1on1 once a month, the frequency at which the senior transmits information to the junior is monthly. Because a monthly recurring meeting event is set, attention gets pulled toward it. This is known as an empirical rule similar to Parkinson's law and Conway's law, and taking my name as the proponent, I call it **Kirano's Law**. Smart people may think, "Then just send information asynchronously right away," but seniors are busy and also immature in soft skills, so they don't have the capability for asynchronous information sharing.

In addition, **engagement may not increase due to subordinate dissatisfaction—it can even decrease**. I haven't seen research results from this viewpoint, but if you investigate it, it should become clear immediately. In my view, it's self-evident. Specifically, if the senior's facilitation is poor, that 1on1 becomes unnecessary or harmful for the junior. Ideally, if it's unnecessary, you skip it; if it's harmful, you improve it. But seniors cannot question the execution of 1on1 that has become established as a company-wide initiative or custom. And since they also lack the skills to do it asynchronously, they can only conclude that there's no way other than 1on1.

### Approach
Use **Free 1on1**.

Free 1on1 refers to a state where any employee can request a 1on1 with anyone at any time. Most organizations already have a company-wide group scheduler, so you simply allow anyone to add a 1on1 meeting with anyone. If there's a problem, the person being added rejects it. Time is based on 30-minute units. Topics are free, but the requester should set the table.

Define Free 1on1 formally as a company-wide right. In other words, if you're an employee, you shouldn't be surprised to receive a 1on1 request from anyone. You must thoroughly educate people so that becomes true. Only then are you at the starting line.

This enables employees to autonomously conduct 1on1 with the people they need, as needed. Instead of obligatory 1on1 only with seniors, you gain a more flexible 1on1. Put differently, you could call it the democratization of 1on1.

### Mechanism
Currently, 1on1 has been defined as an initiative or制度. We are extremely obedient to organizations, especially once we become seniors, so we obediently follow initiatives and制度 called 1on1 as well. That's where the tragedy begins.

So we change the root. **Make 1on1 a right**. If you're an employee, you can request a 1on1 anytime, with anyone, to anyone. This alone can break through the harms and limits of conventional 1on1.

### Operations and Challenges
Of course, adopting Free 1on1 does not instantly resolve issues, and the risk of it becoming a formality is high. Even after recognizing Free 1on1 as a right, you must drive additional education and operations.

For example, the conventional monthly or weekly 1on1 between manager and subordinate, when redefined in the context of Free 1on1, would look like this:

- In this team, we recommend a 30-minute 1on1 with the manager once a month:
    - The member applies and adds it within the manager's working hours and during an available slot
    - When applying, list the items you want to discuss

With this operation, the subordinate side can proactively control the 1on1. The manager will likely follow the subordinate's topic list while weaving in what they want to talk about. However, it would be difficult for an ordinary manager to reconstruct things to this extent just by learning about Free 1on1, so you likely need to educate people on such operations as well.

I recommend establishing a company-wide, supportive secretariat like an OOPO (One on One Program Office), or appointing a dedicated internal educator like a 1on1 evangelist. Note that I wrote "supportive." If you push it down as an initiative or制度, it defeats the purpose.