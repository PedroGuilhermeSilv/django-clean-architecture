## Domain:
### DataClass 
- É uma biblioteca usada adicionar funcionalidades em nossas classes. Utilizando do decorator `@dataclass()` ele automáticamente irá nos adicionar as opções de inicialização(atributos), representação(imprimir os dados) e igualdade(fazer comparação).

### Typing
- É usada para adicionar tipos de dados opcionais e anotações de tipo ao código Python.

## Pirâmede de Teste:
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

## Ferramentas de teste:
- Mocks:
    - Um "mock" em Python é um objeto simulado que imita o comportamento de um objeto real em um contexto controlado. Ele é usado para substituir partes do código que não são desejáveis ou práticas para executar durante os testes.

    - Substituição de Comportamento: Um mock pode ser usado para substituir o comportamento de objetos reais durante a execução dos testes. Isso é útil quando você quer isolar o código que está sendo testado e não quer que ele dependa de componentes externos, como bancos de dados, APIs externas, ou métodos que realizam operações caras ou imprevisíveis.

    - Configuração de Comportamento: Você pode configurar um mock para retornar valores específicos quando chamado, simular exceções, contar quantas vezes foi chamado, verificar com quais argumentos foi chamado, entre outras coisas. Isso permite que você escreva testes específicos para diferentes cenários e comportamentos do seu código.

    - Facilita Testes de Unidade: Usar mocks pode facilitar a escrita de testes de unidade, pois você pode isolar o código que está sendo testado e se concentrar em testar apenas a unidade específica, sem se preocupar com suas dependências externas.

    - Evita Efeitos Colaterais: Ao substituir partes do código com mocks, você pode evitar efeitos colaterais indesejados durante a execução dos testes. Por exemplo, se um método real escreve em um banco de dados, usando um mock você pode evitar que o banco de dados seja modificado durante os testes.

    - Ex: No projeto utilizamos o mock na função validate nos teste unitários da entidade category, para garantir que esse método não tenha influência sobre as funções da entidade.
## SeedWorks
- São objetos que podem ser utilizados de em outras camadas de aplicação de forma a facilitar a implementação e reduzir duplicação de código.

## Slots
- Em Python, os "slots" são uma técnica de otimização para classes. Eles são usados para pré-declarar atributos que uma instância da classe pode ter, o que ajuda a economizar espaço de memória e melhora o desempenho, especialmente em casos em que há muitas instâncias da classe.

- Quando você define slots em uma classe, você está limitando dinamicamente quais atributos essa classe pode ter. Isso significa que, uma vez que os slots são definidos, as instâncias da classe só podem ter atributos que foram especificados nos slots. Isso é diferente do comportamento padrão em Python, onde você pode adicionar ou modificar atributos em qualquer instância de classe em tempo de execução.

## Validação no DDD
- Não devemos permitir a criação de uma entidade em um estado inválido.
- No projeto, o código é a essência, e a essência é o código. Toda inserção deve ser válida para ser persistida.
- No contexto do Domain-Driven Design (DDD), as três tipos de validação se referem a diferentes níveis de validação dentro do domínio da aplicação:
- Validação do Atributo:
    - Esta validação ocorre no nível do próprio atributo de uma entidade ou valor do objeto.
    - Envolve garantir que um valor atribuído a um campo ou propriedade atenda aos critérios de validade especificados.
        Por exemplo, se um campo "idade" só pode aceitar valores positivos, a validação do atributo garantirá que apenas valores positivos sejam aceitos nesse campo.

- Validação do Objeto:
    - A validação do objeto ocorre no nível da entidade ou valor do objeto como um todo.
    - Envolve garantir que o estado do objeto como um todo seja válido e consistente.
    - Isso pode envolver regras de negócios que precisam ser atendidas para que um objeto seja considerado válido.
        Por exemplo, em um sistema de gerenciamento de pedidos, pode haver uma regra de negócios que exija que todos os pedidos tenham pelo menos um item.

- Validação da Integridade:
    - Este tipo de validação aborda a garantia de integridade entre diferentes objetos ou agregados dentro do domínio.
    - Envolve garantir que as relações entre objetos estejam consistentes e que não ocorram violações de integridade referencial.
        Por exemplo, em um sistema de banco de dados, a validação da integridade pode garantir que um pedido só possa ser associado a clientes existentes no sistema.


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