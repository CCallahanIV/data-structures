from setuptools import setup

setup(
    name="data-structures",
    description="this module will be expanded as we write more data-structures",
    version=1.1,
    author="Ted Callahan and Colin Lamont",
    author_email="",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["linked_list", "stack", "dbl_linked_list", "queue_ds", "deque", "binheap", "graph", "weighted_graph", "bst", "pandas"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={}
)
