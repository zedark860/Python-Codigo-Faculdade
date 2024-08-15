def welcome_function(data_user: dict[str, str]) -> None:
    print(f'Nome: {data_user[name]}\nIdade: {data_user[age]}\nCidade: {data_user[city]}')
    
name, age, city = list(map(str, input('Digite o seu nome, idade e cidade: ').split()))
data_user: dict[str, str] = {
    name: name,
    age: age,
    city: city
}

welcome_function(data_user)