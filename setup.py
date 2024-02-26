from setuptools import setup, find_packages

setup(
    name='yavuz_unique',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'my-notebook-app==0.1.0',  # Gerekli bağımlılıkları buraya ekleyin
    ],
    entry_points={
        'console_scripts': [
            'my-notebook-app=my_notebook_app.main:main',
        ],
    },
    url='https://github.com/yavuz0x/yavuz_unique',  # GitHub deposunun URL'sini ekleyin
)
