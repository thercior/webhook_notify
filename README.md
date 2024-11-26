# 🚀 Webhook Notify

## 📒 Sobre

Esta aplicação se trata de webhook criado em Django para enviar notificações via e-mail/whatsapp sobre eventos ocorridos em outros sistemas/aplicações e que utilizam este webhook para notificar tal ocorrência.

## 💡Versão e Funcionalidades

Atualmente a aplicação encontra-se na versão 1.0, e oferece com recursos:

* Envio de notificações de eventos.
* Notificações via e-mail.
* Notificações personalizadas via whatsapp para número próprio.
* Painel admin fluido para acesso das notificações e verificar eventos ocorridos.
* Utilização de Docker para rodar aplicações e banco de dados independente do sistema e versões.

## 🧱 Stack utilizada

Back-end: Python, Docker

## 🛠 Instalação

Estão disponíveis duas formas para rodar a aplicação localmente em sua máquina. Antes de rodar, é necessário baixar a aplicação pelo comando abaixo:

```bash
git clone https://github.com/thercior/webhook_notify.git
```

###### Ambiente virtual

1. No terminal dentro da pasta do projeto clonado, execute o comando abaixo para criar e ativar o ambiente virtual:

   ```shell
   # Criar e ativar para windows
   python -m venv venv
   venv\Scripts\activate

   # Criar e Ativar para Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Em seguida, instale as dependências do projeto conforme a seguir.

   ```shell
   pip install -r requirements.txt
   ```
3. Crie o arquivo .env dentro da pasta config, para colocar as variáveis de ambiente, conforme a seguir:

   ```
   SECRET_KEY='cole chave sua Secret Key' 
   DB_NAME='nome do seu banco'
   DB_USER='nome de usuário do banco'
   DB_PASSWORD='[assword do banco'
   DB_HOST='host do banco' # se localmente, será o localhost
   DB_PORT=sua_porta # se for o postgres, a porta geralmenta 5432
   DEBUG_DEV=True # para rodar localmente True, e criará banco sqlite. Caso rode em produção, coloque False e o banco será o que você configurará aqui
   DEBUG_PRODUCTION=False
   ```

   *Obs: caso não tenha a SECRET_KEY, crie um projeto django do zero e copie e cole a chave dele aqui.*
4. Rode as migrações conforme a seguir

   ```shell
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Crie um super usuário.

   ```shell
   python manage.py createsuperuser
   ```

   Informe um nome de usuário, seu e-mail e a senha.
6. Rode aplicação com o comando abaixo e ela estará disponível em `localhost:8000/chats/`

###### Container Docker

1. Tendo o docker e o docker-compose instalado, no diretório do projeto, rode o seguinte comando para criar a imagem do app:

   ```
   docker-compose build
   ```
2. Com a imagem do app criada, para subir o container, basta executar:

   ```
   docker-compose up -d
   ```
3. Para criar um superuser, basta executar o comando abaixo:

   ```
   docker-compose exec web python manage.py createsuperuser
   ```
4. Execute o passo normalmente, informando nome de usuário, e-mail e senha.
5. A aplicação vai estar disponível em `localhost:8061/api/v1`. Contudo, como as rotas são de post, não vai ter como verificar pelas rotas normais os eventos. Para isso é necessário acessar o painel admin.
6. para acesar o painel admin, vá em `localhost:8061/admin` e entre com o usuário superuser que você utilizou. Terá acesso a uma painel admin personalizado com a lib JAZZMIN.

Para parar o container , basta executar `docker-compose down`

## 📝 Licença

Code Assistent está sobre uma [🔗 Licença MIT](https://github.com/thercior/code-assistent/blob/main/LICENSE)
