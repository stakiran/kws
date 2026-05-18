# QWINCS
QWINCS is an acronym that describes the main communication tools. It is pronounced "Kwinks."

QWINCS stands for:

- Q&A
- Wiki
- Issues
- Notes
- Chat
- Sticky Boards

QWINCS is more of a thought than a tool, emphasizing that **communication tools are not limited to chat apps like Slack or Teams**. There are five other types besides chat, and it's obvious that the more of them you can use effectively, the broader your communication options become. In particular, it helps reduce reliance on primitive in-person attendance and meetings.

QWINCS is also important for soft-skill development. Because you're dealing with concepts, you need to increase the share of interactions done through reading and writing, but that's difficult with chat alone. Of course, going to the office and meetings also doesn't work well, since nonverbal communication is the main channel there too. If you're developing soft skills, you want to understand all six types of QWINCS tools and be able to use them proficiently.

Below, I organize representative examples, overviews, and when each can be used.

## Q&A
- No existing tools

Q&A is a communication tool where anyone can post questions at any time, and anyone can write answers. Within QWINCS, it's the only category that doesn't really have a solid communication tool (though for consumer use there are Stack Overflow, Quora, and the like).

The real value of Q&A lies in **using the power of numbers to quickly resolve what "someone knows."** Information that might take an uninformed person over an hour to figure out can be answered in two minutes by someone who already knows. Including context checks and picking the best answer, it's probably done in five minutes. In other words, you can reduce one hour to five minutes in simple arithmetic—an overly simplistic example, but that's the effect Q&A aims for.

Conversely, you could say it **doesn't work without the power of numbers**, which is also why it still hasn't been developed as a communication tool. At minimum you want several thousand people—ideally tens of thousands. But companies that large are a minority. And large enterprises are bureaucratic, so an "internal platform where anyone can do Q&A" is unlikely to work. Even if you did it, it would probably be limited to a department or team—but then you don't have enough people.

That's why, if you want to realize Q&A, you need to build a platform that gets every employee to participate at the scale of thousands or tens of thousands. Alternatively, you need to achieve enough diversity of answers and response speed to match the "power of numbers" created by participation at that scale. Either way, it's a hard problem.

You might think, "But we have generative AI," yet generative AI still doesn't have the potential to replace Q&A. It can solve things you can find via Google, but what's more important is the internal domain—company-specific knowledge. Questions about the internal domain can only be answered by employees who know it. You might think, "But we can use RAG," and I also think it will catch up in, say, around 2028, but as of 2026 it can't match the quality of "knowledgeable employees answering quickly." Or even if it could, building that kind of environment would likely cost an unrealistic amount. It will take some time for costs to come down.

## Wiki
- Cosense
- Mediawiki
- esa.io
- Confluence

Wikis are an old tool. Originally, they were tools for quickly writing information in plain text in a browser, and enjoying the convenience of a network structure by linking pages to pages, but they can also be used as a communication tool.

A wiki's true value is that it can create **an SSoT (Single Source of Truth) communication area**. Strengths include plain text, being fully browser-based, handling content as independent pages, and freely reusing information and designing navigation via links—all of which make the experience comfortable. Comfort matters. Because it's comfortable, people can access it frequently every day, and therefore it can become an SSoT. An uncomfortable place won't become an SSoT and will almost certainly become a hollow form. Put differently, **a wiki is a communication tool that meets the requirements of an SSoT**.

Therefore, if you want to build an SSoT, you should rely on a wiki.

However, many existing wikis are poorly made (in the sense of being SSoT-oriented). The best answer I know is **Cosense**. First, consider whether you can use Cosense; even if you can't, try hard to make it work as much as possible. If that still doesn't work, then consider other tools or building your own. That's how well-made Cosense is as a wiki.

Conversely, I do not recommend the following wikis:

- Pukiwiki, Mediawiki, and other long-established wikis
    - Their history is long, and they haven't reached modern experience standards
- Enterprise wiki services or features such as Confluence
    - They are secure and feature-rich for enterprise use, but as a result they lose lightness and aren't comfortable
    - They are also expensive and over-specced, making them hard to reach for small-group soft-skill development
- GitHub Wiki and personal wikis in general
    - They are insufficient because they lack modern essential collaboration features such as simultaneous multi-user editing

## Issues
- GitHub Issues
- Backlog

"Issues" refers to ticket-based services. They were originally tools for issue tracking, but they can also be used as general-purpose communication tools. In other words, communicate as one ticket per topic. In fact, GitHub has released Discussions based on Issues.

The real value of Issues is that they are **topic-oriented and task-oriented—you can pack one topic into one page, and also treat it as a task in terms of "whether it's done."** Especially in asynchronous communication, the key is to treat communication itself as tasks: handle them independently one by one, and bring them to completion. You need Issues to realize that.

So if you want to do asynchronous communication, you should introduce Issues. Whether you can introduce Issues and use them well determines the success or failure of an async-first way of working. As a concrete tool, you can't go wrong with GitHub Issues. Other ticket management tools exist; I list Backlog for now, though I've never used it. Essentially, anything is fine as long as it provides lightweight ticket management with the potential (especially comfort from its lightness) to cover everyday communication.

## Notes
- Notion
- Google Docs
- Dropbox Paper
- Box Notes

"Notes" refers to collaboratively editable notes. Historically, this started with static rich-text documents like Microsoft Word, and as technology advanced, it became cloud-based so multiple people can edit simultaneously. Multiple people can access a single note and edit at the same time. You can also see each person's cursor, and in real time you can see who is where (on which line).

The real value of Notes is that they **can be used as a one-dimensional virtual office**. It's long been known that one way to achieve high performance and satisfaction is "everyone physically gathering and collaborating closely," but today that's often unrealistic. So in recent years, the idea of gathering as avatars in a virtual space has been implemented, called a virtual office. Gather and Spatial.Chat are well known, and in Japan there are lightweight options like Remotty and Teracy, but Notes can also actually be considered part of this category.

For example, create one page that resembles an office, and have all members gather there. Create a section for each person, where they write short updates or share information, and react or reply to other members' posts. For important matters or votes, you can create sections near the top. This kind of "hub page" is easiest to understand if you create one per day. If today is 2025/12/19, create a page named 2025-12-19 and have everyone gather there.

Because each member's cursor and writing are visible in real time, you can get an experience as if you're together. Of course, it's not as rich as physically gathering in an office, and it's not as rich as conventional virtual offices, but it still realizes the virtual gathering itself. That's why it's useful **when you want a shared, collective experience, but anything beyond a traditional virtual office would be too rich**.

Another useful use case is discussion. Instead of holding a meeting, create a page, have participants access it, and write comments during the meeting time. The facilitator prompts comments, and the decision-maker writes the final decision—it's a completely different experience from a conventional meeting, but it enables more flexible work and broader, deeper discussion. After all, you don't have to remember everyone's statements, and of course you don't have to stay glued to it.

In this way, you can gather virtually on a per-page basis.

Finally, I'll note a few important points:

- This kind of virtual-office-like usage is also possible with Cosense mentioned in the Wiki section. However, Cosense is a Japan-made wiki, and depending on the company it may be difficult to adopt. In contrast, Notes are likely already adopted in many organizations.
- Notes can also be used to store documents and knowledge, even to build an SSoT. However, the experience may be poor due to factors like "not being very lightweight" and "forcing structure and organization."

## Chat
- Slack
- Teams
- Discord

Chat refers to what is called business chat: channel-based chat tools like Slack, Teams, and Discord.

Unlike LINE or social media direct messages, chat can be structured by organizational units like workspaces and channels. This made it viable for business use, and because it's intuitive and convenient, it became the successor to email and instant messengers. First Slack became popular among engineers, then Discord succeeded in the gaming industry, then the pandemic came and Teams rose, and this genre spread explosively.

The real value of chat is **that it can send notifications**. Depending on settings, writing a mention can notify the other person. If a notification is sent, they'll notice. Traditionally you could just call out to someone directly; what this genre enables is doing the same thing remotely. Notification features exist in other QWINCS tools too, but nothing besides chat has become widespread enough for everyone to use. Chat is the de facto standard for communication tools today. Therefore, when it comes to a **universal way to send notifications remotely**, chat becomes the only option.

From the perspective of soft-skill development, notifications do nothing but disrupt focus. They're harmful. On the other hand, it's probably unrealistic to complete everything without notifications. So it's best to keep chat as a means of sending notifications. Leave it running, but basically don't use it. Check it when a notification arrives—keep it to that level.

In particular, for things you "want someone to look at right away" or "absolutely want them to see without forgetting," they may not notice if you only write them in a wiki, issue, or note. So you attach the URL and send it with a mention. Of course, subsequent back-and-forth happens there (not in chat). In other words, **use chat as a notification-sending device**. I call this approach Chat And Away.

## Sticky Boards
- Miro

Sticky Boards refers to digital whiteboards like Miro. I forced this term to make the word QWINCS work, and I apologize if it's confusing.

Whiteboarding was originally done with analog large sheets of paper and sticky notes, but technological advances made it possible digitally as well. The pioneer is clearly Miro, but other communication tools and platforms have started adding similar features. There's also a pattern where it's done as collaborative editing in diagramming tools like Canva or Figma. Also, the traditional "stick sticky notes" style has expanded to handling diverse information beyond sticky notes (to use a complicated term: objects). You can see examples like creating PowerPoint-level graphical materials, or using it as a venue for online events.

The real value of Sticky Boards is that they **can be used as a two-dimensional virtual office**. Notes are documents and one-dimensional in the vertical direction, but Sticky Boards are canvases and let you use a two-dimensional space (up/down/left/right). Also, Notes are document-like, whereas Sticky Boards let you place various kinds of content more freely.

Where to use them is the same as Notes, but because Sticky Boards have more dimensions, they make it easier to realize the concept of a **world**. The most straightforward example of a world is Minecraft, where various buildings are created from the initial spawn point. You must not destroy existing buildings without permission. It's basically the concept of land, and Sticky Boards make it easy to build a similar worldview.

As for the convenience of worlds, I'm actually not sure I fully understand it. If it were me, I'd think about whether I can get by with QWIN before using Sticky Boards. Soft-skill development is done linguistically, and Sticky Boards—which lean heavily visual—are over-spec'd. However, just as there are people called visual thinkers, Sticky Boards may fit some people precisely because they're Sticky Boards. That's why **if QWIN doesn't fit you, it's worth proactively trying Sticky Boards**.