from django.core.paginator import Paginator
from django.db.models import Count, Avg
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from third.forms import RestaurantForm, ReviewForm, UpdateRestaurantForm
from third.models import Restaurant, Review


def select(request):
    # 조인된 대상 객체명을 소문자로 적어주면 된다.
    restaurants = Restaurant.objects.all() \
        .annotate(reviews_count=Count('review')) \
        .annotate(average_point=Avg('review__point'))

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
        password = request.POST.get('password', '')
        form = UpdateRestaurantForm(request.POST, instance=item)
        if form.is_valid() and password == item.password:
            item = item.save()
    # 뷰 뿌리기
    elif request.method == "GET":
        # item = Restaurant.objects.get(pk=request.GET.get('id'))
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        return render(request, 'third/update.html', {'form': form})

    return HttpResponseRedirect('/third/select/')


def detail(request, id):
    if id is not None:
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all()
        return render(request, 'third/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/third/select/')


def delete(request, id):
    item = get_object_or_404(Restaurant, pk=id)
    if request.method == 'POST' and 'password' in request.POST:
        if item.password == request.POST.get('password') or item.password is None:
            item.delete()
            return redirect('list')
        return redirect('detail', id=id)
    return render(request, 'third/delete.html', {'item': item})

    # for i in range(0, 10):
    #     restaurant = Restaurant(name="음식점" + str(i), address="주소 " + str(i))
    #     restaurant.save()


def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('detail', id=restaurant_id)

    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant': item})
    return render(request, 'third/review_create.html', {'form': form, 'item': item})


def review_delete(request, restaurant_id, review_id):
    if request.method == 'GET':
        item = get_object_or_404(Review, pk=review_id)
        item.delete()
    return redirect('detail', id=restaurant_id)


def review_list(request):
    reviews = Review.objects.all().select_related().order_by('-created_at')
    paginator = Paginator(reviews, 10)

    page = request.GET.get('page')
    items = paginator.get_page(page)

    context = {
        'reviews': items,
    }
    return render(request, 'third/review_list.html', context)
