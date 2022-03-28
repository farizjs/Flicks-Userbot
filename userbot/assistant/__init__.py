""" Init file which loads all of the assistant modules """
from userbot import LOGS


def __list_asst_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    asst_modules = [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return asst_modules


ASST_MODULES = sorted(__list_asst_modules())
LOGS.info("Assistant to load: %s", str(ASST_MODULES))
__asst__ = ASST_MODULES + ["ASST_MODULES"]
