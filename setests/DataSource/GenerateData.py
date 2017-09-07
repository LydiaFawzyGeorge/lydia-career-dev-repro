from DataSource.RandomData import RandomGeneration


class GenerateMyData:
    def my_generated_data_to_register(self,first_name,last_name,email_address,screen_name,password,primarily,role):
        rows=[]
        _first_name = RandomGeneration.random_string(int(first_name))
        rows.append(_first_name)
        _last_name = RandomGeneration.random_string(int(last_name))
        rows.append(_last_name)
        _email_address = RandomGeneration.random_email(int(email_address))
        rows.append(_email_address)
        _screen_name = RandomGeneration.random_string(int(screen_name))
        rows.append(_screen_name)
        _password = RandomGeneration.random_password(int(password))
        print (password)
        rows.append(_password)
        rows.append(primarily)
        rows.append(role)
        return rows
