import turtle as t
for i in range(4):
    t.seth(90 * (i + 1) )
    t.circle(200, 90)
    t.seth(-90 + i * 90)
    t.circle(200, 90)