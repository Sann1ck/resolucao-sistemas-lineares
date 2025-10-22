# Resolução de Sistemas Lineares (Método do Escalonamento)

Este projeto implementa o **método de Gauss-Jordan** em Python para resolver sistemas lineares de qualquer tamanho, determinando automaticamente se o sistema é:

- **S.P.D** – Sistema Possível Determinado  
- **S.P.I** – Sistema Possível Indeterminado  
- **S.I** – Sistema Impossível  

---

## 🧠 Descrição

O algoritmo realiza o processo completo de **escalonamento** (eliminação de Gauss) e **retro-substituição**, 
identificando automaticamente o tipo de sistema e apresentando a solução formatada.

---

## 🧮 Exemplo de uso

 2x +  y + z = 8
-3x + -y + 2z = -11
-2x +  y + 2z = -3

### Entrada (`entrada.txt`):
```
2 1 -1 8
-3 -1 2 -11
-2 1 2 -3
```

### Execução:
```bash
python escalonamento.py < entrada.txt
```

### Saída:
```
Sistema Possível Determinado (S.P.D)
Solução: (2.00, 3.00, -1.00)
```

---

## 🗂 Estrutura do projeto

```
resolucao-sistemas-lineares/
│
├── escalonamento.py
├── README.md
└── entrada.txt
```

---

## ⚙️ Requisitos

- Python 3.7 ou superior  
- Nenhuma biblioteca externa é necessária

---

## 💡 Observação

O código foi desenvolvido com fins **didáticos**, servindo como apoio para o estudo do método de **escalonamento (Gauss-Jordan)** e manipulação de matrizes em Python puro.

---

## ✨ Autor

Desenvolvido por **Daniel Sant'Anna de Araújo**
