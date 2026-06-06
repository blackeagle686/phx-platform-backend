from celery import shared_task

@shared_task
def process_new_service_request(request_id, request_type='standard'):
    """
    Simulates background processing for a new service request.
    In a real app, this might send an email to the admin, notify via Slack/Telegram,
    or sync with a CRM.
    """
    print(f"Processing {request_type} service request ID: {request_id}")
    # Simulate some processing time
    import time
    time.sleep(2)
    print(f"Finished processing {request_type} service request ID: {request_id}")
    return True
