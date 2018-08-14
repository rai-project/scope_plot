import os
from scope_plot import specification
from scope_plot import backend
from scope_plot import schema

FIXTURES_DIR = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "__fixtures")


def generate_fixture(name):
    figure_spec = specification.load(os.path.join(FIXTURES_DIR, name))
    figure_spec = schema.validate(figure_spec)
    figure_spec = specification.apply_search_dirs(figure_spec, [FIXTURES_DIR])
    jobs = specification.construct_jobs(figure_spec, "test.pdf", None)
    for job in jobs:
        backend.run(job)


def test_generate_errorbar():
    generate_fixture("bokeh_errorbar.yml")


def test_generate_regplot():
    generate_fixture("matplotlib_regplot.yml")


def test_generate_bar():
    generate_fixture("bokeh_bar.yml")


def test_generate_subplots():
    generate_fixture("matplotlib_subplots.yml")
