from setuptools import setup, find_packages

setup(
    name="q2-igv",
    version="v1.0",
    packages=find_packages(),
    author="luyulin",
    author_email="luyulinvip@gmail.com",
    description="Q2 plugin for IGV.",
    license='BSD-3-Clause',
    url="https://Q2.org",
    entry_points={
        "Q2.plugins":
        ["q2-igv=q2_igv._igv:igv"]
    },
    zip_safe=False,
    )
