from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.pylab


def release_line(Line):
    Line.remove()


def blurry():
    global Lines


def release():
    global CurrentPoint, Points, AllPoints, CurrentLine, Lines, AllLines
    if CurrentPoint:
        CurrentPoint = None
        CurrentLine = None
        for Line in Lines:
            release_line(Line)
        if AllPoints:
            Points = AllPoints[len(AllPoints)-1]
            Lines = AllLines[len(AllLines)-1]
        else:
            Points = []
            Lines = []
    else:
        if not AllPoints:
            print("All graghs have been deleted!")
        else:
            Lines = AllLines[-1]
            for Line in Lines:
                release_line(Line)
            AllLines.pop()
            AllPoints.pop()
            Lines = []


def button_press(event):
    global CurrentPoint, Points, AllPoints, CurrentLine, Lines, AllLines, Lastline
    if Lastline:
        release_line(Lastline)
        Lastline = None
    if CurrentPoint:
        CurrentLine = plt.plot([CurrentPoint[0], event.xdata],
                               [CurrentPoint[1], event.ydata], color='blue')[0]
        Lines.append(CurrentLine)
    CurrentPoint = (event.xdata, event.ydata)
    Points.append(CurrentPoint)
    if len(Points) == 4:
        AllPoints.append(Points)
        CurrentLine = plt.plot([Points[0][0], event.xdata], [
            Points[0][1], event.ydata], color='blue')[0]
        Lines.append(CurrentLine)
        CurrentPoint = None
        Points = []
        print(Lines)
        AllLines.append(Lines)
        Lines = []
    event.canvas.draw()


def motion_notify(event):
    global CurrentPoint, Lastline, CurrentLine
    if CurrentPoint:
        if Lastline:
            release_line(Lastline)
        CurrentLine = plt.plot([CurrentPoint[0], event.xdata],
                               [CurrentPoint[1], event.ydata], color='green')[0]
        Lastline = CurrentLine
    event.canvas.draw()


def key_press(event):
    print(event.name)
    print(event.key)
    if(event.key == 'q'):
        return
    if(event.key == 'f1'):
        print("this is f1")
    if(event.key == 'c'):
        release()
    if(event.key == 'f1'):
        blurry()
    event.canvas.draw()


fig, ax = plt.subplots()
img = matplotlib.pylab.array(Image.open('test.png'))
plt.imshow(img)
AllPoints = []
AllLines = []
Lines = []
Points = []
CurrentPoint = None
Lastline = None
CurrentLine = None
fig.canvas.mpl_connect('button_press_event', button_press)
fig.canvas.mpl_connect('motion_notify_event', motion_notify)
fig.canvas.mpl_connect('key_press_event', key_press)
plt.show()
