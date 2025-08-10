import json
import os
from datetime import datetime

save_dir="week01/saves"

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

def get_save(slot):
    return os.path.join(save_dir,f"save_slot{slot}.json")

#=========================================================================#
# 以下为功能函数

def save_game(data,slot=1):

    '''保存玩家数据到json文件save.json，并添加时间戳。'''

    data["save_time"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    file_name=get_save(slot)

    if os.path.exists(file_name):

        Ensure=input(f"存档{slot}已存在，是否覆盖？(Y/N)")

        if Ensure.upper()=="Y":

            with open(file_name,"w",encoding="utf-8") as file:
                json.dump(data,file,ensure_ascii=False,indent=4)
            print(f"存档{slot}已保存。")
        else:
            print("存档已取消。")
    else:

        with open(file_name,"w",encoding="utf-8") as file:
            json.dump(data,file,ensure_ascii=False,indent=4)
        print(f"存档{slot}已保存。")

def load_game(slot):

    '''从json文件save.json读取玩家数据。'''

    file_name=get_save(slot)
    if os.path.exists(file_name):
            with open(file_name,"r",encoding="utf-8") as file:
                return json.load(file)
    else:
        return None

def delete_save(slot):
    '''删除指定存档'''

    file_name=get_save(slot)

    if os.path.exists(file_name):
        Ensure=input(f"确定要删除存档{slot}吗？(Y/N)")

        if Ensure.upper()=="Y":
            os.remove(file_name)
            print(f"存档{slot}已删除。")
            
        else:
            print("删除已取消。")  

    else:
        print(f"存档{slot}不存在！")

def list_saves(max_slots=3):

    '''列出所有存档文件。'''

    save_slots=[]

    for slot in range(1,max_slots+1):

        data=load_game(slot)

        if data:
            save_slots.append(f"[{slot}] {data['name']} Lv{data['level']} 存档时间：{data['save_time']}")
        else:
            save_slots.append(f"[{slot}] 空")
    return save_slots