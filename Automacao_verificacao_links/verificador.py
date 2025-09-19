import time
import keyboard
from collections import deque
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# --- INÍCIO DA CONFIGURAÇÃO ---
NOME_ARQUIVO_URLS = "links.txt"
TEMPO_DE_VISUALIZACAO = 0.5
NUMERO_DE_TABS_ABERTOS = 5
# --- FIM DA CONFIGURAÇÃO ---

is_paused = False

def toggle_pause():
    global is_paused
    is_paused = not is_paused
    print(f"\n>> Automação {'PAUSADA' if is_paused else 'RETOMADA'}. Pressione 'alt+c' para alternar. <<")

def carregar_urls_do_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]
        if not urls: print(f"Aviso: O arquivo '{nome_arquivo}' está vazio.")
        return deque(urls)
    except FileNotFoundError:
        print(f"ERRO CRÍTICO: O arquivo '{nome_arquivo}' não foi encontrado.")
        return deque()

def iniciar_verificacao_precisa(urls_a_visitar, num_tabs, tempo_visualizacao):
    if not urls_a_visitar:
        print("Nenhuma URL para verificar. Encerrando.")
        return

    keyboard.add_hotkey('alt+c', toggle_pause)
    print(">>> Atalho 'alt+c' registrado para PAUSAR/RETOMAR. <<<")

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    total_urls = len(urls_a_visitar)
    my_ordered_handles = deque()
    
    # --- LÓGICA DE ABERTURA EM SEGUNDO PLANO ---
    print("Abrindo abas iniciais com foco travado na primeira...")
    # 1. Abre a primeira aba e define o foco nela
    driver.get(urls_a_visitar.popleft())
    my_ordered_handles.append(driver.current_window_handle)

    # 2. Abre as abas restantes EM SEGUNDO PLANO
    initial_tabs_to_open = min(num_tabs - 1, len(urls_a_visitar))
    for _ in range(initial_tabs_to_open):
        url = urls_a_visitar.popleft()
        handles_before = set(driver.window_handles)
        # Comando JavaScript para abrir nova aba sem roubar o foco
        driver.execute_script(f"window.open('{url}', '_blank');")
        handles_after = set(driver.window_handles)
        new_handle = (handles_after - handles_before).pop()
        my_ordered_handles.append(new_handle)
    
    print("Abas iniciais carregando. Foco na primeira. Iniciando ciclo.")
    url_processada_count = 0
    try:
        while my_ordered_handles:
            handle_to_view = my_ordered_handles[0]
            driver.switch_to.window(handle_to_view)
            
            url_atual = driver.current_url
            url_processada_count += 1
            print("-------------------------------------------")
            print(f"VISUALIZANDO ({url_processada_count}/{total_urls}): {url_atual}")
            
            # Pausa e cronômetro
            start_time = time.time()
            while time.time() - start_time < tempo_visualizacao:
                if is_paused:
                    while is_paused: time.sleep(0.1)
                    start_time = time.time()
                time.sleep(0.1)

            # Abre nova aba em background, se houver
            if urls_a_visitar:
                url = urls_a_visitar.popleft()
                handles_before = set(driver.window_handles)
                driver.execute_script(f"window.open('{url}', '_blank');")
                print(f"NOVA ABA EM BACKGROUND: {url}")
                handles_after = set(driver.window_handles)
                new_handle = (handles_after - handles_before).pop()
                my_ordered_handles.append(new_handle)

            # Fecha a aba visualizada
            print(f"FECHANDO ABA ATUAL: {url_atual}")
            driver.close()
            my_ordered_handles.popleft()
            
            # Muda o foco para a próxima da fila
            if my_ordered_handles:
                driver.switch_to.window(my_ordered_handles[0])

    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")
    finally:
        print("\n-------------------------------------------")
        print("Verificação concluída.")
        if driver.service.is_connectable(): driver.quit()
        keyboard.unhook_all()

if __name__ == "__main__":
    urls = carregar_urls_do_arquivo(NOME_ARQUIVO_URLS)
    iniciar_verificacao_precisa(urls, NUMERO_DE_TABS_ABERTOS, TEMPO_DE_VISUALIZACAO)