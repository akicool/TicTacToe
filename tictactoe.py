import pygame
import sys

def win_check(mas, sign):
    zero = 0
    for row in mas:
        zero += row.count(0)
        if row.count(sign)==3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign         
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zero == 0:
        return 'Peace!'       
    return False                    
  
# initializing the constructor
pygame.init()
  

size_block = 220 # 100
margin = 15
width = height = size_block*3 + margin*4



# screen resolution
res = (720, 720) # (width, height)
  
# opens up a window
screen = pygame.display.set_mode(res)
pygame.display.set_caption('Tic-Tac-Toe!')

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0]*3 for i in range(3)]
count = 0 # += 1
game_stop = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_stop:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if count % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                count += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_stop = False
            mas = [[0]*3 for i in range(3)]
            count = 0
            screen.fill(black)


    if not game_stop:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white

                # crate game zone
                x = col*size_block + (col+1) * margin
                y = row*size_block + (row+1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x+5, y+5), (x + size_block-5, y + size_block-5), 3)
                    pygame.draw.line(screen, white, (x + size_block-5, y+5), (x+5, y + size_block-5), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 3)
        if (count - 1) % 2 == 0:
            game_stop = win_check(mas, 'x')
        else:
            game_stop = win_check(mas, 'o')
        
        if game_stop:
            screen.fill(black)
            font = pygame.font.SysFont('stxingkai', 80)
            text1 = font.render(game_stop, True, white)
            text_rect = text1.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text1, [text_x, text_y])

        pygame.display.update()