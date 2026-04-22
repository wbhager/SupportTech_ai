Hello! Welcome to my second full-length self-project. This one is called SupportTech.ai!

I want to create my own AI agent that provides me with only the very best technical knowledge whenever I have questions. I plan to have a fully-functioning UI with a well-designed website that can remember previous questions you had. I want to be involved in every step of the AI training process, even fine-tuning if my hardware allows for it. I will utilize a small (~7B should work fine, hopefully), open-source model from huggingface where I can perform every step of the AI training life cycle, from pre-training to evaluation output. I will use both GPT 5.1 and Claude Sonnet 4-5 as evaluation tools to check my outputs. I will also implement PyTorch in some way, since I want to get familiar with how it works since it is the backbone of the transformer architecture.

<br> <br> <br>

To-do:
    Backend:
        - Set up API server and API endpoints
        - Create first system prompt and system prompt and apply them to user prompts
        - Determine what tools I would like to implement (RAG, etc.)
        - Create tool system prompt and implement the first tool
        - Review LoRA/PEFT/Quantization in order for concepts to stick
        - Gather some data for the model to be trained on, review it, and note down the link to it somewhere



    Frontend:
        - Determine what my frontend stack will be
        - Do basic research on each of the languages I will be implementing on the frontend to better learn the languages
        - Create basic chat interface where users can type in a message and they get a relevant response back
        - Edit responses so that user input and agent output flows seamlessly like monkeytype (if possible)
        - Implement new sections on your HTML site with new tags you haven't used before
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






