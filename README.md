# Verificador de Páginas Web com Fila de Pré-Carregamento

Uma ferramenta de automação em Python criada para inspecionar visualmente múltiplos sites de forma rápida e eficiente, utilizando um sistema inteligente de pré-carregamento e gerenciamento de abas.

## Como Começar: Guia Rápido

Siga estes passos para ter o projeto funcionando em poucos minutos.

### Passo 1: Tenha o Python Instalado

Este script requer **Python 3**. Se você ainda não o tem, baixe a versão mais recente no [site oficial do Python](https://www.python.org/downloads/).

### Passo 2: Obtenha o Código do Projeto

Você pode baixar o código do projeto:

**(Download Direto):**
1.  Clique no botão verde **"< > Code"** no topo desta página do GitHub.
2.  Selecione **"Download ZIP"**.
3.  Extraia o arquivo ZIP em uma pasta de sua escolha.

### Passo 3: Instale as Bibliotecas Necessárias

Abra seu terminal ou prompt de comando (CMD/PowerShell) e instale as três bibliotecas que o script utiliza com os seguintes comandos:

```bash
pip install selenium
```
```bash
pip install webdriver-manager
```
```bash
pip install keyboard
```
**Observação:** Dependendo do seu sistema operacional (Linux/macOS), a instalação da biblioteca `keyboard` pode exigir privilégios de administrador (`sudo pip install keyboard`).

### Passo 4: Crie sua Lista de Links

1.  Na mesma pasta onde está o script, crie um novo arquivo de texto.
2.  Nomeie este arquivo exatamente como `links.txt`.
3.  Dentro dele, cole todas as URLs que você deseja verificar, **uma por linha**.

**Exemplo de `links.txt`:**
```
SeuSite.com.br/informacoes/mapa-do-site

```

### Passo 5: Execute a Automação!

Com tudo pronto, execute o script a partir do seu terminal, na pasta do projeto:

```bash
python verificador.py
```

O navegador Chrome será aberto e o processo de verificação começará automaticamente.

### Passo 6: Pause a Qualquer Momento

Lembre-se: para inspecionar uma página com calma, pressione o atalho **`alt+c`** para pausar a automação. Pressione novamente para continuar.

---

## O Que Este Projeto Faz?

Esta ferramenta foi projetada para resolver um problema comum de desenvolvedores e analistas de conteúdo: a verificação manual de dezenas de páginas web. O script automatiza essa tarefa com funcionalidades inteligentes para maximizar a eficiência.

-   **Fila de Pré-Carregamento:** O script não abre uma página por vez. Ele mantém um número constante de abas abertas (por padrão, 5), garantindo que, enquanto você inspeciona a primeira, as próximas já estão carregando em segundo plano.

-   **Foco Contínuo:** Uma técnica especial é utilizada para abrir novas abas em background **sem nunca roubar o foco visual** da aba principal. Sua visão fica sempre na primeira página da fila, sem distrações.

-   **Fluxo Contínuo (FIFO):** Assim que a primeira página da fila é inspecionada, ela é fechada, uma nova é adicionada ao final da fila, e o foco muda instantaneamente para a próxima página que já estava pré-carregada.

## Configurações

Para uma experiência personalizada, você pode ajustar as seguintes constantes diretamente no topo do arquivo `verificador.py`:

-   `TEMPO_DE_VISUALIZACAO`: O tempo (em segundos) que cada página fica em foco.
-   `NUMERO_DE_TABS_ABERTOS`: A quantidade de abas que o script manterá abertas simultaneamente.

---
**Desenvolvido por Eduardo Nakashima**
