from setuptools import setup, find_packages

setup(
    name="q2",
    version="v1.0",
    packages=find_packages(),
    author="luyulin",
    author_email="luyulinvip@gmail.com",
    description="Q2 program.",
    license='BSD-3-Clause',
    url="https://Q2.org",
    entry_points={
        "console_scripts":
        ["q2=q2._q2:q2"]
    },
    zip_safe=False,
    )
