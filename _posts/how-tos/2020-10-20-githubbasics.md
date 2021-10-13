---
layout: post
author: elliott
categories:
 - how-to
 - exercise
inclass: true
title: Github basics
published: true
---

# Can I Get A Volunteer?

We're going to help Tommy the Tester create his first post.

* Create Github account
* Go to [{{ site.github_repo_url }}]({{ site.github_repo_url }})
* Click 'Create New File'
* This new file will become your post.  Give it the filename `_posts/<username>/2020-08-26-first-post-<username>.md` **Remember the importance of careful typing**
* Add this to the top of the file's text content:

```
---
layout: post
author: <yourgithubname>
title: "Yourname's first post!"
---
```

**Remember, every character matters to a computer.**

* Then, underneath that header, write a bit about yourself.
* Write a commit message in the first text box under the "Commit New File" heading at the bottom of the github page describing what you did, like "Added Tommy's first post".  You can leave the second text input box there blank.
* Look good? Create Pull Request.  Or edit again if something's wrong.
* Your commit will now show up on your Pull Request and automated tests will begin to run.
* :+1: :sunglasses: :fire:


# Automated Tests

We use Travis-CI to automatically run tests on code.  When you submit a pull request, you'll see something like this:
![]({{ site.baseurl }}/img/travis1.png)

Behind the scenes it's building a whole new server and running various tests to make sure your code won't break the site.  You'll want to make sure your code passes these tests, after which you'll see a shiny green check mark next to your pull request.  The test status is also visible in the list of pull requests:

![]({{ site.baseurl }}/img/travis2.png)

If your build fails, don't panic!  It happens to the best of us.  Click 'Details' and see if you can figure out what went wrong.

Also, remember that passing tests is a minimum standard.  It doesn't mean that your code is perfect, so make sure to read over your code carefully.

{% comment %}
# Video on Creating and Updating Posts

This video walks through creating and updating a new post as well as updating a post that's already been merged.  It also goes over some of the basics of branches.

<iframe src="https://player.vimeo.com/video/151900462" width="500" height="375" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

Hope it helps!

{% endcomment %}