import time


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return f'Пользователь: {self.nickname} {self.age}'


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.time_now = 0,
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __contains__(self, keyword):
        return keyword.lower() in self.title.lower()


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __str__(self):
        return f'Видео: {self.title} {self.duration}'

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                return f'Вход выполнен для {nickname}'
        return f'такой пользователь не найден'

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        print(f'Зарегистрирован пользователь {nickname}')
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, keyword):
        found_videos = []
        for video in self.videos:
            if keyword.lower() in video.title.lower():
                found_videos.append(video.title)
        return found_videos

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт')
            return
        for video in self.videos:
            if video.title.lower() == title.lower():
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет: покиньте страницу")
                    return
                for second in range(1, video.duration+1):
                    print(second)
                    time.sleep(1)
                print('Конец видео')
                return


v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

ur = UrTube()

# Добавление видео !!! КАК ДОБАВИТЬ ЛЮБОЕ КОЛИЧЕСТВО ВИДЕО В АРГУМЕНТЫ МЕТОДА?
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

ur.log_in('vasya_pupkin', 'lolkekcheburek')
