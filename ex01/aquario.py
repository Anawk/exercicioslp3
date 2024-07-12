def calculavolume(com, alt, lar):
    return (com * alt * lar) / 1000

def calculapotenciatermostato(vol, des, amb):
    return vol * 0.05 * (des - amb)

def calculafiltragem(vol):
    return vol * 2, vol * 3