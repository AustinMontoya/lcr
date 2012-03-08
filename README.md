# Learning Content Repository

The Learning Content Repository, or LCR, is a research prototype being conducted by the Advanced Distributed Learning initiative to promote re-use of learning resources through a flexible, fast repository framework. It is still in the very early stages of development, but the long-term goal is to provide a federated network of repositories that can selectively store and share learning content among each other, all while providing a simple user interface for each network endpoint.


### Supported Platforms

- Windows XP/Vista/7/Server 2008
- Most Linux distros
- OS X

### Prerequisites

The application uses the following software in its development stack, which must be installed prior to installing the LCR:

- Python (2.6 or later) -- http://python.org/getit/
- virtualenv/pip -- http://www.pip-installer.org/en/latest/installing.html
- MongoDB -- http://www.mongodb.org/downloads

Instructions vary by platform; you should be able to figure it out from the above links without much difficulty. It may be obvious since we are hosting this on Github, but we also recommend installing the git version control system as well.

# Installation

We highly recommend that you already are familiar with using a terminal or command prompt prior to installing the project. 

1. Make sure you have the above software installed and running. The default configuration for each is fine.
1. Create a virtualenv for the project and activate it:
    - On Linux, OS X:
    
    ```bash
    virtualenv ~/lcr
    . ~/lcr/bin/activate
    ```
    - On Windows (from Command Prompt):
    
    ```cmd
    virtualenv \Users\<your_username>\lcr
    \Users\<your_username>\lcr\Scripts\activate.bat
    ```
1. Clone the repo (alternatively, you can download a tarball or zipped copy). Windows git users may wish to perform this step in a separate Git Bash window instead of the command prompt:

    ```bash
    git clone https://github.com/armontoya/lcr.git
    ```

1. Change directories into the repository you just cloned and install the dependencies:

    ```bash
    cd /path/to/cloned/repo
    pip install -r requirements.txt
    ```
1. Start the server:

    ```bash
    python runserver.py
    ```
    
You're done! That wasn't so hard, was it?


