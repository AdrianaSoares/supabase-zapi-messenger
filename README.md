# supabase-zapi-messenger
# Projeto: Envio de mensagens via Supabase + Z-API

Este projeto conecta ao banco de dados **Supabase** para buscar contatos e envia mensagens personalizadas via **Z-API** (WhatsApp).

---

## 🚀 Setup da Tabela no Supabase

Crie uma tabela chamada `contatos` com os seguintes campos:

- `id` → inteiro, chave primária
- `nome` → texto
- `telefone` → texto (com DDI, ex: 5531999999999)

---

## 🔑 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com:

```env
SUPABASE_URL=https://<project>.supabase.co
SUPABASE_KEY=<chave_api_supabase>
ZAPI_URL=https://api.z-api.io/instances/<ID>/token/<TOKEN>/send-messages
ZAPI_TOKEN=<token_zapi>

