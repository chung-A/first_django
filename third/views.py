from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from third.models import Restaurant
from third.forms import RestaurantForm
from django.http import HttpResponseRedirect


def select(request):
    restaurants = Restaurant.objects.all()

    paginator = Paginator(restaurants, 5)
    # third/select?page=2
    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'restaurants': items
    }
    return render(request, 'third/select.html', context)


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/third/select')

    form = RestaurantForm()
    return render(request, 'third/create.html', {'form': form})


# third/update?id=2
# --- 참고 ---
# form = RestaurantForm(request.POST, instance=item)
# if form.is_valid():
#     item = item.save()
# 이렇게 하면 insert 가 됨.
def update(request):
    # request 에 id 파라미터가 있도록
    if request.method == 'POST' and 'id' in request.POST:
        # DB 에서 불러온 기존 데이터를 업데이트
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        form = RestaurantForm(request.POST, instance=item)
        if form.is_valid():
            item = item.save()
    # 뷰 뿌리기
    elif request.method == "GET":
        # item = Restaurant.objects.get(pk=request.GET.get('id'))
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})

    return HttpResponseRedirect('/third/select/')


def detail(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        return render(request, 'third/detail.html', {'item': item})
    return HttpResponseRedirect('/third/select/')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item.delete()
    return HttpResponseRedirect('/third/select/')

    # for i in range(0, 10):
    #     restaurant = Restaurant(name="음식점" + str(i), address="주소 " + str(i))
    #     restaurant.save()
