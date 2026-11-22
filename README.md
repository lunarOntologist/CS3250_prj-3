# Overview

The goal of this assignment is to give you a final opportunity to apply key software engineering practices covered throughout the semester, including project management, teamwork, version control, design, coding best practices, object-oriented principles, and quality assurance. 

# Instructions

You and your team of 3 to 5 members have the freedom to choose what to implement for this project, provided you meet the requirements outlined in this section. 

The first requirement is that the software must be a web application with a Python-based backend that supports user registration and authentication. The project must include at least six user stories. Each user story must include acceptance criteria, an estimated business value, a story point estimate, and a priority score derived from business value and dependencies.

Additionally, you are required to use Scrum as your development methodology, completing at least two sprints during the project. All Scrum ceremonies must be documented using the provided templates and saved in the scrum/ folder. At a minimum, teams must document sprint planning meetings, daily scrums, sprint reviews, and sprint retrospectives.

Each team must create a separate public GitHub repository under the [msu-denver](https://github.com/msu-denver/) organization. Add all team members and the instructor as collaborators to ensure proper access. The project's repository must maintain two long-lived branches:

* **main**: for the stable releases and
* **dev**: for ongoing development. 

To preserve code quality, the **main** branch must be protected and require at least one peer review and approval before pull requests can be merged. This workflow promotes stability, accountability, and best practices in version control.

```
Share the URL of your project's GitHub repository here.
```

The repository should have, at a minimum, the following structure:

```
README.md
Dockerfile
docker-compose.yml (if using a multi-layer architecture)
requirements.txt
src/
tests/
uml/
scrum/
htmlcov/
```

Feel free to add other folders and files as needed. 

Use the provided [README_TEMPLATE.md](README_TEMPLATE.md) as the basis for the repository’s **README.md** file.

The repository README must include a mission statement, a use case diagram, a sequence diagram, and a class diagram representing the project's model classes.

All source code must include a consistent header comment with a brief description and the author(s). It should comply with the PEP 8 style standard and will be reviewed for best practices, including proper commenting, meaningful naming, clean formatting, effective function decomposition, adherence to object-oriented principles, robust error handling, and other quality guidelines.

Provide at least one clearly identified white-box test and one clearly identified black-box test. Describe the purpose of each test, the functionality being tested, and the outcome. Neither test may target user registration or authentication features. Additionally, generate a **test coverage** report under **htmlcov** using Python’s coverage tool to show how much of the code is exercised by your tests.

The final product must be deployed using Docker containerization technology and include all project dependencies frozen in a **requirements.txt** file. Teams seeking the bonus points should implement persistent storage using a database other than SQLite and follow a minimum three-layer architecture (presentation, business logic, and data access). Such projects must be deployed with Docker Compose using at least two containers.

A final progress report must be submitted. The report should include sprint summaries, completed and incomplete user stories, lessons learned, and a burndown chart. An image generated from the burndown chart must be displayed in the repository README.

# Self and Team Evaluation 

Students must complete a self-evaluation and evaluate their team members using [this](TBD) form. This is a mandatory requirement, and the team’s grade will be placed on hold until all members have submitted their evaluations.

# Rubric

✅ Documentation (35 points)

```
+5 Project README: Mission statement
+5 Project README: Use case diagram
+5 Project README: Sequence diagram
+10 Project README: User stories
+5 Project README: Class diagram for model classes
+5 Project README: Test coverage report using Python’s coverage
```

✅ Repository & Process (30 points)

```
+5 GitHub repository organization, branches, and main branch protection
+10 Scrum notes
+15 Team/self evaluation
```

✅ Implementation & Quality (25 points)

```
+10 Implementation of required user stories
+5 Code inspection: PEP8 compliance
+5 Code inspection: Comments, naming, functions, formatting, OOP best practices, error handling
+5 Project deployment
```

✅ Testing (10 points)

```
+10 Testing requirements
```

Total: 100 points

✅ Bonus (5 points)

```
+5 Deployment using Docker Compose and multi-layer architecture
+1 Each optional user story implemented (max 5 points)
```

❌ Penalties

```
-10 User creation not available/working
-10 User authentication not available/working
-5 For each user story not completed (up to 25 points deduction)
-5 Little or no evidence of continuous development on the main branch
-5 Little or no evidence of continuous development on the dev branch
-5 No burndown chart was created
```

# User Stories

Describe the **user stories** for the project, which are short, simple descriptions of a feature told from the perspective of the end user. Each **user story** should include clear **acceptance criteria** and a **point estimate**. The **user stories** must align with the **use case diagram** and should be labeled as US#1, US#2, and so on. 

Use the following template when writing your **user stories**. 

```
As a [type of user], I want to [perform some task] so that I can [achieve some goal].

Acceptance Criteria

Given that [context],
When [action],
Then [expected outcome].
```

US1: As a user, I want to login, so that I can have everything I do be tracked via my account. 
Given that I have inputted my login info, when I press login, then I should be on the home page.

US2: As a user, I want to create events, so that other people can view them. 
Given I have filled out all required fields, when I click post, the event should be saved to a database. 

US3: As a user, I want to view all events on the calendar, so I can stay up-to date. 
Given that I have opened the view events page, I should see all events others have created, as well as my own.

US4: As a user, I want to RSVP to events, to let the owner know what to plan for. 
Given I have opened the RSVP page under an event, when I fill it out, that information should be saved to the post for the owner to see. 

US5: As an event owner, I want to edit my own events, so I may correct typos or show changes in plans. 
Given I have opened the editing page, when I fill out the form, the new information should be saved. 

US6: As a user who has RSVPd to an event, I want to suggest changes to the event. Given I open the editing page, when I fill out the form, my suggested changes should be saved for the owner to look at.

US7 (optional): As an event owner, I want to approve or deny suggestions so that the event is automatically updated. 
Given I have approved a change, when I click confirm, the event should be edited to match the change. 

US8: (Optional) As an event owner, I want to view all current RSVPs on my own events, but not other people's.

US9: (optional) As An event owner, I want to view all past RSVP statuses in a separate menu than the current statuses.

# Product Backlog

The backlog should have all user stories, including the ones that are optional. Assign a user value to each story using the following scale:

3 = High value
2 = Medium value
1 = Low value

Describe dependencies between user stories using their IDs (for example, US3 depends on US1). Fill out the table below. 

| ID | Rank | User value | Story Points | Priority Score | Depends on | Type 
| --- | --- | --- | --- | --- | --- | --- |
| US1 | 1 | 3 | 5 | - | None | Required |
| US2 | 2 | 3 | 3 | - | US1 | Required |
| US3 | 3 | 3 | 3 | - | US2 | Required |
| US4 | 4 | 2 | 5 | - | US3 | Required |
| US5 | 5 | 2 | 2 | - | US2-3 | Required |
| US6 | 6 | 1 | 2 | - | US3-5 | Required |
| US7 | 7 | 1 | 5 | - | US6 | Optional |