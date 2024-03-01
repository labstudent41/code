class TM:
    def __init__(self,tape_string):
        self.tape=list(tape_string)
        self.wr_head=0
        self.state="A"
    def step(self):
        if self.state=="A":
            print("A",end="--->")
            if self.wr_head < len(self.tape) and self.tape[self.wr_head]=="a":
                self.tape[self.wr_head]="#"
                self.wr_head+=1
                self.state="B"
            elif self.wr_head < len(self.tape) and self.tape[self.wr_head]=="b":
                self.tape[self.wr_head]="#"
                self.wr_head+=1
                self.state="E"
            elif self.check():
                self.state="accept"
            else:
                self.state="reject"
        elif self.state=="B":
            print("B",end="--->")
            if self.wr_head < len(self.tape) and self.tape[self.wr_head] in ["a","b"]:
                self.wr_head+=1
                self.state="B"
            elif self.wr_head < len(self.tape) and self.tape[self.wr_head]=="#":
                self.tape[self.wr_head]="#"
                self.wr_head-=1
                self.state="C"
            else:
                self.state="reject"
        elif self.state=="C":
            print("C",end="--->")
            if self.wr_head < len(self.tape) and self.tape[self.wr_head]=="a":
                self.tape[self.wr_head]="#"
                self.wr_head-=1
                self.state="D"
            else:
                self.state="reject"
        elif self.state=="D":
            print("D",end="--->")
            if self.wr_head < len(self.tape) and self.tape[self.wr_head] in ["a","b"]:
                self.wr_head-=1
                self.state="D"
            elif self.wr_head < len(self.tape) and self.tape[self.wr_head]=="#":
                self.tape[self.wr_head]="#"
                self.wr_head+=1
                self.state="A"
            else:
                self.state="reject"
        elif self.state=="E":
            print("E",end="--->")
            if self.wr_head < len(self.tape) and self.tape[self.wr_head] in ["a","b"]:
                self.wr_head+=1
                self.state="E"
            elif self.wr_head < len(self.tape) and self.tape[self.wr_head]=="#":
                self.tape[self.wr_head]="#"
                self.wr_head-=1
                self.state="F"
            else:
                self.state="reject"
        elif self.state=="F":
            print("F",end="--->")
            if self.wr_head < len(self.tape) and self.tape[self.wr_head]=="b":
                self.tape[self.wr_head]="#"
                self.wr_head-=1
                self.state="G"
            else:
                self.state="reject"
        elif self.state=="G":
            print("G",end="--->")
            if self.wr_head < len(self.tape) and self.tape[self.wr_head] in ["a","b"]:
                self.wr_head-=1
                self.state="G"
            elif self.wr_head < len(self.tape) and self.tape[self.wr_head]=="#":
                self.tape[self.wr_head]="#"
                self.wr_head+=1
                self.state="A"
            else:
                self.state="reject"
    def check(self):
        result=False
        for i in self.tape:
            if i=="#":
                result=True
            else:
                result=False
        return result

    def run(self):
        while self.state not in ['accept', 'reject']:
            self.step()
        return self.state

# Example usage
tm = TM("bbaaaabb#")
result = tm.run()
print(f"Result: {result}")





