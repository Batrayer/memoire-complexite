class ParserASTJson:
    def __init__(self):
        self.deep = []
        self.deepLisible = []
        self.valtableau = 0
        self.level = 0
    '''
    Fonction recursive qui check
    '''
    def somethingDeep(self, nodeObj): 
        #if(nodeObj["_nodetype"] != "Assignment") :
        if(len(self.deep) < self.valtableau) :
            self.deep.append(self.level)
            self.deepLisible.append(nodeObj["_nodetype"] +  " " + str(self.level))
        self.valtableau += 1
        print(nodeObj["_nodetype"])
        if(nodeObj["_nodetype"] == "If"): 
            self.ifNode(nodeObj)
        else: 
            self.otherNode(nodeObj)
            

    '''
    If Node has a special element if or else before block_item
    so it must be treated as special
    '''
    def ifNode(self, nodeObj): 

        if(nodeObj["iffalse"] != None and nodeObj["iffalse"] != "null"):
            nodeObjFalse = nodeObj["iffalse"]
            self.level -= 1
            self.getTheDeep(nodeObjFalse)
            self.level += 1
        if(nodeObj["iftrue"] != None and nodeObj["iftrue"] != "null"):
            nodeObjTrue = nodeObj["iftrue"]
            self.level -= 1
            self.getTheDeep(nodeObjTrue)
            self.level += 1

    '''
    Every non special node 
    '''
    def otherNode(self, nodeObj):
        if ("stmt" in nodeObj and nodeObj["stmt"] != None):
            self.getTheDeep(nodeObj["stmt"])

    def getTheDeep(self, nodeObj):
            if(nodeObj["block_items"] != None):
                for node in nodeObj["block_items"]:
                    self.level += 1
                    self.somethingDeep(node)
                    self.level -= 1