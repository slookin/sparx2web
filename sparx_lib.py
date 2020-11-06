import win32com.client
import logging

logger_mapping = logging.getLogger("mapping")
logger_mapping.setLevel(logging.INFO)
fh = logging.FileHandler('mapping.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger_mapping.addHandler(fh)
logger_mapping.addHandler(ch)

logger_revision_mapping = logging.getLogger("rev_mapping")
logger_revision_mapping .setLevel(logging.INFO)
fh = logging.FileHandler('mapping.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger_revision_mapping.addHandler(fh)
logger_revision_mapping.addHandler(ch)

logger = logging.getLogger("html_report")
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('html_report.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)


def open_repository(path, login, password):
    eaApp = win32com.client.Dispatch("EA.App")
    logger.debug("eaApp type: " + str(eaApp))
    eaRep = eaApp.Repository
    if login:
        eaRep.SuppressSecurityDialog = True
        eaRep.OpenFile2(path, login, password)
    else:
        #eaRep.ChangeLoginUser(login,password)
        eaRep.OpenFile(path)
    return eaRep

def single_search(eaRep, term, search_type):
    search_res = eaRep.GetElementsByQuery(search_type, term)
    if search_res.Count == 1:
        element = search_res.GetAt(0)
    else:
        logger.warning("term: "+term+" not found or found multipletimes")
        raise ValueError("term: "+term+" not found or found multipletimes")
    return element



# def recursivePackageSVNUpdate(pkg, level):
#    logger.debug(str("  "*level)+" "+pkg.Name)
#    if pkg.IsVersionControlled:
#        pkg.VersionControlGetLatest(ForceImport=False)
#    for p in pkg.Packages:
#        recursivePackageSVNUpdate(p, level+1)
