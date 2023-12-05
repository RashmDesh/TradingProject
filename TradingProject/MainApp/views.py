from django.shortcuts import render,HttpResponse
from .models import treadingfile
from .forms import tradingform
from django.views import View
import pandas as pd
from datetime import datetime

# Create your views here.
class upload_file(View):
    def get(self,request):
        form=tradingform()
        return render(request,"form.html",{'form':form})
    
    def post(self,request):
        form=tradingform(request.POST,request.FILES)

        file = request.POST.get('file')
        upload_time=request.POST.get('upload_time')

        data=treadingfile(file=file,upload_time=upload_time)
        data.save()

        return HttpResponse("File save")
    
def read_csv(request):

    df=pd.read_csv("C:/Users/rkrat/OneDrive/Desktop/Learning & Test/Python 2023 all learning repo/Django/Neiha Business Technology/TradingProject/templates/uploadedfiles/NIFTY_F1_Xm8mAtb.csv")
    print(df)
    
   # id=[]
    open=df['OPEN']
    low=df['LOW']
    high=df['HIGH']
    close=df['CLOSE']
    date=df['DATE']
    time=df['TIME']
    columns=['date','open','high','low','close','time']
   
    
    timeframedf = pd.DataFrame(list(zip(date,open,high,low,close,time)),
                 columns=columns )
     # set index
    #id= pd.Index(range(0, 92480, 1))
    
    timeframedf['date']=pd.to_datetime(timeframedf['date'])
    
    timeframedf = timeframedf.set_index('date')
    print(timeframedf)

    resampledf=timeframedf.resample('1min',origin='start').agg(
        {'time':'min','open':'first','high':'max','low':'min','close':'last',} )
    print(resampledf)
    
    #string to txt
    resampledf.to_csv('C:/Users/rkrat/OneDrive/Desktop/Learning & Test/Python 2023 all learning repo/Django/Neiha Business Technology/TradingProject/templates/uploadedfiles/resample.txt',sep='\t')

#conveet to json
    json_columns = resampledf.to_json() 
    print(json_columns)

    #upload resample file to djngo DB
    now = datetime.now()
    data=treadingfile(file='C:/Users/rkrat/OneDrive/Desktop/Learning & Test/Python 2023 all learning repo/Django/Neiha Business Technology/TradingProject/templates/uploadedfiles/resample.txt',upload_time=now)
    data.save()



    return HttpResponse()