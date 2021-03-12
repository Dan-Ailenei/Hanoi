
# Sprint

We use a standard process for taking a feature from a PR to its release in
production.


## Workflow

We take an SCRUM approach to our sprints, and we have the following schedule:

Event             | Monday | Tuesday | Wednesday | Thursday | Friday | ... | Monday | Tuesday | Wednesday | Thursday | Friday | ...
-------------------------------------------------------------------------------------------------------------------------------------
Grooming          |    x   |         |     x     |           |        |     |        |         |           |          |        |
Planning (What)   |        |         |           |     x     |        |     |        |         |           |          |        |
Planning (How)    |        |         |           |     x     |        |     |        |         |           |          |        |
Sprint Review     |        |         |           |     x     |        |     |        |         |           |          |        |
Sprint Retro      |        |         |           |     x     |        |     |        |         |           |          |        |


## Jira tickets

Swimlanes:

* __ToDo__: All the tasks that are scheduled for a sprint start here

* __In Progress__: When work is started on one of the tickets, the developer
assigns the ticket to themselves and then moves the ticket from _ToDo_ in
_In Progress_.

* __Review__: After the work for the task is done, the task is moved, by the
assignee, in the swimlane Review, meaning that peers can now review the work.

* __Acceptance Testing__: A ticket is moved over to this column after the code
has been verified, approved and deployed in a test environment. When a
ticket is in this swimlane, it means that the testers can now find the features
related to the ticket in the test environment. The ticket is moved in this
column by the person that deploys the feature to the environment.

* __Done__: A ticket reaches this swimlaine when the work abides by the
_definition of done_, which is: the work associated with the ticket has been
reviewed, tested and deemed acceptable by testers and it is safe to be deployed
on a production environment.

