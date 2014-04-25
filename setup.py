from setuptools import setup, find_packages

setup(name="googleplayapi",
      version="1.0.0",
      author="Emilien Girault",
      author_email="emilien.girault@gmail.com",
      license="BSD",
      description="Google Play API for Android",
      long_description=open("README.md").read(),
      url="https://github.com/upwlabs/googleplay-api",
      classifiers=[
              "Environment :: Console",
              "Development Status :: 3 - Alpha",
              "Programming Language :: Python",
              "Programming Language :: Python :: 2.7",
              "Intended Audience :: Developers",
              "License :: OSI Approved :: BSD License",
              "Natural Language :: English",
              "Operating System :: OS Independent",
              "Environment :: Other Environment",
              "Topic :: Utilities",
          ],
      install_requires=['protobuf'],
      packages=find_packages())
