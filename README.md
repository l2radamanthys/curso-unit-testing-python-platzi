# Prácticas Curso UnitTesting en Python - Platzi 🐍✅

Este repositorio contiene prácticas del curso de **Unit Testing en Python**, utilizando el módulo estándar `unittest`.

---

## 📂 Estructura del proyecto

```
curso-unit-testing-python/
├── src/
│   └── bank_account.py
├── tests/
│   ├── __init__.py
│   ├── test_bank_account.py
│   └── suites.py
└── README.md
```

---

## ⚡️ Ejecutar Tests

### 1. Ejecutar todos los tests

```bash
python -m unittest discover -s tests
```

### 2. Ejecutar todos los tests en modo verbose

```bash
python -m unittest discover -v -s tests
```

### 3. Filtrar tests automáticos por patrón

```bash
python -m unittest discover -s tests -p "test_*.py"
```

### 4. Ejecutar una suite específica de tests

```bash
python tests/suites.py
```

### 5. Ejecutar tests específicos

**Por clase completa:**

```bash
python -m unittest tests.test_bank_account.BankAccountTest
```

**Por un test específico dentro de la clase:**

```bash
python -m unittest tests.test_bank_account.BankAccountTest.test_withdraw
```

---

## 📝 Notas

* Se recomienda ejecutar los tests desde la raíz del proyecto para evitar errores de importación.
* Los tests generan archivos de log (`transactions.log`) que se eliminan automáticamente al finalizar cada prueba para mantener el entorno limpio.
* Todos los mensajes de error y validaciones están en español.

---

## 📚 Recursos

* [Documentación oficial de unittest](https://docs.python.org/3/library/unittest.html)
* [Python Testing en VS Code](https://code.visualstudio.com/docs/python/testing)
