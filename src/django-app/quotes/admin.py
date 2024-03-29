from django.contrib import admin

from .models import Quote, QuoteComment, QuoteRequest


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("shop", "get_customer", "get_description", "status", "price")

    def get_customer(self, obj):
        return obj.quote_request.user

    def get_description(self, obj):
        return obj.quote_request.description

    get_customer.short_description = "Customer"
    get_description.short_description = "Description"


@admin.register(QuoteComment)
class QuoteCommentAdmin(admin.ModelAdmin):
    list_display = ("quote", "user", "comment", "created_at", "updated_at")


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ("description", "user", "shop")
    exclude = ("batch_id",)
