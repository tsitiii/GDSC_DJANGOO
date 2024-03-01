from django.shortcuts import render
from models import BlogPost
# Create your views here.

def post_detail(request, post_id):
    