from setuptools import setup, find_packages

setup(
    name='yavuz_unique',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[
        'my-notebook-app==0.1.0',  # Gerekli bağımlılıkları buraya ekleyin
    ],
    entry_points={
        'console_scripts': [
            'yavuz-word-game=yavuz_unique.scripts.yavuz_game_script:main',
        ],
    },
    author='Yavuz',
    author_email='yavuz0x00@gmail.com',
    description='A short description of your project',
    bugtrack_url='https://github.com/yavuz0x/yavuz_unique',
    long_description=open('README.md').read(),  # README.md dosyasının içeriğini uzun açıklama olarak kullanın
    long_description_content_type='text/markdown',  # README.md dosyasının türünü belirtin
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        # Diğer sınıflandırmaları buraya ekleyin
    ],
)
