# lab4, var4, yaml –> xml
import xmlplain
with open("schedule.yaml") as inf:
    root = xmlplain.obj_from_yaml(inf)
with open("resFile.xml", 'w') as outf:
    xmlplain.xml_from_obj(root, outf, pretty=True)