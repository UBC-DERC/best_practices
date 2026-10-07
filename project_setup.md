# Project Setup

Here is a placeholder for some of the things you'll want to know about setting up your project further.

## best-practices

You now have a project, here's a quick TODO list of things you can work on:

* [ ] Edit the README file:
    * [ ] Add additional funding information
    * [ ] Add a little bit more information to the project description.
    * [ ] Add a section called "Deliverables"
* [ ] **Keep secrets hidden!**
    * [ ] Create a [`.env` file](https://www.dotenv.org/docs/security/env.html) and make sure it's added to your `.gitignore` file (if you are using `git`)
    * [ ] Use a package like `dotenv` for python and `dotenv` in R to load the secrets (passwords, API keys, etc) into your programs.
* [ ] Try using `uv run main.py` to make sure things work.
* [ ] Try running `uv run pytest` to make sure your (simple) tests are working.