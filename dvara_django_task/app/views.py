from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib import messages

from app.forms import CategoryForm
from app.models import SubCategory


class CategoryView(View):
    """ 
        This View renders the template, 
        get subcategories based on selected category and submits the form 
    """
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        """ Returns the template with default values """
        form = CategoryForm()
        records = SubCategory.objects.all().order_by('-id')
        context = {
            "form": form,
            "records": records
        }
        return render(request, self.template_name, context)
    
    def get_subcategory(request):
        """ Returns SubCategory Based on selected Category """
        category_id = request.GET.get('category_id')
        try:
            subcategory_objs = SubCategory.objects.filter(category=category_id).values()
            data = {
                'success': True,
                'records': list(subcategory_objs),
            }
        except SubCategory.DoesNotExist:
            data = {
                'success': False,
                'message': "No Data Found!"
            }
        return JsonResponse(data)
    
    def post(self, request, *args, **kwargs):
        """ Submits the form and redirect to the same page """
        print(request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Form Submitted Successfully.")
            # return redirect('/')
            records = SubCategory.objects.all().order_by('-id')
            data = {
                "success": True,
                "message": "Form Submitted Successfully.",
                "records": list(records.values())

            }
            return JsonResponse(data)
        else:
            data = {
                "success": False,
                "errors": form
            }
            return JsonResponse(data)
        # return render(request, self.template_name, {'form': form})


from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_world():
    return 'Hello, World!'