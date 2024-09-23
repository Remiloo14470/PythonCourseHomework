from PIL import Image, ImageFilter
import pandas as pd
import requests

"""filename = f"./image.jpg"


def image_change(filename):
    my_image = Image.open(filename)
    new_image = my_image.resize((450, 280))
    new_image.show()
    new_image.save(f'./image2.jpg')
    blurred = my_image.filter(ImageFilter.BLUR)
    blurred.show()
    blurred.save(f'./image_blurred.jpg')
    sharpened = my_image.filter(ImageFilter.SHARPEN)
    sharpened.show()
    sharpened.save(f'./image_sharp.jpg')


image_change(filename)"""

'''
data = {
    'Name': ['Emily','Edgar', 'Elly', 'Tom'],
    'Age': [33, 39, 67, 74],
    'City': ['New York', 'Boston', 'London', 'Moscow'],
    'Salary': [3800, 2909, 44000, 2450]
}

df = pd.DataFrame(data)
print(df.head())
print()
print(df['Name'])
print()
print(f'Данные по Эдгару: \n{df.loc[1]}')
print()
print(f'Cредний возраст: {df['Age'].mean()}')
df.to_csv('./employees_data.csv', index=False)'''

'''try:
    data = requests.get('https://vk.ru/feed')
    content = data.content
    text = data.text
    print(data.headers)
    print(data)
except Exception as exc:
    print(f'Ошибка: {exc}')

params = {'q': 'Sea', 'order': 'popular','min_width': '1000', 'min_height': '800'}
try:
    req = requests.get('https://unsplash.com/wallpapers', params=params)
    print(req.url)
except Exception as ex:
    print(f'Ошибка: {ex}')'''