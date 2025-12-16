from .models import Category
from assignments.models import SocialLink

def get_categories(req):
    categories = Category.objects.all()
    return dict(categories=categories)

#  for this define the functions path in setting.py

def get_social_links(req):
    social_link = SocialLink.objects.all()
    return dict(social_link=social_link)
    
 