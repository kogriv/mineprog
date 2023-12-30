from mcpi.minecraft import Minecraft
mc = Minecraft.create()
# Присваиваем переменным x, y и z значения координат
x = 100
y = 110
z = 12
# Меняем позицию игрока
mc.player.setTilePos(x, y, z)
