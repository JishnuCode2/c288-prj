from controller import Robot, Keyboard

robot = Robot()

timestep = int(robot.getBasicTimeStep())

kb = Keyboard()
kb.enable(timestep)

a = robot.getDevice("A motor");
b = robot.getDevice("B motor");
c = robot.getDevice("C motor");
d = robot.getDevice("D motor");
e = robot.getDevice("E motor");
f = robot.getDevice("F motor");

ap=0;
bp=0;
cp=0;
dp=0;
ep=0;
fp=0;

def move_bot(p=0, q=0, r=0, s=0, t=0, u=0):
    a.setPosition(p);
    b.setPosition(q);
    c.setPosition(r);
    d.setPosition(s);
    e.setPosition(t);
    f.setPosition(u);

move_bot()

while robot.step(timestep) != -1:
    key_pressed = kb.getKey();
    print(key_pressed);

    if(key_pressed == 49):
        ap += 0.01
    if(key_pressed == 50):
        ap -= 0.01
        
    if(key_pressed == 51):
        bp += 0.01
    if(key_pressed == 52):
        bp -=0.01
        
    if(key_pressed == 53):
        cp += 0.01
    if(key_pressed == 54):
        cp -= 0.01
        
    if(key_pressed == 55):
        dp += 0.01
    if(key_pressed == 56):
        dp -= 0.01
        
    if(key_pressed == 57):
        ep += 0.01
    if(key_pressed == 48):
        ep -= 0.01
         
    if(key_pressed == 81):
        fp += 0.01
    if(key_pressed == 87):
        fp -= 0.01
        
    move_bot(ap, bp, cp, dp, ep, fp);
        