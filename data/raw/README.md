# Raw Data

Files you inport and transform for your analysis should be placed into this folder. You may choose not to publish them to GitHub (if you are using GitHub for project management). If you don't want your raw files sent to GitHub, uncomment the appropriate line in your [`.gitignore`](../../.gitignore) file.

## Handling Big Data

This project is set up for integration with `git` and GitHub in general. Because of this, users must be aware of file size.  `git` stores copies of your individual files and any subsequent changes. It is best suited to plain-text documents like code or markdown.

Large binary files (videos, zip files, sound files) are not well managed using `git`. If you are including these kinds of files in your project, or working directly with them in you `data/raw` folder (or exporting them from your `data/output` folder), make sure you add them to your `.gitignore` file.

For example, if you are working with a number of `mp4` files in your `data/raw` folder:

```
data/raw
|- observations.csv
|- file1.mp4
|- file2.mp4
\- file3.mp4
```

We could edit our `.gitignore` file to include the following entry:

```
data/raw/*.mp4
```

Which would include all files with an `mp4` extension (video files) in your `data/raw` folder. If you think you might have video files elsewhere, you can simply add `*.mp4` to the `.gitignore` file, which would ignore those video files any where in your repository.

