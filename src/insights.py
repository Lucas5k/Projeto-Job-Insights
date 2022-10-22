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
        my_list_industries["industry"] for my_list_industries in all_industries
    }
    return my_list_industries.difference({""})


def filter_by_industry(jobs, industry):
    my_list_of_industry = list()

    for all_industries in jobs:
        if all_industries["industry"] == industry:
            my_list_of_industry.append(all_industries)
    return my_list_of_industry


def get_max_salary(path):
    all_file = read(path)
    my_list_of_salary = []
    for salary in all_file:
        if salary["max_salary"] != "" and salary["max_salary"].isdigit():
            my_list_of_salary.append(salary["max_salary"])
            larger_salary = int(max(my_list_of_salary, key=int))
    return larger_salary


def get_min_salary(path):
    all_file = read(path)
    my_list_of_salary = []
    for salary in all_file:
        if salary["min_salary"] != "" and salary["min_salary"].isdigit():
            my_list_of_salary.append(salary["min_salary"])
            salary_smaller = int(min(my_list_of_salary, key=int))
    return salary_smaller


def matches_salary_range(job, salary):
    if type(salary) != int:
        raise (ValueError)
    if "min_salary" not in job or "max_salary" not in job:
        raise (ValueError)
    if type(job["max_salary"]) != int or type(job["min_salary"]) != int:
        raise (ValueError)
    if job["max_salary"] < job["min_salary"]:
        raise (ValueError)

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    my_list = list()
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                my_list.append(job)
        except ValueError:
            pass

    return my_list
