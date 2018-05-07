# encoding: utf-8
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

__author__ = 'poet'
# 4/28/18


from datetime import date, datetime
from flask_sqlalchemy import  SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    """ 所有model 基类  默认添加时间戳"""
    __abstract__ =True
    # 设置两个默认的时间戳
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    # 权限
    ROLE_USER = 10
    ROLE_STAFF = 20
    ROLE_ADMIN = 30


    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, index=True, nullable=True)
    email  = db.Column(db.String(64), unique=True, index=True, nullable=False)
    _password = db.Column('password', db.String(256),nullable=False)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    job = db.Column(db.String(64))
    publish_courses = db.relationship('Course')


    def __repr__(self):
        return '<User:{}'.format(self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, origin_password):
        """ Python 风格 的 setter  自动保存 password 的 哈希值"""
        self._password = generate_password_hash


    def check_password(self, password):
        """ 判断 用户输入的密码 和储存的 哈希值 密码是否相等"""

        return check_password_hash(self._password, password)

    @property
    def is_admin(self):
        return self.role == self.ROLE_ADMIN

    @property
    def is_staff(self):
        return self.role == self.ROLE_STAFF

class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    author = db.relationship('User', uselist=False)


