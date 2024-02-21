## Domain:
### DataClass 
- É uma biblioteca usada adicionar funcionalidades em nossas classes. Utilizando do decorator `@dataclass()` ele automáticamente irá nos adicionar as opções de inicialização(atributos), representação(imprimir os dados) e igualdade(fazer comparação).

### Typing
- Com essa biblioteca podemos importar o `Optional` informando quais dos nossos atributos sçao opcionais.

## Testes:
- Testes Unitários:
    - Objetivo: Testar unidades individuais de código, como funções ou métodos, isoladamente.
    - Escopo: Foca em partes específicas do código, verificando se cada unidade funciona conforme o esperado.
    - Isolamento: Deve ser independente e isolado de outras partes do sistema.

- Testes de Integração:
    - Objetivo: Testar a interação entre unidades de código ou módulos para garantir que funcionem corretamente em conjunto.
    - Escopo: Envolve a integração de várias partes do sistema para validar a comunicação e a colaboração entre elas.
    - Isolamento: Pode requerer ambientes de teste mais complexos e dependências reais ou simuladas.

- Testes End-to-End (e2e):
    - Objetivo: Testar o fluxo completo do aplicativo, simulando a experiência do usuário desde o início até o final.
    - Escopo: Engloba todos os componentes do sistema, incluindo interfaces de usuário, servidores, bancos de dados e integrações externas.
    - Isolamento: Testa o sistema como um todo, sem isolar componentes individuais.

## SeedWorks
- São objetos que podem ser utilizados de em outras camadas de aplicação de forma a facilitar a implementação e reduzir duplicação de código.

## Slots
- Previsão dos dados necessários


## Configurações do ambiente de desenvolvimento
- PDM: O PDM (Python Development Mode) é um gerenciador de dependências e ambiente de desenvolvimento para projetos Python.

- Autopep8: Ele reescreve o código Python para seguir as diretrizes de formatação definidas pelo estilo PEP 8, que é o guia de estilo de código Python recomendado pela comunidade.

- Pylint: É uma ferramenta de análise de código estática que verifica o código Python em busca de erros, possíveis problemas, padrões de codificação e outros problemas de qualidade. 

- Ruff:   Não é uma ferramenta tão conhecida quanto Pylint e Autopep8. É um linter para Python que se concentra em fornecer feedback rápido durante a edição do código. Assim como o Pylint, ele pode ajudar a identificar problemas no código Python, mas pode ter características e focos específicos diferentes.

- SonarLint: Analisa código em tempo real para detectar problemas de qualidade e segurança, integrando-se a várias IDEs.

- Sourcery: Uma ferramenta de refatoração de código para Python, que sugere melhorias e otimizações para tornar o código mais eficiente e legível.

- Pytest: Framework de teste Python que simplifica a escrita e execução de testes com uma sintaxe poderosa e flexível.

- Unittest: Framework de teste embutido no Python, parte da biblioteca padrão, que fornece uma estrutura para escrever testes de unidade.

- DevContainer: Extensão no vscode para rodar o container diretamente na IDE.