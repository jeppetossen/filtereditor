from os import path
import glob
import importlib
import warnings

# Find all the model names to be imported
modules = glob.glob(path.join(path.dirname(__file__), "*.py"))
names = [path.splitext(path.basename(n))[0] for n in modules]
names = [n for n in names if n != "__init__"]

# Determine the app name assuming appname/models/*.py structure
app = path.basename(path.abspath(path.join(__file__, '..', '..')))

# Import each, assuming that e.g. Mymodel lives in models/mymodel.py
for name in names:
    mpath = "%s.models.%s" % (app, name)
    mo = importlib.import_module(mpath)
    clsname = name.capitalize()
    try:
        globals()[clsname] = mo.__dict__[clsname]
    except KeyError:
        # warnings.warn("No class named %s in %s.py" % (clsname, name))
        warnings.warn(f"No class named {clsname} in {name}.py")
