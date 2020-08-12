import setuptools

setuptools.setup(
	name="CVUtils",
	version='1.0',
	packages=setuptools.find_packages(),
	install_requires=[
		'cython', 'numpy', 'opencv-python', 'sklearn', 'pandas',
		'ipython', 'pylint', 'ipympl', 'pyyaml', 'tqdm', 'future',
	],
	python_requires='>=3.6',
)
