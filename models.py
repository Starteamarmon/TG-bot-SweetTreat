from tortoise import Tortoise, fields, models

class User(models.Model):
    id = fields.IntField(pk=True)
    chat_id = fields.IntField()
    name = fields.CharField(max_length=100)
    phone_num = fields.CharField(max_length=20)

    def __str__(self):
        return f"User(id={self.id}, name={self.name})"

# Определение модели заказа
class Order(models.Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField('models.User', related_name='orders')
    order = fields.CharField(max_length=255)
    date_creat = fields.DatetimeField(auto_now_add=True)
    # date_need = fields.CharField(max_length=255)

    def __str__(self):
        return f"Order(id={self.id}, user_id={self.user_id}, order={self.order})"

# Инициализация Tortoise ORM
async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['models']}
    )
    await Tortoise.generate_schemas()

from tortoise import Tortoise