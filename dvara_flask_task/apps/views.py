from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from apps import app
from .models import Category, SubCategory
from .forms import CategoryForm


@app.route('/', methods=['GET', 'POST'])
def category():
    if request.method == 'POST':
        missing = list()
        for k, v in request.form.items():
            if v == "":
                missing.append(k)
        if missing:
            data = {
                'success': False,
                'message': f"Missing fields for {', '.join(missing)}"
            }
            return data
        subcategory_obj = SubCategory.query.filter_by(
            id=request.form.get('subcategory')
        ).first_or_404(description='There is no data with {}'.format(request.form.get('subcategory')))
        sub_category = SubCategory(
            category_id=request.form.get('category'),
            subcategory=subcategory_obj.subcategory,
        )
        sub_category.save()
        records = SubCategory.query.order_by(SubCategory.id.desc()).all()
        if records:
            result = [{
                'id': obj.id,
                'subcategory': obj.subcategory,
                'category': obj.category.categories
            } for obj in records]
            data = {
                "success": True,
                "records": result
            }
        else:
            data = {
                'success': False,
                'message': "No Data Found!"
            }
        return data
    else:
        records = SubCategory.query.order_by(SubCategory.id.desc()).all()
        form = CategoryForm(request.form)
        form.category.choices = [('', 'Select Category')]+[(g.id, g.categories) for g in Category.query.order_by(Category.id).all()]
        form.subcategory.choices = [('', 'Select SubCategory')]
        context = {
            "records": records,
            "form": form
        }
        return render_template("index.html", context=context)

@app.route('/get_subcategory')
def get_subcategory():
    category_id = request.args.get('category_id', 0, type=str)
    subcategory_objs = SubCategory.query.filter_by(category_id=category_id).order_by(SubCategory.id)
    if subcategory_objs:
        result = [{
            'id': obj.id,
            'subcategory': obj.subcategory
        } for obj in subcategory_objs]
        data = {
            'success': True,
            'records': result
        }
    else:
        data = {
            'success': False,
            'message': "No Data Found!"
        }
    return data