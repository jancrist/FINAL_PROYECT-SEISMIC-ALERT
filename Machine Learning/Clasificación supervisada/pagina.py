import streamlit as st 
import pickle 
import pandas as pd

with open(r'C:\Users\rodri\OneDrive\Escritorio\proyecto_final\lin_reg.pkl', 'rb') as li:
    lin_reg = pickle.load(li)

with open(r'C:\Users\rodri\OneDrive\Escritorio\proyecto_final\log_reg.pkl', 'rb') as lo:
    log_reg = pickle.load(lo)

with open(r'C:\Users\rodri\OneDrive\Escritorio\proyecto_final\svc_m.pkl', 'rb') as sv:
    svc_m = pickle.load(sv)

def classify(num):
    if num == 0:
        return 'Peligrosidad baja'
    
    elif num == 1:
        return 'Peligrosidad media'
    
    else:
        return 'Peligrosidad alta'

def main():
    st.title('Peligrosidad de sismos')

    st.sidebar.header('Parametros para el usuario')

    def user_input_parameters():
        Profundidad = st.sidebar.slider('Profundidad', -3.78, 655.267)
        Magnitud = st.sidebar.slider('Magnitud', 0.00, 12.00)
        data = {'depth' : Profundidad,
                'mag' : Magnitud
        }
        features = pd.DataFrame(data, index = [0])
        return features

    df = user_input_parameters()

    option = ['Regresión Lineal', 'Regresión Logística', 'SVM']
    model = st.sidebar.selectbox('Elege el modelo que quieres usar', option)
    
    st.subheader('Parametros seleccionados')
    st.subheader(model)
    st.write(df)

    if st.button('RUN'):
        if model == 'Regresión Lineal':
            st.success(classify(lin_reg.predict(df)))
        elif model == 'Regresión Logística':
            st.success(classify(log_reg.predict(df)))
        else:
            st.success(classify(svc_m.predict(df)))

if __name__ == '__main__':
    main()