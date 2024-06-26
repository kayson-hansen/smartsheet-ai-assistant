# smartsheet-ai-assistant

smartersheet. the ai assistant that can automate all of your annoyingly
difficult smartsheet tasks.

smartersheet is a chrome extension that adds an ai copilot to your smartsheet,
supercharging the productivity of project managers. think of it like stack
overflow, but more often correct, more relevant, and more convenient.

ask it to sort a column, to write a formula (yes, you can already do this in
smartsheet, but might as well do it here too, right?), to merge columns, to
delete rows, to update data, to set automations, to create reports, and anything
in between.

# setup

1. create an anthropic account, get credits, get api key

2. with your smartsheet organizational account, generate an api key

3. run `sh setup.sh` to set environment variables and create a .env file with
   those variables

4. change directory to backend/, then run `poetry install` to install
   dependencies

5. run `poetry run langchain serve --port=8100` to run the backend server

6. change directory to frontend, then run
   `yarn run webpack --entry ./content-script.js --config webpack.config.js` to
   run the frontend server
