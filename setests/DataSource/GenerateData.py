from DataSource.RandomData import RandomGeneration


class GenerateMyData:
    def my_generated_data_to_register(self,first_name,last_name,email_address,screen_name,password,primarily,role):

        first_name = RandomGeneration.random_string(int(first_name))

        last_name = RandomGeneration.random_string(int(last_name))

        email_address = RandomGeneration.random_email(int(email_address))

        screen_name = RandomGeneration.random_string(int(screen_name))

        password = RandomGeneration.random_password(int(password))
        print (password)


        register_values= {"FName": first_name, "LName": last_name, "Email": email_address, "ScreenName": screen_name,
          "Password": password, "Primarily": primarily, "Role": role}
        return register_values
