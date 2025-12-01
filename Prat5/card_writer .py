import RPi . GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO . setwarnings ( False )
leitor = SimpleMFRC522 () # cria um objeto da classe leitor MRFC
texto = " correto "
print ( " Aprox para gravar " ) #o print não aparecera no serviço, mas não há problema.
leitor . write ( texto ) # executa um metodo do objeto leitor que escreve um dado na memoria do cartao
print ( " Concluido " )