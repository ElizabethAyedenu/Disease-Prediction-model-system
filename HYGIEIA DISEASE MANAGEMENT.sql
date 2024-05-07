CREATE DATABASE Hygieia_Disease_management;
USE Hygieia_Disease_management;
-- DROP DATABASE Hygieia_Disease_management; 

create table patient (
	patient_id INT AUTO_INCREMENT PRIMARY KEY,
	patient_first_name  VARCHAR(50),
	patient_last_name  VARCHAR(50),
	age INT,
	gender VARCHAR(50),
	weight INT,
	hereditary_status VARCHAR(3)
);
CREATE TABLE disease(
disease_id INT AUTO_INCREMENT,
disease_name VARCHAR(50),
disease_type VARCHAR (20),
PRIMARY KEY (disease_id)
);

CREATE TABLE confirmatory_test(
confirmatory_test_id INT AUTO_INCREMENT,
confirmatory_test_name VARCHAR(30),
PRIMARY KEY (confirmatory_test_id)
);

CREATE TABLE symptom(
symptom_id INT AUTO_INCREMENT,
very_dry_skin int, sores_that_heal_slowly int, more_infections_than_usual int,
nausea int, stomach_pains int, urinate_a_lot int, feel_very_thirsty int, 
lose_weight_without_trying int, blurry_vision int, itching_hands_or_feet int, feel_very_hungry int, 
fever int, fatigue int, loss_of_appetite int, vomiting int, abdominal_pain int, dark_urine int, 
light_colored_stools int , joint_pain int , jaundice int , rash int , bone_pain int, pain_in_joint int, 
muscle_pain int, cramp int, eye_pain int, cough_with_yellow_or_green_mucus int, shortness_of_breath int, 
high_temperature int, chest_pain int, aching_body int, feeling_very_tired int, wheezing_noises_when_you_breathe int,
feeling_confused int, feverish int, cold int, sweating int, headache int, pain_in_muscle int, dizzy int, 
cough int, fatigue_ int, short_of_breath int, loss_of_taste_or_smell int, nasal_congestion int, 
runny_nose int, throat_soreness int, diarrhea int, eye_irritation int, headaches int, kidney_failure int, 
respiratory_failure int, weight_gain int, belly_pain int, feeling_tired int, muscle_and_joint_pain int, 
hair_loss_and_skin_problem int, trouble_sleeping int, memory_loss int, hearing_loss int, depression_and_anxiety int, 
throat_sore int, dysentry int, bleeding int, dizziness int, hiccups int, maculopapular_rash int, shock int,
disease_id INT,
PRIMARY KEY (symptom_id),
FOREIGN KEY (disease_id) REFERENCES disease(disease_id)
);

CREATE TABLE diagnosis(
diagnosis_id INT AUTO_INCREMENT,
patient_id INT,
symptom_id INT,
confirmatory_test_id INT,
result varchar(20),
PRIMARY KEY (diagnosis_id),
FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
FOREIGN KEY (symptom_id) REFERENCES symptom(symptom_id),
FOREIGN KEY (confirmatory_test_id) REFERENCES confirmatory_test(confirmatory_test_id)
);
-- SELECT diagnosis.diagnosis_id, diagnosis.patient_id, diagnosis.symptom_id, symptom_name, symptom_type, cause, disease_id,
-- diagnosis.confirmatory_test_id, confirmatory_test.confirmatory_test_name, diagnosis.result
-- FROM diagnosis, symptom, confirmatory_test
-- WHERE diagnosis.symptom_id = symptom.symptom_id;
SELECT * FROM symptom JOIN disease ON symptom.disease_id = disease.disease_id

-- drop table diagnosis;



