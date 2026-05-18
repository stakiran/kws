# Block Writing
Block writing is a method of building up various blocks (chunks of text).

Below, I'll introduce in one go the foundational knowledge you need to practice block writing. After you finish reading, you should be ready to start block writing.

## Examples of blocks
For example, in Markdown you can represent it as "1 heading = 1 block" like this:

```
# Block 1
...

# Block 2
...

# Block 3
...
```

In Cosense, you can also treat chunks separated by blank lines as blocks.

```
Block 1
 This is Block 1
  This is Block 1
 This is Block 1
 This is Block 1

Block 2

 Block 3
 This is Block 3
This is Block 3

Block 4
 This is Block 4
This is Block 4
 This is Block 4
 This is Block 4
This is Block 4
```

I don't use it, but you can also place blocks on a two-dimensional canvas like Miro or OneNote.

## Keep blocks within a single page / single file
In any case, blocks should fit within a single unit. For example, **represent them within a single page or a single file**. Even if you had 50 blocks and each block were 1,000 characters, you'd end up with 50,000 characters in total, but you should still keep it as one unit. It's easier to scan the blocks that way. Switching pages or files becomes noise, even if it takes only 0.1 seconds.

In block writing, by scanning the blocks you get the next ideas. Concretely, you make decisions such as creating a block to cover a missing perspective, or creating a wrap-up block because things are starting to come into focus. You must eliminate noise as much as possible. You could say the goal is to make movement between blocks seamless. The more seamless, the better.

Note that how seamless this feels depends on the writing tool. Whether it's a local text editor, a local IDE, a SaaS note app or wiki, or a SaaS IDE, local is more seamless, and text editors are more seamless. There are still plenty of users who stick with Vim or Emacs, or on Windows, users like me who use Hidemaru Editor—and these people understand how important seamlessness is.

In block writing, you especially want to move quickly between blocks. In Markdown terms, it's particularly useful if you can **jump between headings with a single shortcut key**. This level of interaction isn't widely recognized, and if you want it, you need to make use of editor extensions and advanced settings.

## Run the cycle
Next, block writing uses the creative-thinking process of "diverge → converge → distill." Specifically, you create divergent blocks, and while scanning them you create convergent blocks. You go back and forth—creating these two types, breaking them, creating them again—and eventually, when it feels like things are "about to come into view," you finish by creating a distilling block (a summary block) to bring things to a pause. Completing this one pass is called a **cycle**. You can run the cycle n times, but when you start the (n+1)th cycle, you begin from the summary block of the nth cycle.

In other words, in block writing you proceed while continuously producing summaries. Once your conclusion and actions are decided and you judge that it can't be improved further, you can stop there. Sometimes one cycle is enough; sometimes you'll do more than ten. Do your best effort depending on the situation. I call this way of working **summary-driven**.

When submitting something, it's better to create a separate document from the final summary. A text written as-is in block writing probably won't be acceptable as a deliverable. However, among internal members it may still work—and it should, ideally. The trail of blocks is like source code: it contains all decisions and their context. **Blocks also function as a shared language.** In particular, each block has a specific role (described later), so it's easy to read. Of course, just as source code can be clean, blocks can be clean too—but if it's something your future self can read and continue stacking onto, it will likely make sense to others as well.

## Types of blocks
Finally, let's cover the types of blocks.

First, understand that there are these three types:

- Divergent blocks
- Convergent blocks
- Distilling blocks

As a rough guideline, you might create about 10 divergent blocks, 1 to 3 convergent blocks, and 1 distilling block. First, write a bunch of divergent blocks to lay out information. Then, while scanning them, do light organization and structuring—of course not in your head, but reflected as convergent blocks. After repeating this for a while, the big picture and concrete actions start to emerge, so you express them as a distilling block. Or even if nothing is emerging, you can still provisionally put down a hypothesis. That's one full cycle.

You can come up with more granular block types yourself, but I'll introduce some convenient ones backed by my extensive experience. You could call them **block patterns**, analogous to design patterns. You don't have to accept them blindly, but if you can't create your own yet, I recommend following them first.

## Block patterns
In block patterns, a block is composed of a "letter," a "title," and a "body." For example, in a consideration block, the letter is k, the title is the theme you want to consider, and in the body you scribble down what you thought about that theme.

There are two ways to arrange blocks: "top to bottom" and "bottom to top." Usually you'll do "top to bottom," but if you always start from the latest, you'll have to scroll all the way down every time. If you want to eliminate that effort, try to stick to "bottom to top," though this way of thinking may feel unfamiliar until you get used to it.

There are also two targets for ordering: "cycles" and "blocks." Let's look at cycles first. The following uses `===` as separators and lays out three cycles. There are numbers next to the separators, which shows they're arranged "bottom to top." In other words, the 3rd cycle is written at the top.

```
# === 3

# Block

# Block

# Block

# === 2

# Block

# Block

# === 1

# Block

# Block
```

Next, let's look at blocks. The following shows three blocks. Whether they are top-to-bottom or bottom-to-top can't be determined from this alone—and usually it doesn't need to be.

```
# === 3

# Block

# Block

# Block
```

As stated, in block writing you scan blocks and ultimately derive a summary. You can just line up the blocks however you like. Of course, if you're meticulous, you may find it easier to arrange them strictly in order.

Now that we've covered components and ordering, let's get to the main point.

The following are **divergent blocks**.

```
# k (put your theme here)
Consideration block. k stands for Kento.
State a theme and write what you thought about it.
Because it's divergent, it's fine if it's not well organized.

# b
Brainstorm block. b stands for Brain-storming.
Without even setting a theme, write down anything that vaguely comes to mind.

# r
Reference block. r stands for Reference.
List paths to reference information such as book titles, URLs, or file paths.
It's recommended to list only the paths, but you may add brief notes.
Because it's just a link collection, don't let the notes bloat. If it bloats, it becomes harder to use later.
```

Basically, you dump what's in your head with brainstorm blocks, dig into specific topics as needed with consideration blocks, and capture external information and other context you must keep in mind with reference blocks.

As you do that, concrete parts start to come into view, so you summarize them using convergent blocks. The following are **convergent blocks**.

```
# a (you may or may not write a theme)
Action block. a stands for Action.
Write specific "to-dos" as bullet points.
You don't have to write a theme, but you can.

# d
Direction block. d stands for Direction.
Write what you've come to see regarding directionality, such as strategy or policy.
It's good if you can cover both directions you should take and directions you should not take.

# c
Concept block. c stands for Concept.
This is different from the notion of "concept" in SSE; here it means "something that should be defined as a term."
If it already exists as a technical term or internal term, write it.
If it doesn't, give it a name and put it into words. You may coin a new term.
In any case, always write the name and definition.

# cx
Context block. cx stands for Context.
Write, concisely, the context you must capture in this writing.
Background, assumptions, current situation, and other constraints you can't ignore.
```

In other words, as you brainstorm and consider, concrete actions, directions, concepts, and context gradually become visible. You capture them properly by writing them as blocks. Having them only in your head doesn't mean you understand them; only when you actually put them into language and write them do they become real. You could say block writing **implements thinking** by writing blocks. Just thinking in your head is armchair theory, or the equivalent of being a commentator. You have to write and implement.

As you go back and forth between divergence and convergence, conclusions gradually become visible—or you reach a point where you must cut it off. You then write the result as a distilling block. The following are **distilling blocks**.

```
# s
Summary block. s stands for Summary.
Write the conclusion concisely.
An executive summary of the big picture, the decisions you made (or want to make) this time, and a short-term task list, etc.

# ====
Separator line.
Used to separate cycles.
For readability, ease of typing, and consistency, anything is fine—===, ---, etc.
```