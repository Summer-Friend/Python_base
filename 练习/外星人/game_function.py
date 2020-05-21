'''
@Author: your name
@Date: 2020-01-30 14:29:12
@LastEditTime : 2020-01-30 19:19:55
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\练习\外星人\game_function.py
'''
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

#按键部分#########################################
def check_keyup_events(event,ship):
    #响应松开
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    elif event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key==pygame.K_UP:
        ship.moving_up=False
    elif event.key==pygame.K_DOWN:
        ship.moving_down=False
    
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #响应按下
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    elif event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key==pygame.K_UP:
        ship.moving_up=True
    elif event.key==pygame.K_DOWN:
        ship.moving_down=True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    #关闭游戏按q
    elif event.key ==pygame.K_q:
        sys.exit()
        
        
def check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets):
     for event in pygame.event.get():
            #点击关闭的事件响应
            if event.type==pygame.QUIT:
                sys.exit()  
            elif event.type==pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y =pygame.mouse.get_pos()
                check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)
            #确保连续移动
            #上下左右键都加进去了
            elif  event.type==pygame.KEYDOWN:
                check_keydown_events(event,ai_settings,screen,ship,bullets)
            elif  event.type==pygame.KEYUP:
                check_keyup_events(event,ship)
                
                
def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    #单击play开始新游戏
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        #重置游戏设置
        ai_settings.initial_dynamic_settings()
        
        #隐藏光标(就是鼠标)
        pygame.mouse.set_visible(False)
        
        stats.reset_stats()
        stats.game_active = True
        
        aliens.empty()
        bullets.empty()
        
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        
                   
#屏幕部分#####################################3
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    
    screen.fill(ai_settings.bg_color)
    sb.show_score()
    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        
    ship.blitme()
    aliens.draw(screen)
    #alien.blitme()
    if not stats.game_active:
        play_button.draw_button()
        
    #屏幕绘制
    pygame.display.flip()
   
#子弹部分################################# 
#同时用来更新外星人   
def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
    #删除已经消失的子弹，否则其依然存在并消耗内存
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    #调试用的，确认子弹确实已经消失
    #print(len(bullets))
    #检查是否有子弹击中了外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    
    if collisions:
        for aliens in collisions.values():    
            stats.score += ai_settings.alien_points*len(aliens)
            sb.prep_score()
    
    if len(aliens) == 0:
       #删除现有的子弹并创建一群新的外星人
       bullets.empty()
       ai_settings.increase_speed()
       create_fleet(ai_settings,screen,ship,aliens)
                

def fire_bullet(ai_settings,screen,ship,bullets):
    #创建子弹，并将其加入编组
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)             

#外星人部分################################################         
def get_number_aliens_x(ai_settings,alien_width):
    #计算一行最多容纳的长度
    available_space_x = ai_settings.screen_width-2*alien_width
    #计算最多的外星人个数
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_aliens_rows(ai_settings,ship_height,alien_height):
    #计算一行最多容纳的高度
    #可以随意调整
    available_space_y = (ai_settings.screen_height-(3*alien_height)-ship_height*2)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
    
def create_fleet(ai_settings,screen,ship,aliens):
    alien = Alien(ai_settings,screen)
    #计算最多的外星人个数
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_aliens_rows(ai_settings,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):    
       #创建第一行外星人
       for alien_number in range(number_aliens_x):
           #创建一个外星人并将其加入当前行
           create_alien(ai_settings,screen,aliens,alien_number,row_number)


def check_fleet_edges(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
#碰撞响应
def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    if stats.ship_left > 0:
        #剩余飞船数减一
        stats.ship_left -= 1
    
        aliens.empty()
        bullets.empty()
    
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
    
        #暂停
        sleep(0.5)
    else:
        stats.game_active = False
        #光标立刻出现
        pygame.mouse.set_visible(True)

#外星人到达底部响应
def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #按照飞船碰撞处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break
            
    
            
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    #检查是否有外星人越界并更新位置
    check_fleet_edges(ai_settings,aliens)
    aliens.update()     
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
    '''  
    #检测碰撞
    #没意思，，，所以没加
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
    '''