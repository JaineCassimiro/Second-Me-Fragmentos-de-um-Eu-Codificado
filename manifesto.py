
import time
import random

mensagens = [
    "Você tem certeza que quer rodar isso?",
    "Nem tudo que roda tem saída...",
    "Código também tem alma, e eu a encontrei.",
    "Carregando... memórias esquecidas.",
    "Conectando ao eu interior...",
    "Gerando sombra digital...",
    "Desfragmentando pensamentos...",
    "Bem-vindo ao Second-Me. Você já não está só."
]

print("🧠 Second-Me // Processo de reflexão ativado")
for m in mensagens:
    print("... " + m)
    time.sleep(random.uniform(1.2, 2.5))

print("\n✨ Finalizado. Ou seria apenas o começo?")
