#玩家信息表
from save_system import save_game,load_game,list_saves,delete_save

player={
    "name":"一号存档",
    "level":5,
    "hp":99.5,
    "mp":100,
    "attack":10,
    "defense":5,
    "speed":100000,
    "is_alive":True
}

MAX_SLOTS=3

for info in list_saves(MAX_SLOTS):
    print(info)

act=int(input("请选择要执行的操作：\n1.存档\n2.读取\n3.删除\n4.退出\n"))

if act==1:
    slot_number = int(input("请输入要保存的存档槽位编号(1~3):"))

    save_game(player,slot_number)

    current_data=None

elif act==2:

    slot_number = int(input("请输入要读取的存档槽位编号(1~3):"))

    current_data=load_game(slot_number)

elif act==3:
    slot_number = int(input("请输入要删除的存档槽位编号(1~3):"))

    delete_save(slot_number)

    current_data=None

elif act==4:

    print("操作已取消。")
    exit()

else:
    print("Wrong input!")
    exit()

if current_data:
    print("名称：",current_data["name"])
    print("等级：",current_data["level"])
    print("生命值：",current_data["hp"])
    print("专注值：",current_data["mp"])
    print("攻击力：",current_data["attack"])
    print("防御力：",current_data["defense"])
    print("速度：",current_data["speed"])
    print("存档时间：",current_data["save_time"])