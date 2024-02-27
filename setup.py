from setuptools import setup, find_packages

setup(
    name='yavuz_unique',
    version='0.1.0',
    author='Yavuz',  # Kendi adınızı buraya ekleyin
    author_email='yavuz0x00@gmail.com',  # Kendi e-posta adresinizi buraya ekleyin
    packages=find_packages(),
    install_requires=[
        'my-notebook-app==0.1.0',  # Gerekli bağımlılıkları buraya ekleyin
    ],
    entry_points={
        'console_scripts': [
            'yavuz-word-game=yavuz_unique.scripts.yavuz_game_script:main',
        ],
    },
    url='https://github.com/yavuz0x/yavuz_unique',  # GitHub deposunun URL'sini ekleyin
)
