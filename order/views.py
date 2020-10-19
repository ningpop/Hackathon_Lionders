from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import Item, Order
from .forms import OrderForm, UpdateOrderForm, ItemForm
from users import models as usermodel

# Create your views here.

def order_list(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/signin/')
    # orders = Order.objects.filter(user_id=request.user.pk).order_by('created_at')
    orders = Order.objects.filter()
    context = {
        'orders': orders,
    }
    return render(request, 'order_list.html', context)

def order(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('login')
        elif request.user.usertype=="lionders":
            return redirect('login')
        else:
            items = Item.objects.all()
            total_price=0
            current_user = get_object_or_404(usermodel.Consumer_Users,pk = request.user.id)
            if current_user.have_order_sheet == False:
                new_order = Order(normal_user_info=current_user,total_price=0)
                new_order.save()
                current_user.have_order_sheet = True
                current_user.save()
                ordered_items = new_order.items.all()
                for item in ordered_items:
                    total_price += item.price
                ex_items = list(set(items) - set(ordered_items))
                return render(request,'order.html',{'items':items,'order':new_order,'ordered_items':ordered_items,'ex_items':ex_items,'total_price':total_price})
            else:
                my_order = current_user.order_set.all().order_by('-ordered_time')
                ordered_items = my_order[0].items.all()
                for item in ordered_items:
                    total_price += item.price
                ex_items = list(set(items) - set(ordered_items))
                return render(request,'order.html',{'items':items,'order':my_order[0],'ordered_items':ordered_items,'ex_items':ex_items,'total_price':total_price})
    else:
        return redirect('login')



def add_item(request,order_id,item_id):
    order = get_object_or_404(Order,pk=order_id)
    order.items.add(item_id)
    return redirect('order')


def remove_item(request,order_id,item_id):
    order = get_object_or_404(Order,pk=order_id)
    order.items.remove(item_id)
    return redirect('order')

def delete_item(requestm, item_id):
    item = get_object_or_404(Item,pk=item_id)
    item.delete()
    return redirect('create_objs')


def order_delete(request, id):
    item = get_object_or_404(Order, pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('order-list')  # 리스트 화면으로 이동합니다.
    return render(request, 'order_delete.html', {'item': item})


def order_update(request):
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(Order, pk=request.POST.get('id'))
        form = UpdateOrderForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()

    elif 'id' in request.GET:
        item = get_object_or_404(Order, pk=request.GET.get('id'))
        form = OrderForm(instance=item)
        return render(request, 'order_update.html', {'form': form})
    return HttpResponseRedirect("../orderlist")

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        request.POST._mutable = True
        # request.POST['user'] = request.user
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('../order/orderlist')
    form = ItemForm()
    return render(request, 'item_create.html', {'form': form})