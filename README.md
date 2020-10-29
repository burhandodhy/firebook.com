# firebook.com
The real innards of firebook.com code base.


When submitting a pull request to Project, we ask that you squash your commits before we merge.

Some applications that interact with git repos will provide a user interface for squashing. Refer to your application's document for more information.

If you're familiar with Terminal, you can do the following:

* Make sure your branch is up to date with the master branch.
* Run `git rebase -i master`.
* You should see a list of commits, each commit starting with the word "pick".
* Make sure the first commit says "pick" and change the rest from "pick" to "squash".
-- This will squash each commit into the previous commit, which will continue until every commit is squashed into the first commit.
* Save and close the editor.
* It will give you the opportunity to change the commit message. 
* Save and close the editor again.
* Then you have to force push the final, squashed commit: `git push --f origin <branch name>`.

Squashing commits can be a tricky process but once you figure it out, it's really helpful and keeps our repo concise and clean.
