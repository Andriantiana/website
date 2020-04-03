from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from hashlib import md5 #Pour affichage avatars mais considérer autre chose pour la mise en production
from app import db
from app import login

#Table Followers
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
    )

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default = datetime.utcnow)
    #Utilisateurs suivis
    followed = db.relationship(
        'User', secondary = followers,#secondary configure la table d'association
        primaryjoin = (followers.c.follower_id == id),#indique la condition qui lie l'entité à la gauche(follower) dans la table d'association
        secondaryjoin = (followers.c.followed_id == id),#indique la condition qui lie l'entité à droite dans la table d'association
        backref = db.backref('followers', lazy = 'dynamic'), lazy = 'dynamic')#Un mode dynamic configure la requête pour qu'elle ne s'exécute pas tant qu'elle n'est pas spécifiquement demandée

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
          
    #Methode à revoir pour remplacer Gravatar
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
    #Methode pour gestion des followed et leurs posts     
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
    
    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            
    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0
            
    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id = self.id)
        return followed.union(own).order_by(Post.timestamp.desc())


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
   
    
    def __repr__(self):
        return '<Post {}>'.format(self.body)
        
        
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
    
    
    
