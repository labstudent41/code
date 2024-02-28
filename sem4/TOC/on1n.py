class TM:
    def __init__(self,tape_string):
        self.tape=list(tape_string)
        self.wr_head=0
        self.state="A"
    def step(self):
        if self.state=="A":
            print("A",end="--->")
            if self.wr_head < len(self.tape) and self.tape[self.wr_head]=="0":
                self.tape[self.wr_head]="X"
                self.wr_head+=1
                self.state="B"
            elif self.wr_head < len(self.tape) and self.tape[self.wr_head]=="Y":
                self.tape[self.wr_head]="Y"
                self.wr_head+=1
                self.state="D"
            elif self.wr_head==len(self.tape):
                self.state="accept"
            else:
                self.state="reject"
        elif self.state=="B":
            print("B",end="--->")
            if self.wr_head < len(self.tape) and self.tape[self.wr_head] in ["0","Y"]:
                self.wr_head+=1
                self.state="B"
            elif self.wr_head < len(self.tape) and self.tape[self.wr_head]=="1":
                self.tape[self.wr_head]="Y"
                self.wr_head-=1
                self.state="C"
            else:
                self.state="reject"
        elif self.state=="C":
            print("C",end="--->")
            if self.wr_head < len(self.tape) and self.tape[self.wr_head] in ["0","Y"]:
                self.wr_head-=1
                self.state="C"
            elif self.wr_head < len(self.tape) and self.tape[self.wr_head]=="X":
                self.tape[self.wr_head]="Y"
                self.wr_head+=1
                self.state="A"
            else:
                self.state="reject"
        elif self.state=="D":
            print("D",end="--->")
            if self.wr_head==len(self.tape):
                self.state="accept"
            elif self.wr_head < len(self.tape) and self.tape[self.wr_head]=="Y":
                self.tape[self.wr_head]="Y"
                self.wr_head+=1
                self.state="D"
            else:
                self.state="reject"
    def run(self):
        while self.state not in ['accept', 'reject']:
            self.step()
        return self.state

# Example usage
tm = TM("000111")
result = tm.run()
print(f"Result: {result}")

                
            
            
            
