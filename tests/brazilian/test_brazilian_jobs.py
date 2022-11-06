from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    results = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for result in results:
        assert result['title'] is True
