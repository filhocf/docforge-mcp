# RFC-001: Leitura Rica de Documentos para IA

**Status**: Proposto  
**Data**: 2026-06-22  
**Autor**: Claudio Ferreira Filho  

## Problema

A tool `read_document` atual extrai apenas texto plano de arquivos DOCX/PDF. Isso causa:

1. **Perda de formatação**: bold, italic, underline, strikethrough não são visíveis para a IA
2. **Perda de estrutura**: headings perdem hierarquia, tabelas viram texto corrido
3. **Impossibilidade de detectar alterações**: quando o usuário edita um documento (reordena seções, adiciona ênfase, reformata), a IA não consegue identificar o que mudou
4. **Perda de contexto semântico**: a IA não distingue um título de um parágrafo, um item de lista de texto corrido

## Proposta

### Tool 1: `read_document_rich` (Quick Win)

Retorna o conteúdo do DOCX como **Markdown** preservando:
- Headings com níveis (`#`, `##`, `###`)
- Formatação inline (`**bold**`, `*italic*`, `~~strike~~`, `__underline__`)
- Tabelas em formato Markdown
- Listas (bullets e numeradas) com indentação
- Imagens como `![alt](placeholder)`

**Implementação**: usar `markitdown` (Microsoft) ou `docx2python(html=True)` + conversor HTML→MD.

**Parâmetros**:
```
read_document_rich(
    file_path: str,
    format: "markdown" | "html" | "structured" = "markdown"
)
```

### Tool 2: `compare_documents` (Evolução)

Compara duas versões de um DOCX e retorna as diferenças:

```
compare_documents(
    original_path: str,
    modified_path: str,
    granularity: "paragraph" | "sentence" | "word" = "paragraph"
)
```

**Retorno**:
```json
{
  "summary": "3 parágrafos alterados, 1 movido, 2 adicionados",
  "changes": [
    {"type": "modified", "paragraph": 5, "before": "...", "after": "...", "formatting_changes": ["added bold"]},
    {"type": "moved", "from_position": 3, "to_position": 7, "text": "..."},
    {"type": "added", "position": 12, "text": "..."},
    {"type": "deleted", "position": 8, "text": "..."}
  ]
}
```

**Implementação**: `docx-editor` (hash-anchored paragraphs) ou `docx2python` paragraph-level diff + `deepdiff`/`redlines`.

### Tool 3: `read_document_structured` (Opcional)

Retorna JSON com metadados completos por parágrafo:

```json
[
  {"index": 0, "style": "Heading 1", "text": "Título", "bold": true, "level": 1},
  {"index": 1, "style": "Normal", "text": "Conteúdo...", "bold": false, "italic": false},
  {"index": 2, "style": "List Paragraph", "text": "Item 1", "list_level": 0}
]
```

## Bibliotecas Candidatas

| Biblioteca | PyPI | Uso |
|---|---|---|
| **markitdown** (Microsoft) | `pip install markitdown` | DOCX/PDF→Markdown. Tem MCP server oficial (`markitdown-mcp`) |
| **docx2python v3** | `pip install docx2python` | Extração com html=True, Par.style, Par.runs, Par.lineage |
| **docx-editor** | `pip install docx-editor` | Track changes, hash refs, word-level diff, batch edit |
| **docx-revisions** | github balalofernandez | Read/write `<w:ins>`/`<w:del>` |
| **redlines** | `pip install redlines` | Diff de texto com marcação visual (strike/highlight) |

## Referências Externas

- Microsoft MarkItDown MCP: https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp
- docx-editor plugin Claude Code: https://github.com/pablospe/docx-editor
- docx2python: https://github.com/ShayHill/docx2python

## Decisões Pendentes

1. Usar MarkItDown como dependência ou reimplementar com docx2python?
2. Para `compare_documents`: manter snapshot da versão anterior automaticamente (antes de cada `edit_*`)?
3. Adicionar como tools separadas ou substituir `read_document` com flag `rich=True`?
4. Suporte a PDF (MarkItDown já suporta) ou só DOCX inicialmente?

## Impacto no Uso

- **Criação + edição**: fluxo atual (`create_word_from_markdown` → `edit_*`) continua igual
- **Leitura para IA**: `read_document_rich` substitui `read_document` como default quando a IA precisa "entender" o doc
- **Detecção de alterações**: `compare_documents` resolve o caso "editei, vê o que mudou"
- **Compatibilidade**: `read_document` (texto puro) continua existindo para extração simples

## Prioridade

- Tool 1 (`read_document_rich`): **Alta** — quick win, muda experiência imediata
- Tool 2 (`compare_documents`): **Média** — resolve caso específico mas requer mais engenharia
- Tool 3 (`read_document_structured`): **Baixa** — JSON verboso, útil para automação mas não para interação
