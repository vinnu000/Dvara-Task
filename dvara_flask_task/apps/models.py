from apps import db


class Category(db.Model):
    __tablename__ = 'category'
    id          = db.Column(db.Integer, primary_key=True)
    categories  = db.Column(db.String(30), nullable=True)

    def save(self):
        db.session.add(self)
        db.session.commit()
    

class SubCategory(db.Model):
    __tablename__ = 'subcategory'
    id          = db.Column(db.Integer, primary_key=True)
    subcategory = db.Column(db.String(30), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category    = db.relationship(Category, backref=db.backref('category'))

    def save(self):
        db.session.add(self)
        db.session.commit()
