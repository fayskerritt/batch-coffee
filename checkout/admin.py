from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'expected_delivery_date',
                       'delivery_cost', 'order_total',
                       'sub_total', 'grand_total', 'original_bag',
                       'stripe_pid',)

    fields = ('order_number', 'user_account', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode_zipcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'expected_delivery_date',
              'delivery_cost', 'sub_total', 'order_total',
              'grand_total', 'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'expected_delivery_date',
                    'full_name', 'delivery_cost', 'sub_total',
                    'order_total', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
