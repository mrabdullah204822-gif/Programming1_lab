def requisition_approval(total, staff_id, requisition_id):

    if total < 500:
        approval_status = "Approved"
        req_number = str(requisition_id)
        last_part = req_number[-3:]
        reference_number = staff_id + last_part

    else:
        approval_status = "Pending"
        reference_number = ""

    return approval_status, reference_number