#Example TypeDecl node, with IdentifierType child node, represented as a dict:
#     "type": {
#         "_nodetype": "TypeDecl",
#         "coord": "c_files/funky.c:8",
#         "declname": "o",
#         "quals": [],
#         "type": {
#             "_nodetype": "IdentifierType",
#             "coord": "c_files/funky.c:8",
#             "names": [
#                 "char"
#             ]
#         }
#     }

class NodePerso(): 
    def __init__(self, nodetype, coord, declname, quals, type): 
        self.nodetype = nodetype
        self.coord = coord
        self.declname = declname
        self.quals = quals
        self.type = type