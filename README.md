# Thank you for your interest in the BarRaider Knowledgebase

***Note:** This is the knowledgebase source code. If you're looking for the knowledgebase website visit https://cyberlightdev.github.io/barraider-kb.*

## Contributing
You, yes you, can contribute fixes and add content to the BarRaider Knowledgebase.  If you are experienced with Git and Github, feel free to fork the repository and submit a pull request with your contributions.  Otherwise, head over to the [Bar Raiders Discord](http://discord.barraider.com) to provide your feedback.  Please understand that this may take longer, as someone else will need to understand, and then implement, your changes.

**Trusted Contributors**
Trusted Contributors and BarRaider Moderators are invited to submit changes without approval.  If you are given this access, you may accept your own Pull Requests. Please do not commit unfinished work to `main` as this will be immediatley deployed to the KB.  

### Local Installation
Git and [Python 3](https://www.python.org/downloads/windows/) are the only prerequisites for local development.  Once they have been installed...

1. `git clone` your fork (using the Green "Code" btton) to create a local copy of the site.
2. Open the command prompt (Windows), navigate to the location you cloned the project to.
3. Run command `pip install mkdocs-material mkdocs-glightbox mkdocs-video`. If you receive an error that Pip is not recognized, close and re-open the command prompt and try again
4. Start a local development server by running the command `mkdocs serve`.  By default, this will build and run the website at `http://localhost:8000/` on your machine.

### Auto-Reload (Local Install Only)
The development server will constantly listen for changes to either `mkdocs.yml` or anything in the `docs/` folder until stopped.  If you notice that auto-reload has failed or the local server will not load a page, check for errors in the command prompt.  If there is an error (or if you edit `base.yml`) you will need to run the serve command again to restart it.

### Editing On GitHub
For smaller edits such as typos and adding a single line, you are able to edit the files directly in GitHub.  Either way, the `main` branch has automatic options within GitHub, so you will still need to be working in a Fork (or a separate branch of the main repo, if you have access).

We encourage larger edits be made using the local installation method because of the integrated development server.

## Working On The Content
Most of the content is written in standard Markdown, but we have added a few helpful packages on top of that.

### Admonition
[Admonition](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#usage) provides integrated call outs in our pages in a Markdown-like syntax.

Example:
```markdown
!!! info "Did you turn it on?"

    **Note:** OBS must be open for most of these features to work!
```
Will look like...
![Admonition Example](docs/img/admonition-example.jpg)

### Embedding Youtube Videos
We have a special variant of an image to display an embeded Youtube video.  

```markdown
![type:video](https://www.youtube.com/embed/7mioa-hnndw)
```
will show an embeded version of: https://www.youtube.com/watch?v=7mioa-hnndw

*Note that the `watch?v=` must be changed to `embed/` for this to work.*

### HTML in Markdown:
To account for a few missing elements in Markdown, certain HTML tags are permitted directly in the Markdown.  The following code adds the first image from [OBS Tools > Getting Started](https://cyberlightdev.github.io/barraider-kb/obs-tools/getting-started/)

```markdown
<figure markdown>
![Step 1](img/gs1.png)
    <figcaption>
        Check that your settings match the settings in this image. <br /><strong>Set your own password.</strong>
        </figcaption>
    </figure>
```
**Note:** The syntax for the HTML is a bit problematic, as the indentation seems to matter more than it should.  If you use this feature, please be sure that your images display correctly **in the local installation** before submitting a Pull Request.