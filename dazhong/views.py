from django.shortcuts import render

# Create your views here.
def coffee_store_analysis(request):
    return render(request,'coffee_store.html')

def pyecharts1(request):
    return render(request,'Coffee_SalesAnalysis3rename.html')




def pyecharts2(request):
    return render(request,'Coffee_SalesAnalysis2_resize.html')



def pyecharts3(request):
    return render(request,'Coffee_SalesAnalysis1_resize.html')


def coffee_store_analysis1(request):
    return render(request,'coffee_store1.html')

#============0602 update no video======================================
def coffee_store_analysis2(request):
    return render(request,'coffee_store_0602.html')

#============0608 update ===================================================
def coffee_store_analysis3(request):
    return render(request,'coffee_store_0608.html')


def countryanalysis(request):
    return render(request,'countryanalysis.html')


def piecharts(request):
    return render(request,'piecharts.html')

def RegionRankDetailBar(request):
    return render(request,'RegionRankDetailBar.html')


def region_boxplot(request):
    return render(request,'region_boxplot.html')

def citybrandrank(request):
    return render(request,'citybrandrank.html')

def BrandRankDetailBar(request):
    return render(request,'BrandRankDetailBar.html')


def VimeVideo(request):
    return render(request,'vime.html')