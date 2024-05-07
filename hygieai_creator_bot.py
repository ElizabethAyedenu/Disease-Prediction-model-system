#what should this bot do
#it should generate a dataset of n rows of data for malaria patients
# columns(symptoms): id, fever, gender, cold, sweating, headache,severity,muscle pain,nausea, vomiting.
#dtypes: id-nominal(int), symptoms-boolean(0-false|1-True)gender-category(male|female),severity-category(Nil|Mild|Severe).
import random
import pandas as pd

def NRows():
    nrows = int(input("enter number of rows: "))
    return nrows

# def id(nrows):
#     ID = []                                   mine
#     for x in range(nrows):
#         ID.append(x + 1)
#     return ID

# def gender(nrows):
#     Genders = ['male', 'female']
#     Gender = []
#     for items in range(nrows):                    mine
#         Gender.append(random.choice(Genders))
#     return Gender

'''def fever(nrows):
    diag = ['Yes', 'No']
    status = []
    for items in range(nrows):
        status.append(random.choice(diag))
    return status
'''
    
def malaria(nrows):
    diag = [1, 0]
    Mal_Symptoms = ['weight_gain', 'belly pain and loss of appetite', 'feeling tired', 'headache', 'muscle_and_joint_pain', 'hair loss and skin problems', 'trouble_sleeping', 'memory_loss', 'hearing_loss', 'depression and anxiety', 'sore_throat', 'diarrhoea', 'bleeding', 'nausea', 'vomiting', 'hiccups', 'shortness_of_breath', 'maculopapular_rash', 'shock_from_fluid_loss']
    symptom_data = {}
    

    for symptom_name in Mal_Symptoms:
        symptom_status = []
        for i in range(nrows):
            symptom_status.append(random.choice(diag))
        symptom_data[symptom_name] = symptom_status

    return symptom_data




def diabetes(nrows):
    diag = [1, 0]
    betes_symptoms = ['very_dry_skin', 'sores_that_heal_slowly', 'more_infections_than_usual', 'nausea', 'stomach_pains', 'urinate_a_lot', 'feel_very_thirsty', 'lose_weight_without_trying', 'blurry_vision', 'itching_hands_or_feet', 'feel_very_hungry']
    betes_symptom_data = {}

    for symptom_name in betes_symptoms:
        symptom_status = []
        for i in range(nrows):
            symptom_status.append(random.choice(diag))
        betes_symptom_data[symptom_name] = symptom_status

    return betes_symptom_data

'''def severity(nrows,symptom_data):
    for k,v in symptom_data.items()
        if k'''
    

    



nrows = NRows()
# ids = id(nrows) mine
# genders = gender(nrows) mine
# fever_statuses = fever(nrows)
symptom_data = malaria(nrows)
symptom_data_betes = diabetes(nrows)

# malaria={'id':ids,'Gender':genders} useful his
mal = {}
mal.update(symptom_data)


betes = {}
betes.update(symptom_data_betes)

malaria_df = pd.DataFrame(mal)
malaria_df.to_csv('malaria_df.csv', index=False)

diabetes_df = pd.DataFrame(betes)
diabetes_df.to_csv('diabetes_df.csv', index=False)
#print(ids)
#print(genders)
#print(fever_statuses)
#for symptom_name, status_list in symptom_data.items():
    #print(f"{symptom_name}: {status_list}")
            
    