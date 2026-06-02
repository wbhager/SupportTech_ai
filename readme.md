Hello! Welcome to my second full-length self-project. This one is called SupportTech.ai!

I want to create my own AI agent that provides me with only the very best technical knowledge whenever I have questions. I plan to have a fully-functioning UI with a well-designed website that can remember previous questions you had. I want to be involved with every step of the AI life cycle apart from pre-training, which does not make as much sense to implement for this project. I will utilize a small, open-source model from huggingface that I can run and fine-tune on my computer with its current compute. I will incorporate tools such as web search, file reader, and RAG (LangChain). I will use GPT 5.1 as my orchestrator that will determine what tool / process will be implemented, and Claude Sonnet 4-5 as my evaluation agent to check my outputs, and I will create a flywheel where the agent will be fine-tuned on these evaluated responses. PyTorch is the engine underneath the fine-tuning, and after I create my fine-tuning loop, I plan to adjust some PyTorch to make some very fine-grained decisions and potentially create a routing classifier with some PyTorch after that.

When my project is finished, I want to make it so that I can run it whenever I want on my own computer, and I will have a video demonstration of how my agent works on GitHub because it costs money monthly renting computer power remotely for other people to use my agent.

Don't forget command D for being able to edit multiple words at once! (Command + Shift + L for all instances)

<br> <br> <br>

To-do:

    Backend:
        - Implement system info / log parser!
        - Implement RAG (LangChain) (truncate or chunk large files first)!
        - Implement memory!
        - Review LoRA/PEFT/Quantization in order for concepts to stick
        - Begin the fine-tuning evaluation flywheel!

    Frontend:
        - Continue the TechWithTim React tutorial to get a different perspective on beginning in React
        - Fix the occaionally-spawning bubbles situation and make them always spawn
        - Brainstorm ideas for what I want my interface to look like
        - Start implementing the early ideas for my interface design, I can always add to it/change it later
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

FRONTEND MISSION: Make it stylish! Add some background textures and tools that I haven't used before and really make this new interface pop out more than my
previous agent. Also, fix the bubbles so that it works for the user side! Also, move bubble logic into different files and different folders so the app.tsx file is not cluttered

BACKEND MISSION: Implement system info/log parser!
