# Instalação

1. Entre na pasta backend, crie um ambiente virtual e ative-o:

    ```bash
    cd backend
    python -m venv venv
    source venv/bin/activate  # No Windows, use: venv\Scripts\activate
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements/local.txt
    ```

3. Se for ultilizar o banco de dados PostgreSQL configure-o:

    Certifique-se de que o PostgreSQL esteja rodando e crie o banco de dados:

    ```sql
    CREATE DATABASE SmartFarma;
    ```

    Configure as credenciais no arquivo `.env`:

    ```bash
    USE_POSTGRESQL=True
    DATABASE_URL=postgres://<usuario>:<senha>@localhost:5432/SmartFarma
    ```

4. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

5. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```
    Acesse o sistema
    * acessar o swagger-ui: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
    * acessar a documentação: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)
