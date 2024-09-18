from django.shortcuts import render
import psycopg2
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render
import pytz

def index(request):
    try:
        # Configurações do banco de dados
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "servmachine",
                "USER": "servmachinedjango",
                "PASSWORD": "Marcelo1969#",
                # "HOST": "3.14.245.219",
                "HOST": "18.223.237.128",
                "PORT": 5432,
            }
        }

        # Extrair configurações do banco de dados
        db_config = DATABASES["default"]

        connection = psycopg2.connect(
            dbname=db_config["NAME"],
            user=db_config["USER"],
            password=db_config["PASSWORD"],
            host=db_config["HOST"],
            port=db_config["PORT"]
        )
        print("Conexão ao banco de dados bem-sucedida!")

        # Aqui você pode executar consultas, inserções, atualizações, etc.
        cursor = connection.cursor()

        # Obter a data atual
        today = datetime.today().date()

        # Consulta SQL com a cláusula WHERE para filtrar os resultados da tabela api_training
        training_query = "SELECT * FROM api_training WHERE start >= %s ORDER BY start ASC"
        cursor.execute(training_query, (today,))

        # Obtendo os nomes das colunas da tabela api_training
        training_col_names = [desc[0] for desc in cursor.description]

        # Obtendo os dados retornados da tabela api_training
        training_rows = cursor.fetchall()

        # Consulta SQL para a tabela api_article
        article_query = "SELECT * FROM api_article"
        cursor.execute(article_query)

        # Obtendo os nomes das colunas da tabela api_article
        article_col_names = [desc[0] for desc in cursor.description]

        # Obtendo os dados retornados da tabela api_article
        article_rows = cursor.fetchall()

        # Fechar o cursor
        cursor.close()

        # Fechar a conexão
        connection.close()

        # Formatando a data e hora para o formato DD/MM/AAAA HH:MM:SS da tabela api_training
        # formatted_training_rows = []
        # for row in training_rows:
        #     formatted_row = list(row)
        #     formatted_row[3] = row[3].strftime('%d/%m')  # Assumindo que a data de início está na quarta posição
        #     formatted_row[4] = row[4].strftime('%d/%m')  # Assumindo que a data de início está na quarta posição
        #     formatted_row[10] = row[4].strftime('%H:%M')  # Assumindo que a data de início está na quarta posição
        #     formatted_row[9] = row[3].strftime('%H:%M')  # Assumindo que a data de início está na quarta posição
        #     formatted_training_rows.append(formatted_row)

        sao_paulo_tz = pytz.timezone('America/Sao_Paulo')

        formatted_training_rows = []
        for row in training_rows:
            formatted_row = list(row)
            if isinstance(row[3], datetime):
                utc_time = row[3].replace(tzinfo=pytz.utc)
                local_time = utc_time.astimezone(sao_paulo_tz)
                formatted_row[3] = local_time.strftime('%d/%m/%Y')
                formatted_row[9] = local_time.strftime('%Hh')
            if isinstance(row[4], datetime):
                utc_time = row[4].replace(tzinfo=pytz.utc)
                local_time = utc_time.astimezone(sao_paulo_tz)
                formatted_row[4] = local_time.strftime('%d/%m/%Y')
                formatted_row[10] = local_time.strftime('%Hh')
            formatted_training_rows.append(formatted_row)

        return render(request, 'index.html', {'training_col_names': training_col_names, 'treinamentos': formatted_training_rows, 'article_col_names': article_col_names, 'artigos': article_rows})

    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return render(request, 'error.html')

def homenagem(request, artigo_id):
    try:
        # Configurações do banco de dados
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "servmachine",
                "USER": "servmachinedjango",
                "PASSWORD": "Marcelo1969#",
                "HOST": "18.223.237.128",
                "PORT": 5432,
            }
        }

        # Extrair configurações do banco de dados
        db_config = DATABASES["default"]

        connection = psycopg2.connect(
            dbname=db_config["NAME"],
            user=db_config["USER"],
            password=db_config["PASSWORD"],
            host=db_config["HOST"],
            port=db_config["PORT"]
        )
        print("Conexão ao banco de dados bem-sucedida!")

        # Aqui você pode executar consultas, inserções, atualizações, etc.
        cursor = connection.cursor()

        # Consulta SQL para buscar o artigo pelo ID
        artigo_query = "SELECT * FROM api_article WHERE id = %s"
        cursor.execute(artigo_query, (artigo_id,))

        # Obtendo os dados do artigo
        artigo = cursor.fetchone()

        # Fechar o cursor
        cursor.close()

        # Fechar a conexão
        connection.close()

        return render(request, 'homenagem.html', {'artigo': artigo})

    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)
        return render(request, 'error.html')
    

def ceo(request):
    return render(request, 'ceo.html')
# def index(request):
#     return render(request, 'index.html')

def profissionais(request):
    return render(request, 'profissionais.html')

def alunos(request):
    return render(request, 'alunos.html')

def old_profissionais(request):
    return render(request, 'old_profissionais.html')


from django.shortcuts import redirect

# def visualizar_certificado(request):
#     if request.method == 'POST':
#         id = request.POST.get('personId')
#         cpf = request.POST.get('cpf')
        
#         DATABASES = {
#             "default": {
#                 "ENGINE": "django.db.backends.postgresql",
#                 "NAME": "servmachine",
#                 "USER": "servmachinedjango",
#                 "PASSWORD": "Marcelo1969#",
#                 "HOST": "18.223.237.128",
#                 "PORT": 5432,
#             }
#         }

#         # Extrair configurações do banco de dados
#         db_config = DATABASES["default"]
#         try:
#             connection = psycopg2.connect(
#                 dbname=db_config['NAME'],
#                 user=db_config['USER'],
#                 password=db_config['PASSWORD'],
#                 host=db_config['HOST'],
#                 port=db_config['PORT']
#             )
#             cursor = connection.cursor()
            
#             # Consultar o banco de dados para obter o profissional pelo ID
#             professional_query = "SELECT * FROM api_professional WHERE id = %s"
#             cursor.execute(professional_query, (id,))
            
#             # Obter o resultado da consulta
#             professional = cursor.fetchone()
            
#             # Fechar o cursor e a conexão
#             cursor.close()
#             connection.close()
            
#             if professional:
#                 if professional[7] == cpf:
#                     certificate_url = f'https://servmachine.com.br/certificates?id={id}&document={cpf}'
#                     return HttpResponseRedirect(certificate_url)
#                 else:
#                     # Se o nome fornecido pelo usuário não corresponder ao nome no banco de dados
#                     # redirecione para outra página
#                     return redirect('alunos')
#             else:
#                 # Se o profissional não for encontrado, retorne uma mensagem de erro
#                 return JsonResponse({'success': False, 'message': 'Profissional não encontrado.'})
#         except psycopg2.Error as e:
#             # Lidar com erros de conexão ou consulta
#             return JsonResponse({'success': False, 'message': f'Erro: {e}'})
    
#     # Se o método não for POST ou se não houver dados no POST, retorne o template
#     return render(request, 'index.html')
def visualizar_certificado(request):
    if request.method == 'POST':
        id = request.POST.get('personId')
        cpf = request.POST.get('cpf')
        
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "servmachine",
                "USER": "servmachinedjango",
                "PASSWORD": "Marcelo1969#",
                "HOST": "18.223.237.128",
                "PORT": 5432,
            }
        }

        # Extrair configurações do banco de dados
        db_config = DATABASES["default"]
        try:
            connection = psycopg2.connect(
                dbname=db_config['NAME'],
                user=db_config['USER'],
                password=db_config['PASSWORD'],
                host=db_config['HOST'],
                port=db_config['PORT']
            )
            cursor = connection.cursor()
            
            # Consultar o banco de dados para obter o profissional pelo ID
            professional_query = "SELECT * FROM api_professional WHERE id = %s"
            cursor.execute(professional_query, (id,))
            
            # Obter o resultado da consulta
            professional = cursor.fetchone()
            
            # Fechar o cursor e a conexão
            cursor.close()
            connection.close()
            
            if professional:
                if professional[7] == cpf:
                    certificate_url = f'https://servmachine.com.br/certificates?id={id}&document={cpf}'
                    return JsonResponse({'success': True, 'certificate_url': certificate_url})
                else:
                    return JsonResponse({'success': False, 'message': 'CPF não corresponde ao registrado.'})
            else:
                return JsonResponse({'success': False, 'message': 'Profissional não encontrado.'})
        except psycopg2.Error as e:
            return JsonResponse({'success': False, 'message': f'Erro: {e}'})
    
    return JsonResponse({'success': False, 'message': 'Método não permitido. Utilize POST.'})

# def visualizar_certificado_en(request):
#     if request.method == 'POST':
#         id = request.POST.get('personIdEn')
#         cpf = request.POST.get('cpf')
        
#         DATABASES = {
#             "default": {
#                 "ENGINE": "django.db.backends.postgresql",
#                 "NAME": "servmachine",
#                 "USER": "servmachinedjango",
#                 "PASSWORD": "Marcelo1969#",
#                 "HOST": "18.223.237.128",
#                 "PORT": 5432,
#             }
#         }

#         # Extrair configurações do banco de dados
#         db_config = DATABASES["default"]
#         try:
#             connection = psycopg2.connect(
#                 dbname=db_config['NAME'],
#                 user=db_config['USER'],
#                 password=db_config['PASSWORD'],
#                 host=db_config['HOST'],
#                 port=db_config['PORT']
#             )
#             cursor = connection.cursor()
            
#             # Consultar o banco de dados para obter o profissional pelo ID
#             professional_query = "SELECT * FROM api_professional WHERE id = %s"
#             cursor.execute(professional_query, (id,))
            
#             # Obter o resultado da consulta
#             professional = cursor.fetchone()
            
#             # Fechar o cursor e a conexão
#             cursor.close()
#             connection.close()
            
#             if professional:
#                 if professional[7] == cpf:
#                     certificate_url = f'https://servmachine.com.br/certificates?id={id}&document={cpf}&locale=en'
#                     return HttpResponseRedirect(certificate_url)
#                 else:
#                     # Se o nome fornecido pelo usuário não corresponder ao nome no banco de dados
#                     # redirecione para outra página
#                     return redirect('alunos')
#             else:
#                 # Se o profissional não for encontrado, retorne uma mensagem de erro
#                 return JsonResponse({'success': False, 'message': 'Profissional não encontrado.'})
#         except psycopg2.Error as e:
#             # Lidar com erros de conexão ou consulta
#             return JsonResponse({'success': False, 'message': f'Erro: {e}'})
    
#     # Se o método não for POST ou se não houver dados no POST, retorne o template
#     return render(request, 'index.html')
def visualizar_certificado_en(request):
    if request.method == 'POST':
        id = request.POST.get('personIdEn')
        cpf = request.POST.get('cpf')
        
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.postgresql",
                "NAME": "servmachine",
                "USER": "servmachinedjango",
                "PASSWORD": "Marcelo1969#",
                "HOST": "18.223.237.128",
                "PORT": 5432,
            }
        }

        # Extrair configurações do banco de dados
        db_config = DATABASES["default"]
        try:
            connection = psycopg2.connect(
                dbname=db_config['NAME'],
                user=db_config['USER'],
                password=db_config['PASSWORD'],
                host=db_config['HOST'],
                port=db_config['PORT']
            )
            cursor = connection.cursor()
            
            # Consultar o banco de dados para obter o profissional pelo ID
            professional_query = "SELECT * FROM api_professional WHERE id = %s"
            cursor.execute(professional_query, (id,))
            
            # Obter o resultado da consulta
            professional = cursor.fetchone()
            
            # Fechar o cursor e a conexão
            cursor.close()
            connection.close()
            
            if professional:
                if professional[7] == cpf:
                    certificate_url = f'https://servmachine.com.br/certificates?id={id}&document={cpf}&locale=en'
                    return JsonResponse({'success': True, 'certificate_url': certificate_url})
                else:
                    return JsonResponse({'success': False, 'message': 'CPF does not match the registered one.'})
            else:
                return JsonResponse({'success': False, 'message': 'Professional not found.'})
        except psycopg2.Error as e:
            return JsonResponse({'success': False, 'message': f'Error: {e}'})
    
    return JsonResponse({'success': False, 'message': 'Method not allowed. Use POST.'})