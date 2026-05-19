# MEMORY.md — docforge-mcp

## Estado Atual (19/mai/2026)

- **Versão**: 0.1.0 (pre-release, não publicado no PyPI ainda)
- **Repo**: https://github.com/filhocf/docforge-mcp
- **Origem**: Fork de ForLegalAI/mcp-ms-office-documents (MIT), divergiu em escopo
- **Status**: Funcional, 38 tools, 16 arquivos de teste, CI ativo

## Pendente

- [ ] Tag v0.1.0 + publish PyPI (trusted publisher)
- [ ] Configurar PyPI trusted publisher no GitHub
- [ ] Atualizar mcp.json local (substituir mcp-ms-office-documents)
- [ ] Atualizar systemd service (porta 8958)
- [ ] Gemini Code Assist ativar no repo

## Decisões

- Nome: docforge-mcp (PyPI livre, domínio claro)
- Filosofia: ecossistema completo (criar+ler+editar+converter) vs upstream one-shot
- Manter PRs #57/#58/#59 no upstream como contribuição pontual
- Backward compat: CLI `mcp-ms-office-documents` ainda funciona
- Licença: MIT dual copyright (ForLegalAI + filhocf)
