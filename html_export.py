import shutil
import traceback
from sparx_lib import logger
from sparx_lib import open_repository
import argparse
import yaml

config_file = open("config.yaml","r")
config = yaml.load(config_file, Loader=yaml.FullLoader)
config_file.close()

#print(config)
#exit(1)

parser = argparse.ArgumentParser(description='Rebuild eaWeb')
parser.add_argument('models', metavar='Model', type=str, nargs='+', help='model name, "all" means - all models', default="Sprint 1.4")

args = parser.parse_args()

logger.debug("arg models: "+str(args.models))
if args.models[0]=="all":
    export_tasks = config["models"]
else:
    export_tasks=[]
    for element in config["models"]:
        if element.get("model") in args.models:
            export_tasks.append(element)

logger.debug("export_tasks: "+str(export_tasks))
#logger.debug("args: " + args)
#logger.debug("export_tasks: " + export_tasks)

try:
    # shutil.copy(SOURCE_MODEL, MODEL_PATH)
    # eaRep = open_repository(MODEL_PATH)
    eaRep = open_repository(config["repository"], config["login"], config["password"])
    logger.debug("eap opened")
    models = eaRep.Models

    # model search begin
    # look like stupid way for find specific Model, but couldn't find other solution right now
    for element in export_tasks:
        GUID = ""
        logger.debug("model: "+element["model"])

        for i in range(0,models.Count):
            if models.getAt(i).Name == element["model"]:
                GUID = models.getAt(i).PackageGUID
        if GUID == "":
            raise Exception("Couldn't find model")
        # /model search end

        # sync
        # RootPackage = eaRep.GetPackageByGuid(GUID)
        # recursivePackageSVNUpdate(RootPackage, 0)
        # logger.debug("updated from svn")
        eaRep.GetProjectInterface().RunHTMLReport(PackageGUID=GUID,
                            ExportPath=element["path"], ImageFormat='PNG', Style='t-magic', Extension='.html')
        logger.debug("html report created")

except Exception as err:
    traceback.print_exc()
    logger.exception("eaRep fails")

#RunHTMLReport
#def RunHTMLReport(self, PackageGUID=defaultNamedNotOptArg, ExportPath=defaultNamedNotOptArg,
#                  ImageFormat=defaultNamedNotOptArg, Style=defaultNamedNotOptArg
#                  , Extension=defaultNamedNotOptArg):

try:
    eaRep.Exit()
except:
    pass
