<h1>
<image src="docs/assets/img/main-title.png"  width="400">
</h1>


<!-- [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) -->
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) 2024 Edgardo Palazzo (epalazzo@fra.utn.edu.ar)
<!-- [![Github All Releases](https://img.shields.io/github/downloads/Edinburgh-Chemistry-Teaching/Data-driven-chemistry/total)]() -->
<!-- [![DOI](https://jose.theoj.org/papers/10.21105/jose.00192/status.svg)](https://doi.org/10.21105/jose.00192) -->

Ingreso al material: [https://frautn.github.io/F2-electromagnetismo/](https://frautn.github.io/F2-electromagnetismo/)  

En este repositorio se encuentra el material para realizar algunas prácticas computacionales que complementan el trabajo en clase de la unidad sobre electromagnetismo de la materia Física 2, en la Facultad Regional Avellaneda de la Universidad Tecnológica Nacional.  

Se trata de cuadernos Jupyter que intercalan explicaciones téoricas (texto y ecuaciones) con implementaciones en código que permiten resolver problemas inherentes. Dichos cuadernos se pueden ejecutar en línea en Google Colaboratory, sin necesidad de instalar software, y para tal fin se incluyen enlaces a los distintos módulos. Para quien lo considere necesario, en la sección "Entorno" se indica como realizar lo propio en forma local, sin acceder a Google Colab.

## Actividades

| Módulo | Contenido                 | Enlace |
|------|---------------------------------|------|
| 1    |  Campo eléctrico de cargas puntuales | [![modulo_1](docs/assets/img/colab-badge-es.svg)](https://colab.research.google.com/github/frautn/F2-electromagnetismo/blob/main/modulos/em01_campo_electrico.ipynb) |
| 2    | Potencial eléctrico |[![modulo_2](docs/assets/img/colab-badge-es.svg)](https://colab.research.google.com/github/frautn/F2-electromagnetismo/blob/main/modulos/em02_potencial_electrico.ipynb)|
| 3    | Distribuciones de carga contínuas - parte 1: cálculos numéricos sumando cargas puntuales |[![modulo_3](docs/assets/img/colab-badge-es.svg)](https://colab.research.google.com/github/frautn/F2-electromagnetismo/blob/main/modulos/em03_distribuciones_continuas.ipynb)|
| 4    | Distribuciones de carga contínuas - parte 2: cálculos simbólicos |[![modulo_4](docs/assets/img/colab-badge-es.svg)](https://colab.research.google.com/github/frautn/F2-electromagnetismo/blob/main/modulos/em04_distribuciones_continuas_simbolico_preliminar.ipynb)|
|     | Ejercicios del módulo 4 |[<img src="docs/assets/img/Icon_pdf_file.svg" alt="pdf_icon" width="25"/>]()|
| 5   | Campos y equipotenciales en presencia de conductores |[![modulo_5](docs/assets/img/colab-badge-es.svg)](https://colab.research.google.com/github/frautn/F2-electromagnetismo/blob/main/modulos/em05_conductores.ipynb)|
| 6   | Trabajo final de electrostática: plantilla para la entrega de los ejercicios propuestos |[![modulo_6](docs/assets/img/colab-badge-es.svg)](https://colab.research.google.com/github/frautn/F2-electromagnetismo/blob/main/modulos/em06_trabajo_final.ipynb)|
|     | Ejercicios de electrostática para entregar |[<img src="docs/assets/img/Icon_pdf_file.svg" alt="pdf_icon" width="25"/>]()|


<!-- 
## Reconocimientos

A los autores del curso Mecánica. -->


<!-- ### Telling us about how you are using the resource
If you just want to tell us how you have been using the resource just send us an email or raise an issue pointing to your work.  -->

<!-- ## Reutilizando este material para otro curso

The easiest way is by cloning the material and adapting it to your needs. This can be just using some partial material or expanding on the existing material. The best way to do this is by either [cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the repo and building up on it, or using the current repository as a [template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) for your own or your organisations GitHub account, for more details see the [overview](overview.md) document.  -->

<!-- 
## Dependencies and Installation

This project uses the Python programming language, and requires Python >= 3.9.

Units will require different packages from the scientific Python ecosystem. The easiest way to install dependencies is using the Anaconda distribution, otherwise the [requirements.txt](requirements.txt) file also summarises the needed packages. 

Units are written and available as [Jupyter Notebooks](https://jupyter.org/). If you just want to get started with the Units use the links to the CoLab notebooks provided. Otherwise you can follow these steps to get your local environment setup:

1. Get your anaconda distribution setup. See [here](https://datacarpentry.org/2016-05-29-PyCon/install.html) for detailed instructions.
2. Open a terminal or anaconda promt.
2. Create an environment using the following command
	
	```
	conda create -n ddc python=3.9
	```
	
3. Activate the environment and install the required packages into it:
	
	``` 
	conda activate ddc
	conda install jupyter pandas scipy nglview==3.0.3 ipywidgets==7.6.0 pint mendeleev vpython matplotlib jupyter-server==1.23.6
	```
	
4. Now you can start your Jupyter notebooks as:
	
	```
	jupyter notebook Unit_01/Unit_01_problem_solving_I.ipynb
	``` -->


<!-- ## Reference

Paper v. 1.0.1 -->

<!-- ## Further resources

- [CCPBioSim Training Material](https://github.com/CCPBioSim)
- [A computational chemistry Python book developped at Bath University](https://pythoninchemistry.org/ch40208/introduction/about_this_book.html)
- [MolSSi training Material](http://education.molssi.org)
- [Software Carpentries introduction to Python and Data](https://software-carpentry.org/lessons/) -->

## Reconocimiento

Este material está inspirado y fuertemente basado en el curso de mecánica racional de la Universidad de La Matanza, curso en el cual todo se realiza en código Python. El curso se puede acceder en su repositorio: [Mecánica Analítica Computacional](https://github.com/unlam/MecanicaAnaliticaComputacional). Se agradece a su autor [V. A. Bettachini](https://github.com/bettachini) y a su colaborador [M. A. Real](https://github.com/realmariano).

## Entorno

Este es el entorno virtual recomendado para ejecutar los cuadernos sin usar Google Colab. Es recomendable tener instalado Anaconda y crear un entorno como el siguiente:

```bash
conda create -n utn -c conda-forge python==3.10.12
conda install -n utn -c conda-forge ipykernel ipympl matplotlib numpy pandas scikit-image sympy
```

## Licencia

Este material está disponible libremente sin barreras de acceso bajo una licencia [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).
