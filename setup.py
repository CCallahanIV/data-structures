from setuptools import setup

setup(
    name="data-structures",
    description="this module will be expanded as we write more data-structures",
    version=1.1,
    author="Ben Shields and Colin Lamont, initially forked from Ted Callahan's repo, which he worked on with Colin Lamont.",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["linked_list", "stack", "dbl_linked_list", "queue_ds", "deque", "binheap", "graph", "weighted_graph"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={}
)
