import sys
import os

# Adiciona o diretório atual ao path
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

try:
    from gitautodeploy import main
except ImportError as e:
    print(f"Erro ao importar gitautodeploy: {e}")
    print("Verifique se as dependências estão instaladas: pip install -r requirements.txt")
    sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrompido pelo usuário.")
        sys.exit(0)
    except Exception as e:
        print(f"Erro fatal: {e}")
        sys.exit(1)
