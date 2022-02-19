import pyautogui
import time #biblioteca que permite que você controle o tempo de espera

pyautogui.alert("O código vai começar, não mova e não mexa no mouse e no teclado do seu pc")
# a listas de comandos de cada teclas pode ser encontrada aqui https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
pyautogui.PAUSE =0.5 #espera meio segundo para executar cada linha de código
#abrir o google drive
pyautogui.press('winleft') #aperta uma tecla
pyautogui.write('opera') #digita o texto que você ordena
pyautogui.press('enter') #pressione o enter
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/u/0/my-drive')
pyautogui.press('enter')

# entrar na área de trbalho
time.sleep(4)
pyautogui.hotkey('winleft', 'd') # o hotkey serve para você fazer combinações de teclas com o python



# cliquei no arquivo que eu quero fazer backup e arrastar ele
pyautogui.moveTo(117, 201)# move o mouse para (x,y)
time.sleep(2)
pyautogui.mouseDown()
pyautogui.moveTo(778, 779)
# enquanto eu estou arrastando eu vou mudar para o google drive
time.sleep(2)
pyautogui.hotkey('alt', 'tab')  #muda de uma tela para outra, no caso a ultima aberta

# larguei o arquivo no google drive
pyautogui.mouseUp() # larga o mouse
# esperar 5 segundos
time.sleep(5)
pyautogui.alert("O código acabou de rodar, pode usar o seu computador novamente")