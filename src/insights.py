from src.jobs import read


def get_unique_job_types(path):
    all_types_jobs = read(path)
    my_list_types = {
        my_list_types["job_type"] for my_list_types in all_types_jobs
    }
    return my_list_types


def filter_by_job_type(jobs, job_type):
    my_list_of_jobs = list()

    for all_job in jobs:
        if all_job["job_type"] == job_type:
            my_list_of_jobs.append(all_job)
    return my_list_of_jobs


def get_unique_industries(path):
    all_industries = read(path)
    my_list_industries = {
        my_list_industries['industry'] for my_list_industries in all_industries
    }
    return my_list_industries.difference({''})


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    all_file = read(path)
    my_list_of_salary = []
    for salary in all_file:
        if salary["max_salary"] != '' and salary["max_salary"].isdigit():
            my_list_of_salary.append(salary["max_salary"])
            larger_salary = int(max(my_list_of_salary, key=int))
    return larger_salary


def get_min_salary(path):
    all_file = read(path)
    my_list_of_salary = []
    for salary in all_file:
        if salary["min_salary"] != '' and salary["min_salary"].isdigit():
            my_list_of_salary.append(salary["min_salary"])
            salary_smaller = int(min(my_list_of_salary, key=int))
    return salary_smaller


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
