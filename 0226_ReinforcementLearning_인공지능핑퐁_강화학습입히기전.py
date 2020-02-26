from tkinter import *
import random
import time

class Ball:

    def __init__(self, canvas, paddle, color):
        
        self.canvas = canvas
        self.paddle = paddle
        self.canvas_height = self.canvas.winfo_height()
        print('높이', self.canvas_height)
        self.canvas_width = self.canvas.winfo_width()
        print('넓이', self.canvas_width)

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) #공 좌표 및 색깔(oval : object 형태 타입)

        self.canvas.move(self.id, 250, 100) #공을 캔버스 중앙으로 이동
  
        starts = [ -3, -2, -1,  1,  2,  3 ]
        random.shuffle( starts )
        self.x = starts[0]
        self.y = -3 
        self.canvas.bind_all('<Key>', self.turn_space )


    # 키보드 방향키 -> 을 누르면 turn_right 라는 함수가 실행되게해라!

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

    def turn_space( self, evt ):
       starts =[ -9, -8, -7, -3, -2, -1 ]
       random.shuffle(starts)
       self.y = -3
       self.x =  starts[0]            
                
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords( self.id )
        ball_pos = self.canvas.coords( self.id )
        paddle_pos = self.canvas.coords( self.paddle.id) 
        print  (  paddle_pos[0], ( ball_pos[0], ball_pos[1] ), ( self.x, self.y ) )  
        
        if  pos[1] <= 0:
            self.y = 3
        if  pos[3] >= self.canvas_height:
            self.y = -3
        if  pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3 
            
        if  self.hit_paddle(pos) == True:
            self.y = -3
            


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)  # 패들의 높이와 넓이 그리고 색깔

        self.canvas.move(self.id, 200, 300)  # 패들 사각형을 200,300 에 위치
        self.x = 0  # 패들이 처음 시작할때 움직이지 않게 0으로 설정
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()  # 캔버스의 높이를 반환한다. 
        self.canvas_width = self.canvas.winfo_width()  # 캔버스의 넓이를 반환한다. 캔버스 밖으로 패들이 나가지 않도록
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)  # 왼쪽 화살표 키를 '<KeyPress-Left>'  라는 이름로 바인딩
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)  # 오른쪽도 마찬가지로 바인딩한다.
        self.canvas.bind_all('<KeyPress-Up>', self.turn_up)  # 왼쪽 화살표 키를 '<KeyPress-Left>'  라는 이름로 바인딩
        self.canvas.bind_all('<KeyPress-Down>', self.turn_down)  # 
        
    def draw(self):
        pos = self.canvas.coords(self.id)
        # print(pos)
        self.canvas.move(self.id, self.x, 0)
        if pos[0] <= 0:
            self.x = 1  # 멈춰라 
        elif  pos[2] >= self.canvas_width:
            self.x = -1
    
        # 패들이 화면의 끝에 부딪히면 공처럼 튕기는게 아니라 움직임이 멈춰야한다.
        # 그래서 왼쪽 x 좌표(pos[0]) 가 0 과 같거나 작으면 self.x = 0 처럼 x 변수에 0 을
        # 설정한다.  같은 방법으로 오른쪽 x 좌표(pos[2]) 가 캔버스의 폭과 같거나 크면
        # self.x = 0 처럼 변수에 0 을 설정한다.

    def turn_left(self, evt):  # 패들의 방향을 전환하는 함수
        self.x = -4

    def turn_right(self, evt):
        self.x = 4
        
    def turn_up(self, evt):
        self.y = -4

    def turn_down(self, evt):
        self.y = 4        

    def move(self, x):
        self.x = x

tk = Tk()     # 1. tk 를 인스턴스화 한다.



tk.title("Game")  # 2. tk 객체의 title 메소드(함수)로 게임창에 제목을 부여한다.



tk.resizable(0, 0) # 3. 게임창의 크기는 가로나 세로로 변경될수 없다라고 말하는것이다.
tk.wm_attributes("-topmost", 1) #4. 다른 모든 창들 앞에 캔버스를 가진 창이 위치할것을 tkinter 에게 알려준다.
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)


canvas.pack()       # 앞의 코드에서 전달된 폭과 높이는 매개변수에 따라 크기를 맞추라고 캔버스에에 말해준다.
tk.update()   # tkinter 에게 게임에서의 애니메이션을 위해 자신을 초기화하라고 알려주는것이다.

paddle = Paddle( canvas, 'blue')
ball1 = Ball( canvas, paddle, 'red')


while 1:
    ball1.draw()
    paddle.draw() 
    
    tk.update_idletasks()   # 우리가 창을 닫으라고 할때까지 계속해서 tkinter 에게 화면을 그리고
    tk.update()
    time.sleep(0.01)  # 100분의 1초마다 잠들어라 !

 
