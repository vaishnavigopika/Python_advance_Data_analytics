class name:
    def __init__(self,name):
        self.name=name 
    def gopika(self):
        print("Hello",self.name)
    def adithya(self):
       print("Hello",self.name)
    def nayana(self):
        print("Hello",self.name)
    def revrev(self):
        print("Hello",self.name)
    def jayboi(self):
        print("Hello",self.name)

class Mentor:
    def __init__(self):
        self.next = None
    
    def handle(self, query):
        print("[Mentor]", query)
        if "attendance" in query.lower():
            print("Mentor: Handled")
            return True
        if self.next:
            return self.next.handle(query)
        return False


class Management:
    def __init__(self):
        self.next = None
    
    def handle(self, query):
        print("[Management]", query)
        if "grades" in query.lower():
            print("Management: Handled")
            return True
        if self.next:
            return self.next.handle(query)
        return False


class Founder:
    def __init__(self):
        self.next = None
    
    def handle(self, query):
        print("[Founder]", query)
        if "scholarship" in query.lower():
            print("Founder: Handled")
            return True
        print("Not available")
        return False


class student:
    def __init__(self, name):
        self.name = name
        self.mentor = Mentor()
        management = Management()
        founder = Founder()
        self.mentor.next = management
        management.next = founder
    
    def get_details(self, query):
        print(query)
        self.mentor.handle(query)


if __name__ == "__main__":
    s = student("John")
    s.get_details("What is attendance")
    s.get_details("What are the grades")
    s.get_details("Scholarship info")
