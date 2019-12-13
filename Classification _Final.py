# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 04:15:05 2019

@author: dell1
"""
print("please put your photo on the desktop , and then enter its name and fromate" )
print ('\n')
print ("For example: name.png , name.jpg , etc..")
try:
   import Image
except ImportError:
   from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
#Basic OCR
# print(pytesseract.image_to_string(Image.open('C:\\Users\\OWNER\\Desktop\\test.png')))
#In French
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra’))
image_name = input()
print ('\n')
z = 'C:\\Users\\OWNER\\Desktop\\' + image_name
image_content = pytesseract.image_to_string(Image.open(z))
print (image_content)
m = e = p = 0
image_content = image_content.lower()
medicine_keywords = ["eye","organic","heart", "logy","medic","health" , "insurance" , "ache" , "acne" , "allergic" , "allergy" , "allergies" , "antibiotics" , "asprin" , "body" , "breath" , "burn" , "caffeine" , "cancer" , "chemo" , "chest" , "clinic" , "cold" , "congested" , "cough" , "cramp" , "crutches" , "cure" , "dehydrated" , "dehydration" , "dental" , "dentist" , "diabetes" , "diagnosed" , "diet" , "dizzy" , "dizziness" , "doctor", "dose" , "ear" , "elbow" , "emergency" , "faint" , "fatigue" , "fever" , "flu" , "forehead" , "germ" , "gland" , "heal" , "hiccup" , "hospital" , "hurt" , "infect" , "inhaler" , "insomnia" , "jaw" , "kidney" , "knee" , "lasik" , "lung" , "massage" , "medication" , "morphine" , "muscle" , "nasal" , "nausea" , "needle" , "nose" , "nurse" , "pain" , "panadol" , "paracetamol" , "pill" , "pimple" , "pneumonia" , "poison" , "prescription" , "recovery" , "rehab" , "relieve" , "respiratory" , "rest" , "ribs" , "sick" , "skull" , "sneeze" , "sneezing" , "sniffle" , "sniffling" , "sore" , "spine" , "steroid" , "stomach" , "surgeon" , "surgery" , "swelling" , "swollen" , "symptom" , "thirsty" , "throat" , "throbbing" , "thyroid" , "tissues" , "tissue" , "tooth" , "teeth" , "treatment" , "tumor" , "ulcer" , "unbearable" , "unwell" , "veins" , "vitamin" , "vomit" , "wrist" , "fitness" , "eczema" , "vegan" , "workout" , "yoga" , "skinny" , "fat" , "carbohydrates" , "appetite" , "protein" , "amino" , "patient" , "addiction" , "nutrition" , "mental" , "drug" , "genetics" , "gene" , "disease", "pregnant" , "pregnancy" , "paramedic" , "virus" , "cloning" , "bio" , "autism" , "alzheimer" , "mental" , "puberty" , "suicide" , "injury" , "injuries" , "smoking" , "alcohol" , "breast" , "fibrosis" , "hepatitis" , "immunity" , "immunization" ,"therapy" , "trauma" , "disorder" , "spinal" , "schizophrenia" , "cell" , "pancreas" , "nutrition" , "liver" , "metabolic" , "lipid" , "transplant" , "patient" , "psychology" , "physiology" , "diagnostic" , "bone" , "ctscan" , "xray" , "x-ray" , "x-ray" , "appetite" , "enzyme" , "eyelid" , "infantile" , "vascular" , "anxiety", "death" , "depression" , "suffer" , "toxic" , "biology"]
engineering_keywords = ["gauss" "coloumb" , "maxwell","array","engineering" , "design" , "project" , "degree" , "energy" , "power" ,  "energy" , "civil" , "architicture" , "mechanics" , "dynamics" , "statics" , "maths" , "physics" , "construction" ,  "infrastructure" , "structure" , "site" , "computer" , "software" , "web" , "internet" , "network" , "java" , "html" , "http",  "programming" , "code", "python" , "c++" , "density" , "volume" , "engine" , "electrical" , "electricity" , "electronics" , "circuits" , "capacitor" , "inductor" , "resistance" , "transistor" , "mosfet" , "nmos" , "pmos" , "bjt" , "voltage" , "volt" , "equipment" , "analysis" , "equation" , "statistical" , "statistics" , "logic" , "filter" , "amplifier" , "equation" , "multiplication" , "matrix" , "matrices" , "signal" , "byte" , "bit" , "arithmetic" , "embedded" , "output" , "input" , "analog" , "digital" , "microcontroller" , "microprocessor" , "scalar" , "vector" , "thermodynamics" , "work"  , "heat" ]
politics_keywords = ["bank","acess","president","vicepresident","law","account","activism","activist","nationalism","policy","bbc","polit","campaign","candidate","capitalism","central","state","citizen","civil","commit","government","wealth","communism","community","objection","conservative","party","crisis","currency","debt","defence","demand","democarcy","department","development","diplomacy","discipline","discrimination","diversity","economic","election","war","revoultion","environment","governance","risks","finance","exchange","feminism","financ","fund","independence","inequality","inflation","islamic","labour","leardship","legal","leisure","liberal","mobilization","nuclear","parliament","complaints","liberalism","poverty","press","propaganda","racism","republican","revolutionary","rights","sexism","strategy","strikes","supervision","taxes","volunteering","voter","organisation","revolt","revolting"]

print ("Words related to medical field:")  
for word in medicine_keywords:
     if (word in image_content) :
            m = m+1
            print(word)
print('/n')         
print ("Words related to engineering field:")  
for word in engineering_keywords:
     if (word in image_content) :
            e = e+1
            print(word)
            
print('/n')         
print ("Words related to engineering field:")             
for word in politics_keywords:
     if (word in image_content) :
            p = p+1
            print(word)
print('\n')            
if m > 0 and m > p and m > e :
      print("this Photo is related to Medical field")

elif e > 0 and e > m and e > p :
     print("this Photo is related to Engineering field")

elif p > 0 and p > m and p > e :
     print("this Photo is related to Politics field")

else: 
    print("this document is not related to any of the defined categories")

print (m)
print (e)
print (p)  
print ('__________________________________________________________________________________') 

 