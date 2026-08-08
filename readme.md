Hello! Welcome to my second full-length self-project. This one is called SupportTech.ai!

This is my own full-stack AI agent that simplifies techincal concepts, documentation, and papers down for anyone to be able to understand. I have a fully-functioning UI with a well-designed website that has a capable short term and long term memory (courtesy of postgresql). I utilize open-source model from huggingface that I can run and fine-tune on my Mac with its limited compute. I have implemented tools such as Tavily web search, a file reader, and RAG (ChromaDB). I use GPT 5.1 as my orchestrator model that determines what tool / process will be implemented.

I am in the middle of configuring Claude Sonnet 4-5 to be my evaluation model to check my outputs, and I will create a flywheel where the agent will be fine-tuned on the best of the evaluated responses. After I finalize my fine-tuning loop, I plan to adjust some of the underlying PyTorch to so that I can make fine-grained decisions and potentially create a routing classifier.

The primary reason I made this was because I wanted to be involved in as many parts of the AI training life-cycle as I possibly could. Aside from pre-training and some advanced fine-tuning techniques, I have accomplished this mission.

Note-to-self: Create video demonstration to put on GitHub once finished!
Note-to-self: Don't forget command D for being able to edit multiple words at once! (Command + Shift + L for all instances)

<br> <br> <br>

To-do:

    Backend:
        - Continue the fine-tuning evaluation flywheel!
        - Perform edge-case testing everywhere to check for bugs
        - Review LoRA/PEFT/Quantization in order for concepts to stick


    Frontend:
        - Brainstorm additional ideas for what I could later include on my site
        - Edit responses so that user input and agent output flows seamlessly like monkeytype (if possible)
        - Continue developing color themes as the site gets more populated and there are more things to color in

<br> <br> <br>

History on the project:

4/6: Initialized Project, sorted out GitHub repository issues, came up with initial project concept (tech support tool) and barebones stack (python fastapi backend, python for orchestration, javascript/css/html frontend), set up .env, .gitignore and uv, learned about and implemented a health check endpoint to see if the server is running, and set up barebones communication with the OpenAI API

4/7: Deliberated on the structure of my agent workflow and modified it to include a smaller model so that I can work with all stages of the AI training life cycle, researched how I would be able to implement rag within my workflow, decided upon my new, small model to do work with it however I can (Qwen2.5-3B-Instruct)

4/8: Extensively read up on and researched PEFT, LoRA and quantization, attempted the first run with the new code to run the barebones Qwen2-3B model but was left with some extremely slow processing, attempted a few more times with smaller models until I finally got it to run in a fast time with the 0.5B parameter model, tried again with larger models but did not get anything to work so I'm sticking with the 0.5B model for now

4/13: More closely analyzed the bare-bones code that is needed to get basic responses from my model, switched the device_map from CPU to MPS since I found out that my mac has small graphics processing units that can tackle larger models and upgraded back to the Qwen2.5-1.5B-Instruct model, reviewed a similar project to my own that performed QLoRA for fine-tuning and went over several of the coding decisions one-by-one so that each one made sense to me, reviewed and discovered more about libraries, classes and objects, learned about the dropout regularization technique

4/14: Initialized index.html file and set up a barebones site, set up a server extension that can make my server go live just by the click of a button, researched html basics to be even more familiar with it, started re-formatting project by putting files in relevant folders, decided upon the objectives that I will attempt to complete first on both the frontend and backend

4/15: Fixed up to-do list some more, updated structure further by adding more subfolders, initialized app.js and style.css files, initialized formatter, system, and tool prompt templates that will be utilized most easily using Path, briefly read up on read up on how to actually build and run an api server with various api endpoints using a router

4/16: Updated stack to include React instead of the basic html, css, and javascript files, began studying up on React so that I can easily design a complex user interface

4/21: Read further on how to build and run a complex api server with several routes, separated logic from main file into api_server and generate_response files, constructed first and main route (chat endpoint), added chat route as a usable route in the application

4/22: Set up react environment inside of my frontend folder, updated configurations by deleting and modifying some so that there would be no issues using both TypeScript and React together, went through much of a lengthy YouTube tutorial on all things React, installed bootstrap and prettify for extra css functionality and automatic code optimal restructuring respectively, learned some very useful shortcuts to make things easier (option shift click for copying code in between, command d, command shift l (puts cursor on next, all of the same words, respectively))

4/23: Finished the lengthy YouTube React tutorial and started honing in on some of the specific things you can make happen in React, learned about the major differences between JavaScript and TypeScript

4/26 + 4/27: Further React studying

4/28: Began attempting to connect the frontend and backend by adding middleware to the api server code to set appropriate permissions and to connect React on port 5173 to the fastapi backend in port 8000, initialized a react app that is set up to send basic requests to my model and then provide back the responses (although the requests are not going through at the current moment), got rid of unnecessary css code that came with the default react webpage design

5/3: Further looked into middleware to gain a deeper understanding of its purpose and how you can shape it to do what you need it to do, finished documenting some modifications to earlier code and massively updated the to-do list items

5/4: Set up HuggingFace (HF) token for higher rates and faster downloads, read up on the logistics for deploying projects such as this one to production with React and decided to not make the project public 24/7 due to the costs (I put my end-game plan near the top of this readme), established the connection between frontend and backend with a fully-working react site after updating faulty import logic across a few of the backend files and commenting out system prompt lines that I don't need quite yet, decided upon a purple/pink/white default color scheme and that users will be able to select from several different color themes when this is done, deleted unnecessary app and index css since I wanted to start from scratch, started setting up color palettes to switch from

5/5: Fixed theme-switching bug by controlling the theme at the root level instead of making it its own div element, tried out different layouts to display my color-theme toggle options, the input container, and the output response, determined that I want to have a label in the top right corner named color that, when hovered over, will show all of the buttons for the possible themes that can be chosen

5/6: Fixed more formatting mistakes by putting the color theme options in the top right corner, keeping the input container, submit button, and response at the bottom of the page, and limiting the size of the container so that it is not too overly wide, adjusted text-box size to be much smaller, spent time debugging the alignment of some of the items

5/7: Completely fixed alignment issue with the color theme toggle, added really cool hover feature that adds a gold shine and reveals the button themes that also hover with their own color schemes, created first system prompt where the main focus is providing concise answers with short analogies, debugged and then successfully added markdown to my responses so that lengthier responses are made to be more readable, rewrote the generate_response function to follow along with Qwen's chat template, adjusted file paths to resolve relative to script instead of hardcoding

5/11: Poured through several different AI service websites (Arc, Tines, Warp, Liveblock, Rasa) for AI implementation ideas on what consumers would want, website design ideas, and interesting smaller feature ideas that could make certain things easier, brainstormed some ideas for where I could take this project after completing the core components and decided upon this new path: Core agent + tools + RAG → data flywheel → fine-tuning loop → eval pipeline, decided upon the first tools I want to implement (web search, code interpreter, file reader), began looking into web search implementation

5/12: Went back over the new direction for the project and started implementing a new file structure for the backend to incorporate additional new logic files such as, the gpt orchestator file and responder file where Qwen gets fed a system prompt depending on if tools were used or not, the first tool file (web search), log/data files, and eval files, went over a possible orchestration solution and looked closely at how it would be implemented

5/13: Studied up further on the transformer architecture, constructed the web_search.py file where I would conduct a web search using the Tavily API, set up the list of tools that GPT would scour before it would decide which tool should be called and added the defining characteristics of a web_search, learned more about how orchestrators operate for agents such as my own, removed some redundant code in my generate_response.py file

5/14: Updated GitHub and my file explorer with the name of the project instead of the project placeholder

5/17: Debugged faulty virtual environment when the project stopped loading after I updated the name of the project, where I created a new venv with the same dependencies after force installing uvicorn and cleared the cache so shell was able to find the new location for uvicorn

5/18: Added first version of newly-designed submit button and input-text box, started experimenting with unique ways for the messages to populate the screen and implemented the first version of messages coming in via colored water bubbles, finished implementing the first version of the orchestrate.py file which will have gpt be able to pick which tool, if any, should be used, implemented the full first version of the responder.py file that will give qwen the additional tool data needed to answer a question as well as a system prompt for qwen to look over and decide upon an answer given user input

5/19: Fixed up some calling logic so that my files called orchestrate and responder correctly instead of the generate_response file, added web_search logic inside of the chat endpoint so that web search can actually be implemented, spent time debugging the chat endpoint because web search was not correctly being called, spent time debugging the bubble creation and trying to determine why the bubbles were being created only occasionally on the assistant side and not at all for the user side

5/20: Tested to see if web search was working by re-wording a descriptor field to allow to web search much more often and prompting it with real-time data such as the weather and recent sports questions, finished debugging the chat endpoint by realizing that I didn't even import my function into the chat endpoint file originally, spent further time debugging the bubbles and was able to get the assistant bubble to appear consistently but way too low, corrected the app.tsx code to get the bubbles to float to the correct spots and sometimes create the user bubble, but bubble consistency is still a problem

5/21: Spent time trying to diagnose which background process from my code was causing my computer to overheat, was not able to find the singular cause but I do know the process was running for over a day and it was resolved by force quitting the process (which may have been 2 different processes according to task manager) and restarting my computer

5/22: Updated the max size for Tavily search requests so that Qwen is not overloaded with too much information to process

5/25: FINALLY fixed the bubble formatting issues after much debugging and got them to align perfectly on both sides without extending too far out, begun constructing file reading tool that will take in all sorts of files, including pdfs, and even tables from those pdfs because some of the files that I would be reading from would be things like research papers, upgraded the max size for Tavily search requests again since I ran into another not-enough-context situation

5/26: Learned a bit more about the two main file_reading libraries and decided to go with pdfplumber, wrote the file reading function to read in files with a file path hardcoded since I would likely be reading the files in from the same place

5/27: Changed my mind and altered the file reading function to require a file path argument since it would add flexibility as to what files across a computer you can read, created 5 different handler functions to handle each type of file that could be read in (pdf, md, txt, py, and json), merged the md/txt/py handlers together since their logic was the exact same, added the file reading tool to the chat endpoint so that it could be used

5/28: Went back over React basics to see how much better I understood the underlying concepts and structure, spent a while testing the different file types and attempting to debug my plaintext handler that seems to only output json when it encounters it in files that are not json files, updated the augmented questions to give to Qwen for additional context for each question so that each tool gets a different question (which will likely be key to helping solve this issue)

6/2: Continued debugging the file_handler to see if it could still handle files with mixed file types but decided to put this problem away potentially for another day, finished testing the other file types and was able to read everything in including straight json files, added several more file types that Qwen will be able to parse and elaborate on, did research on several new tools I could build next before rag and memory and decided on a system info / log parser tool

6/3: Implemented and tested log_parser file from start to finish by adding the tool to the orchestrator file, letting the tool be called if gpt says it should be used in the chat endpoint, augmenting the message with context about how to use the log_parser tool in the responder file, and testing to see if sending log contents before a query, after a query, and without a query works

6/4: Debugged log parser tool until I found the place in chat endpoint file where I made the wrong function call at the very end and then fixed the syntax so that
Qwen would actually take the added context queries into account when answering the question, read up on the final three large backend tasks that I want to have done (memory, RAG, fine-tuning/evaluation flywheel), began constructing the memory

6/5: Read up further on memory construction and relevant documentation, created a few different iterations of an add_to_history, get_history, get_trimmed_history, and del_history, set up short-term-memory by adding in conversation_id and injected it inside the orchestrate function for gpt and the response function for qwen, set up conversation ids in react in a way that one generates when the page is refreshed and the component remounts

6/8: Corrected the function calls that were not calling the functions by the exact names, updated delete-conversation logic to make sure I'm only deleting the conversation and not deleting a conditional statement, moved the conv_id tsx variable inside of the app because it is a hook that uses useState and must be inside a component, added assistant messages to history since I forgot to add them before, lowered the number of messages held in short term memory to 3-4 (3 for gpt, 4 for qwen) to take up less overall RAM, tested short-term memory with a few different examples and had success with them all other than qwen remembering a number I told it to remember, began the process of pivoting over from handling a qwen2.5:1.5b model with huggingface transformers to the Ollama application where I can quantize my model and efficiently run the 3b parameter model

6/9: Freed up memory on computer, fixed a faulty Ollama installation by installing Ollama directly instead of by using homebrew, cleaned up zshell run commands and added /usr/local/bin permanently to the path to act as a shortcut map, tested functionality to see how much more the 3b parameter model could take compared to the 1.5b model

6/10: Resolved some recurring path issues with the integrated terminal so that uv and ollama are always findable without export commands, read up on constructing RAG, decided that I would go with chromadb and a mini sentence-transformer embedding model to implement rag that would chunk my own code documents (research papers and other documentation later, most likely), decided upon postgresql as my long-term memory query language, began implementing rag by adding an additional ingest.py and embeddings folder and wrote some of the bare-bones code that will be needed to start making my rag system work

6/11: Learned more about the basics of the full process of RAG, finished constructing the ingest file where I have functions that chunk text, read in a file, and then read in all the files, constructed the rag file that does the actual retrieving of the relevant chunks after everything was already ingested, started looking into how I would alter my orchestrate file to have rag occur without issue

6/12: Added the retrieval function from rag.py to the orchestrator file, decided upon having rag trigger every single time due to simplicity of implementation and that I don't need to massively scale to the point where it'd be a problem, added chunks to the augmented message in orchestrator to add context, added debugging lines and tested to see why rag wasn't initially working (the files weren't pointing to the correct embedding path), added additional debugging statements to see which chunks were being output and some additional metadata about them (0 were being output, made the silly mistake of forgetting to ingest the files)

6/15: Wrote code to upsert all of the rag files' chunks whenever I call for it, upgraded the embedding model from all-MiniLM to all-mpnet-base to bge-large for higher retrieval quality, added filename prepending so that qwen knows what chunks are associated with which file, increased top_k from 3-5 for a wider chunk retrieval net, added a distance similarity threshold to filter out irrelevant chunks and debugging lines to show me this information whenever I provide a query to my UI, added a GPT system prompt (renamed the old tool prompt to orchestrator_prompt and used that) to provide more speicifcations about how to identify which tool to use if any, fixed file_reader so that it only will run if the user specifies a full file path in their query, installed postgresql and psycopg2-binary to help with implementing long-term memory, ran a temporary instance of postgres on my computer successfully to test to see if it would connect

6/16: Initialized db.py to connect to postgres and exposes functions for manipulating data, established a connection pipeline and a server for the pipeline connecting the postgres database to python, defined save-conversation and save-message functions inside db.py, created a conversations, messages, and evaluation table to store long-term memory and evaluation data

6/29: Finished get_conversation_history and save_evaluation functions, added error handling to the postgresql connection, adjusted columns/constraints/keys within the psql tables, updated memory file by calling the db functions into the memory file so that memory and db storage can be updated together, created conversation title generation logic

7/1: Finished setting up title generation logic by adding it to the beginning of the logic in the orchestrator function, fixed library import logic to maintain consistency across files, initialized conversations endpoint file

7/2: Fixed the inconsistent bubble animation due to correcting a bug that involved the bubbles starting to move at a negative time, added to the conversations endpoint file the three different endpoints that can get conversation title names, get the messages from within a conversation, and delete a message from both in memory and in the postgresql database, linked the psql storage to my UI by adding the conversations endpoint file router to my app in api_server so now my messages/conversations are now written/saved to a database, added/updated delete logic to the db and memory files, updated psql constraints so that a deleted conversation has a clean cascade that deletes every child associated with it

7/3: Added button that displays all of the titles of conversations had, tested with different ways that conversations could be listed and the buttons to move when they were clicked on, added a new-chat button to start a new chat if needed, tested to ensure that it was possible to append to previous conversations

7/5: Decided on the structure for my fine-tuning/evaluation flywheel and that the evaluation would happen asynchronously, wrote the first version of the evaluation prompt that states the context for what Claude Sonnet (the evaluation model) will use to come up with a score, provides the json structure for the response the model will provide (a score field and a feedback field), and explains how the score will be computed, started writing the evaluator.py file that will call claude and generate an evaluation response

7/8: Put asyncio logic inside of chat.py where the evaluator function runs asynchronously while the main event loop happens when triggered by a user query, began constructing evaluator function, set up the user content containing info on the query, qwen's response, and whether or not a tool/rag was used, return the parsed output that will get logged into the evaluations table in psql, implemented error handling within the evaluation (malformed claude output) and outside the evaluation (parsing, network timeout, etc. error)

7/10: Designed AI evaluation system where the scoring system (1-5) would be determined from only the Qwen response (nothing to do with RAG or tool responses) and run asynchronously immediately after the qwen response is returned, wrote and refined the AI-feedback fine-tuning system prompt, update evaluation function to include both evaluating a qwen response and logging the response inside the evaluations postgres table, corrected more faulty import styles across my codebase

7/14: Initialized and finished first version of the dataset_builder.py file that will construct a high-scores-only dataset of a jsonl structure with each line having only an instruction and a response for qwen to fine-tune on, denormalized evaluation table by including columns user message and the qwen response so that there wouldn't need to be extra joining and unnecessary complexity, updated the save_evaluation function in logger and db to pass the user message and qwen response to the postgres table

8/5: Publicized project, updated project description to be more up-to-date, adjusted some to-do list items

8/7: Fixed lots of dependency issues and syntax errors that came from testing out the evaluation logic and logging all of that into my evaluations table, updated both the qwen_system and claude evaluation prompts repeatedly so that qwen produced the types of responses that I wanted and that claude could accurately grade based on what qwen was assigned to do

FRONTEND MISSION: Make it stylish! Add some background textures and tools that I haven't used before and really make this new interface pop out more than my
previous agent. Also, move bubble logic into different files and different folders so the app.tsx file is not cluttered

BACKEND MISSION: Figure out if you're keeping step 0 in the system_prompt file. The additional statement is occasionally being added, but seemingly at the cost of markdown. I'd like to include both, but if all else fails, the basics including markdown works in the previous commit that I have where I only include steps 1-6
