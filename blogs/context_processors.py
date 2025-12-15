from .models import Category

def get_categories(req):
    categories = Category.objects.all()
    return dict(categories=categories)