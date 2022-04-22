from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.


def index(request):
    if(request.method == 'POST'):        
        return JsonResponse({"Function Called":100})
        
    
    else:
        return render(request, "home_page.html")

    
def optimize(request):
    
    if(request.method == 'POST'):
        owned_char = []
        Albedo = request.POST.get("Albedo",0)
        if(Albedo):
            owned_char.append("Albedo")

        Aloy = request.POST.get("Aloy",0)
        if(Aloy):
            owned_char.append("Aloy")

        Amber = request.POST.get("Amber",0)
        if(Amber):
            owned_char.append("Amber")

        Barbara = request.POST.get("Barbara",0)
        if(Barbara):
            owned_char.append("Barbara")

        Beidou = request.POST.get("Beidou",0)
        if(Beidou):
            owned_char.append("Beidou")

        Bennet = request.POST.get("Bennet",0)
        if(Bennet):
            owned_char.append("Bennet")

        Chongyun = request.POST.get("Chongyun",0)
        if(Chongyun):
            owned_char.append("Chongyun")

        Diluc = request.POST.get("Diluc",0)
        if(Diluc):
            owned_char.append("Diluc")

        Diona = request.POST.get("Diona",0)
        if(Diona):
            owned_char.append("Diona")

        Eula = request.POST.get("Eula",0)
        if(Eula):
            owned_char.append("Eula")

        Fishcl = request.POST.get("Fishcl",0)
        if(Fishcl):
            owned_char.append("Fishcl")

        Ganyu = request.POST.get("Ganyu",0)
        if(Ganyu):
            owned_char.append("Ganyu")

        Hu_Tao = request.POST.get("Hu_Tao",0)
        if(Hu_Tao):
            owned_char.append("Hu_Tao")

        Jean = request.POST.get("Jean",0)
        if(Jean):
            owned_char.append("Jean")

        Kaedehara_Kazuha = request.POST.get("Kaedehara_Kazuha",0)
        if(Kaedehara_Kazuha):
            owned_char.append("Kaedehara_Kazuha")

        Kaeya = request.POST.get("Kaeya",0)
        if(Kaeya):
            owned_char.append("Kaeya")

        Kamisato_Ayaka = request.POST.get("Kamisato_Ayaka",0)
        if(Kamisato_Ayaka):
            owned_char.append("Kamisato_Ayaka")

        Keqing = request.POST.get("Keqing",0)
        if(Keqing):
            owned_char.append("Keqing")

        Klee = request.POST.get("Klee",0)
        if(Klee):
            owned_char.append("Klee")

        Kujou_Sara = request.POST.get("Kujou_Sara",0)
        if(Kujou_Sara):
            owned_char.append("Kujou_Sara")

        Lisa = request.POST.get("Lisa",0)
        if(Lisa):
            owned_char.append("Lisa")

        Mona = request.POST.get("Mona",0)
        if(Mona):
            owned_char.append("Mona")

        Ninguang = request.POST.get("Ninguang",0)
        if(Ninguang):
            owned_char.append("Ninguang")

        Noelle = request.POST.get("Noelle",0)
        if(Noelle):
            owned_char.append("Noelle")

        Qiqi = request.POST.get("Qiqi",0)
        if(Qiqi):
            owned_char.append("Qiqi")

        Raiden_Shogun = request.POST.get("Raiden_Shogun",0)
        if(Raiden_Shogun):
            owned_char.append("Raiden_Shogun")

        Razor = request.POST.get("Razor",0)
        if(Razor):
            owned_char.append("Razor")

        Rosaria = request.POST.get("Rosaria",0)
        if(Rosaria):
            owned_char.append("Rosaria")

        Sangonomiya_Kokomi = request.POST.get("Sangonomiya_Kokomi",0)
        if(Sangonomiya_Kokomi):
            owned_char.append("Sangonomiya_Kokomi")

        Sayu = request.POST.get("Sayu",0)
        if(Sayu):
            owned_char.append("Sayu")

        Sucrose = request.POST.get("Sucrose",0)
        if(Sucrose):
            owned_char.append("Sucrose")

        Tartaglia = request.POST.get("Tartaglia",0)
        if(Tartaglia):
            owned_char.append("Tartaglia")
            
        Thoma = request.POST.get("Thoma",0)
        if(Thoma):
            owned_char.append("Thoma")

        Venti = request.POST.get("Venti",0)
        if(Venti):
            owned_char.append("Venti")

        Xiangling = request.POST.get("Xiangling",0)
        if(Xiangling):
            owned_char.append("Xiangling")

        Xiao = request.POST.get("Xiao",0)
        if(Xiao):
            owned_char.append("Xiao")

        Xingqiu = request.POST.get("Xingqiu",0)
        if(Xingqiu):
            owned_char.append("Xingqiu")

        Xinyan = request.POST.get("Xinyan",0)
        if(Xinyan):
            owned_char.append("Xinyan")

        Yanfei = request.POST.get("Yanfei",0)
        if(Yanfei):
            owned_char.append("Yanfei")

        Yoimiya = request.POST.get("Yoimiya",0)
        if(Yoimiya):
            owned_char.append("Yoimiya")

        Zhongli = request.POST.get("Zhongli",0)
        if(Zhongli):
            owned_char.append("Zhongli")

        df = pd.read_excel(r'C:\Users\anand\Desktop\vscode\Teapot Housing\Teapot Data.xlsx')
        owned_char = set(owned_char)
        scores = []
        for index,row in df.iterrows():
            req_characters = []
            score = 0
    
            req_characters.append(row['char_1'])
            req_characters.append(row['char_2'])
            req_characters.append(row['char_3'])
            req_characters.append(row['char_4'])
            req_characters.append(row['char_5'])
            req_characters.append(row['char_6'])
    
            intersection = owned_char.intersection(req_characters)
            intersection = list(intersection)
    
            for i in intersection:
                score = score + 1

            
            scores.append(score*20)
        df['primogems'] = scores
        df = df.sort_values(by = ['primogems','Trust_level_req'], ascending = [False,True]).copy()
        # return render(request, 'optimizer_output.html',{'data':df})
        tot_primos = sum(df['primogems'])
        return HttpResponse(df.to_html(na_rep = " ", col_space = 80, justify = "left"))





    else:
        return render(request, "optimizer_page.html")

    

