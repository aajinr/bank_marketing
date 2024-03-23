from setuptools import setup, find_packages

setup(
    name='bank_marketing',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas==1.5.3',
        'numpy==1.24.2',
        'scikit-learn==1.2.1',  # Note the package name difference: 'sklearn' vs 'scikit-learn'
        'matplotlib==3.8.3',
        'imblearn==0.12.0',
        'pre-commit==3.6.2',
        'black==24.3.0'
    ]
)