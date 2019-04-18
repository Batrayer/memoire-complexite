class ParserASTJson:
    def __init__(self):
        self.deep = []
        self.deepLisible = []
        self.variable = []
        self.usedVariable = []
        self.valtableau = 0
        self.level = 0
        self.complexiteBasic = 0
        self.complexiteVariable = []
        self.args = []
        self.insideCondFor = False
        self.insideFor = False
        self.magie = []
        self.nodeOperation = ["+", "-", "/", "*", "%", ">", "<", ">=", "<="]
    '''
    Fonction recursive qui check
    '''
    def somethingDeep(self, nodeObj): 
        if (len(self.deep) < self.valtableau) :
            self.deep.append(self.level)
            self.deepLisible.append(nodeObj["_nodetype"] +  " " + str(self.level))
        self.valtableau += 1
        nodeType = nodeObj["_nodetype"]
        if (nodeType == "BinaryOp"):
            self.binaryNode(nodeObj)
        elif (nodeType == "If"): 
            self.ifNode(nodeObj)
        elif (nodeType == "Decl"): 
            self.declNode(nodeObj)
        elif (nodeType == "For"):
            self.forNode(nodeObj)
        elif (nodeType == "FuncDef"):
            self.funcDefNode(nodeObj)
        elif (nodeType == "FuncCall"):
            self.funcCallNode(nodeObj)
        elif (nodeType == "Return"):
            self.funcReturnNode(nodeObj)
        elif (nodeType == "Assignment"):
            self.assignmentNode(nodeObj)
        elif (nodeType == "UnaryOp"):
            self.unaryOpNode(nodeObj)
        else:
            self.otherNode(nodeObj)
            

    '''
    If node is a for => register variable used in each for 
    '''
    def forNode(self, nodeObj):
        nbOp = self.complexiteBasic
        self.complexiteBasic = 0
        if ("cond" in nodeObj):
            self.insideCondFor = True
            self.somethingDeep(nodeObj["cond"])
            self.insideCondFor = False
        if ("init" in nodeObj):
            self.somethingDeep(nodeObj["init"])
        if ("next" in nodeObj):
            self.somethingDeep(nodeObj["next"])
            # self.usedVariable.append(assignement["lvalue"]["name"]) si la var est assignée dans le for
        self.insideFor = True
        self.otherNode(nodeObj)
        self.insideFor = False
        print("For: " + str(self.usedVariable))
        self.magie.append(str(self.usedVariable)+ " " + str(self.complexiteBasic))
        self.usedVariable = []
        self.complexiteBasic = nbOp + self.complexiteBasic
    '''
    Binary node is a calculation it has a left side and a right side and a sign (+ - * / % ...)
    '''
    def binaryNode(self, nodeObj):
        print("BinaryNode")
        print(nodeObj["left"]["_nodetype"] == "ID" and self.insideCondFor)
        if("left" in nodeObj):
            if (nodeObj["left"]["_nodetype"] == "ID" and self.insideCondFor):
                self.usedVariable.append(nodeObj["left"]["name"])
            self.somethingDeep(nodeObj["left"])
        if(nodeObj["op"] in self.nodeOperation):
            if(self.insideCondFor):
                self.usedVariable.append(nodeObj["op"])
            self.incComplexite()
        if("right" in nodeObj):
            if (nodeObj["right"]["_nodetype"] == "ID" and self.insideCondFor):
                self.usedVariable.append(nodeObj["right"]["name"] )
            self.somethingDeep(nodeObj["right"])
    def assignmentNode(self, nodeObj):
        print("AssignementNode")
        self.incComplexite()
        if ("rvalue" in nodeObj):
            self.somethingDeep(nodeObj["rvalue"])  
    def unaryOpNode(self, nodeObj):
        self.incComplexite()
    '''
    If node is a decleration node => register variable for future use
    '''
    def declNode(self, nodeObj, param = False):
        if ("type" in nodeObj and nodeObj["type"]["_nodetype"] == "FuncDecl"):
            if ("args" in nodeObj["type"] and nodeObj["type"]["args"]["_nodetype"] == "ParamList"):
                if ("params" in nodeObj["type"]["args"]):
                    for node in nodeObj["type"]["args"]["params"]:
                        self.declNode(node, True)
        else:
            if(param):
                self.args.append(nodeObj["name"])
            else:
                self.variable.append(nodeObj["name"])
        self.otherNode(nodeObj)
    '''
    If Node has a special element if or else before block_item
    so it must be treated as special
    '''
    def ifNode(self, nodeObj):
        complexiteActuel = self.complexiteBasic
        complexiteF = 0
        complexiteT = 0
        if("cond" != None):
            self.somethingDeep(nodeObj["cond"])
        if (nodeObj["iffalse"] != None and nodeObj["iffalse"] != "null"):
            nodeObjFalse = nodeObj["iffalse"]
            self.level -= 1
            self.getTheDeep(nodeObjFalse)
            self.level += 1
            complexiteF = self.complexiteBasic - complexiteActuel
            self.incComplexite(-complexiteF)
        if (nodeObj["iftrue"] != None and nodeObj["iftrue"] != "null"):
            nodeObjTrue = nodeObj["iftrue"]
            self.level -= 1
            self.getTheDeep(nodeObjTrue)
            self.level += 1
            complexiteT = self.complexiteBasic - complexiteActuel
            self.incComplexite(-complexiteT)
        
        if (complexiteF >= complexiteT):
            self.incComplexite(complexiteF)
        else :
            self.incComplexite(complexiteT)


    '''
    Function node 
    '''
    def funcDefNode(self, nodeObj):
        if ("decl" in nodeObj and nodeObj["decl"] != None):
            self.declNode(nodeObj["decl"])
        if ("body" in nodeObj and nodeObj["body"] != None):
            for node in nodeObj["body"]["block_items"] :
                self.somethingDeep(node)

    def funcReturnNode(self, nodeObj):
        if("expr" in nodeObj and nodeObj["expr"] != None):
            self.somethingDeep(nodeObj["expr"])

    def otherNode(self, nodeObj):
        if ("stmt" in nodeObj and nodeObj["stmt"] != None):
            self.getTheDeep(nodeObj["stmt"])
    '''
    Increment basic complexite point
    '''
    def incComplexite(self, i = 1):
        self.complexiteBasic = self.complexiteBasic + i

    def funcCallNode(self, nodeObj): 
        if ("name" in nodeObj and nodeObj["name"] != None):
            if(nodeObj["name"]["name"] == "rand"):
                self.incComplexite()
            else:
                print("Function complexity unknown for : " + nodeObj["name"]["name"] + "incrementing by one")
                self.incComplexite()

    def getTheDeep(self, nodeObj):
            if (nodeObj["block_items"] != None):
                for node in nodeObj["block_items"]:
                    self.level += 1
                    self.somethingDeep(node)
                    self.level -= 1