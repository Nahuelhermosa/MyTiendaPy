from setuptools import setup, find_packages

setup(
    name="my_tienda",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "mi-tienda=my_tienda.main:menu",  # comando en consola
        ],
    },
    author="Nahuel Hermosa",
    description="Paquete de gestión de clientes para una tienda en línea",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)