from django.db import models
import datetime
# Create your models here.

items_number = 14

Description = {
        '01':'精心為您挑選來自不同產區的每日精選咖啡，帶給您多元的咖啡風味。',
        '02':'精心為您挑選來自不同產區的每日精選咖啡，帶給您多元的咖啡風味。',
        '03':'以一半每日精選咖啡和一半牛奶調製而成順口平衡的咖啡風味，咖啡風味隨著每日精選咖啡豆的不同而產生精彩的風味變化，但卻都有著順口平衡的好風味。',
        '04':'融合濃縮咖啡及現蒸牛奶，加上豐厚細緻的奶泡，呈現醇厚咖啡風味。',
        '05':'以較短秒數醇厚的Ristretto Shot製作，口感濃郁、蘊含濃縮咖啡的甜味，搭配豐厚細緻的奶泡，重現經典義式咖啡的美好風味。',
        '06':'濃郁醇厚的濃縮咖啡，搭配新鮮蒸煮的優質鮮奶，覆上綿密細緻的奶泡。',
        '07':'濃郁醇厚的濃縮咖啡，搭配優質鮮奶，經典咖啡風味。',
        '08':'融合新鮮蒸奶及香草風味糖漿後，倒入濃縮咖啡並在奶泡上覆以香甜焦糖醬，呈現多層次風味，是星巴克深受歡迎的飲料。',
        '09':'融合優質鮮奶及香草風味糖漿後，倒入濃縮咖啡並在牛奶上覆以香甜焦糖醬，呈現多層次風味，是星巴克深受歡迎的飲料。',
        '10':'由濃縮咖啡、摩卡醬及新鮮蒸奶調製，覆上輕盈柔細的鮮奶油，帶來香濃的巧克力及咖啡風味。',
        '11':'由濃縮咖啡、摩卡醬及優質鮮奶調製，覆上輕盈柔細的鮮奶油，帶來香濃的巧克力及咖啡風味。',
        '12':'以歐洲方式調製，結合經典濃縮咖啡及熱水，帶來濃郁豐富的咖啡滋味。',
        '13':'以歐洲方式調製，帶來濃郁豐富的咖啡滋味。',
        '14':'濃郁豐厚的濃縮咖啡是星巴克咖啡的靈魂，它醇厚的口感、綿長香氣及焦糖般的甜味，豐富而令人難忘。'
}

Name = {
        '01':'每日精選咖啡',
        '02':'冰每日精選咖啡',
        '03':'咖啡密斯朵',
        '04':'卡布奇諾',
        '05':'濃粹那堤',
        '06':'那堤',
        '07':'冰那堤',
        '08':'焦糖瑪奇朵',
        '09':'冰焦糖瑪奇朵',
        '10':'摩卡',
        '11':'冰摩卡',
        '12':'美式咖啡',
        '13':'冰美式咖啡',
        '14':'濃縮咖啡',
}
Price = {
        '01':85,
        '02':85,
        '03':85,
        '04':120,
        '05':135,
        '06':120,
        '07':120,
        '08':140,
        '09':140,
        '10':135,
        '11':135,
        '12':95,
        '13':95,
        '14':80,
}

class Item(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	price = models.IntegerField(default=0)
	img_src = models.CharField(max_length=30, default="images/pic01.jpg")

	def insert(self, key):
		self.name = Name[key]
		self.description = Description[key]
		self.price = Price[key]
		self.img_src = "images/"+key+".jpg"

class Customer(models.Model):
    table = models.CharField(max_length=3)
    password = models.CharField(max_length=16)

class Order(models.Model):
    order_id = models.IntegerField()

class SingleOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
	#table = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    temp_choices = (
        ("iced", "正常冰"),
        ("little-iced", "少冰"),
        ("cool", "去冰"),
        ("hot", "熱"),
    )
    temp = models.CharField(max_length=4, choices=temp_choices)
    sugar_choices = (
        ("normal", "正常糖"),
        ("little", "少糖"),
        ("no", "無糖"),
    )
    sugar = models.CharField(max_length=4, choices=sugar_choices)
    count = models.IntegerField()
    status_choices = (
        ("unsent", "未下單"),
        ("unconfirmed", "未確認"),
		("confirmed", "已確認(待處理)"),
		("making", "製作中"),
        ("payed", "已付款")
    )
    status = models.CharField(max_length=4, choices=status_choices, default="unsent")

    def as_dict(self):
        return {
            "name": self.name,
            "temp": self.temp,
            "sugar": self.sugar,
            "count": self.count,
            "status": self.status,
            "id": self.pk,
            "confirmed": self.status == '已確認(待處理)',
    }
    # comment = models.CharField(max_length=100, blank=True)
