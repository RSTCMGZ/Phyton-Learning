from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


projelerim = [
    {
        'ad': 'Proje 1',
        'resim': 'https://picsum.photos/id/237/200/300',
        'aciklama': ' Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium maxime ipsum doloribus quos assumenda sequi magnam, facere fugiat',
        'slug': 'proje-1',
        'faydasi': 'bu ürün süper'

    },
    {
        'ad': 'Proje 2',
        'resim': 'https://picsum.photos/id/2/200/300',
        'aciklama': ' Lorem ipsum dolor sit amet consectetur adipisicing elit. assumenda sequi magnam, facere fugiat',
        'slug': 'proje-2'
    },
    {
        'ad': 'Proje 3',
        'resim': 'https://picsum.photos/id/20/200/300',
        'aciklama': ' Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium maxime ipsum doloribus quos ',
        'slug': 'proje-3'

    },
     {
        'ad': 'Proje 4',
        'resim': 'https://picsum.photos/id/65/200/300',
        'aciklama': ' Lorem ipsum dolor sit amet consectetur adipisicing elit. ',
        'slug': 'proje-4'
    },
]


def projeler(request):
    return render(request,'projeler.html',{'projelers':projelerim})

def proje_detay(request,detay_slug):
    projem = {}
    for i in projelerim:
       if i['slug'] == detay_slug:
           projem = i
    print(projem)


    return render(request,'proje-detay.html',{'proje':projem})