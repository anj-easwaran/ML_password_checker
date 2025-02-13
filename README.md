# ML_password_checker

# Password Strength Checker

## Summary
This project is a **Password Strength Checker** that uses Machine Learning to evaluate password strength. The application is built using Python, Tkinter, and Scikit-Learn, featuring a simple graphical user interface (GUI) that allows users to test their passwords.

## TO-NOTE

The script uses multi-core processing to speed up the model-building process.

## Machine learning model
- **Ensemble Learning**: Combines multiple decision trees to improve accuracy and reduce overfitting.
- **Combats Overfitting**: Unlike individual decision trees, Random Forest generalizes better by averaging multiple models.
- **Combats noisy data**: Less sensitive to outliers or minor variations in password structures.
= **Other features:**
- Identifies important character patterns without manual selection.
- Captures complex relationships between character sequences and password strength.
- Can efficiently train on large datasets with multiple processors.
- Can process many passwords quickly due to parallel processing.


## Technologies Used
- Python 
- Tkinter (GUI Framework)
- Pandas (Data Processing)
- NumPy (Numerical Operations)
- Scikit-Learn (Machine Learning)

## Installation & Setup
### Prerequisites
Ensure you have **Python 3.7+** installed. Install dependencies with:
```bash
pip install pandas numpy scikit-learn tkinter
```

### Running the Application
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   cd password-strength-checker
   ```
2. Place your dataset (`data.csv`) in the project directory.
3. Run the application:
   ```bash
   python password_checker.py
   ```

## 📌 How It Works
1. Reads `data.csv` containing passwords and their strength labels.
2. Uses TF-IDF Vectorization to transform passwords and trains Random Forest Classifier.
3. Users enter a password in the Tkinter GUI.
4. The model analyzes and predicts the strength as Weak, Medium, or Strong.
5. Updates the GUI with a color-coded message indicating password strength.

## 🏆 Example
| Password        | Prediction  | Color  |
|---------------|------------|--------|
| `1234`       | Weak       | 🔴 Red |
| `helloWorld` | Medium     | 🟠 Orange |
| `P@ssw0rd!`  | Strong     | 🟢 Green |

