import re

senha = input("Digite sua senha: ")

pontuacao = 0

if len(senha) >= 12:
    pontuacao += 1
    print("✅ Possui pelo menos 12 caracteres")
else:
    print("❌ Menos de 12 caracteres")

if re.search(r"[A-Z]", senha):
    pontuacao += 1
    print("✅ Possui letra maiúscula")
else:
    print("❌ Não possui letra maiúscula")

if re.search(r"[a-z]", senha):
    pontuacao += 1
    print("✅ Possui letra minúscula")
else:
    print("❌ Não possui letra minúscula")

if re.search(r"\d", senha):
    pontuacao += 1
    print("✅ Possui número")
else:
    print("❌ Não possui número")

if re.search(r"[^a-zA-Z0-9]", senha):
    pontuacao += 1
    print("✅ Possui caractere especial")
else:
    print("❌ Não possui caractere especial")

print("\n--- Resultado ---")

if pontuacao <= 2:
    print("🔴 Senha FRACA")
elif pontuacao <= 4:
    print("🟡 Senha MÉDIA")
else:
    print("🟢 Senha FORTE")