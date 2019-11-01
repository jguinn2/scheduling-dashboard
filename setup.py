import setuptools

with open("ReadME.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "scheduling-dashboard-pkg-mayorGreen",
    version = "0.0.1",
    author = "Charles Randles, Joseph Kendall-Morwick, Jacob Guinn, Jacob Trickel",
    author_email = "crandles@missouriwestern.edu, jkendallmorwick@missouriwestern.edu, jguinn2@missouriwestern.edu, jtrickel@gmail.com",
    description = "A scheduling dashboard for colleges",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/mayorGreen/scheduling-dashboard",
    packages = setuptools.find_packages(),
    classifiers = ["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent",
                   ],
    python_requires = '>= 3.0',

)