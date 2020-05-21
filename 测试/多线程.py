'''
@Author: your name
@Date: 2020-01-30 10:58:17
@LastEditTime : 2020-01-30 13:34:22
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\测试\多线程.py
'''
def infos_out():
    infos=[]
    x={'name':'a','job':'b'}
    print(x['name'])
    for element in x:
        infos.append(element)
        print(element)
    print(infos)
    return infos

def infos_out_2():
    infos = []
    name=1
    content=2
    laugh=3
    comment=4
    info = {
            'name':name,
            'content':comment,
            'laugh':laugh,
            'comment':comment,
        }
    infos.append(info)
    print('name:',info['name'])
    print('names:',infos)
    return  infos

    
if __name__ == "__main__":
    infos_out()
    infos_out_2()