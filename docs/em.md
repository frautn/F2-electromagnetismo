---
layout: course
author: edgui

title: F2 - Electromagnetismo
---



# Electromagnetismo usando Python
<!-- [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Github All Releases](https://img.shields.io/github/downloads/Edinburgh-Chemistry-Teaching/Data-driven-chemistry/total)]()
[![DOI](https://jose.theoj.org/papers/10.21105/jose.00192/status.svg)](https://doi.org/10.21105/jose.00192) -->

Data-Driven Chemistry is a collection of learning material for an introductory Python course for undergraduate chemistry students. The presented material here serves as a public version of [Data-Driven Chemistry](http://www.drps.ed.ac.uk/22-23/dpt/cxchem08031.htm) as taught at the University of Edinburgh in the School of Chemistry. 

## Actividades:

| Módulo | Contenido                 | Enlace |
|------|---------------------------------|------|
| 1    |  Campo eléctrico de cargas puntuales | [![modulo_1](assets/img/colab-badge-es.svg)](https://colab.research.google.com/github/frautn/F2/blob/main/electromagnetismo/em01_campo_electrico.ipynb) |
| 2    | Potencial eléctrico |[![modulo_2](assets/img/colab-badge-es.svg)]()|
| 3    | Campo eléctrico de distribuciones de cargas contínuas - parte 1: cálculos numéricos sumando cargas puntuales |[![modulo_3](assets/img/colab-badge-es.svg)](https://colab.research.google.com/github/frautn/F2/blob/main/electromagnetismo/em02_distribuciones_continuas.ipynb)|
| 4    | Campo eléctrico de distribuciones de cargas contínuas - parte 2: cálculos simbólicos |[![modulo_4](assets/img/colab-badge-es.svg)](https://colab.research.google.com/github/frautn/F2/blob/main/electromagnetismo/em02_distribuciones_continuas.ipynb)|
|     | Ejercicios del módulo 4 (alguna descripción) |[<img src="assets/img/Icon_pdf_file.svg" alt="pdf_icon" width="25"/>](https://colab.research.google.com/github/frautn/F2/blob/main/electromagnetismo/em02_distribuciones_continuas.ipynb)|
| 5   | Conductores |[![modulo_5](assets/img/colab-badge-es.svg)]()|


<!-- ## Dependencies and Installation

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
	```

## Getting started with the material

This [overview](overview.md) document will give you an idea of how to engage with the material either as a student or instructor. Please read this first before getting started. 

## Authors and their contributions

Authors are, in alphabetical order:
- James Cumby (JC)
- Valentina Erastova (VE)
- Matteo Degiacomi (MTD)
- Jasmin Güven (JJG)
- Claire Hobday (CLH)
- Antonia Mey (ASJSM)
- Hannah Pollak (HP)
- Rafal Szabla (RS)

JC, VE, CLH, and ASJSM have been teaching this course at the University of Edinburgh since the academic year 2021/22. JJG and HP have been course demonstrators. RS taught one unit and created content for it in 2020/21, when the course was run in a shortened form as a replacement for physical chemistry laboratory practicals during the pandemic. MTD shared and adapted materials developed in 2018 for his course at Durham University aimed at chemistry research students, and made some additional contributions.

Specific contributions by each author are as follows.
- JC: Created the material for `Unit_01`, `Unit_10`, and the helper_functions, gave feedback on other materials, and helped edit the manuscript.    
- MTD: Contributed material to `Unit_03`, `Unit_05`, `Unit_07`, and `Unit_08`, and helped edit the manuscript.    
- VE: Created material for `Unit_05` and `Unit_08`, contributed to `Unit_06`, and helped edit the manuscript.   
- JJG: Contributed material to `Unit_09`, and helped edit the manuscript.   
- CLH: Created material for `Unit_03` and `Unit_04`, and helped edit the manuscript.    
- ASJSM: Created material for `Unit_02`, `Unit_06`, `Unit_07`, and `Unit_09`, provided feedback and small contributions to most other units, and wrote the manuscript.   
- HP: Contributed material to `Unit_05` and `Unit_08`, and helped edit the manuscript.   
- RS: Created the material for molecular geometries forming part of `Unit_06` and gave feedback on the manuscript.   

## Acknowledgements

The authors would like to acknowledge the help of all the PhD student demonstrators on this course, who helped with assessment material, testing the course content and providing teaching assistance in the classes. 


## Contributing to the resource and raising issues

Contributions to the learning resource are welcome. Contributions can be made through creating an issue or a pull request.

### For issues
- To create an issue, contributors are encouraged to follow the [GitHub quickstart guide on creating an issue.](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-an-issue)
- Make sure to include the following into your issue:
	-  Are you using the Colab or a local install version
	-  If it is a local install version what version of the different packages are you running?
	-  Are you using it as a student or instructor
	-  Is the issue reporting a bug, an enhancement, or a feature request		

### For pull requests
- To create a pull request, contributors are encouraged to follow the [GitHub quickstart guide on creating a fork and submitting a pull request.](https://docs.github.com/en/get-started/quickstart/contributing-to-projects)

### Telling us about how you are using the resource
If you just want to tell us how you have been using the resource just send us an email or raise an issue pointing to your work. 

## Reusing and building on the material for your own course

The easiest way is by cloning the material and adapting it to your needs. This can be just using some partial material or expanding on the existing material. The best way to do this is by either [cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the repo and building up on it, or using the current repository as a [template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) for your own or your organisations GitHub account, for more details see the [overview](overview.md) document. 


## Reference

Paper v. 1.0.1

## Further resources

- [CCPBioSim Training Material](https://github.com/CCPBioSim)
- [A computational chemistry Python book developped at Bath University](https://pythoninchemistry.org/ch40208/introduction/about_this_book.html)
- [MolSSi training Material](http://education.molssi.org)
- [Software Carpentries introduction to Python and Data](https://software-carpentry.org/lessons/)


## License

These materials are made freely available, and are licensed under a [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license. -->
