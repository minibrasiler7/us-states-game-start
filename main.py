import turtle
import pandas

s = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
town_guess = []
pen.speed("fastest")
s.title("US game quiz")
image = "blank_states_img.gif"
s.addshape(image)
turtle.shape(image)
score = 0
game_on = True
data = pandas.read_csv("50_states.csv")
while len(town_guess)<50:
    answer = s.textinput(title=f"{score}/ 50 Guess state", prompt= "Could you find another stat?")
    answer = answer.title()
    list_etat = data.state.tolist()
    if answer == "Exit":
        break
    elif answer in list_etat and answer not in town_guess:
        x = data[data["state"] == answer].x.tolist()[0]
        y = data[data["state"] == answer].y.tolist()[0]
        pen.goto(x, y)
        pen.write(answer)
        score += 1
        town_guess.append(answer)

liste_etat = data.state.tolist()
liste_a_apprendre = []
for etat in liste_etat:
    if etat not in town_guess:
        liste_a_apprendre.append(etat)


new_data = pandas.DataFrame(liste_a_apprendre)
new_data.to_csv("State to learn")
