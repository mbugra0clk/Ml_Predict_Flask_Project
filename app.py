from flask import Flask, request, render_template
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Flask uygulaması
app = Flask(__name__)

# Veri ve model hazırlığı
df = pd.read_csv('C:\ML\Ml_Flask_Project\student_lifestyle_dataset.csv')

# Gereksiz sütunu kaldır
if 'Student_ID' in df.columns:
    df = df.drop(columns=['Student_ID'])

# Kategorik değişkenleri dönüştür (One-Hot Encoding)
encoder = OneHotEncoder(sparse_output=False)
encoded_array = encoder.fit_transform(df[['Stress_Level']])
encoded_columns = encoder.get_feature_names_out(['Stress_Level'])

data_encoded = pd.DataFrame(encoded_array, columns=encoded_columns)
df = pd.concat([df.drop(columns=['Stress_Level']), data_encoded], axis=1)

# Hedef değişken ve özellikleri ayırdım
target_column = 'GPA'
features = df.drop(columns=[target_column])
target = df[target_column]

# Eğitim ve test veri setlerini ayır
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Modeli oluştur ve eğit
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Ana sayfa rotası
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Eğitimde kullanılan tüm özellikler
        all_features = features.columns
        
        # Kullanıcıdan gelen veriler
        user_input = {
            'Study_Hours_Per_Day': float(request.form['Study_Hours_Per_Day']),
            'Extracurricular_Hours_Per_Day': float(request.form['Extracurricular_Hours_Per_Day']),
            'Sleep_Hours_Per_Day': float(request.form['Sleep_Hours_Per_Day']),
            'Social_Hours_Per_Day': float(request.form['Social_Hours_Per_Day']),
            'Physical_Activity_Hours_Per_Day': float(request.form['Physical_Activity_Hours_Per_Day']),
            'Stress_Level_High': 1 if request.form['Stress_Level'] == 'High' else 0,
            'Stress_Level_Low': 1 if request.form['Stress_Level'] == 'Low' else 0,
            'Stress_Level_Moderate': 1 if request.form['Stress_Level'] == 'Moderate' else 0,
        }

        # Kullanıcı girdisini veri çerçevesine dönüştür
        input_data = pd.DataFrame([user_input])
        
        # Eksik sütunları sıfır ile doldur
        for col in all_features:
            if col not in input_data.columns:
                input_data[col] = 0

        # Sütun sırasını eğitimdeki gibi ayarla
        input_data = input_data[all_features]

        # Model ile tahmin yap
        prediction = model.predict(input_data)
        score = model.score(X_test, y_test)

        # Sonuçları result.html'e gönder
        return render_template('result.html', prediction=round(prediction[0], 2), score=round(score, 2))
    except Exception as e:
        return f"Bir hata oluştu: {e}"

if __name__ == '__main__':
    app.run(debug=True)