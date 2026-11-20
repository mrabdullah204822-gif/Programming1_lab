from datetime import date

class Ticket:
    def __init__(self, ticket_id, employee_id, employee_name, issue_description):
        self.ticket_id = ticket_id
        self.submission_date = date.today()
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.issue_description = issue_description
        self.priority = self.assign_priority()
        self.resolution_message = ""

        if "password reset" in issue_description.lower():
            self.status = "Resolved"

            new_password = employee_id[:2] + employee_name[:2]

            self.resolution_message = "Password reset successfully. New password: " + new_password

        else:
            self.status = "In Progress"

            if self.priority == "High":
                self.resolution_message = "Pending Manager Approval"
            else:
                self.resolution_message = "Waiting for IT Support"

    def assign_priority(self):
        issue = self.issue_description.lower()

        if ("system outage" in issue or
            "server down" in issue or
            "network down" in issue or
            "security breach" in issue or
            "critical" in issue):

            return "High"

        elif "password reset" in issue:
            return "Low"

        else:
            return "Medium"

    def update_status(self, new_status):
        if new_status == "Closed" and self.priority == "High":
            print("Manager approval is required.")

        elif new_status in ["Resolved", "In Progress", "Closed"]:
            self.status = new_status

            if new_status == "Resolved":
                self.resolution_message = "Issue resolved."

            elif new_status == "In Progress":
                self.resolution_message = "Waiting for IT Support."

            elif new_status == "Closed":
                self.resolution_message = "Ticket closed."

            print("Ticket status updated successfully.")

        else:
            print("Invalid status.")

    def manager_approval(self, choice):
        if self.priority == "High":

            if choice == "1":
                self.status = "Closed"
                self.resolution_message = "Approved by manager."

                print("Manager approved the ticket.")
                print("Ticket status: Closed")

            elif choice == "2":
                self.status = "In Progress"
                self.resolution_message = "Rejected by manager. Further work required."

                print("Manager rejected the ticket.")
                print("Ticket status: In Progress")

            else:
                print("Invalid choice.")

        else:
            print("This ticket does not require manager approval.")


class HelpDeskManagement:
    def __init__(self):
        self.ticketlist = []
        self.ticket_id = 10100

    def submit_ticket(self):
        employee_id = input("Enter Employee ID: ")
        employee_name = input("Enter Employee Name: ")
        issue_description = input("Describe Your Issue: ")

        ticket = Ticket(
            self.ticket_id,
            employee_id,
            employee_name,
            issue_description
        )

        self.ticketlist.append(ticket)

        print("Ticket submitted successfully.")
        print("Ticket ID:", ticket.ticket_id)
        print("Priority:", ticket.priority)
        print("Status:", ticket.status)
        print("Resolution Message:", ticket.resolution_message)

        self.ticket_id += 1

    def view_tickets(self):
        if len(self.ticketlist) == 0:
            print("No tickets available.")
            return

        for ticket in self.ticketlist:
            print("---------------- Ticket Details ----------------")
            print("Submission Date:", ticket.submission_date)
            print("Ticket ID:", ticket.ticket_id)
            print("Employee ID:", ticket.employee_id)
            print("Employee Name:", ticket.employee_name)
            print("Issue:", ticket.issue_description)
            print("Priority:", ticket.priority)
            print("Status:", ticket.status)
            print("Resolution Message:", ticket.resolution_message)

    def update_ticket_status(self):
        ticket_id = input("Enter Ticket ID to Update: ")

        if not ticket_id.isdigit():
            print("Please enter a valid Ticket ID.")
            return

        ticket_id = int(ticket_id)

        for ticket in self.ticketlist:
            if ticket.ticket_id == ticket_id:

                print("1. Resolved")
                print("2. In Progress")
                print("3. Closed")

                choice = input("Enter your choice: ")

                if choice == "1":
                    ticket.update_status("Resolved")

                elif choice == "2":
                    ticket.update_status("In Progress")

                elif choice == "3":
                    ticket.update_status("Closed")

                else:
                    print("Invalid choice.")

                return

        print("Ticket ID not found.")

    def manager_approval(self):
        ticket_id = input("Enter Ticket ID for Manager Approval: ")

        if not ticket_id.isdigit():
            print("Please enter a valid Ticket ID.")
            return

        ticket_id = int(ticket_id)

        for ticket in self.ticketlist:
            if ticket.ticket_id == ticket_id:

                if ticket.priority == "High":
                    print("1. Approve Resolution")
                    print("2. Reject Resolution")

                    choice = input("Enter your choice: ")

                    ticket.manager_approval(choice)

                else:
                    print("Manager approval is not required.")

                return

        print("Ticket ID not found.")

    def display_summary(self):
        total_tickets = len(self.ticketlist)
        resolved = 0
        in_progress = 0
        closed = 0

        for ticket in self.ticketlist:
            if ticket.status == "Resolved":
                resolved += 1

            elif ticket.status == "In Progress":
                in_progress += 1

            elif ticket.status == "Closed":
                closed += 1

        print("========== Ticket Statistics ==========")
        print("Total Tickets Submitted:", total_tickets)
        print("Total Resolved Tickets:", resolved)
        print("Total Tickets In Progress:", in_progress)
        print("Total Closed Tickets:", closed)

    def menu_system(self):
        while True:
            print("========== Help Desk Ticketing System ==========")
            print("1. Submit New Ticket")
            print("2. View All Tickets")
            print("3. Update Ticket Status")
            print("4. Manager Approval")
            print("5. Ticket Statistics")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.submit_ticket()

            elif choice == "2":
                self.view_tickets()

            elif choice == "3":
                self.update_ticket_status()

            elif choice == "4":
                self.manager_approval()

            elif choice == "5":
                self.display_summary()

            elif choice == "6":
                print("Thank you for using Help Desk System.")
                break

            else:
                print("Please enter a valid choice.")


helpdesk = HelpDeskManagement()
helpdesk.menu_system()
