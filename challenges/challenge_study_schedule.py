def study_schedule(permanence_period, target_time):
    if target_time is None or len(permanence_period) == 0:
        return None
    try:
        output = [i for i in permanence_period if i[0] <= target_time <= i[1]]
    except (TypeError):
        return None

    number_of_students = len(output)

    return number_of_students
