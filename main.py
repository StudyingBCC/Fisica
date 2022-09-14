import physics as ps
import matplotlib.pyplot as plt
import pandas as pd


angulo = float(input("Qual o ângulo?: "))
v_inicial = float(input("Qual a velocidade inicial?: "))
pInicial = float(input("Qual a posição inicial?: "))
tempo = 0

intervalos = []
posicoes_x = []
posicoes_y = []
vX = []
vY = []
vT = []
comp_vx = []
comp_vy = []
angulos = []

while(tempo >= 0):
  pos_x = ps.pos_x(angulo, v_inicial, tempo)
  pos_y = ps.pos_y(angulo, pInicial, v_inicial, tempo)
  v0x = ps.v_0_x(v_inicial, angulo)
  v0y = ps.v_0_y(v_inicial, angulo)
  vx = v0x
  vy = ps.v_y(v_inicial, angulo, tempo)
  vt = ps.v_t(v_inicial, angulo, tempo)

  if tempo > 0:
    ang = ps.ang(ps.v_0_x(v_inicial, angulo), ps.v_y(v_inicial, angulo, tempo))
  else:
      ang = angulo

  intervalos.append(tempo)
  posicoes_x.append(pos_x)
  posicoes_y.append(pos_y)
  vX.append(vx)
  vY.append(vy)
  vT.append(vt)
  comp_vx.append(v0x)
  comp_vy.append(v0y)
  angulos.append(ang)

  if tempo > 0 and pos_y < 0:
    break

  tempo += 0.1


plt.figure('Movimento Balístico')
plt.ylabel('Altura')
plt.xlabel('Distância')
plt.plot(posicoes_x, posicoes_y, color="deeppink")
plt.xlim(left = -1)
plt.grid(True)

planilha = pd.DataFrame({'T(s)': intervalos, 'X(m)':posicoes_x, 'Y(m)': posicoes_y, 'V0x(m/s)': comp_vx, 'V0y(m/s)': comp_vy, 'Vx(m/s)': vX, 'Vy(m/s)': vY, 'Vt(m/s)': vT, 'α(°)': angulos})

print(planilha)

plt.show()