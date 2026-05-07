Hello! Welcome to my second full-length self-project. This one is called SupportTech.ai!

I want to create my own AI agent that provides me with only the very best technical knowledge whenever I have questions. I plan to have a fully-functioning UI with a well-designed website that can remember previous questions you had. I want to be involved in every step of the AI training process, even fine-tuning if my hardware allows for it. I will utilize a small, open-source model from huggingface where I can perform every step of the AI training life cycle, from pre-training to evaluation output. I will use both GPT 5.1 and Claude Sonnet 4-5 as evaluation tools to check my outputs. I will also implement PyTorch in some way, since I want to get familiar with how it works since it is the backbone of the transformer architecture.

When my project is finished, I want to make it so that I can run it whenever I want on my own computer, and I will have a video demonstration of how my agent works on GitHub because it costs money monthly renting computer power remotely for other people to use my agent.

Don't forget command D for being able to edit multiple words at once! (Command + Shift + L for all instances)

<br> <br> <br>

To-do:

    Backend:
        - Debug the basic message request to the Qwen model that will allow my frontend and backend to finally be connected
        - Create first system prompt and system prompt and apply them to user prompts
        - Determine what tools I would like to implement (RAG, etc.)
        - Create tool system prompt and implement the first tool
        - Review LoRA/PEFT/Quantization in order for concepts to stick
        - Gather some data for the model to be trained on, review it, and note down the link to it somewhere

    Frontend:
        - Watch the TechWithTim React tutorial to get a different perspective on beginning in React
        - Brainstorm ideas for what I want my interface to look like
        - Start implementing the early ideas for my interface design, I can always add to it/change it later
        - Edit responses so that user input and agent output flows seamlessly like monkeytype (if possible)
        - Start implementing a color scheme that can slowly be added to as the site starts to come along

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

5/7: Completely fixed alignment issue with the color theme toggle,

MISSION: Create the first version of the system prompt that the model can utilize, implement hover-with-hidden-buttons design and up the number of color themes! Make the text box grow as you start adding stuff to it, and have some sort of cool color-switch or mini-animation when you start typing stuff in!
