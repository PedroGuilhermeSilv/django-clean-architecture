## Domain:
### DataClass 
- É uma biblioteca usada adicionar funcionalidades em nossas classes. Utilizando do decorator `@dataclass()` ele automáticamente irá nos adicionar as opções de inicialização(atributos), representação(imprimir os dados) e igualdade(fazer comparação).

### Typing
- É usada para adicionar tipos de dados opcionais e anotações de tipo ao código Python.

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
- Em Python, os "slots" são uma técnica de otimização para classes. Eles são usados para pré-declarar atributos que uma instância da classe pode ter, o que ajuda a economizar espaço de memória e melhora o desempenho, especialmente em casos em que há muitas instâncias da classe.

- Quando você define slots em uma classe, você está limitando dinamicamente quais atributos essa classe pode ter. Isso significa que, uma vez que os slots são definidos, as instâncias da classe só podem ter atributos que foram especificados nos slots. Isso é diferente do comportamento padrão em Python, onde você pode adicionar ou modificar atributos em qualquer instância de classe em tempo de execução.

## Validação no DDD
- Validação de Objetos de Domínio:

    - Métodos de Validação Interna: Os objetos de domínio geralmente encapsulam a lógica de validação dentro de si mesmos. Isso significa que cada objeto de domínio é responsável por garantir que esteja em um estado válido antes de permitir que qualquer operação seja executada sobre ele. Por exemplo, uma classe que representa um pedido pode ter métodos para verificar se todas as informações obrigatórias foram fornecidas, se os valores dos campos estão dentro de limites aceitáveis e assim por diante.

    - Invariantes de Domínio: Muitas vezes, a validação no DDD é expressa por meio de invariantes de domínio. Estes são conjuntos de regras que devem ser verdadeiros para que um objeto de domínio seja considerado válido. Os invariantes são aplicados em todas as operações sobre o objeto e garantem que ele permaneça em um estado consistente. Por exemplo, em um sistema de gerenciamento de estoque, um invariante pode ser que a quantidade em estoque nunca pode ser negativa.

- Validação de Operações:

    - Validação Pré-Operação: Antes de executar uma operação sobre um objeto de domínio, é importante validar se essa operação é permitida de acordo com as regras de negócios do domínio. Por exemplo, antes de enviar um pedido, pode ser necessário verificar se todos os itens do pedido estão em estoque.

    - Validação Pós-Operação: Após a execução de uma operação, é necessário garantir que o objeto de domínio resultante permaneça em um estado válido. Isso pode envolver a verificação de invariantes de domínio novamente após a operação ter sido concluída. Por exemplo, após a confirmação de um pedido, pode ser necessário verificar se a quantidade em estoque foi atualizada corretamente.

    - Transações e Atomicidade: A validação de operações muitas vezes está intimamente ligada ao conceito de transações no DDD. As operações devem ser atomicamente válidas, o que significa que elas devem ser executadas como uma unidade indivisível e garantir que o objeto de domínio permaneça em um estado válido durante todo o processo. Se uma operação falhar em qualquer ponto, o sistema deve garantir que ele retorne ao estado anterior de forma consistente.


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