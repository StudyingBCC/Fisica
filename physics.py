import math as m

gravidade = 9.80665

def v_0_x(v_inicio, angulo):
    angulo = m.radians(angulo)
    cos_ang = round(m.cos(angulo), 6)

    return round(v_inicio * cos_ang, 6)

def pos_x(angulo, v_inicio, tempo):
    velocidade = v_0_x(v_inicio, angulo)

    return round(velocidade * tempo, 4)

def v_0_y(v_inicio, angulo):
    angulo = m.radians(angulo)
    sen_ang = round(m.sin(angulo), 6)

    return round(v_inicio * sen_ang, 6)

def v_y(v_inicio, angulo, tempo):
    v0y = v_0_y(v_inicio, angulo)

    return round(v0y - round(gravidade * tempo, 6), 6)

def pos_y(angulo, pInicio, v_inicio, tempo):
    v0y = v_0_y(v_inicio, angulo)

    return round(pInicio + v0y * tempo - ((gravidade * (m.pow(tempo, 2)))/2), 4)

def ang(v_x, v_y):
    tg_ang = v_y / v_x

    return m.degrees(m.atan(tg_ang))

def v_t(v_inicio, angulo, tempo):
    return round(m.sqrt(m.pow(v_0_x(v_inicio, angulo), 2) + m.pow(v_y(v_inicio, angulo, tempo), 2)), 4)