
    # elif cp=="Non-Anginal":
    #     cp=2
    # else:
    #     cp=3
    # if fbs=="Yes":
    #     fbs=1
    # else:
    #     fbs=0
    if restecg=="Normal":
        restecg=0
    elif restecg=="STT Abnormality":
        restecg=1
    else:
        restecg=2
    if exang=="Yes":
        exang=1
    else:
        exang=0
    #  print("The email address is '" + age + "|"+sex+"|"+cp+"|"+trestbps+"|"+chol+"|"+fbs+"|"+restecg)
    # Get the data from the POST request.

    print("all models=",all_models)
    # print("Data recived", age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,thal,0,0)
    age=int(age)
    cp=int(cp)
    trestbps=int(trestbps)
    chol=int(chol)
    fbs=int(fbs)
    thalach=int(thalach)
    oldpeak=int(oldpeak)
    slope=int(slope)
    ca=int(ca)
    features=[age, gender, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,slope,ca,thal]
    print(features)
    dict={};
    avg=0
    for model in all_models:
        print("Model" , model)
        res=model.predict([features])
        print("res=",res[0],type(res))
        if res[0]==1:
            dict[model]="High Chance of Heart Disease"
        else:
            dict[model]="Low Chance of Heart Disease"
        avg+=res
    print("average=",type(avg))
    accuracy=avg[0]/5
    accuracy=round(accuracy,2)
    for result in dict:
        print("sfadgD", result)
    prediction = all_models[0].predict([features])
