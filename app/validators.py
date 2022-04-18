from app.models import Choice


def request_is_valid(*, data, question_id):
    if not(data and isinstance(data, list)):
        return False
    choices = Choice.objects.filter(questions_id=question_id).values_list('id')
    for val in data:
        if not isinstance(val, int):
            return False
        if (val,) not in choices:
            return False
    if len(data) != len(set(data)):
        return False
    return True
