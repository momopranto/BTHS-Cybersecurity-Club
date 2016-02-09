#Let's Git Going: An Overview of Git and Github

This week's presentation can be found [here](https://goo.gl/kb6TPA).

You should all already have a vague idea of what Github is and does, since you're using it right now!  This week we covered the basics of Github, the advantages of using it, and how to work it from the command line with git.
##What is Github?
Github can be thought of as Google Drive for code, with a few extra features.  It allows users to upload their code to allow other users to view it, edit it, or make their own modifications on it, all while keeping track of past edits.
##Who uses Github? Why?
Github can be thought of as a social network for code.  It's mainly used by software developers to host their code, collaborate on team projects, and to receive feedback on their work.  Github recently added a feature allowing users to upload 3D files, so some mechanical engineers have started adding AutoCAD files and the like on Github as well.  Some writers will use it to write up books and manuscripts, although this isn't as common, and some teachers will use the site to host educational resources- like this repo for this club!
##Repositories
Github hosts *Git* repositories on the web.  Respositories, or repos, can be thought of as folders.  A repo is essentially a strage unit for a project that allows you to track versions of your files.
##Basic Git Workflow- on recording changes
Taken from git-scm.com:
> You have a bona fide Git repository and a checkout or working copy of the files for that project. You need to make some changes and commit snapshots of those changes into your repository each time the project reaches a state you want to record.

>Remember that each file in your working directory can be in one of two states: tracked or untracked. Tracked files are files that were in the last snapshot; they can be unmodified, modified, or staged. Untracked files are everything else – any files in your working directory that were not in your last snapshot and are not in your staging area. When you first clone a repository, all of your files will be tracked and unmodified because you just checked them out and haven’t edited anything.

>As you edit files, Git sees them as modified, because you’ve changed them since your last commit. You stage these modified files and then commit all your staged changes, and the cycle repeats.

>![alt tag](https://git-scm.com/book/en/v2/book/02-git-basics/images/lifecycle.png)

##A bit of Git
A quick rundown of a few basic terminal commands:
 - ```git init```: creates a new repository
 - ```git pull```: syncs the local repo with the latest version of the remote repo
 - ```git status```: shows which files have been modified (what needs to be commited to the repo to update it)
 - ```git add [file]```: snapshot a file in preparation to commmit
 - ```git commit [file]```: records a version of a file permanently to repo
 - ```git push``` uploads all commits in local repo to remote repo; updates all files
 - ```git clone [url]```: downloads a repo and all of its version history; you can modify someone else's project by cloning and working off the clone
