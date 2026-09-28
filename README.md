# EasySupport AI — Assistente Inteligente de Suporte

## 1. Problema resolvido
O EasySupport AI é um assistente corporativo inteligente desenvolvido para automatizar a triagem de chamados, classificar a urgência de atendimentos de suporte baseando-se em Machine Learning, e consultar políticas internas de forma segura utilizando RAG (Retrieval-Augmented Generation) com verificação de fontes e abstenção.

## 2. Arquitetura
O sistema está estruturado em camadas desacopladas:
- **Interface**: Streamlit para a experiência conversacional e painel de aprovação humana.
- **Orquestrador**: LangGraph para gerir o fluxo de validação, classificação, busca e decisão.
- **Classificador**: scikit-learn (Regressão Logística com TF-IDF) para predição de urgência.
- **Recuperador (RAG)**: LangChain e ChromaDB para busca semântica em documentos Markdown.
- **Servidor de Ferramentas**: Model Context Protocol (MCP) com FastMCP para interações seguras com a base de dados SQLite de chamados.

## 3. Pré-requisitos
- Python 3.10 ou superior instalado na máquina.
- Chave de API da OpenAI.

## 4. Instalação
1. Clone ou descarregue o repositório para o seu computador[cite: 20].
2. Crie e ative um ambiente virtual[cite: 20]:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # No Windows (PowerShell)