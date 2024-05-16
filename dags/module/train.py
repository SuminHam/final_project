import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

def train_fn(preprocessed_data):
    data = preprocessed_data
    
    y = data['total']
    x = data.drop(columns = ['total'])
   #split data 
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
   
    # XGBRegressor 모델 생성
    model = XGBRegressor()

    # 모델 훈련
    model.fit(x_train, y_train)

    # 모델 훈련 후 예측
    y_pred = model.predict(x_test)