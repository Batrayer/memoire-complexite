class ParserASTJson:
    def __init__(self):
        self.deep = []
        self.deepLisible = []
        self.variable = []
        self.usedVariable = []
        self.valtableau = 0
        self.level = 0
    '''
    Fonction recursive qui check
    '''
    def somethingDeep(self, nodeObj): 
        if(len(self.deep) < self.valtableau) :
            self.deep.append(self.level)
            self.deepLisible.append(nodeObj["_nodetype"] +  " " + str(self.level))
        self.valtableau += 1
        print(nodeObj["_nodetype"])
        if (nodeObj["_nodetype"] == "If"): 
            self.ifNode(nodeObj)
        elif (nodeObj["_nodetype"] == "Decl"): 
            self.declNode(nodeObj)
        elif (nodeObj["_nodetype"] == "For"):
            self.forNode(nodeObj)
        else:
            self.otherNode(nodeObj)
            

    '''
    If node is a for => register variable used in each for 
    '''
    def forNode(self, nodeObj):
        assignement = nodeObj["init"]
        cond = nodeObj["cond"]
        print(cond)
        if (cond["_nodetype"] == "BinaryOp"):
            self.binaryNode(cond)
        #if (assignement != None):
            #print(assignement)
            #self.usedVariable.append(assignement["lvalue"]["name"])
        self.otherNode(nodeObj)

    def binaryNode(self, nodeObj):
        if(nodeObj["left"]["_nodetype"] == "Id"):
            self.usedVariable.append("left : " + nodeObj["left"]["name"])
        elif (nodeObj["left"]["_nodetype"] == "BinaryOp"):
            self.binaryNode(nodeObj)
        if(nodeObj["right"]["_nodetype"] == "Id"):
            self.usedVariable.append("right : " + nodeObj["right"]["name"] )
        elif(nodeObj["right"]["_nodetype"] == "BinaryOp"):
            self.binaryNode(nodeObj)
    '''
    If node is a decleration node => register variable for future use
    '''
    def declNode(self, nodeObj):
        self.variable.append(nodeObj["name"])
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