import os
# print(os.name)
# Создание и удаление папки
# os.mkdir("new_folder")
# os.rmdir("new_folder")
# os.rename("new.txt", "old.txt")


# if os.path.exists("old.txt"):
#     print("File exists")
#     os.remove("old.txt")
# else:
#     print("File does not exist")
#     open("old.txt", "w").close()
    
# os.makedirs("new_folder/inner_folder", exist_ok=True)
# os.removedirs("new_folder/inner_folder")

# folers = "folders/" * 132
# os.makedirs(folders, exist_ok=True)
# # os.removedirs(folders)

# # os.chdir("C:/")
# print("Текущее положение:", os.getcwd())
# # folders = "folders/" * 2
# # os.makedirs(folders,exist_ok=True)
# os.replace("new.txt","c:/old.txt")


# for _, _, filenames in os.walk("."):
#     print(filenames) if ... else ...
    
# for _, _, filenames in os.walk("."):
# for filename in filenames:        
#         print(filename, end=", ") if filename.endswith(".py") else ...


# from sys import*
# import subprocess




# # print(version)
# # print(platform)

# # code = subprocess.call(["python", "p1.py"])

# # path.append("C:/Users/user/Documents")
# # # print (path)
# # import test123
# # print (test123.x)


# # if platform == "win32":
# #     subprocess.call("mspaint")
# # elif platform.startswith("linux"):
# #     subprocess.call("gnome-calculator")
    
    
# import shutil
# # высокоуровневые операции для работы с файлами

# shutil.copy("txt.txt","txt10.py")

# shutil.copytree(".", "new_folder-1")
# shutil.copytree("..", "new_folder-2")


# shutil.make_archive("archive", "zip", "sub_dir")
# shutil.make_archive("archive", "gztar", "sub_dir")
# usage = shutil.disk_usage("c:\\")
# print(usage)
# print(f'{usage.total / (1024 ** 3) :.1f}')

# dx, dy = -5, -5


# def move_ball():
#     global dx, dy
#     canvas.move(ball, dx, dy)
#     root.after(50, move_ball)
#     x1, y1, x2, y2 = canvas.coords(ball)
#     if x1 <= 0:
#         dx = -dx
#     if y1 <= 0:
#         dy = -dy

# def move_ball():
#     global dx, dy
#     canvas.move(ball, dx, dy)
#     x1, y1, x2, y2 = canvas.coords(ball)
    
#     # Отскок от стен
#     if x1 <= 0 or x2 >= 400:
#         dx = -dx
#     if y1 <= 0:
#         dy = -dy
    
#     # Проигрыш при падении вниз
#     if y2 >= 300:
#         print("Проигрыш!")
#         return
    
#     # Отскок от платформы
#     px1, py1, px2, py2 = canvas.coords(paddle)
#     if y2 >= py1 and x2 >= px1 and x1 <= px2:
#         dy = -dy
    
#     root.after(50, move_ball)
    
import logging
import colorlog

logging.debug("Подробная информация для отладки")      # DEBUG
logging.info("Общая информация о работе")
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

# Настройка цветного логирования
handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(levelname)s:%(name)s:%(message)s'
))

logger = colorlog.getLogger('example')
logger.addHandler(handler)

logger.debug("Подробная информация для отладки")      # DEBUG
logger.info("Общая информация о работе")
logger.warning("Предупреждение о проблеме")   
logger.error("Ошибка в программе")                    # ERROR
logger.critical("Критическая ошибка!")

