# 🧠 ML_student-performance

### 🇪🇸 Predicción del rendimiento académico de estudiantes con Machine Learning  
### 🇬🇧 Predicting student academic performance using Machine Learning

---

## 📌 Descripción del problema | Problem Description

### 🇪🇸
Este proyecto tiene como objetivo predecir la nota final (`G3`) de estudiantes de secundaria, utilizando datos sociodemográficos, familiares y de estilo de vida. El propósito es identificar patrones que puedan ayudar a detectar a estudiantes en riesgo o con alto potencial académico.

### 🇬🇧
This project aims to predict the final grade (`G3`) of high school students using sociodemographic, family, and lifestyle data. The goal is to find patterns that may help identify students at risk or with high academic potential.

---

## 📊 Dataset

### 📁 Archivos utilizados:
- `student-mat.csv`
- `student-por.csv`

Fuente original: [UCI Machine Learning Repository - Student Performance Data Set](https://archive.ics.uci.edu/ml/datasets/student+performance)

Los datos fueron fusionados usando claves comunes como escuela, edad, sexo, etc., generando un nuevo dataset con 382 estudiantes. Se creó una muestra ligera para este proyecto: `student-merged-sample.csv`.

---

## 🤖 Solución adoptada | Adopted solution

1. **EDA (Análisis exploratorio de datos)**  
   - Distribuciones de variables
   - Correlaciones con la nota final

2. **Preprocesamiento**  
   - Codificación de variables categóricas
   - División en conjuntos de entrenamiento y prueba

3. **Modelado**  
   - Modelos probados: Regresión lineal, Random Forest  
   - Métricas usadas: MAE, RMSE

4. **Resultado**  
   - El modelo seleccionado fue Random Forest por su mejor desempeño

5. **Exportación del modelo**  
   - Guardado en `src/models/final_model.pkl` usando `joblib`

---

## 📁 Estructura del proyecto | Project Structure

```plaintext
ML_student-performance/
│
├── README.md
└── src/
    ├── data_sample/          # Subconjunto del dataset (máx 5MB)
    │   ├── student-mat.csv
    │   ├── student-por.csv
    │   └── student-merged-sample.csv
    │
    ├── img/                  # Gráficos de EDA y evaluación
    ├── notebooks/            # Notebooks de desarrollo y pruebas
    │   └── merge_and_clean.ipynb
    │
    ├── results_notebook/     # Notebook final limpio
    │   └── final_model.ipynb
    │
    ├── models/               # Modelo final entrenado (.pkl)
    │   └── final_model.pkl
    │
    └── utils/                # Scripts auxiliares
        └── data_merge.py

```

## 🧾 Requisitos

- Python 3.10+
- pandas, numpy, seaborn, matplotlib
- scikit-learn
- joblib

Instalar con:

```bash
pip install -r requirements.txt

```

## 🎥 Presentación

El proyecto cuenta con una presentación complementaria explicando los resultados y el enfoque usado.  
**Formato**: PDF o presentación sin software comercial. *(Disponible en el repositorio si es entregada)*

The project includes a companion presentation explaining the results and the approach used.
**Format**: PDF or presentation without commercial software. *(Available in the repository if submitted)*

---

## 📬 Autora | Author

**annahico**  

Proyecto para evaluación del curso de Machine Learning del Bootcamp Data Science en The Bridge.

Project for evaluation of the Machine Learning course of the Data Science Bootcamp at The Bridge.