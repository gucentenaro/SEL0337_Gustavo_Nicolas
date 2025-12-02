# SEL0337_Gustavo_Nicolas
Repositório criado para o envio da prática 5 da disciplina SEL0337.

**Prática 5: SystemD e Versionamento com Git**

Autores: Gustavo Bruno Centenaro (14653929)
       Nícolas Máximo Lombardi de Carvalho (14781422)
       
**Relatório do Projeto**

Este repositório documenta a implementação de serviços de inicialização automática no Linux (SystemD) e a utilização de ferramentas de controle de versão (Git/GitHub) em um ambiente embarcado. O objetivo principal foi configurar um script em Python para controlar um LED (Blink) que inicia automaticamente no boot do sistema operacional.

**Arquivos no Repositório**

**blink_nicogu.py**: Script principal em Python utilizando a biblioteca RPi.GPIO para fazer o LED piscar (GPIO 18).

**parar.service**: Unidade de serviço do SystemD criada para gerenciar a execução do script Python em segundo plano.

**parar_led.sh**: Script Shell auxiliar destinado a desligar o LED e liberar o pino GPIO quando o serviço é interrompido (ExecStop).

**historico_git.txt**: Log gerado contendo o histórico de commits realizados na Raspberry Pi.

**Parte 1: Configuração do SystemD**

Nesta etapa, o objetivo foi criar um Unit File para que o Linux gerencie o script de blink como um serviço de sistema (daemon).

Procedimento realizado:

Desenvolvimento do script blink_nicogu.py para controle de hardware.

Criação do arquivo parar.service definindo os parâmetros ExecStart (para rodar o Python) e ExecStop (para limpar a GPIO).

Configuração de permissões e ativação do serviço para iniciar no boot (systemctl enable).

**Resultados e Observações:**
A inicialização automática funcionou como esperado: ao reiniciar a Raspberry Pi, o LED começou a piscar sem intervenção do usuário, comprovando o funcionamento do ExecStart.

Entretanto, a execução não ocorreu 100% livre de falhas. Durante os testes de parada manual do serviço (systemctl stop), notou-se que o LED permanecia aceso. Isso indicou a necessidade de ajustes finos nas permissões de usuário e nos caminhos absolutos dos scripts. Apesar desse comportamento no desligamento, o objetivo principal de automação no boot e a compreensão da estrutura do SystemD foram alcançados com sucesso.

**Parte 2: Controle de Versão (Git)**

Nesta etapa, foi configurado o ambiente de desenvolvimento na Raspberry Pi para sincronização com o GitHub.

Procedimento realizado:

Instalação e configuração das credenciais globais do Git (user.name e user.email).

Criação de Token de Acesso Pessoal (PAT) no GitHub para autenticação segura.

Execução do ciclo de versionamento: git add, git commit e git push.

Geração de logs de histórico para documentação.

**Evidências**


<img width="761" height="445" alt="image" src="https://github.com/user-attachments/assets/357cc7fd-96aa-45ac-bcbf-9ae32ab23045" />


A montagem física foi realizada utilizando a GPIO 18 da Raspberry Pi conectada a um LED e resistor na protoboard. O funcionamento do serviço foi validado via terminal através do comando systemctl status.

