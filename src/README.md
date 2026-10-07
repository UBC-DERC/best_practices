# The `src` Folder

It's often good practice to try to keep our `root` folder empty, except for the critical project management and description files we want to use.

These files will include our README, the LICENSE file, and, more than likely, one key script that controls our workflow. To keep our code clean (and to help with testing), we would then put functions and other scripts into a `src` or source folder.

This way, your whole workflow should run if someone copies your repository and just runs:

```bash
python main_script.py
```

And those other files would call to functions or scripts in your `src` folder.
