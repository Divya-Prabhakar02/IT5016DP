"""
A Program to develop a prototype of the requisition system
Author: Divya Prabhakar/20240563
"""
class RequisitionSystem():                                     #Identifying Class
    unique_id_counter = 10000                                 #Global Unique ID counter
    def __init__(self):
        self.approved_requisition= 10                           #Creating lists for different response
        self.notapproved_requisition=20
        self.pending_requisition = 30
        self.requests = []    
        self.staff_ID = input("Enter the staff ID")                                  #creating lists to store all request
        self.date = input("Enter today's date")                #accepting some basic information like date name
        self.name = input("Enter the name of the staff")
    def staffinfo(self):
        self.Requisition_id = unique_id_counter                      #Generating RequisitionID Automatically
        unique_id_counter+=1
        return self.Requisition_id
    def requisition_details(self):
        self.requisition_total = 0                                         
        self.itemlist = []                                      #Accepting List for the item
        while True:
            item = input("Enter the item (type'exit' when done):")
            if item.lower == 'exit':
                break
            cost = float(input("Enter the price of each item"))
            self.itemlist.append(item)
            self.itemlist.append(cost)            #Appending the list to add multiple item and their cost         
            self.requisition_total+=cost
        return self.requisition_total,item
    
    def requisition_approval(self):                   
        if self.requisition_total < 500:
            self.status == "Approved"
            self.approved_requisition+=1
        elif  self.requisition_total >= 500:
            self.status == "Not Approved"
            self.notapproved_requisition+=1
        else:
            self.status = "Pending"
            self.pending_requisition-=1
        print(f"Status :${self.status}")

    def respond_requisition(self,manager_response):
        if manager_response.lower == "approved":
            self.status = "Approved"
        else:
            self.status = "Not Approved"
        return self.status
    
    def generate_approval_ref(self):
        self.number = self.staff_ID+self.Requisition_id[-3:]
        return self.number
    

    
    def submission(self):
        request = {
            "id": self.Requisition_id,
            "staff name": self.name,
            "total": self.requisition_total,
            "status": self.status,
            "approval_ref": self.number
        }
        self.requests.append(request)
        print(f"Request submitted with ID {self.Requisition_id} and status '{self.status}'.")
        print(f"Approval reference number: {self.number}")
    
    def display_requisition(self):
        print(f"Date:{self.date}")
        print(f"Staff ID:{self.staff_ID}")
        print(f"Staff Name:{self.name}")
        print(f"Reuisition ID:{self.Requisition_id}")
        print(f"Total:{self.requisition_total}")
        print(f"Status:{self.status}")
        print(f"Approval Reference Number:{self.number}")

    def reqiuistion_statistics(self):
        print(f"Requisition Submitted: {self.requests}")
        print(f"Approved Requests: {self.approved_requisition}")
        print(f"Pending Requests: {self.pending_requisition}")
        print(f"Not Approved Requests: {self.notapproved_requisition}")

# Main program loop
def main():
    system = RequisitionSystem()

    while True:
        choice = input("\n1. Display Requisition Details\n2. Display Requisition\n3. View Statistics\n4. Exit\nChoose an option: ")
        if choice == "1":
            system.requisition_details()
            system.requisition_approval
        elif choice == "2":
            system.submission()
            system.display_requisition()
        elif choice == "3":
            system.reqiuistion_statistics()
        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()

