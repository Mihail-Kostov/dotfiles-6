=========
Workflow
=========
Find simple workflows for productivity, efficiency, and collaboration.

Concept
========
::

   The morning question,  |  5 | Rise, wash, and address *Powerful Goodness*;
   What good shall I do   |  6 | contrive day's business and take the
   this day?              |  7 | resolution of the day; prosecute the present
                          |    | study; and breakfast.
                          |  8 -
                          |  9 | Work.
                          | 10 |
                          | 11 |
                          | 12 -
                          |  1 | Read or overlook my accounts, and dine. 
                          |  2 -
                          |  3 | Work.
                          |  4 |
                          |  5 |
                          |  6 -
                          |  7 | Put things in their places, supper, music,
                          |  8 | or diversion, or conversation;
    Evening question,     |  9 | examination of the day.
    What good have I done | 10 -
    today?                | 11 |
                          | 12 |
                          |  1 | Sleep.
                          |  2 |
                          |  3 |
                          |  4 |

   -- Benjamin Franklin


Goals
=======
* Document personal workflow
* Develop methods to retain and analyze relevant information
* Develop heuristics to identify tasks and sub-tasks  


Objectives
-----------
* Create workflow.rst
* Document existing labelling strategies
* Analyze and merge existing labelling strategies
* Define and describe inputs: tasks
* Define and describe resources: skills, time, tools
* Define and describe outputs: artifacts, products, deliverables
* Develop integrated workflow information flows

  * Tasks, Lists, Labels, Services, Tools (pyrtm-task-cli, pytodo?)
  * Logs: workhours, heka, elasticsearch, kibana



Tasks
======

Daily
------
* Daily Google Tasks list

  * Daily: Uncheck list box(es), update date


Scheduled
----------
* Google Calendar events (and reminders)


Recurring
-----------
* Repeating Google Calendar events (and reminders)
* Repeating ReadTheMilk tasks


Phone 
-------
* While you were out stickies
* `Email Labels`_: ``.p``


Emails
-------
* `Email Labels`_: ``.tasks``, ``.tasks.done``


Text Files
------------
* TODO, TODO.rst, TODO.md, TODO.html
* CHANGES, CHANGELOG, HISTORY, HISTORY.txt, HISTORY.rst
* README, README.md, README.rst  

Text File Attributes
~~~~~~~~~~~~~~~~~~~~~~
* Absolute local file path  
* Byte-order-marker
* File extension  
* Line endings (DOS, UNIX)  
* Shebang line
* Creation time  
* Modification time
* Local undo/backup cache
* Lightweight Markup Headings (h0 -> title)
* ReStructuredText Bibliographic Fields:
  ``:Author:`` <name>,  ``:Title:`` <title>


Code
-----
* Repository `Text Files`_
* Comment tags: TODO, FIXME, XXX

.. code-block:: sh

   hg grep 'TODO|FIXME|XXX'
   git grep 'TODO|FIXME|XXX'

Code Attributes
~~~~~~~~~~~~~~~~
* Absolute local file path
* Shebang line
* File extension
* Relative repository path
* Repository name
* Repository remote URL(s)
* Repository file history log
* Repository file history log across renames
* Local undo/backup cache  


Issues
--------
A finite request, report, or work item.

Also referred to as tickets, issues, or cards.

Issue attributes
~~~~~~~~~~~~~~~~~

* a title
* a description
* comments
* metadata

  * GitHub

    * title
    * body
    * user
    * assignee
    * state:

      * open
      * closed

    * milestone (configurable)
    * labels: (configurable)
  
      * bug
      * duplicate
      * enhancement
      * help wanted
      * invalid
      * question
      * wontfix


  * BitBucket

    * title (Title)
    * content (Description)
    * reported_by
    * assignee
    * follower_count
    * status:

      * new
      * open
      * resolved
      * on hold
      * invalid
      * duplicate
      * wontfix

    * kind:
      
      * bug
      * enhancement
      * proposal
      * task

    * priority:
      
      * trivial
      * minor
      * major
      * critical
      * blocker

    * component (configurable)
    * milestone (configurable)
    * version (configurable)

  * Google Code (configurable templates)

    * Summary
    * Description
    * Reporter
    * Attachments
    * Status: (configurable)
      
      * Open: (configurable)

        * New
        * Accepted
        * Started
        * MoreINFOneeded
        * NeedsTesting
        * Completed
        * PassedTesting

      * Closed: (configurable)

        * Fixed
        * Verified
        * Invalid
        * Duplicate
        * WontFix
        * Done

    * Owner
    * Cc
    * Labels: (configurable)
      
         * OpSys-*
         * Milestone-Release*
         * Component-*
         * Security
         * Performance
         * Usability
         * Maintainability

  * Trac

    * Component



Patches
---------
Also referred to as a diff.

When an author has modified a file in a repository,
there is a difference (in terms of text lines and/or bytes changed) 
between their local revision and
the repository revision they started with.
That's called a 'diff' or a 'patch'.

To share those changes, an author must submit a patch to
a repository maintainer, who is responsible for applying
or not applying the changes to a branch of a repository.

The patch review feedback cycle -- classically over NNTP or SMTP (email) --
can produce lots of text: both revisions to the patch and an
asynchronous stream of emails and IRC messages.

Patch attributes
~~~~~~~~~~~~~~~~~

* Header (first n chars of first line)
* Header
* Body (made of hunks)  


Patch Workflow
~~~~~~~~~~~~~~~
* Send patch(es) as an email attachment ("a patch bomb")

  * TST,BLD,CLN: code and test an ENHancement or fix a BUG
  * DOC: write  
  * DOC: prepend Code Labels to first line of patch header (commit message)
  * DOC: write a commit message
  * (.sent, .code) Open Loop: wait for feedback (add email label)
  * (pending) respond, revise, respond (add email labels) 
  * (pending) correlate manual line references in feedback emails with
    the correct revision of the patch
  * (pending|accepted|rejected) review constructive feedback
  * (closed,done) Reach 'done'; update TODO system

* Receive patch(es) as an email attachment

  * (.unread) Open Loop: they're waiting for feedback
  * (.read) read, review, revise, respond: email, editor
  * (.tested) Test: run existing or documentation tests
  * (pending) Respond: [Email] Feedback
  * (pending|accepted|rejected) Evauluate: Apply or do not apply
  * (accepted) Update release log (Desire Code Labels)  
  * (released) Release: issue a version identifier with merged patch  
  * (closed,done) Reach 'done'; update TODO system  


Pull Requests
--------------
Projects hosted with GitHub and BitBucket generally support accepting,
reviewing, and merging changes as pull requests; which, like
regular patches people used to send over the email,
are hunks of differences between one or more files.

Unlike a patch archived in a mailing list,
pull requests have
a free-form comment stream
and line-based commenting
-- features which simplify the change review and evaluation feedback loop.


Pull Request Workflow
~~~~~~~~~~~~~~~~~~~~~~~
* Send a Pull Request

  * Branch/fork, update, commit
  * Compare, test (review diff)
  * DOC: Prepend Code Labels to first line of patch header (commit message)
  * Send a pull request

    * (.sent, .code) Email: Send a URL to the branch to pull from
    * (.code) GitHub: Click 'Send Pull Request'
    * (.code) BitBucket: Click 'Send Pull Request'  

  * (.code) Open Loop: wait for feedback
  
* Review a Pull Request

  * Open Loop: they're waiting for feedback
  * Check whether the tests pass with the pull request applied
  * Read, Review, Test*, Respond
  * Apply or do not apply  
  * Update release log (Desire Code Labels)



Lists
======

Mental
-------
* Mnemonics
* String around one's finger
* Note on one's hand  
* Cognitive representation (mental picture) of a list
* Graph with edges that have magnitude

Mental List Attributes
~~~~~~~~~~~~~~~~~~~~~~~
Context:

* Date
* Location
* Project  


Paper
------

Pros
~~~~~
* Classic, ubiquitous
* Visual  
* Battery-free  
  
Cons
~~~~~
* Backup / collaboration strategy
* Correlating list status
* Keeping track of WHEN things were added/update/*renamed*/completed 
* Assigning and sorting by priority  

Implementations
~~~~~~~~~~~~~~~~~
Schedule
   : Chronological sequence of events
   
Calendar
   : Visual grid of day, week, month, quarter, year

   Weekly views: ``M-Su``, ``Su-Sa``

Agenda
   : Action items to accomplish within a given context
   
To-do List
   : List of items to accomplish,
   visually designating completion
   by ``[x]`` checkmarks,
   strikethrough (crossing things off)

Hipster PDA
   : Pocket-sized notebook sheet of paper

   https://bitbucket.org/westurner/pyrtm-task-cli/src/tip/simp.py


Text
-----
Typed plaintext.  Usually with some form of lightweight markup for
lists, nested lists, bold, italic, [underline, strikethrough].

Stored with:

* Paper
* Filesystem
* VCS Repository (git, hg)  

Pros
~~~~~
* Simple
* Great with a keyboard, syntax highlighting, and syntax checking  

Cons
~~~~~
* Synchronicity: keeping everyone on the same revision of the page
* Mobile Interface: no
* Picking a syntax (try pandoc while deciding)
* Lightweight markup language syntax learning curve  

Syntax
~~~~~~~
ReStructuredText, Markdown, [MediaWiki, BBCode, Textile]::

   * one
   * two
   * three

   - red
   - green
   - blue

ReStructuredText::

   * [x] one **bold**
   * [ ] two *italic*
   
     * [x] two.one
     - [ ] two.two \* two

   * [ ] ``three``

Markdown::

   * [x] one **bold** 
   * [ ] two *italic*
     * [x] two.one
     * [ ] two.two \* two
   * [ ] ``three`` (also `three`)


Labels
=======

Task Labels
---------------

-next
   : a next action

-waiting
   : a task that is blocked

-someday
   : an opportunity for a later date

random
   : a note to self

.d
   : degree catchall

.d.<course>
   : degree course

.bills
   : bills

.p.<project>
   : project

.career
   : career

.civic
   : civic

o.<orgname>
   : organization

health
   : health

.healthy
   : health

.ride
   : vehicle

@home
   : when at home

@campus
   : when at school

@class
   : when in class

@work
   : when at work

@team
   : <TODO>

@phone
   : when at the phone

@pc
   : when at a computer

@online
   : when at a computer with internet access

@email
   : when checking email

@forum
   : when reading forums

@reading
   : when having time for reading

@errands
   : when running errands

@grocery
   : when in a grocery

@list
   : general shopping list


Task Labels
------------


Email Labels
-------------
.tasks

.tasks.daily

.tasks.done

l.
   : mailing lists

d.
   : degree

p.
   : people

wd.
   : web development


Code Labels
------------
Tests, Documentation, Enhancements, Bugs, Builds, Merges

Comma-delimited, CASE-insensitive prefix-labelling::

   TST: <desc>

   DOC,ENH: <desc>
   BUG,TST: <desc>

   # ... BLD, MERGE


Project Labels
----------------
dotfiles
   :

dotvim
   :

provis
   :

workhours
   :

menuapp
   :

pyrpo
   :

pyline
   :

self-directed-learning
   : 

   Research:

   * Report
   * Presentation

   Development:

   * STEM Labs

career
   :

skills
   :

networking
   :

paycheck
   :

health
   :

diet
   :

exercise
   :

relax
   :







Services
==========
Web applications and web services
https://en.wikipedia.org/wiki/List_of_collaborative_software

Systems designed to track task state for one or more people
moving toward achieving objectives that satisfy the goals.


Service Evaluation Criteria
----------------------------------
There is a spectrum between
"we'll remember which checkboxes for you"
and "this task is part of a project
supported by these people
in these roles
with these permissions."

* Web Interface: yes/link/no/date
* Mobile Interface: yes/link/no/date
* iOS App: yes/link/no/date
* Android App: yes/link/no/date  
* BlackBerry App: yes/link/no/date
* WinMo App: yes/link/no/date
* API: yes/link/no
* XML: yes/link/no  
* JSON: yes/link/no
* Sharing/Internal: yes/link/no
* Sharing/External: yes/link/no  
* Integrates with Google Calendar: yes/link/no
* Integrates with Gmail: yes/link/no
* Integrates with Twitter: yes/link/no
* Integrates with Evernote: yes/link/no
* Integrates with Github: yes/link/no
* Cost/Free: yes/link/no
* Cost/Paid: yes/link/no
* Reminders/Pop-up: yes/link/no
* Reminders/Email: yes/link/no


Google Calendar
-----------------
* Web Interface: https://google.com/calendar/
* Mobile Interface: https://www.google.com/calendar/m
* iOS App: yes
* Android App: yes
* BlackBerry App: no (EOL 2012)
* API: https://developers.google.com/google-apps/calendar/
* JSON: yes  
* XML: yes  


RememberTheMilk
------------------
* Web Interface: https://www.rememberthemilk.com/
* Mobile Interface: 
* iOS App: yes
* Android App: yes
* BlackBerry App: yes  
* API: https://www.rememberthemilk.com/services/api/
* XML: yes
* JSON: yes
* Integrates with Google Calendar: yes
* Integrates with Gmail: yes
* Integrates with Twitter: yes
* Integrates with Evernote: yes  


Google Tasks
-------------
* Integrates with Google Calendar: https://www.google.com/calendar/
* Web Interface: https://www.gmail.com/mail/help/tasks/
* Mobile Interface: http://gmail.com/tasks
* API: https://developers.google.com/google-apps/tasks/
* JSON: yes  



Google Keep
------------
* Checkbox sticky notes
* Web Interface: https://drive.google.com/keep/  
* Mobile Interface: yes
* API: no
* Sharing/Internal: no  
* Sharing/External: no  



Wikis
-----
Roadmaps, Outlines

* GitHub Wiki
* BitBucket Wiki  
* Trac Wiki
* MediaWiki  


Mailing Lists
--------------
Email relay application server

* Mailman: listserv e-mail relay server with archive
* Google Groups: https://groups.google.com/

`<https://en.wikipedia.org/wiki/Electronic_mailing_list>`_


Forge Sites
-------------
Code Repository + Mailing List / Forums + Wikis + Downloads + Issue Tracking

`<https://en.wikipedia.org/wiki/Forge_(software)>`_

`<https://en.wikipedia.org/wiki/Comparison_of_open-source_software_hosting_facilities>`_


Github Repos, Issues, Wikis
-----------------------------
* Free public GitHub repositories
* Web Interface: https://github.com/
* Mobile Interface: https://mobile.github.com/
* API: https://developer.github.com/v3/
* API note: most recent 1000 events
* XML: no
* JSON: yes

GitHub renders the first README {.md, .rst, .txt, } it finds.

GitHub ReStructuredText does not support Sphinx ReStructuredText.

Workflow
~~~~~~~~~
Ways to work with tasks and GitHub:

* Store a README, HISTORY, ROADMAP, TODO, etc. file in a repo {.md, .rst, .txt}
  ::
  
     1. [ ] mkdir tasks && cd tasks
     2. [ ] git init
     3. [ ] echo "Tasks list" >> README.md  
     4. [ ] git add README.md
     5. [ ] git diff README.md  
     6. [ ] git commit
     7. [ ] git remote add origin ssh://git@github.com/<username>/<reponame>  
     8. [ ] git push origin master

  * Learn to git pull, diff, patch, merge, stash, push, and send pull requests
    (with a terminal interface)

    * `hub <http://hub.github.com/>`_ --
      a wrapper script for git that can be aliased with ``alias git=hub``
    * `gitflow <https://github.com/nvie/gitflow>`_ --
      adds ``git flow <command>``
      `branching workflow <https://datasift.github.io/gitflow/IntroducingGitFlow.html>`_
      automation commands.
    * `hubflow <https://github.com/datasift/gitflow>`_ --
      adds ``git hf <command>``
      branching workflow automation commands by extending gitflow.

  
* Create a GitHub Issue with a title and a description (Markdown) {.md}
  ::

     1. [ ] Open the GitHub url in the browser
     2. [ ] Click 'Issues'
     3. [ ] Click 'New Issue'

  * Per-objective
  * Collaborators add labels, a milestone, and an assignee to the issue
  * Link to issues with ``#123`` in commit messages, issues, and wikis
  * Close the issue when it is done or not going to be done

    * Close a GitHub issue with the web interface 'Close' button
    * Close a GitHub issue with text in a **commit message** or **pull
      request description**::
      
         ENH: add new feature (closes: #01 #02)
         BUG: fix bug (fixes: #03)    

      See: `Closing issues via commit messages <https://help.github.com/articles/closing-issues-via-commit-messages>`_


* Create a GitHub Issue with a GitHub Markdown Task List (Markdown) {.md}::

   - [x] one --bold-- 
   - [ ] two -italic-
     - [x] two.one
     - [ ] two.two \- two
   - [ ] ``three`` (also `three`)

  * Check off each checkbox to complete the issue
  * Add list items with checkboxes (``- [x] Task three``)   

* Create a GitHub Wiki page w/ title and text (Markdown) {.md}

  * Create a Roadmap page with a sprint/release plan of issue number/links

* Publish Task Reports into a repository as HTML served by GitHub Pages

  * Create a Sphinx ReStructuredText ``conf.py``
  * Render the ReStructuredText into HTML with ``sphinx-build -b html``
  * Host ``_build/html`` in the ``gh-pages`` branch

    * e.g. with `<https://github.com/davisp/ghp-import>`_

  * Consider building and hosting Sphinx ReStructuredText documentation
    with `ReadTheDocs <https://readthedocs.org/>`_


BitBucket Repos, Issues, Wikis
---------------------------------
* Free public and private hg and git repositories
* Web Interface: https://bitbucket.org/
* Mobile Interface: Third Party
* Integration with Jira: Yes
* Integration with Crucible: yes

Workflow
~~~~~~~~~~
* Store a README, HISTORY, ROADMAP, TODO, etc. file in a repo {.md, .rst, .txt}
  ::
  
     1. [ ] mkdir tasks && cd tasks
     2. [ ] hg init
     3. [ ] echo "Tasks list" >> README.md  
     4. [ ] hg add README.md
     5. [ ] hg diff README.md  
     6. [ ] hg commit
     7. [ ] Add "bb = ssh://hg@bitbucket.org/${USERNAME}/${REPONAME}" to ``[paths]`` in ./.hgrc
     8. [ ] hg push bb

  * Learn to hg pull, diff, patch, merge, shelve, push, and send pull requests
    (with a terminal interface)

    * `mq <http://mercurial.selenic.com/wiki/MqExtension>`_ --
      a mercurial extension for working with Mercurial Patch Queues
    * `tortoisehg <http://tortoisehg.bitbucket.org/>`_ --
      an excellent VCS gui for Mercurial (and git, with hg-git)

  
* Create a BitBucket Issue with a title and a description (Markdown) {.md}
  ::

     1. [ ] Open the BitBucket url in the browser
     2. [ ] Click 'Issues'
     3. [ ] Click 'Create Issue'

  * Per-objective
  * Apply kind and priority values to the issue with the web interface
  * Collaborators assign an issue to a user  
  * Link to issues with ``#123`` in commit messages, issues, and wikis
  * Close the issue when it is done or not going to be done

    * Close a BitBucket issue with the 'Resolve' button
    * Close a BitBucket issue with text in a patch header 
      (a **commit message** or **pull request description**)::
      
         ENH: add new feature (closes: #01 #02)
         BUG: fix bug (fixes: #03)

      See: `Resolve issues automatically when users push code <https://confluence.atlassian.com/display/BITBUCKET/Resolve+issues+automatically+when+users+push+code>`_


* Create a GitHub Issue with a GitHub Markdown Task List (Markdown) {.md}::

   - [x] one --bold-- 
   - [ ] two -italic-
     - [x] two.one
     - [ ] two.two \- two
   - [ ] ``three`` (also `three`)

  * Check off each checkbox to complete the issue
  * Add list items with checkboxes (``- [x] Task three``)   

* Create a GitHub Wiki page with a title and text (Markdown) {.md}

  * Create a Roadmap page with a sprint/release plan with
    headings and issue number/links

* Publish Task Reports into a repository as HTML served by GitHub Pages

  * Create a Sphinx ReStructuredText project folder with a ``conf.py``

    * e.g. with `<https://github.com/audreyr/cookiecutter-pypackage>`_

  * Render ReStructuredText into HTML with ``sphinx-build -b html``
  * Host ``_build/html`` in the ``gh-pages`` branch

    * e.g. with `<https://github.com/davisp/ghp-import>`_

  * Consider building and hosting Sphinx ReStructuredText documentation
    with `ReadTheDocs <https://readthedocs.org/>`_

Trac
-----

Redmine
--------

GitLab
-------



Tools
=======

pyrtm-task-cli
---------------
A python CLI for working with tasks and pyrtm RememberTheMilk API.

Query/rename tasks in Python and generate a printable, minimal HTML
Hipster PDA from a template.

workhours
----------
Aggregate streams of event tuples generated by various activity streams
(bookmarks, existing browser history, ``.usrlog`` files)


TaskWarrior
-------------
TaskWarrior is a task management tool written in C with lots of plugins
written in other languages.

TaskWarrior comes with an awesome commandline interface for adding,
updating, and reporting on tasks, their statuses, and their priorities.

There are plugins to host and synchronize TaskWarrior task databases.


