from django.db.models import Max

def generate_code(model, prefix, field_name='code', padding=4):
    """
    Generates a unique code for a model instance.
    Format: PREFIX-0001
    """
    last_record = model.objects.all().order_by('id').last()
    
    if not last_record:
        return f"{prefix}-{str(1).zfill(padding)}"
    
    # Try to get the last ID to increment
    # This assumes IDs are auto-incrementing integers
    next_id = last_record.id + 1
    return f"{prefix}-{str(next_id).zfill(padding)}"
