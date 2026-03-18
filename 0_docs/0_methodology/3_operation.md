<!-- PATH: 0_docs/0_methodology/3_operation.md -->

# Plataforma Coursebox.ai

Neste capítulo vamos sumarizar objetivamente os principais campos da ferramenta.

## 📌 Índice
- [Plataforma Coursebox.ai](#plataforma-courseboxai)
  - [📌 Índice](#-índice)
  - [Acesso](#acesso)
    - [Navegação pela ferramenta](#navegação-pela-ferramenta)
  - [Mãos a obra](#mãos-a-obra)
    - [Conta](#conta)
    - [Home Page](#home-page)
    - [Prompt do Curso](#prompt-do-curso)
      - [Carregar](#carregar)
      - [Audiência](#audiência)
      - [Estrutura](#estrutura)
      - [Configurações](#configurações)
      - [O Prompt Geral](#o-prompt-geral)
      - [Atenção](#atenção)
    - [Revisão Pré Processamento](#revisão-pré-processamento)
  - [Encerramento](#encerramento)
  - [Próxima etapa](#próxima-etapa)

## Acesso

O acesso acontecerá diretamente pela [Coursebox.ai](https://www.coursebox.ai/pt). Em nosso caso será necessário utilizar uma conta compartilhada entre os componentes da equipe. Para isso ocorre de maneira sustetável e com o menor estresse para as partes o professor responsável irá delegar o acesso à uma conta gmail, dessa maneria caso seja necessário inserir qualquer código de validação em duas etapas o operador terá total autonomia.

### Navegação pela ferramenta

Durante o mês de fevereiro realizamos uma breve apresentação com um exercício demonstrativo conjunto com os operadores e também lhes foi solicitado que se cadastrassem para realizar testes e atividade exploratórias. 

## Mãos a obra

### Conta

<!-- Ilustração - print da tela -->
![Print tela de longin](images/3-00_login.png)

Login: @gmail.com
Senha: **********

### Home Page

<!-- Ilustração - print da tela -->
![Print home page](images/3-0_veryBegin.png)

Ao realizar o login vamos nos deparar com uma tela com os cursos que já foram construídos, configurações e outras elementos. Vamos clicar no botão com o "**+**" escrito **"Criar Curso"**, circulado em vermelho na imagem abaixo.

<!-- Ilustração - print da tela -->
![Print home page](images/3-0_veryBegin_enfase.png)

### Prompt do Curso

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-1_inicio.png)

Após ter cliclado no botão **"Criar Curso"** somos redirecionados para a página acima, nela temos uma série de elementos que vamos definir na subssessões que seguem.

> OBS.: vamos primeiro preencher os campos **Carregar**, **Audiência**, **Estrutura** e **Configurações**. Em seguida daremos atenção

#### Carregar

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-1_inicio_enf_1.png)

Essa etapa é a parte mais importante para a qualidade do conteúdo que será gerado pela plataforma [Coursebox.ai](https://www.coursebox.ai/pt), porque é onde vamos definir as fontes de consulta.

Ao clicar nesse botão teremos a interface abaixo apresentada:

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-2_carregarArquivos.png)

No segundo passo [link](2_treatment.md) construímos as notas de aula em formato `.md`, vamos criar uma cópia desse arquivo e vamos mudar alterar sua extessão para `.txt` assim tornando a informação mais fácil de "digerir" para a _LLM_ (Large Laguage Model) da plataforma. 

No primeiro passo [link](1_separation.md) separamos tanto o trecho do documento de referência quanto a audio transcrição da aula. No entanto, vamos anexar apenas a parte escolhida do professor do documento de referência. 

As notas de aula tomam um papel fundamental na lógica de construção, servindo de **estrutura do curso**, então verifique se esse arquivo está com a seguinte marcação:

<div align="center">
  <img src="images/3-4_botao_UsarComoEstruturaDoCurso.png" width="500px" height="auto" alt="Print do botão">
</div>

Alternativamente, se alguma das referência disponbilizar algum site também podemos associa-lo.

#### Audiência

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-1_inicio_enf_2.png)

Ao clicar nesse botão teremos a interface abaixo apresentada:

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-3_audiencia.png)

Basicamente um prompt onde vamos informar o público alvo para a atividade. Note que, ao longo da nossa jornada teremos dois públicos-alvo completamente diferentes:

1. "Curso da ARCTEL: Empoderamento de Lideranças Femininas em setores regulação e regulamentação" de Telecomunições e afins; São todos paises de lingua portuguesa que vão participar.

2. "PLIA-DF: Plataforma de Letramento em Inteligência Artificial para
Docente DF"; São professores de todas as áreas do ensino que atuem no Ensino Médio.

Por essa razão precisamos de dois prompts diferentes para descrever os diferentes públicos-alvo:

- Lideranças Femininas do curso ARCTEL
```text
<!-- Cria uma descrição simples e direta do publico alvo -->
```

- Professores da Secretária de Educação do Distrito Federal (SEDF)
```text
<!-- Cria uma descrição simples e direta do publico alvo -->
```

#### Estrutura

Retornando a tela anterior, temos:

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-1_inicio_enf_3.png)

Ao clicar nesse botão teremos a interface abaixo apresentada:

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-5_redundancia_estrutura.png)

Que é uma tela um tanto quanto redundânte quando comparamos com a [Carregar](#carregar) que vimos antes, nela vamos apenas garantir que o documento notas de aula esteja marcado como **"Usar como Estrutura do curso"**. Dessa tela vamos clicar em "Parâmetros Fixos", como podemos ver abaixo:

<div align="center">
  <img src="images/3-5_redundancia_estrutura_2.png" width="750px" height="auto" alt="Print do botão">
</div>

Na nova tela vamos comparar com os parâmetros da print abaixo, exceto que utilizamos o valor de **Seções** igual à 5.

> Se estivermos construindo cursos do PLIA-DF, sobre ferramentas de IA, vamos marcar em **"Tarefas por Seção"** como valor  de **3**;

<div align="center">
  <img src="images/3-5_redundancia_estrutura_3.png" width="750px" height="auto" alt="Print do botão">
</div>

#### Configurações

Retornando a tela anterior, temos:

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-1_inicio_enf_4.png)

Clique nesse botão, este procedimento será o mais simples e rápido, na nova tela vamos apenas comparar com os parâmetros da print abaixo:

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-6_configuracoes.png)

#### O Prompt Geral

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-1_inicio.png)

Enquanto fomos adicionando as configurações e anexando documentos é certo que a caixa do prompt inicial foi preenchida automáticamente, no entanto vamos tomar um pouco mais de cuidado na construção desse prompt.

Ao utilizar o arquivo `aula_01_notas_v1.md` da primeira geração (e provavelmente a mais curta) vamos criar um texto resumo com os tópicos esperados e definições fundamentais, depois a duração aproximada de 1h30 à 2h30, para o curso da ARCTEL ou 2h à 4h para o PLIA-DF.

Formato de Prompt
```text
# Contexto
Este curso fará parte da trilha de aprendizado {do módulo ou ferramenta} do {ARCTEL ou PLIA-DF}.

# Duração
{Lógia de duração informada}

# Púlico Alvo
{Lógia de duração informada}

# Conteúdo Esperados no Curso
<!-- Aqui o operador terá que preencher -->

# Retorno
Curso com linguagem formal direta, sem rebuscamento desnecessário. Imagens coloridas, criativas e divertidas, mas sem infantilizar o assunto ou a forma. Tarefaz crítica e formadoras de conhecimento. Quizes abordando definições fundamentais, sem pegadadinhas.
```

#### Atenção

Antes de clicar em **Gerar** verifique se o switch (barra de deslizar) **"Visualizar estrutura"** está ativado. Vide imagem abaixo:

<!-- Ilustração - print da tela -->
![Print gearar seu curso](images/3-1_inicio_enf_5.png)

### Revisão Pré Processamento

Ao deixar a opção de **"Visualizar estrutura"** ativada a plataforma produz uma sugestão de estrutura para o curso. Em tópicos simples a plataforma apresenta os capítulos que vão compor o curso, os títulos de cada páginas por capítulo, indica a presença de tarefas, quizes e afins.

> É fundamental verificar essa estrutura e se necessário realizar correções manuais.

## Encerramento

## Próxima etapa