from DataSource.RandomData import RandomGeneration


class GenerateMyData:
    def my_generated_data_to_register(self,first_name,last_name,email_address,screen_name,password,primarily,role):

        _first_name = RandomGeneration.random_string(int(first_name))

        _last_name = RandomGeneration.random_string(int(last_name))

        _email_address = RandomGeneration.random_email(int(email_address))

        _screen_name = RandomGeneration.random_string(int(screen_name))

        _password = RandomGeneration.random_password(int(password))
        print (password)


        register_values= {"FName": _first_name, "LName": _last_name, "Email": _email_address, "ScreenName": _screen_name,
          "Password": _password, "Primarily": primarily, "Role": role}
        return register_values
