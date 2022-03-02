from django.shortcuts import render,redirect

from interestapp.forms import formname



# Create your views here.




def calculation(release_date,load_date,p,i):
    release_date_year = release_date.year
    release_date_month = release_date.month
    release_date_day = release_date.day
    load_date_year = load_date.year
    load_date_month = load_date.month
    load_date_day = load_date.day
    cal_year = load_date_year - release_date_year
    cal_month = load_date_month - release_date_month
    cal_day = load_date_day - release_date_day
    if p <= 5000:
        i = 3
    elif p >= 5001:
        i = 2


    total_days = cal_year*12*30 + cal_month*30 + cal_day
    if total_days < 0:
        return "Release data must be greater than loan date"

    elif total_days <= 360:
        total_month = total_days//30
        total_month_pay = ((p*i)/100)*total_month
        total_day = total_days - total_month*30
        total_days_pay = (((p*i)/100)/30)*total_day
        total_pay = total_month_pay + total_days_pay + p
        return total_pay
    else:
        total_year = total_days//360
        total_month = total_days//30 - total_year*12
        total_day = total_days - total_month*30 -total_year*12*30
        for i in range(total_year):
            interest_per_month = (p/100)*3
            interest_12_month = interest_per_month * 12
            p = p + interest_12_month

        interest_per_month = (p/100)*3
        interest_total_month = interest_per_month*total_month
        interest_per_day = (interest_per_month/30)*total_day
        p = interest_total_month + p + interest_per_day
        return p














def index(request):
    form = formname()
    if request.method == "POST":
        form = formname(request.POST)

        if form.is_valid():
            release_date = form.cleaned_data['start_date']
            loan_date = form.cleaned_data['end_date']
            p = form.cleaned_data['principal']
            i = form.cleaned_data['interest']
            var = calculation(release_date,loan_date,p,i)
            print(var)
            return render(request,'interestapp/calculated.html',{'var' : var})

            # return render(request,'interestapp/index.html',{'form':var})
            # print(var1.day)
    return render(request,'interestapp/index.html',{'form':form})