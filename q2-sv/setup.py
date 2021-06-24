from setuptools import setup, find_packages

setup(
    name="q2-sv",
    version="v1.0",
    packages=find_packages(),
    author="luyulin",
    author_email="luyulinvip@gmail.com",
    description="Q2 plugin for SV.",
    license='BSD-3-Clause',
    url="https://Q2.org",
    entry_points={
        "Q2.plugins":
        ["q2-sv=q2_sv._sv:sv",
		 "q2-sv-batch=q2_sv._sv:sv_batch",
		]
    },
    zip_safe=False,
    )
