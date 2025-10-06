# 📚 Estructura de Datos - IS-304
> Repositorio oficial de la asignatura **Estructura de Datos** (IS-304) - Carrera de Software, ULEAM

---

## 📋 Información General

| Campo | Información |
|-------|-------------|
| **Asignatura** | IS-304 - Estructura de Datos |
| **Carrera** | Software |
| **Nivel** | 3 |
| **Paralelo** | C |
| **Período Académico** | 2025-2 (Período Ordinario) |
| **Créditos** | 3 |
| **Docente** | Ing. Israel Gómez Calderón |
| **Facultad** | Ciencias de la Vida y Tecnologías |
| **Universidad** | ULEAM - Universidad Laica Eloy Alfaro de Manabí |

---

## 🎯 Descripción del Curso

Esta asignatura desarrolla competencias fundamentales en el diseño, análisis e implementación de estructuras de datos, aplicando conceptos de abstracción, tipos abstractos de datos y análisis de complejidad algorítmica. El curso utiliza Python como lenguaje principal, enfocándose en la resolución de problemas computacionales mediante la selección óptima de estructuras de datos.

### Resultado de Aprendizaje Principal

Generar software que utilice estructuras de datos eficientes para la solución de problemas computacionales, aplicando técnicas de análisis de complejidad y optimización.

---

## 📖 Contenido del Curso

### Unidad 1: Fundamentación de las Estructuras de Datos
- Introducción y Abstracción
- Tipos Abstractos de Datos (TAD)
- Representación y Propiedades de TAD
- Complejidad Algorítmica (Temporal y Espacial)
- Análisis de Algoritmos

### Unidad 2: Estructuras Lineales - Pilas y Colas
- Pilas (Stacks) - Implementación y Aplicaciones
- Colas (Queues) - Implementación y Aplicaciones
- Colas Dobles (Deque)
- Colas de Prioridad
- Aplicaciones prácticas: validadores, evaluadores de expresiones

### Unidad 3: Estructura Lineal - Listas
- Listas Simplemente Enlazadas
- Listas Doblemente Enlazadas
- Listas Circulares
- Iteradores y Protocolos Python

### Unidad 4: Estructuras No Lineales
- Árboles Binarios
- Árboles Binarios de Búsqueda (BST)
- Recorridos de Árboles
- Operaciones de Inserción, Eliminación y Búsqueda

---

## 🗂️ Estructura del Repositorio

```
estructura-datos-2025/
│
├── 📁 Unidad_1_Fundamentacion/
│   ├── TAD/
│   │   ├── ejercicios_basicos/
│   │   ├── ejercicios_intermedios/
│   │   └── ejemplos_resueltos/
│   │
│   └── Complejidad/
│       ├── analisis_algoritmos/
│       └── medicion_rendimiento/
│
├── 📁 Unidad_2_Pilas_Colas/
│   ├── Pilas/
│   │   ├── implementaciones/
│   │   ├── aplicaciones/
│   │   └── validadores/
│   │
│   └── Colas/
│       ├── implementaciones/
│       ├── simulaciones/
│       └── prioridades/
│
├── 📁 Unidad_3_Listas/
│   ├── lista_simple/
│   ├── lista_doble/
│   └── lista_circular/
│
├── 📁 Unidad_4_Arboles/
│   ├── arboles_binarios/
│   ├── arboles_busqueda/
│   └── recorridos/
│
├── 📁 Ejercicios_Practica/
│   └── 25_ejercicios_grupos_1-4.txt
│
├── 📁 Exposiciones/
│   ├── Grupo_1_TAD/
│   ├── Grupo_2_Propiedades_TAD/
│   ├── Grupo_3_Complejidad/
│   ├── Grupo_4_Pilas/
│   ├── Grupo_5_Colas/
│   ├── Grupo_6_Deque/
│   └── Grupo_7_Prioridades/
│
├── 📁 Proyectos/
│   ├── proyecto_parcial_1/
│   └── proyecto_parcial_2/
│
├── 📄 README.md
├── 📄 CONTRIBUTING.md
└── 📄 LICENSE
```

---

## 🔧 Requisitos Previos

### Conocimientos
- Programación Orientada a Objetos (POO)
- Python básico e intermedio
- Estructuras de control y funciones
- Manejo de arreglos y listas

### Software Necesario
- **Python 3.10+** ([Descargar](https://www.python.org/downloads/))
- **IDE recomendado**: 
  - VS Code con extensión Python
  - PyCharm Community Edition
  - Jupyter Notebook
- **Git** para control de versiones

---

## 🚀 Instalación y Configuración

### Clonar el Repositorio

```bash
git clone [https://github.com/israelgo93/EstructuraDatos](https://github.com/israelgo93/EstructuraDatos).git
cd estructura-datos-2025
```

### Crear Entorno Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Instalar Dependencias

```bash
pip install -r requirements.txt
```

### Dependencias Principales
```txt
# requirements.txt
matplotlib>=3.5.0
numpy>=1.21.0
pytest>=7.0.0
black>=22.0.0
pylint>=2.12.0
```

---

## 📊 Evaluación

| Componente | Ponderación | Descripción |
|------------|-------------|-------------|
| **Actuación (C1)** | 30% | Exposiciones, participación en clase, habilidades blandas |
| **Producción (C2)** | 15% | Trabajos autónomos, informes de investigación |
| **Experimentación (C3)** | 20% | Prácticas de laboratorio, implementaciones |
| **Acreditación (C4)** | 35% | Exámenes parciales |

### Distribución por Parcial
- **Primer Parcial**: Unidades 1 y 2
- **Segundo Parcial**: Unidades 3 y 4

---

## 💻 Lenguajes y Tecnologías

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
</p>

---

## 📚 Referencias Bibliográficas

### Textos Principales

1. **Goodrich, M., Tamassia, R., & Goldwasser, M.** (2013)  
   *Data Structures and Algorithms in Python*  
   John Wiley & Sons

2. **Miller, B., & Ranum, D.** (2011)  
   *Problem Solving with Algorithms and Data Structures using Python*  
   Franklin, Beedle & Associates

3. **Cormen, T., Leiserson, C., Rivest, R., & Stein, C.** (2022)  
   *Introduction to Algorithms* (4th Edition)  
   MIT Press

### Recursos en Línea

- [Documentación Oficial de Python](https://docs.python.org/3/)
- [Python Data Structures - Real Python](https://realpython.com/tutorials/data-structures/)
- [Visualgo - Visualización de Algoritmos](https://visualgo.net/)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

---

## 👨‍💻 Sobre el Docente

**Ing. Israel Gómez Calderón**
- 📧 Email: [israel.gomez@uleam.edu.ec](mailto:israel.gomez@uleam.edu.ec)
- 🏫 Facultad de Ciencias de la Vida y Tecnologías
- 🎓 Carrera de Software - ULEAM

### Horario de Clases
- **Lunes**: 10:00 AM - 1:00 PM
- **Viernes**: 7:00 AM - 9:00 AM

### Horario de Consultas
Coordinar previamente por correo electrónico o Aula Virtual.

---

## 🤝 Contribuciones

Este repositorio está destinado principalmente para fines académicos. Sin embargo, se aceptan contribuciones de:

### Estudiantes del Curso
- Correcciones de errores
- Optimizaciones de código
- Documentación adicional
- Casos de prueba

### Cómo Contribuir

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

### ⭐ Si este repositorio te fue útil, considera darle una estrella

**Última actualización**: Octubre 2025

**© 2025 ULEAM - Universidad Laica Eloy Alfaro de Manabí**

[🔝 Volver arriba](#-estructura-de-datos---is-304)

</div>
