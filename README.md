# Home Credit Default Risk — Machine Learning

Proyecto de Machine Learning orientado a la predicción de riesgo de incumplimiento crediticio,
desarrollado como parte del Examen de Machine Learning.

## Objetivo
Construir un modelo de clasificación binaria que estime la probabilidad de default de un cliente,
integrando múltiples fuentes de información financiera y aplicando buenas prácticas de
ingeniería de características, validación y despliegue.

---

## Metodología
Se utilizó la metodología **CRISP-DM**, separando el proyecto en las siguientes fases:

- Data Understanding
- Data Preparation
- Feature Engineering
- Modeling
- Evaluation
- Deployment

---

##  Estructura del proyecto
HomeCredit/
│
├── data/ # Datos en formato parquet
├── artifacts/ # Modelo entrenado
│ └── home_credit_model.joblib
│
├── examen_HOME_CREDIT.ipynb # Notebook principal
│
└── README.md


---

## Fuentes de datos
- application
- bureau
- previous_application
- installments_payments
- POS_CASH_balance

Las tablas fueron agregadas a nivel cliente (`SK_ID_CURR`) antes de su integración.

---

## Modelado
- Modelo: Regresión Logística
- Manejo de desbalance: `class_weight='balanced'`
- Validación: Stratified K-Fold Cross Validation
- Métrica principal: AUC-ROC

AUC promedio obtenido: **~0.63** (baseline aceptable para problema desbalanceado).

---

##  API (prototipo)
Se implementó una API con FastAPI que expone un endpoint `/evaluate_risk`
para retornar la probabilidad de default y una recomendación de decisión.

---

##  Conclusión
El modelo desarrollado constituye una línea base sólida y reproducible,
con posibilidades claras de mejora futura mediante modelos más complejos
y optimización de hiperparámetros.

---

## Creadores:
Joscelynne Díaz y Joaquin Medina 
