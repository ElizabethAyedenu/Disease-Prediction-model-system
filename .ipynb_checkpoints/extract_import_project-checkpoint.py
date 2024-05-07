import mysql.connector
from bs4 import BeautifulSoup
import requests

try:
    
        


    
    # request website url
    website =requests.get("https://www.cdc.gov/parasites/malaria/index.html")
    website_2= requests.get("https://en.wikipedia.org/wiki/Malaria")
    website_3= requests.get("https://en.wikipedia.org/wiki/Parkinson's_disease")
    website_4 = requests.get("https://en.wikipedia.org/wiki/HIV%2FAIDS#Signs_and_symptoms")
    website_4a= requests.get('https://en.wikipedia.org/wiki/Influenza-like_illness')
    website_5= requests.get('https://en.wikipedia.org/wiki/Cholera')
    website_6= requests.get('https://www.who.int/news-room/fact-sheets/detail/ebola-virus-disease')
    website_6a= requests.get('https://en.wikipedia.org/wiki/Ebola#Signs_and_symptoms')
    website_7 = requests.get('https://en.wikipedia.org/wiki/COVID-19')


    website.raise_for_status()
    website_2.raise_for_status()
    website_3.raise_for_status()
    website_4.raise_for_status()
    website_5.raise_for_status()
    website_6.raise_for_status()
    website_6a.raise_for_status()
    website_7.raise_for_status()

    # beautiful soup parser
    soup = BeautifulSoup(website.text,"html.parser")
    soup2 = BeautifulSoup(website_2.text,"html.parser")
    soup3 = BeautifulSoup(website_3.text,"html.parser")
    soup4a= BeautifulSoup(website_4a.text, 'html.parser')
    soup4 = BeautifulSoup(website_4.text,"html.parser")
    soup5= BeautifulSoup(website_5.text,'html.parser')
    soup6= BeautifulSoup(website_6.text,'html.parser')
    soup6a= BeautifulSoup(website_6a.text,'html.parser')
    soup7 = BeautifulSoup(website_7.text,'html.parser')

    
    # Disease Names
    disease_name = soup.find("div", class_="card-body pt-0 bg-white").strong.text
    print(disease_name)
    disease_name_2 = soup3.find('table', class_= "infobox").tr.text
    print(disease_name_2)
    disease_name_3 = soup4.find("table", class_= 'infobox').tr.text
    print(disease_name_3)
    disease_name_4= soup5.find('table', class_='infobox').tr.text
    print(disease_name_4)
    disease_name_5 = soup6a.find('table', class_='infobox').tr.text
    print(disease_name_5)
    disease_name_6 = soup7.find('table',class_='infobox').tr.text
    print(disease_name_6)

       
    
    # Disease cause
    c= soup3.find_all('p')[26]
    c2=soup4.find('table', class_='infobox').find('tbody')
    c3=soup5.find('table',class_='infobox').tbody
    c4= soup7.find('table', class_= 'infobox').find_all('tr')
    park1= c.get_text().split(".")[3].split(" ")[11]
    park2=c.find_all('a')[5].get_text()
    malaria= soup.find("div", class_="card-body pt-0 bg-white").get_text(strip=True).split(" ")[7].strip(".")
    parkinson= park1+' '+"and"+' '+park2
    hiv_aids= c2.find_all('tr')[8].td.get_text().strip('[4]')
    cholera= c3.find_all('tr')[9].i.get_text()
    ebo_cause= 'ebola virus'
    covid_19 = c4[10].td.text
    
    print('successful_1')
    
     

    # Disease Symptoms

    # SCRAPPING FROM PARENT BODY
    # MALARIA
    sym_name= soup2.find('tbody')
    symname= soup2.find('p')

    # SCRAPPING FROM PARENT BODY PARKINSON
    parkin=soup3.find('table', class_= "infobox").tbody

       
    # # SCRAPPING FROM DAUGHTER BODY MALARIA

    s2= symname.find_all('a')[6]
    s3=symname.find_all('a')[11]
    s= sym_name.find_all('tr')[5]
    addsym=soup2.find_all('p')[6]
    addsym1=soup2.find_all('p')[4]
    addsym2=soup2.find_all('p')[5]
    complication= sym_name.find_all('tr')[6]
    diagnosis= sym_name.find_all("tr")[9]
    print('successful_2')

   
    # SCRAPPING FROM DAUGHTER BODY PARKINSON
    p=parkin.find_all("tr")[5]
    complication_2= parkin.find_all('tr')[5]
    diagnosis_2=parkin.find_all('tr')[10]
    diagnosis_3=parkin.find_all('tr')[9]
    print('successful_3')

    

    # SCRAPPING FROM  HIV/AIDS
    hiv= soup4a.find('div', class_= 'mw-content-ltr mw-parser-output')
    complication_3=soup4.find('table', class_="infobox").tbody
    print('successful_4')

  
    # # MALARIA SYMPTOMS

    s4=addsym1.get_text().split(" ")
    sy=addsym1.get_text().split(",")
    signs=addsym2.get_text().split(",")

    sym=s.find('td').get_text().split(",")[0]
    sym1=s.find('td').get_text().split(",")[1]
    sym2=s.find('td').get_text().split(",")[2]
    sym3=s.find('td').get_text().split(",")[3].strip("[1]")
    symp=s2.get_text()
    symp1=s3.get_text()
    s5=s4[6]
    s6=s4[24]
    s7=s4[47].strip(",")
    s8=s4[50].split(".")
    s9=s8[0]
    sy1=sy[3]
    sy2=signs[6]
    sy3=signs[8]
    sy4=signs[10]
    sy5=signs[11]
    sy6=signs[12].split(" ")[2].split(".")[0]
    addsymp=addsym.find('a').get_text()
    print('successful_5')

     # #   MALARIA COMPLICATION/ PART OF SYMPTOMS
    comp=complication.find('td').get_text().split(",")[0]
    comp1=complication.find('td').get_text().split(",")[1]
    comp2=complication.find('td').get_text().split(",")[2].strip("[1]")
    comp3=complication.find('td').get_text().split(",")[3]
    comp4=complication.find('td').get_text().split(",")[4].strip("[2]")
    print('successful_6')
    malaria_symptom =[sym,sym1,sym2,sym3,symp,symp1,s5,s6,s7,s9,sy1,sy2,sy3,sy4,sy5,sy6,addsymp,comp,comp1,comp2,comp3,comp4]
    
    # print(malaria_symptom)
    

    # PARKINSON SYMPTOMS
    park_sym=p.find('td').get_text().split(",")[0]
    park_sym1=p.find('td').get_text().split(",")[1]
    park_sym2=p.find('td').get_text().split(",")[2]
    park_sym3=p.find('td').get_text().split(",")[3].strip("[1]")
    print('successful_7')

    # PARKINSON COMPLICATION
    comp_2=complication_2.find('td').get_text().split(",")[0]
    comp_3=complication_2.find('td').get_text().split(",")[1]
    comp_4=complication_2.find('td').get_text().split(",")[2]
    comp_5=complication_2.find('td').get_text().split(",")[3].strip("[2] ")
    comp_6=complication_2.find('td').get_text().split(",")[4].strip("and ")
    print('successful_8')

    parkinson_symptom = [park_sym,park_sym1,park_sym2,park_sym3,comp_2,comp_3,comp_4,comp_5,comp_6]


   #  HIV/AIDS SYMPTOMS
    h_text=hiv.find_all('p')[1].get_text()
    h=h_text.split(',')[2].split(' ')[19]
    h1=h_text.split(',')[3]
    h2=h_text.split(',')[4]
    h3=h_text.split(',')[5]
    h4=h_text.split(',')[6]
    h5=h_text.split(',')[7]
    h6=h_text.split(',')[8]
    h7=h_text.split(',')[9]
    h8=h_text.split(',')[10].split(' ')[2]
    h_text2 = soup4.find_all('p')[12].get_text()
    h9= h_text2.split(',')[3]
    h10= h_text2.split(',')[4]
    ha= h_text2.split(',')[5].strip('a ')
    hb= h_text2.split(',')[6]
    hc= h_text2.split(',')[7]
    hd= h_text2.split(',')[8].strip('and/or ').split('.')[0]
    he= h_text2.split(',')[12].split(' ')[3]
    hf_= h_text2.split(',')[12].split(' ')[5]
    hg= "CD4+ less than 200"
    print('successful_9')

    # HIV COMPLICATIONS
    comp_7=complication_3.find_all('td')[5].get_text().split(',')[0]
    comp_8=complication_3.find_all('td')[5].get_text().split(',')[1].strip('[4]')
    print('successful_10')
    hiv_symptom = [h,h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,ha,hb,hc,hd,he,hf_,hg,comp_7,comp_8]
          
    
    # CHOLERA SYMPTOMS
    
    cho= soup5.find('table',class_='infobox').find_all("tr")[5].td.get_text().split(',')
    cho1=cho[0]
    cho2=cho[1]
    cho3=cho[2].strip('[2][3]')
    cho_2= soup5.find('div', class_="mw-body-content").find_all('p')[7].text.split(',')
    cho_3= soup5.find('div', class_="mw-body-content").find_all('p')[7].text.split(',')[0].split('.')[1].split(' ')[8]
    cho_4= soup5.find('div', class_="mw-body-content").find_all('p')[7].text.split(',')[0].split('.')[1].split(' ')[9]
    cho4= cho_3+" "+cho_4
    cho5 = cho_2[1]
    cho6 = cho_2[2]
    cho7 = cho_2[3].strip(' or ').strip('Kussmaul breathing').strip('.')
    cho8 = cho_2[4].strip('a ')
    cho9 = cho_2[6]
    cho10= cho_2[9]
    cho11 = cho_2[10].split(' ')[3]
    print('success_1')

     # CHOLERA COMPLICATIONS
    complication_4= soup5.find('table', class_= 'infobox').tbody
    comp_9= complication_4.find_all('tr')[6].td.get_text().split(',')[0]
    comp_10= complication_4.find_all('tr')[6].td.get_text().split(',')[1].strip('[2]')
    print('success_2')
    cholera_symptoms = [cho1,cho2,cho3,cho4,cho5,cho6,cho7,cho8,cho9,cho10,cho11,comp_9,comp_10]
    

    # EBOLA SYMPTOMS
    ebola= soup6.find('article', class_='sf-detail-body-wrapper').find_all('ul')[2]
    eb1= ebola.find_all('li')[0].get_text()
    eb2= ebola.find_all('li')[1].get_text()
    eb3= ebola.find_all('li')[2].get_text()
    eb4= ebola.find_all('li')[3].get_text()
    eb5= ebola.find_all('li')[4].get_text()
    eb6= ebola.find_all('li')[5].get_text()
    eb7= ebola.find_all('li')[6].get_text()
    eb8= ebola.find_all('li')[7].get_text()
    eb9= ebola.find_all('li')[8].get_text()
    eb10= ebola.find_all('li')[9].get_text()
    eb11= ebola.find_all('li')[10].get_text()
    ebola_2= soup6a.find('table', class_='infobox').find_all('tr')[5]
    e1= ebola_2.find_all('a')[2].get_text()
    e2= ebola_2.find_all('a')[5].get_text()
    e3= ebola_2.find_all('a')[6].get_text().strip(' [1]')
    e4= soup6a.find_all('p')[6].get_text().split('.')[3].split(',')[0].split(' ')[6]
    e5= soup6a.find_all('p')[6].get_text().split('.')[3].split(',')[1]
    e6= soup6a.find_all('p')[6].get_text().split('.')[3].split(',')[2]
    e7= soup6a.find_all('p')[6].find_all('a')[13].text
    e8= soup6a.find_all('p')[6].find_all('a')[16].text
    e9= soup6a.find_all('p')[6].find_all('a')[18].text
    e10= soup6a.find_all('p')[6].find_all('a')[19].text
    e11= soup6a.find_all('p')[6].find_all('a')[20].text
    e12= soup6a.find_all('p')[6].find_all('a')[24].text
    print('success_3')
        
    # EBOLA COMPLICATIONS
    ebo_comp= soup6a.find('table', class_='infobox').find_all('tr')[6].td.get_text().strip('[2]')
    print('success_4')

    ebola_symptoms = [eb1,eb2,eb3,eb4,eb5,eb6,eb7,eb8,eb9,eb10,eb11,e1,e2,e3,e4,e5,e6,e7,e9,e10,e11,e12,ebo_comp]

    # COVID SYMPTOMS
    covid2= soup7.find_all('p')[7]
    covid3= soup7.find_all('p')[8]
    covid_1= c4[6].td.get_text().split(',')
    cov1=covid_1[0]
    cov2=covid_1[1]
    cov3=covid_1[2]
    cov4=covid_1[3]
    cov5=covid_1[4]
    cov6=covid_1[5].split(';')[0]
    cov7 = covid2.find_all('a')[8].get_text()
    cov8 = covid2.find_all('a')[9].get_text()
    cov9 = covid2.find_all('a')[10].get_text()
    cov10 = covid2.find_all('a')[11].get_text()
    cov11 = covid2.find_all('a')[12].get_text()
    cov12 = covid2.find_all('a')[13].get_text()
    cov13 = covid2.find_all('a')[7].get_text()
    cov14 = covid3.find_all('a')[1].get_text()
    cov15 = covid3.find_all('a')[2].get_text()
    co1 = covid3.find_all('a')[3].get_text()
    co2 = covid3.find_all('a')[4].get_text()
    co3 = covid3.find_all('a')[5].get_text()
    co4 = "toes swelling or turning purple"
    print('success_5')
    
    # COVID COMPLICATIONS
    cov_= soup7.find('table', class_= 'infobox').find_all('tr')[7]
    cov_comp = cov_.find('td').find_all('a')[0].get_text()
    cov_comp1 = cov_.find('td').find_all('a')[1].get_text()
    cov_comp2 = cov_.find('td').find_all('a')[2].get_text()


    cov_comp3 = cov_.find('td').find_all('a')[3].get_text()
    cov_comp4 = cov_.find('td').find_all('a')[4].get_text()
    cov_comp5 = cov_.find('td').find_all('a')[5].get_text()
    cov_comp6 = cov_.find('td').find_all('a')[6].get_text()
    cov_comp7 = cov_.find('td').find_all('a')[7].get_text()

    covid_symptoms = [cov3,cov4,cov5,cov6,cov7,cov8,cov9,cov10,cov11,cov12,cov13,cov14,cov15,co1,co2,co3,co4,cov_comp,cov_comp1,cov_comp2,cov_comp3,cov_comp4,cov_comp5,cov_comp6,cov_comp7]
  
   
    # #  MALARIA DIAGNOSIS
    mal_diag= diagnosis.find('td').get_text().split(",")[0]
    mal_diag2= diagnosis.find("td").get_text().split(",")[1].strip("[1]")
    malaria_test = [mal_diag,mal_diag2]
    print('success_6')  
    

    # PARKINSON DIAGNOSIS
    park_diag_1= diagnosis_2.th.get_text()
    park_diag_2=diagnosis_3.th.get_text()
    parkinson_test = [park_diag_1,park_diag_2]
    print('success_7')
    

    # HIV DIAGNOSIS
    diagnosis_4= soup4.find('table', class_= 'infobox').tbody
    h_diag3=diagnosis_4.find_all('td')[9].get_text().strip('[4]')
    hiv_test = [h_diag3]
    print('success_8') 


    # CHOLERA DIAGNOSIS
    cho_diag= complication_4.find_all('tr')[11].td.get_text().strip('[2]')
    cholera_test= [cho_diag]
    print('success_9')

    # EBOLA DIAGNOSIS
    ebola_diag = soup6a.find('table', class_='infobox').find_all('tr')[9].th.get_text()
    ebola_diag2 = soup6a.find('table', class_='infobox').find_all('tr')[10].th.get_text()
    ebola_test = [ebola_diag, ebola_diag2]
    print('success_10')

    
    # COVID DIAGNOSIS
    covid_diag1 = c4[11].td.text.split(',')[0]
    cov_diag2 = c4[11].td.text.split(',')[1]
    cov_diag3 =  c4[11].td.text.split(',')[2]
    covid_test = [covid_diag1,cov_diag2,cov_diag3]
    print('final_success')

    # POPULATE VALUES IN MYSQL
    db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="pharmacist",
    database="hygieia_disease_management"
    )
    if db.is_connected==False:
        print("not connected")
    else:
        print ("connected")
    mycursor=db.cursor()
    mycursor.execute("INSERT INTO disease(disease_name,disease_type) VALUES(%s,%s)", (disease_name,"Type A"))
    mycursor.execute("INSERT INTO disease(disease_name,disease_type) VALUES(%s,%s)", (disease_name_2,"Type B"))
    mycursor.execute("INSERT INTO disease(disease_name,disease_type) VALUES(%s,%s)", (disease_name_3,"Type C"))
    mycursor.execute("INSERT INTO disease(disease_name,disease_type) VALUES(%s,%s)", (disease_name_4,"Type D"))
    mycursor.execute("INSERT INTO disease(disease_name,disease_type) VALUES(%s,%s)", (disease_name_5,"Type E"))
    mycursor.execute("INSERT INTO disease(disease_name,disease_type) VALUES(%s,%s)", (disease_name_6,"Type F"))
    db.commit()
    causes=[malaria,
            parkinson,
            hiv_aids,
            cholera,
            ebo_cause,
            covid_19
            ]
    sql = "INSERT INTO symptom(symptom_name,symptom_type,cause,disease_id) VALUES(%s,%s,%s,%s)"
    mycursor.execute("INSERT INTO confirmatory_test(confirmatory_test_name) VALUES(%s)", (mal_diag,))
    mycursor.execute("INSERT INTO confirmatory_test(confirmatory_test_name) VALUES(%s)", (mal_diag2,))
    mycursor.execute("INSERT INTO confirmatory_test(confirmatory_test_name) VALUES(%s)", (park_diag_2,))
    mycursor.execute("INSERT INTO confirmatory_test(confirmatory_test_name) VALUES(%s)", (h_diag3,))
    mycursor.execute("INSERT INTO confirmatory_test(confirmatory_test_name) VALUES(%s)", (cho_diag,))
    mycursor.execute("INSERT INTO confirmatory_test(confirmatory_test_name) VALUES(%s)", (ebola_diag,))
    mycursor.execute("INSERT INTO confirmatory_test(confirmatory_test_name) VALUES(%s)", (covid_diag1,))
    mycursor.execute("INSERT INTO confirmatory_test(confirmatory_test_name) VALUES(%s)", (cov_diag2,))
    mycursor.execute("INSERT INTO confirmatory_test(confirmatory_test_name) VALUES(%s)", (cov_diag3,))
    
    
    val = [
        (sym,'type 1',malaria,1),
        (sym1,'type 2',malaria,1),(sym2,'type 3',malaria,1 ),(sym3,'type 4',malaria,1),
        (symp,'type 5',malaria,1),(symp1,'type 6',malaria,1),(s5,'type 7',malaria,1),
        (s6,'type 8',malaria,1),(s7,'type 9',malaria,1),(s9,'type 10',malaria,1),
        (sy1,'type 11',malaria,1),(sy2,'type 12',malaria,1),(sy3,'type 13',malaria,1),
        (sy4,'type 14',malaria,1),(sy5,'type 15',malaria,1),(sy6,'type 16',malaria,1),
        (addsymp,'type 17',malaria,1),(comp,'type 18',malaria,1),(comp1,'type 19', malaria,1),
        (comp2,'type 20',malaria,1),(comp3,'type 21',malaria,1),(comp4, 'type 22',malaria,1),

        (park_sym,'type 215',parkinson,2),(park_sym1,'type 216',parkinson,2),
        (park_sym2,'type 217',parkinson,2), (comp_5,'type 218',parkinson,2),(comp_6,'type 219',parkinson,2),
    ('Tremor','type 220','parkinson',2),
    ('slow movement','type 221','parkinson',2),
    ('pain','type 222','parkinson',2),
('drooling','type 223','parkinson',2),
('smell dysfunction','type 224','parkinson',2),
     ('Rigid muscles','type 225','parkinson',2),
('small handwriting','type 226','parkinson',2),
('frequent urination','type 227','parkinson',2),
('extreme tiredness','type 228','parkinson',2),
('impaired posture and balance','type 229','parkinson',2),
('speech changes','type 230','parkinson',2),
('increased blood pressure','type 231','parkinson',2),
('sexual dysfunction','type 232','parkinson',2),
('constipation','type 233','parkinson',2),
('restless leg syndrome','type 234','parkinson',2),
('mask_like facial expression','type 235','parkinson',2),('less blinking','type 236','parkinson',2),


        (h,'type 32',hiv_aids,3),(h1,'type 33',hiv_aids,3),(h2,'type 34',hiv_aids,3),
        (h3,'type 35',hiv_aids,3),(h4,'type 36',hiv_aids,3),(h5,'type 37',hiv_aids,3),
        (h6, 'type 38', hiv_aids, 3),(h7,'type 39',hiv_aids,3),(h8,'type 40',hiv_aids,3),
        (h9,'type 41',hiv_aids,3),(h10,'type 42',hiv_aids,3),(ha,'type 43',hiv_aids,3),
        (hb,'type 44',hiv_aids,3),(hc,'type 45',hiv_aids,3),(hd,'type 46',hiv_aids,3),
        (he, 'type 47', hiv_aids, 3),(hf_, 'type 48', hiv_aids, 3),(hg, 'type 49', hiv_aids,3),
        (comp_7,'type 50',hiv_aids,3),(comp_8,'type 51',hiv_aids,3),

        
        (cho1,'type 52',cholera,4),(cho2,'type 53',cholera,4),(cho3,'type 54',cholera,4),
        (cho4,'type 55',cholera,4),(cho5,'type 56',cholera,4),(cho6,'type 57',cholera,4),
        (cho7,'type 58',cholera, 4),(cho8,'type 59',cholera,4),(cho9,'type 60',cholera,4),
        (cho10,'type 61',cholera,4),(cho11,'type 62',cholera,4),(comp_9,'type 63',cholera,4),
        (comp_10,'type 64',cholera,4), ('less sweating','type 65','cholera',4),('low urination','type 66','cholera',4),('dry skin','type 67','cholera',4),('dry mucous membrane','type 68','cholera',4),
    ('irritability','type 69','cholera',4),('rapid weight loss','type 70','cholera',4),('dizziness','type 71','cholera',4), ('shock','type 72','cholera',4),('leg cramps','type 73','cholera',4),('body weakness','type 74','cholera',4),('low potassium level','type 75','cholera',4),('loss of plasma','type 76','cholera',4),


        (eb4,'type 77',ebo_cause,5),(eb5,'type 78',ebo_cause,5),(eb6,'type 79',ebo_cause,5),
        (eb1,'type 80',ebo_cause,5),(eb2,'type 81',ebo_cause,5),(eb3,'type 82',ebo_cause,5),
        (eb7,'type 83',ebo_cause,5),(eb8,'type 84',ebo_cause,5),(eb9,'type 85',ebo_cause,5),
        (eb10,'type 86',ebo_cause,5),(eb11,'type 87',ebo_cause,5),(e1,'type 88',ebo_cause,5),
        (e2,'type 89',ebo_cause,5),(e3,'type 90',ebo_cause,5),(e4,'type 91',ebo_cause,5),
        (e5,'type 92',ebo_cause,5),(e6,'type 93',ebo_cause,5),(e7,'type 94',ebo_cause,5),
        (e9, 'type 95',ebo_cause,5),(e10, 'type 96',ebo_cause,5),(e11, 'type 97',ebo_cause,5),
        (e12,'type 98',ebo_cause,5),(ebo_comp,'type 99',ebo_cause,5),


        (cov3,'type 100',covid_19,6),
        (cov4,'type 101',covid_19,6),(cov5,'type 102',covid_19,6),(cov6,'type 103',covid_19,6),
        (cov7,'type 104',covid_19,6),(cov8,'type 105',covid_19,6),(cov9,'type 106',covid_19,6),
        (cov10,'type 107',covid_19,6),(cov11,'type 108',covid_19,6),(cov12,'type 109',covid_19,6), 
        (cov13,'type 200',covid_19,6),(cov14,'type 201',covid_19,6),
        (cov15,'type 202',covid_19,6),(co1,'type 203',covid_19,6),(co2,'type 204',covid_19,6),
        (co3,'type 205',covid_19,6),(co4,'type 206',covid_19,6),
        (cov_comp,'type 207',covid_19,6),(cov_comp1,'type 208',covid_19,6),
        (cov_comp2,'type 209',covid_19,6),(cov_comp3,'type 210',covid_19,6),
        (cov_comp4,'type 211',covid_19,6),(cov_comp5,'type 212',covid_19,6),
        (cov_comp6,'type 213',covid_19,6),(cov_comp7,'type 214',covid_19,6)

        ]
    mycursor.executemany(sql, val)
    # db.commit()
    
    db.commit()

    print(mycursor.rowcount, "was inserted.")
    
    
except Exception as e:
    print(e)
        
    
    


    


    





