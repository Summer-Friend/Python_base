'''
@Author: your name
@Date: 2020-01-19 16:13:56
@LastEditTime : 2020-01-19 16:29:23
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\编程测试\字典排序.py
'''
def dictionairy():  
  
    # 声明字典
    key_value ={}     
 
    # 初始化
    key_value[2] = 56       
    key_value[1] = 2 
    key_value[5] = 12 
    key_value[4] = 24
    key_value[6] = 18      
    key_value[3] = 323 
 
    print ("按键(key)排序:")   
 
    # sorted(key_value) 返回一个迭代器
    # 字典按键排序
    for i in sorted (key_value) : 
        print ((i, key_value[i]), end =" ") 
    print ("\n按值(value)排序:")   
    #key=lambda 元素: 元素[字段索引],lambda后面跟的随便定，冒号后面的kv[1]就是按照第二个元素进行排序
    print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))    
    print(key_value.items())
def main(): 
    # 调用函数
    dictionairy()              
      
# 主函数
if __name__=="__main__":      
    main()