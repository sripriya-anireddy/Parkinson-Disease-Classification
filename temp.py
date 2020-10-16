# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
model=pickle.load(open('train.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template('PDC.html')
@app.route('/login', methods=["POST"])
def login():
    DDP=request.form["DDP"]
    SLocal=request.form["Local"]
    Rap=request.form["Rap"]
    LocalAbs=request.form["LocalAbs"]
    PPQ5=request.form["PPQ5"]
    DDA=request.form["DDA"]
    JLocal=request.form["Local"]
    APQ3=request.form["APQ3"]
    APQ5=request.form["APQ5"]
    APQ11=request.form["APQ11"]
    localDB=request.form["localDB"]
    AC=request.form["AC"]
    NTH=request.form["NTH"]
    HTN=request.form["HTN"]
    NoOfPulses=request.form["NoOfPulses"]
    NoOfPeriods=request.form["NoOfPeriods"]
    MeanPeriod=request.form["MeanPeriod"]
    StandardDeviationOfPeriod=request.form["StandardDeviationOfPeriod"]
    NoOfVoiceBreaks=request.form["NoOfVoiceBreaks"]
    DegreeOfVoiceBreaks=request.form["DegreeOfVoiceBreaks"]
    FractionOfLocallyUnvoicedFrames=request.form["FractionOfLocallyUnvoicedFrames"]
    Mean=request.form["Mean"]
    Median=request.form["Median"]
    StandardDeviation=request.form["StandardDeviation"]
    MinPitch=request.form["MinPitch"]
    MaxPitch=request.form["MaxPitch"]
    ID=request.form["ID"]
    total=[[int(ID),float(JLocal),float(LocalAbs),float(Rap),float(PPQ5),float(DDP),float(SLocal),float(localDB),float(APQ3),float(APQ5),float(APQ11),float(DDA),float(AC),float(NTH),float(HTN),float(Median),float(Mean),float(StandardDeviation),float(MinPitch),float(MaxPitch),int(NoOfPulses),int(NoOfPeriods),float(MeanPeriod),float(StandardDeviationOfPeriod),float(FractionOfLocallyUnvoicedFrames),int(NoOfVoiceBreaks),float(DegreeOfVoiceBreaks)]]
    p=model.predict(total)
    p=p[0]
    if p==0 or p==1:
        return render_template('result.html',label = "The result is = "+str(p)+"No Danger")
 
if __name__=='__main__':
    app.run(debug=True,port=5000)



