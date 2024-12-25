from setuptools import setup, find_packages
import os

setup(
    name="py_visual_algo",
    version="0.2.1",
    packages=find_packages(),
    install_requires=[
        "matplotlib>=3.0.0",
        "networkx>=2.5",
    ],
    include_package_data=True,
    data_files=[
    (
        "examples",
        [os.path.join("examples", f) for f in os.listdir("examples") if f.endswith(".py")],
    )
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "flake8>=3.8",
            "black>=22.0",
            "pdoc>=12.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "py-visual-algo=py_visual_algo.ui.cli:cli",
        ]
    },
    author="DaryoushAlipour",
    author_email="ai.tirotir@gmail.com",
    description="Interactive Algorithm Visualizer",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tirotir-ir/py_visual_algo",
    project_urls={
        "Bug Tracker": "https://github.com/tirotir-ir/py_visual_algo/issues",
        "Documentation": "https://tirotir-ir.github.io/py_visual_algo",
        "Source Code": "https://github.com/tirotir-ir/py_visual_algo",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries",
        "Topic :: Education",
    ],
    python_requires=">=3.7",
    zip_safe=False,
)
