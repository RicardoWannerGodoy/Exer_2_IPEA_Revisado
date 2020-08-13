####[EM CONSTRUÇÃO]


## Meu Primeiro Programa em *Python*


#### **Pergunta**
**1.** Tenha clareza do objeto que quer estudar?<br/>
**Resp:** Sim, vamos avaliar uma base de pesquisa realizada com uma população de uma comunidade carente de Salvador - BA.

**2.** Qual a pergunta de pesquisa?<br/>
**Resp:** Os investimentos em políticas públicas socioeconômicas têm um impacto maior na qualidade de vida e na segurança da população em áreas de risco do que gastos com o aparelhamento policial?

**3.** Se tem uma pergunta, tem uma hipótese? O que acha que ocorre?<br/>
**Resp:** Investir na satisfação da sociedade e na melhoria do bem-estar social e muito mais enriquecedor do que investir em aparelhamento policial.

**4.** ABM é adequado para a pergunta?<br/>
**Resp:** Sim, uma análise preditiva e uma demonstração pela a metodologia de ABM, poderá apresentar ao gestor público um norte a ser seguido com as implantações de políticas públicas.


#### **main.py**


```import Reader
import Calculator
dados = Reader.run()

listValues = []
for item in dados.values():
    listValues.append(item)

analitics14 = Calculator.createAnalitics(listValues[0])
analitics23 = Calculator.createAnalitics(listValues[1])
analitics34 = Calculator.createAnalitics(listValues[2])
analitics44 = Calculator.createAnalitics(listValues[3])

percentage14 = Calculator.createPercentage(analitics14)
percentage23 = Calculator.createPercentage(analitics23)
percentage34 = Calculator.createPercentage(analitics34)
percentage44 = Calculator.createPercentage(analitics44)

print("AVALIAÇÃO DE POLÍTICAS PUBLICAS")
resposta=1
amostra=20
while resposta!=0:
    print("\n --Menu--\n")
    print("Escolha a opção desejada:\n1-Definir quantidade de amostra;\n2-Previsão de percentuais de resposta;\n")
    resposta = int(input("Opção: "))
    if resposta==1:
        amostra=int(input("Digite o numero novo de amostra: "))
    elif resposta == 2:
        print("\n --Previsão de percentuais--\n")
        print("Escolha a dimensão desejada:\n1-Social;\n2-Econômica;\n3-Política;\n4-Cultural;\n")
        dimensao = int(input("Opção: "))
        if dimensao == 1:
            print(Calculator.createPercentage(Calculator.createPrevision(amostra,percentage14)))

    elif resposta == 0:
        break
    else:
        print("Escolha uma opção válida!")
```

#### **Método/Processo I e II**
**1.** Se ABM for adequado, provavelmente, é fácil determinar:

**2.** Os Agentes em si.

**2.1** Quais são os agentes? Pessoa física, eleitor, paciente,
residências/famílias, grupos de interesse, bancos?<br/>
**Resp:** Moradores da comunidade, 4 dimensões das politicas públicas: Social, Econômica, Política e Social.

**2.2** Qual é o processo a se replicar? É padrão? As regras são conhecidas? Há literatura?<br/>
**Resp:** Estamos replicando uma pesquisa realizada com a população que morra nessa comunidade carente.

**3.** Quais são as regras?<br/>
**Resp:** Pegamos uma pergunta chave de cada dimensão e iremos replica-la randomicamente, com um aumento que o usuário do sistema poderá digitar.

**3.1** São ações dos agentes?<br/>
**Resp:** Os agentes se interagem para que ocorra uma grandeza de percentuais em nos demais.

**3.2** São de origem behaviorista, probabilística, a partir de percepções, mercado, condicionais, baseadas em limites (thresholds). Eles são ad hoc?<br/>
**Resp:** Sim, sua origem é probabilística, e é justamente isso que queremos descobrir com o modelo.

**4.** Qual é o ambiente?<br/>
**Resp:** Uma comunidade carente com moradores que receberam do estado uma quantidade de ações socioeconômicas.

**4.1** Os outros agentes?<br/>
**Resp:** O estado aqui representado pelos três entes da federação.

**4.2** Como é o encontro entre os agentes?<br/>
**Resp:** A partir de um aumento da amostra e randomicamente o sistema busca um melhor percentual assertivo, de acordo com um percentual conhecido.

**4.3** Como o ambiente muda?<br/>
**Resp:** A mudança se faz devido a alteração de percentuais apresentada em cada dimensão.

**4.4** As ações são simultâneas? Ou uma após a outra?<br/>
**Resp:** As ações são simultâneas.

**5.** Qual é o processo?<br/>
**Resp:** De acordo com que se coloca como amostra teremos seus percentuais de respostas apresentadas e seus quantitativos.

**5.1** O que ocorre em qual ordem?<br/>
**Resp:** Primeiro o arquivo main, depois o “Reader” e posteriormente o “Calculator”.

**5.2** Qual é o sistema inicial? Dotações, características?<br/>
**Resp:** Reader: ele lê o arquivo de entrada que é um tcv que contém 17 variáveis e 21 linhas.

**5.3** Por quanto tempo a simulação roda? Faz diferença? Há compatibilidade observada?<br/>
**Resp:** A simulação roda uma vez e busca os valores e percentuais de cada dimensão.

**6.** Use o PROTOCOLO ODD [1] como guia na elaboração do projeto e do texto.<br/>


#### **Validação!!!**

**1.** Antes de começar, é bom ter ideia de como vai validar o modelo (ABM).<br/>
**Resp:** A validação ocorrerá de acordo com a soma dos resultados obtidos nas repostas a mesma terá de resultar em 100%.

**2.** Há dados empíricos que podem ser replicados?<br/>
**Resp:** Não.

**3.** O modelo replica o status quo?<br/>
**Resp:** Sim, como estamos utilizando a importação de dados real para o sistema rodas, temos sim a replicação do "estado das coisas".

**4.** Idealmente, replica-se uma trajetória no tempo.<br/>
**Resp:** No caso desse modelo não tem uma linha de tempo, no caso não é utilizado uma regra de data.

**5.** Então, testam-se alternativas {pós-trajetória {e podem-se fazer algumas sugestões, recomendações, dado o contexto
da pesquisa.<br/>
**Resp:** Sim, vou incorporação no meu projeto de qualificação as informações e conteúdos adquiridos nessa disciplina, e utilizarei esse código desenvolvido para uma projeção das avaliações de políticas públicas.

**6.** Essa literatura não está consolidada, mas em evolução.<br/>
**Resp:** De fato a literatura em questão está em evolução, e será muito útil na construção do conhecimento.

**7.** Minimamente, a questão da validação tem que ser discutida no texto!<br/>
**Resp:** A questão da validação realmente foi discutida ao longo da construção desse memorial com base no que foi construído no código apresentado aqui.


#### **Verificação e teste**

**1.** Você tem certeza que o código faz o que você acha que faz?<br/>
**Resp:** Sim, ele testa fazendo a princípio o que foi proposto, mas tem oportunidade de crescimento.

**2.** Cada parte foi testada?<br/>
**Resp:** Sim, todos os testes foram realizados com sucesso.

**3.** Use print para verificar resultados intermediários!<br/>
**Resp:** Sim, foram utilizados print e a exportação do resultado para um arquivo txt.

**4.** Você utilizou debug para acompanhar o que ocorre com quando agente, a cada passo.<br/>
**Resp:** Sim, foram utilizados todos os recursos existentes na ferramenta, inclusive o *"debug"*.

